import os
import subprocess
from xxlimited import Error


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

        command = ["python", target_file]
        command.extend(args or [])
        try:
            completed = subprocess.run(command, text=True, capture_output=True ,timeout=30,check=False)
            output = ""
            if completed.returncode != 0:
                output+=f"""Process exited with code {completed.returncode}"""
            if completed.stderr is None and completed.stdout is None:
                output+="""No output produced"""
            else:
                output+=f"""STDERR:{completed.stderr} and STDOUT:{completed.stdout}"""

            return output
        except :
            return f"Waassipppp"

    except OSError as error:
        return f'Error: something went wrong calling run_python_file function Logs:{error}'
