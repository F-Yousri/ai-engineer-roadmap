import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

def translate(text: str, target_language: str) -> str:
    """Translates text to a target language. Example of a simple text transformation.
    """
    resp = client.chat.completions.create(
        model="gemini-2.5-flash",
        max_tokens=1000,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant that translates text to a target language."
                ),
            },
            {
                "role": "user",
                "content": f'Translate the following text to {target_language}: "{text}"',
            },
        ],
    )
    return resp.choices[0].message.content.strip()

if __name__ == "__main__":
    sample_text = "Hello, how are you?"
    target_lang = "Spanish"
    print(translate(sample_text, target_lang))