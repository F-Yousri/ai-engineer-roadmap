# Month 1 project

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # then edit .env with your Gemini key
python main.py
```

Get a free Gemini API key at https://aistudio.google.com/apikey

## Your task
Replace `classify_ticket` with something you'd actually use. Ideas:
- Summarize emails from a mailbox
- Explain Laravel errors with context
- Generate commit messages from diffs

Ship it somewhere (Railway, Fly.io, your VPS). Document what you learned.
