"""
Ingest documents: chunk, embed (local via Ollama), store in pgvector.

Prereqs:
  docker compose up -d
  psql postgresql://rag:rag@localhost:5432/rag -f schema.sql
  ollama pull nomic-embed-text
"""
import os
import sys
import psycopg
import requests
from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/embeddings"
DB_URL = "postgresql://rag:rag@localhost:5432/rag"


def embed(text: str) -> list[float]:
    r = requests.post(OLLAMA_URL, json={"model": "nomic-embed-text", "prompt": text})
    r.raise_for_status()
    return r.json()["embedding"]


def chunk(text: str, size: int = 500, overlap: int = 50) -> list[str]:
    """Simple word-based chunker. Swap for semantic chunking in a real system."""
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunks.append(" ".join(words[i:i + size]))
        i += size - overlap
    return chunks


def ingest_file(path: Path, conn) -> int:
    text = path.read_text(encoding="utf-8", errors="ignore")
    chunks = chunk(text)
    with conn.cursor() as cur:
        for idx, c in enumerate(chunks):
            vec = embed(c)
            cur.execute(
                "INSERT INTO documents (source, chunk_index, content, embedding) "
                "VALUES (%s, %s, %s, %s)",
                (str(path), idx, c, str(vec)),
            )
        conn.commit()
    return len(chunks)


if __name__ == "__main__":
    folder = Path(sys.argv[1] if len(sys.argv) > 1 else "./docs")
    with psycopg.connect(DB_URL) as conn:
        total = 0
        for f in folder.rglob("*.md"):
            n = ingest_file(f, conn)
            print(f"{f}: {n} chunks")
            total += n
        print(f"Done. {total} chunks indexed.")
