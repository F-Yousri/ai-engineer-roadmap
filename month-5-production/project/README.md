# Month 5 project — Production hardening

## Run the client
```bash
pip install -r requirements.txt
cp .env.example .env
python llm_client.py
```
You'll see: a response, then a cache hit on the second call, then a cost summary.

## Run Langfuse (observability)
```bash
docker compose -f langfuse-compose.yml up -d
# open http://localhost:3000, create an account, grab keys
# then instrument llm_client.py via the langfuse Python SDK
```

## Your task
- [ ] Wire llm_client into your month 2/3/4 projects — delete direct OpenAI calls
- [ ] Add rate limiting (token bucket) and retry-with-backoff
- [ ] Add structured logging with request IDs
- [ ] Add input/output moderation (Gemini's safety settings + regex for PII)
- [ ] Build a small dashboard (even `cost_summary()` counts) showing daily cost
- [ ] Write a blog post on your tradeoffs — commit as blog.md
