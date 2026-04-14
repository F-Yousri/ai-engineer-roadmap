"""
Minimal agent with tool use via Gemini's OpenAI-compatible function calling.

Agent = LLM in a loop with tools. Keep it dumb and explicit until you need more.
"""
import os
import json
import math
import sqlite3
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


# --- Tools -----------------------------------------------------------------

def tool_calculate(expression: str) -> str:
    """Safe-ish calculator. For demo only — use a real sandbox in prod."""
    allowed = {"__builtins__": {}, **{k: getattr(math, k) for k in dir(math) if not k.startswith("_")}}
    try:
        return str(eval(expression, allowed, {}))
    except Exception as e:
        return f"error: {e}"


def tool_sql_query(query: str) -> str:
    """Query a demo sqlite db."""
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE orders (id INT, amount REAL, status TEXT)")
    conn.executemany(
        "INSERT INTO orders VALUES (?, ?, ?)",
        [(1, 49.99, "paid"), (2, 120.00, "refunded"), (3, 15.50, "paid")],
    )
    try:
        rows = conn.execute(query).fetchall()
        return json.dumps(rows)
    except Exception as e:
        return f"error: {e}"


TOOLS = {
    "calculate": tool_calculate,
    "sql_query": tool_sql_query,
}

TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Evaluate a math expression.",
            "parameters": {
                "type": "object",
                "properties": {"expression": {"type": "string"}},
                "required": ["expression"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "sql_query",
            "description": "Run a read-only SQL query against the orders table.",
            "parameters": {
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
            },
        },
    },
]


# --- Agent loop ------------------------------------------------------------

def run(task: str, max_steps: int = 8) -> str:
    messages = [
        {"role": "system", "content": "You are a careful assistant with tools. Use them when needed, then answer."},
        {"role": "user", "content": task},
    ]
    for step in range(max_steps):
        resp = client.chat.completions.create(
            model="gemini-2.5-pro",
            messages=messages,
            tools=TOOL_SCHEMAS,
        )
        msg = resp.choices[0].message
        messages.append(msg.model_dump(exclude_none=True))

        if not msg.tool_calls:
            return msg.content or ""

        for call in msg.tool_calls:
            name = call.function.name
            args = json.loads(call.function.arguments or "{}")
            result = TOOLS[name](**args)
            print(f"[step {step}] {name}({args}) -> {result[:80]}")
            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result,
            })

    return "max steps exceeded"


if __name__ == "__main__":
    print(run("What's the total revenue from paid orders, and what's that in EUR at 0.93 rate?"))
