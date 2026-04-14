# Month 5 — Production Concerns

**Goal:** turn your prototype into something with production-grade observability, cost control, and resilience. This is where 7 years of backend experience is a direct advantage.

## Learning tasks

### Observability (pick one and actually instrument)
- [ ] [Langfuse](https://langfuse.com/) — open-source, self-host free
- [ ] [Helicone](https://www.helicone.ai/) — alternative
- [ ] [LangSmith](https://www.langchain.com/langsmith) — paid, but trial works

### Reading
- [ ] [Chip Huyen — AI Engineering](https://www.oreilly.com/library/view/ai-engineering/9781098166298/) (the one book worth buying; on O'Reilly subscription if you have it)
- [ ] [Google — Responsible AI guidelines for Gemini](https://ai.google.dev/gemini-api/docs/safety-guidance)
- [ ] [Anthropic — Prompt caching](https://docs.claude.com/en/docs/build-with-claude/prompt-caching)
- [ ] [Anthropic — Batch API](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

### LinkedIn Learning
- [ ] LLMOps: Building Real-World Applications With Large Language Models

## Deliverable

Harden your project.

**Requirements:**
- [ ] Response caching (prompt + input hash → response)
- [ ] Fallback chain: Gemini Flash → Groq Llama → local Ollama (graceful degradation)
- [ ] Rate limiting and retry with backoff
- [ ] Structured logs with request IDs
- [ ] Cost dashboard: per request, per feature, per day
- [ ] Observability tool wired up (Langfuse recommended)
- [ ] Safety: input/output moderation, PII redaction for logs
- [ ] Write a blog post on your tradeoffs. Commit as `project/blog.md`.
