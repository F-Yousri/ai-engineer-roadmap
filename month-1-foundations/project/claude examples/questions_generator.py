import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

def generate_questions(topic, num_questions=5) -> str:
    """Generates questions about a given topic."""
    resp = client.chat.completions.create(
        model = "gemini-2.5-flash",
        max_tokens = 10000,
        messages = [
            {
                "role": "system",
                "content": f'you are an expert in {topic}. be brief and to the point when generating questions.' 
            },
            {
                "role": "user",
                "content": f'generate {num_questions} questions about {topic}.'
            }
        ]
    )
    return resp.choices[0].message.content.strip()

if __name__ == "__main__":
    topic = "Artificial Intelligence"
    num_questions = 5
    print(
        generate_questions(topic, num_questions)
    )