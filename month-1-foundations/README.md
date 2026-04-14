# Month 1 — Foundations

**Goal:** understand LLMs as a building block. Get comfortable calling an LLM API and shaping outputs with prompts.

**Primary stack:** Gemini 2.5 Flash via [Google AI Studio](https://aistudio.google.com/apikey).

## Learning tasks

### Watch / read
- [ ] [Andrej Karpathy — Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g) (1 hr)
- [ ] [Google — Gemini API quickstart](https://ai.google.dev/gemini-api/docs/quickstart)
- [ ] [Google — Prompting strategies for Gemini](https://ai.google.dev/gemini-api/docs/prompting-strategies)

### Hands-on
- [ ] Work through [Anthropic's API Fundamentals course](https://github.com/anthropics/courses/tree/master/anthropic_api_fundamentals) (point examples at Gemini — swap 2 lines)
- [ ] Work through [Anthropic's Prompt Engineering Interactive Tutorial](https://github.com/anthropics/courses/tree/master/prompt_engineering_interactive_tutorial)

### LinkedIn Learning
- [ ] Generative AI for Developers (Morten Rand-Hendriksen)
- [ ] Introduction to Prompt Engineering for Generative AI (Ronnie Sheer)

## Deliverable

Build a small app that uses Gemini to do something non-trivial. Examples:
- Inbox summarizer
- Support ticket classifier with structured JSON output
- "Explain this Laravel error" CLI tool

Ship it somewhere real (Railway, Fly.io, your VPS). Commit the code into `project/`.

**Checklist:**
- [ ] App works end-to-end
- [ ] Uses structured output (JSON mode or schema)
- [ ] Has a README explaining what it does and what you learned
- [ ] Deployed to a real URL (or at least a working Docker image)
