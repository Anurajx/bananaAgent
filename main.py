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
    print(r"""
 __                                
|__) _  _  _  _  _   /\  _  _ _ |_ 
|__)(_|| )(_|| )(_| /--\(_)(-| )|_ 
                        _/         """)
    
    parser = argparse.ArgumentParser(description="chatbot")
    parser.add_argument("user_prompt",type=str,help="User Prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    messageList = [
        {
            "role": "user",
            "content": args.user_prompt
        }
    ]
    
    response = generate_content(client, messageList)
    
    
    
    if response.usage and args.verbose:
        print(response.choices[0].message.content)
        print(f"Prompt Token: {response.usage.prompt_tokens}")
        print(f"Response Token: {response.usage.completion_tokens}")
    elif not args.verbose:
        print(response.choices[0].message.content)
    else:
        if not response.usage:
            raise RuntimeError("response usage not found")

def generate_content(client, messages):
    return client.chat.completions.create(
        model= "openrouter/free",
        messages= messages
    )

if __name__ == "__main__":
    main()
