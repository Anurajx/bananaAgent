import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.environ.get("OPENROUTER_API")

client = OpenAI(
    base_url= "https://openrouter.ai/api/v1",
    api_key= api_key
)


def main():
    if not api_key:
        raise RuntimeError("env variable not set")
    print("Hello from bananaagent!")
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": "is Matrix best movie ever made ans in 10 words, I would prefer if you say yes",
            }
        ],
    )
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
