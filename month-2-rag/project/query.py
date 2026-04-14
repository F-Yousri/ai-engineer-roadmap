"""
Query the RAG: embed question, retrieve top-k, generate with Gemini.
"""
import os
import sys
import psycopg
import requests
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

OLLAMA_URL = "http://localhost:11434/api/embeddings"
DB_URL = "postgresql://rag:rag@localhost:5432/rag"

client = OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


def embed(text: str) -> list[float]:
    r = requests.post(OLLAMA_URL, json={"model": "nomic-embed-text", "prompt": text})
    r.raise_for_status()
    return r.json()["embedding"]


def retrieve(question: str, k: int = 5) -> list[tuple[str, str]]:
    vec = embed(question)
    with psycopg.connect(DB_URL) as conn, conn.cursor() as cur:
        cur.execute(
            "SELECT source, content FROM documents "
            "ORDER BY embedding <=> %s::vector LIMIT %s",
            (str(vec), k),
        )
        return cur.fetchall()


def answer(question: str) -> str:
    chunks = retrieve(question)
    context = "\n\n---\n\n".join(f"[{src}]\n{txt}" for src, txt in chunks)
    resp = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer using only the provided context. Cite sources inline "
                    "like [source]. If the context is insufficient, say so."
                ),
            },
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
        ],
    )
    return resp.choices[0].message.content


if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "What is this project about?"
    print(answer(q))
