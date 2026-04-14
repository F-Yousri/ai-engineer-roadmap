# Month 2 — Retrieval, Embeddings, and RAG

**Goal:** build a retrieval-augmented generation system end-to-end and understand each layer.

**Primary stack:** Ollama for embeddings (`nomic-embed-text`), pgvector for storage, Gemini Flash for generation. Zero cost.

## Learning tasks

### DeepLearning.AI short courses (free)
- [ ] [Building and Evaluating Advanced RAG](https://www.deeplearning.ai/short-courses/building-evaluating-advanced-rag/)
- [ ] [Preprocessing Unstructured Data for LLM Applications](https://www.deeplearning.ai/short-courses/preprocessing-unstructured-data-for-llm-applications/)
- [ ] [Vector Databases: from Embeddings to Applications](https://www.deeplearning.ai/short-courses/vector-databases-embeddings-applications/)

### Reading
- [ ] [Pinecone Learning Center — RAG section](https://www.pinecone.io/learn/)
- [ ] [pgvector README](https://github.com/pgvector/pgvector)
- [ ] [Supabase pgvector guide](https://supabase.com/docs/guides/ai)

### LinkedIn Learning
- [ ] Advanced RAG Applications with Vector Databases

## Deliverable

RAG system over a dataset you care about (your notes, a codebase, company docs).

**Requirements:**
- [ ] Ingestion pipeline with chunking strategy documented
- [ ] Embeddings via Ollama `nomic-embed-text` (local, free)
- [ ] Storage in pgvector (Postgres)
- [ ] Generation via Gemini Flash
- [ ] A small hand-labeled eval set (20–50 queries) with expected sources
- [ ] Measure retrieval precision/recall; write findings in README

Commit into `project/`.
