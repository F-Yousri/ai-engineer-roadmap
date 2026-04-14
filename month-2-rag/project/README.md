# Month 2 project — Local RAG

## Setup
```bash
# 1. Postgres + pgvector
docker compose up -d
psql postgresql://rag:rag@localhost:5432/rag -f schema.sql

# 2. Ollama for embeddings
# install from https://ollama.com
ollama pull nomic-embed-text

# 3. Python deps
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # add your Gemini key
```

## Use
```bash
# Put your markdown docs in ./docs/ then:
python ingest.py ./docs
python query.py "your question here"
```

## Your task

Swap the `./docs` input for a dataset you care about (your notes, Laravel
docs, a codebase). Build a 20–50 question eval set in `eval_set.json`
with expected source files and run retrieval precision@k. Write findings
in this README.
