"""
Production-shaped LLM client: caching, fallback chain, cost tracking.

Fallback order: Gemini Flash -> Groq Llama -> local Ollama.
Cache: SQLite, keyed by (model, messages_hash).
"""
import hashlib
import json
import os
import sqlite3
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Rough $/1M token prices — update these periodically.
PRICING = {
    "gemini-2.5-flash": {"in": 0.075, "out": 0.30},
    "llama-3.3-70b-versatile": {"in": 0.00, "out": 0.00},  # Groq free tier
    "llama3.3:8b": {"in": 0.00, "out": 0.00},              # local
}

PROVIDERS = [
    ("gemini-2.5-flash", "https://generativelanguage.googleapis.com/v1beta/openai/", "GEMINI_API_KEY"),
    ("llama-3.3-70b-versatile", "https://api.groq.com/openai/v1", "GROQ_API_KEY"),
    ("llama3.3:8b", "http://localhost:11434/v1", None),
]


# --- Cache -----------------------------------------------------------------

_cache = sqlite3.connect("llm_cache.db", check_same_thread=False)
_cache.execute("CREATE TABLE IF NOT EXISTS cache (key TEXT PRIMARY KEY, value TEXT)")


def _hash(model: str, messages: list) -> str:
    h = hashlib.sha256()
    h.update(model.encode())
    h.update(json.dumps(messages, sort_keys=True).encode())
    return h.hexdigest()


def _cache_get(key: str) -> str | None:
    row = _cache.execute("SELECT value FROM cache WHERE key = ?", (key,)).fetchone()
    return row[0] if row else None


def _cache_set(key: str, value: str) -> None:
    _cache.execute("INSERT OR REPLACE INTO cache VALUES (?, ?)", (key, value))
    _cache.commit()


# --- Cost log --------------------------------------------------------------

_cache.execute(
    "CREATE TABLE IF NOT EXISTS usage ("
    "ts REAL, model TEXT, in_tok INT, out_tok INT, cost REAL, cached INT)"
)


def _log_usage(model: str, in_tok: int, out_tok: int, cached: bool) -> None:
    p = PRICING.get(model, {"in": 0, "out": 0})
    cost = (in_tok * p["in"] + out_tok * p["out"]) / 1_000_000
    _cache.execute(
        "INSERT INTO usage VALUES (?, ?, ?, ?, ?, ?)",
        (time.time(), model, in_tok, out_tok, cost, int(cached)),
    )
    _cache.commit()


# --- Client ----------------------------------------------------------------

def chat(messages: list, use_cache: bool = True) -> str:
    key = _hash("fallback-chain", messages)
    if use_cache and (hit := _cache_get(key)):
        _log_usage("cache", 0, 0, cached=True)
        return hit

    last_err = None
    for model, base_url, env_key in PROVIDERS:
        api_key = os.environ.get(env_key) if env_key else "ollama"
        if env_key and not api_key:
            continue
        try:
            client = OpenAI(api_key=api_key or "x", base_url=base_url)
            resp = client.chat.completions.create(model=model, messages=messages)
            content = resp.choices[0].message.content or ""
            u = resp.usage
            _log_usage(model, u.prompt_tokens if u else 0, u.completion_tokens if u else 0, cached=False)
            _cache_set(key, content)
            return content
        except Exception as e:
            print(f"[fallback] {model} failed: {e}")
            last_err = e
    raise RuntimeError(f"all providers failed: {last_err}")


def cost_summary():
    rows = _cache.execute(
        "SELECT model, SUM(in_tok), SUM(out_tok), SUM(cost), SUM(cached) "
        "FROM usage GROUP BY model"
    ).fetchall()
    print(f"{'model':<30} {'in':>10} {'out':>10} {'cost $':>10} {'cached':>8}")
    for m, i, o, c, cached in rows:
        print(f"{m:<30} {i or 0:>10} {o or 0:>10} {c or 0:>10.4f} {cached or 0:>8}")


if __name__ == "__main__":
    print(chat([{"role": "user", "content": "Say hi in 5 words."}]))
    print(chat([{"role": "user", "content": "Say hi in 5 words."}]))  # cache hit
    print()
    cost_summary()
