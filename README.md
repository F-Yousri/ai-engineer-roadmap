# AI Engineer Roadmap

A 6-month, self-paced roadmap to pivot from backend engineering (PHP/Laravel, 7 yrs) into AI application engineering. Designed around free resources, LinkedIn Learning, and a Gemini + Ollama default stack.

**Time commitment:** ~8–10 hrs/week alongside a day job.
**Budget:** under $50 total. Most months are $0.

## Default Stack

- **Hosted LLMs:** [Google AI Studio](https://aistudio.google.com) — Gemini 2.5 Flash (default), 2.5 Pro (hard tasks). Free tier.
- **Local LLMs + embeddings:** [Ollama](https://ollama.com/) — `llama3.3:8b`, `qwen2.5:7b`, `nomic-embed-text`.
- **Fast open-model inference:** [Groq](https://console.groq.com/) — free tier, great for speed tests.
- **SDK pattern:** write code against the OpenAI Python SDK. Gemini, Groq, Ollama, OpenRouter all expose OpenAI-compatible endpoints. Swap providers by changing a base URL.

## Roadmap

| Month | Focus | Folder |
|-------|-------|--------|
| 1 | LLM foundations & API basics | [month-1-foundations](./month-1-foundations) |
| 2 | Retrieval, embeddings, RAG | [month-2-rag](./month-2-rag) |
| 3 | Evals & engineering discipline | [month-3-evals](./month-3-evals) |
| 4 | Agents & tool use | [month-4-agents](./month-4-agents) |
| 5 | Production: cost, latency, observability | [month-5-production](./month-5-production) |
| 6 | Specialize, publish, apply | [month-6-specialize](./month-6-specialize) |

## How to use this repo

Each month's folder has its own README with:
- Learning tasks with checkboxes — tick them as you go
- A deliverable project spec
- A `project/` subfolder to commit your work

Commit as you progress. By month 6 this repo is part of your portfolio.

## Meta-resources

See [resources/newsletters-and-blogs.md](./resources/newsletters-and-blogs.md) for the ~30 min/week reading list that keeps you oriented.
