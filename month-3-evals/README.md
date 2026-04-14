# Month 3 — Evaluations

**Goal:** learn the engineering discipline that separates toys from products. This is where your senior backend instincts shine.

**Primary stack:** Gemini as LLM-judge (cheap/free). Open-source eval frameworks.

## Learning tasks

### Reading (essential)
- [ ] [Hamel Husain — Your AI product needs evals](https://hamel.dev/blog/posts/evals/)
- [ ] Read the rest of [Hamel's blog](https://hamel.dev/) — especially posts on LLM evaluations and fine-tuning
- [ ] [Eugene Yan — applied-llms.org](https://applied-llms.org/)

### Tools (pick one and use it)
- [ ] [promptfoo](https://www.promptfoo.dev/) — provider-agnostic eval framework
- [ ] [Inspect AI](https://inspect.aisi.org.uk/) — alternative, built by UK AISI

### DeepLearning.AI
- [ ] [Automated Testing for LLMOps](https://www.deeplearning.ai/short-courses/automated-testing-llmops/)

## Deliverable

Add a full eval suite to your month-2 RAG project.

**Requirements:**
- [ ] Retrieval evals: precision@k, recall@k on your labeled set
- [ ] Generation evals: LLM-as-judge with a rubric (faithfulness, relevance, completeness)
- [ ] Regression tests: CI fails if key metrics drop
- [ ] Eval results written to `project/evals/results.md` with a history

Write a short blog post (Dev.to, Medium, your site) explaining what you measured and what surprised you. Commit the draft in `project/blog.md`.
