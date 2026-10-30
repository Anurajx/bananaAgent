import argparse
import json
import os

from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console

from functions.get_file_content import schema_get_files_content
from functions.get_files_info import schema_get_files_info
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from prompts import system_prompt

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
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": args.user_prompt
        }
    ]

    console = Console()
    with console.status("Thinking machine"): #Animation
        response = generate_content(client, messageList)


    message = response.choices[0].message

    if message.tool_calls:
        for tool_call in message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            print(f"Calling function: {tool_call.function.name}({function_args})")
    elif response.usage and args.verbose:
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
        messages= messages,
        tools=available_functions
    )


available_functions = [
    schema_get_files_info,
    schema_get_files_content,
    schema_run_python_file,
    schema_write_file
]

if __name__ == "__main__":
    main()
