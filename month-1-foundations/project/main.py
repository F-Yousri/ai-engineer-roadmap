"""
Month 1 starter: call Gemini via the OpenAI-compatible SDK.

Why OpenAI SDK? So your code stays portable. Swap base_url + model to
switch between Gemini, Groq, Ollama, OpenRouter — no code changes.
"""
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)


def classify_ticket(text: str) -> dict:
    """Example: structured output. Classifies a support ticket."""
    resp = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[
            {
                "role": "system",
                "content": (
                    "You classify support tickets. Return JSON with keys: "
                    "category (billing|technical|account|other), "
                    "urgency (low|medium|high), summary (one sentence)."
                ),
            },
            {"role": "user", "content": text},
        ],
        response_format={"type": "json_object"},
    )
    import json
    return json.loads(resp.choices[0].message.content)


if __name__ == "__main__":
    sample = "My server has been down since 3am and I'm losing customers. Please help ASAP."
    print(classify_ticket(sample))
