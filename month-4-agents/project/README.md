# Month 4 project — Agent with tools

## Run
```bash
pip install -r requirements.txt
cp ../../month-1-foundations/project/.env .env  # reuse the key
python agent.py
```

## Your task
- [ ] Replace the toy tools with real ones from your month 2 project
      (e.g., `rag_search(question)` that calls your retriever)
- [ ] Add error handling: what happens when a tool fails?
- [ ] Log every step (you'll want this in month 5)
- [ ] Run the same task on Gemini 2.5 Pro and Claude Sonnet — document differences
- [ ] Re-use month 3's eval harness to score the agent vs. a non-agent baseline
