import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

conversation_history = []

while True:
    user_input = input("User: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    conversation_history.append({"role": "user", "content": user_input})

    resp = client.chat.completions.create(
        model="gemini-2.5-flash",
        max_tokens=1000,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful assistant that engages in a conversation with the user."
                ),
            },
            *conversation_history,
        ],
    )

    assistant_response = resp.choices[0].message.content.strip()
    print(f"Assistant: {assistant_response}")
    conversation_history.append({"role": "assistant", "content": assistant_response})