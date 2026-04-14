"""
Minimal eval harness. Runs questions through your RAG, computes:
  - retrieval: precision@k vs. expected sources
  - generation: LLM-as-judge score (faithfulness, relevance)

This is deliberately ~100 lines so you can read it all. Graduate to
promptfoo or Inspect AI once you understand it.
"""
import json
import os
import sys
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "month-2-rag" / "project"))
from query import retrieve, answer  # reuse month 2 code

judge = OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


def precision_at_k(retrieved_sources: list[str], expected: list[str], k: int) -> float:
    top = retrieved_sources[:k]
    if not top:
        return 0.0
    hits = sum(1 for s in top if any(e in s for e in expected))
    return hits / len(top)


def judge_answer(question: str, ans: str, rubric: str) -> dict:
    resp = judge.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role": "system",
                "content": (
                    "Score the answer against the rubric. Return JSON with "
                    "faithfulness (0-5), relevance (0-5), notes (string)."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Question: {question}\n\nRubric: {rubric}\n\nAnswer: {ans}"
                ),
            },
        ],
        response_format={"type": "json_object"},
    )
    return json.loads(resp.choices[0].message.content)


def run(path: str = "eval_set.json", k: int = 5):
    cases = json.loads(Path(path).read_text())
    results = []
    for case in cases:
        retrieved = retrieve(case["question"], k=k)
        sources = [src for src, _ in retrieved]
        p_at_k = precision_at_k(sources, case["expected_sources"], k)
        ans = answer(case["question"])
        scores = judge_answer(case["question"], ans, case["rubric"])
        results.append({
            "question": case["question"],
            "precision_at_k": p_at_k,
            "faithfulness": scores["faithfulness"],
            "relevance": scores["relevance"],
            "answer": ans,
            "notes": scores.get("notes", ""),
        })
        print(f"Q: {case['question']}")
        print(f"  p@{k}={p_at_k:.2f}  faith={scores['faithfulness']}  rel={scores['relevance']}")

    avg_p = sum(r["precision_at_k"] for r in results) / len(results)
    avg_f = sum(r["faithfulness"] for r in results) / len(results)
    avg_r = sum(r["relevance"] for r in results) / len(results)
    print(f"\nAverages: precision@{k}={avg_p:.2f}  faithfulness={avg_f:.2f}  relevance={avg_r:.2f}")
    Path("results.json").write_text(json.dumps(results, indent=2))


if __name__ == "__main__":
    run()
