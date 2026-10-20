import os

def write_file(working_directory: str, file_path: str, content: str) -> str :
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

        if os.path.isdir(target_file):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

    except OSError as error:
        raise ValueError(f'Error: Cannot write to "{file_path}" as something went wrong calling write_file function') from error
    return ""
