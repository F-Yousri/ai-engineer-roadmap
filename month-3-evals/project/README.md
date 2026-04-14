# Month 3 project — Evals

Build on top of month 2. This folder assumes month 2 project is working.

## Setup
```bash
pip install -r ../../month-2-rag/project/requirements.txt
cp ../../month-2-rag/project/.env .env
```

## Run
```bash
# Edit eval_set.json to match YOUR corpus
python evaluate.py
cat results.json
```

## Your task
- [ ] Grow eval_set.json to 20–50 realistic questions
- [ ] Tag each question by difficulty (easy/medium/hard)
- [ ] Add a regression guard: fail CI if avg precision drops below threshold
- [ ] Try promptfoo.yaml for the same tests — compare DX
- [ ] Write findings in results.md (not just numbers — what surprised you?)
