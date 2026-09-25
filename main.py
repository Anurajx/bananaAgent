import os
from dotenv import load_dotenv
from openai import OpenAI
import argparse

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
    
    parser = argparse.ArgumentParser(description="chatbot")
    parser.add_argument("user_prompt",type=str,help="User Prompt")
    args = parser.parse_args()
    
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": args.user_prompt,
            }
        ],
    )
    
    
    
    if response.usage :
        print(f"Prompt Token: {response.usage.prompt_tokens}")
        print(f"Response Token: {response.usage.completion_tokens}")
    else:
        raise RuntimeError("response usage not found")
    
    print(response.choices[0].message.content)

if __name__ == "__main__":
    main()
