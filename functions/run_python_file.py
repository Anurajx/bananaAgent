import os
import subprocess
import sys


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_dir_abs_path = os.path.abspath(working_directory)
        if not working_dir_abs_path:
            return (f"Error: failed to get absolute path of {working_directory}")

        target_file =  os.path.normpath(os.path.join(working_dir_abs_path, file_path))
        if not target_file:
            return (f"Error: failed to resolve target directory {file_path}")


        if_valid_target = os.path.commonpath([working_dir_abs_path, target_file]) == working_dir_abs_path
        if not if_valid_target:
            return (f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = [sys.executable , target_file]
        if args:
            command.extend(args or [])
        try:
            completed = subprocess.run(command, text=True, capture_output=True ,timeout=30,check=False)
            output = ""
            if completed.returncode != 0:
                output+=f"""Process exited with code {completed.returncode}\n"""
            if not completed.stderr and not completed.stdout :
                output+="""No output produced\n"""
            else:
                output+=f"""STDERR:{completed.stderr} and STDOUT:{completed.stdout} Done"""

            return output
        except subprocess.TimeoutExpired:
            return "Error: The process timed out after 30 seconds."

        except Exception as e:
              return f"Error running subprocess: {str(e)}"

    except OSError as error:
        return f'Error: something went wrong calling run_python_file function Logs:{error}'





schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs python file with provided arguments in a specified directory relative to the working directory, at end returns output of python program",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to execute python program from, relative to the working directory",
                },
                "args": {
                    "type": "list[str] | None",
                    "description": "List of arguments to give to python file, it can be None (default is None)",
                },
            },
        },
    },
}
