import argparse
import json
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console

from call_function import available_functions, call_function
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

    # messages=[] #Handles message history
    processComplete = False

    with console.status("Thinking machine"): #Animation
        for _ in range(20):
            response = generate_content(client, messageList)

            try:
                message = response.choices[0].message
            except:
                print("API response invalid, check your quota limit")
                break
            messageList.append(message)

            if message.tool_calls:
                for tool_call in message.tool_calls:
                    # function_args = json.loads(tool_call.function.arguments or "{}")
                    # print("STARTING EXECUTION")
                    result_message = call_function(tool_call, args.verbose)
                    messageList.append(result_message)
                    # print(f"-> {result_message['content']}")
                    # print(f"Calling function: {tool_call.function.name}({function_args})")
                    #
            elif response.usage and args.verbose:
                processComplete= True
                print(response.choices[0].message.content)
                print(f"Prompt Token: {response.usage.prompt_tokens}")
                print(f"Response Token: {response.usage.completion_tokens}")
                break

            elif not args.verbose:
                processComplete= True
                print(response.choices[0].message.content)
                break
            else:
                processComplete= True
                if not response.usage:
                    raise RuntimeError("response usage not found")


    if not processComplete:
        print("Agent could not complete given task in given time")
        sys.exit(1)





def generate_content(client, messages):
    return client.chat.completions.create(
        model= "openrouter/free",
        messages= messages,
        tools=available_functions
    )




if __name__ == "__main__":
    main()
