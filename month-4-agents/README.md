# Month 4 — Agents and Tool Use

**Goal:** build an agent that uses tools to accomplish multi-step tasks, and understand when an agent is the right pattern vs. overkill.

**Primary stack:** Gemini 2.5 Pro for iteration. Optional: $10 of Anthropic credit at the end to compare Claude on the same task.

## Learning tasks

### Essential reading
- [ ] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) (read twice)
- [ ] [Google — Function calling with Gemini](https://ai.google.dev/gemini-api/docs/function-calling)
- [ ] [Anthropic — Tool use docs](https://docs.claude.com/en/docs/build-with-claude/tool-use)

### Hands-on
- [ ] [LangGraph tutorials](https://langchain-ai.github.io/langgraph/tutorials/) — agent + multi-agent examples
- [ ] Explore the [Claude Agent SDK](https://docs.claude.com/en/api/agent-sdk)

## Deliverable

Rebuild part of your month-2 project as an agent that uses tools.

**Requirements:**
- [ ] Agent uses at least 3 tools (e.g., SQL query, web fetch, calculator)
- [ ] Handles failure modes: retries, tool errors, bad outputs
- [ ] Compare agent vs. non-agent versions on the same eval set
- [ ] Track cost per task and latency
- [ ] Write up findings: when is the agent worth the cost/latency? Commit as `project/findings.md`

### Stretch
- [ ] Run the same agent on Gemini 2.5 Pro and Claude Sonnet. Document differences.
