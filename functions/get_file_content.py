import os

import config


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs_path = os.path.abspath(working_directory) #Deduces absolute path starting from root
        if not working_dir_abs_path:
            return (f"Error: failed to get absolute path of {working_directory}")

        target_dir =  os.path.normpath(os.path.join(working_dir_abs_path, file_path)) # join file path and the absolute dir path then format it to norm path
        if not target_dir:
            return (f"Error: failed to resolve target directory {file_path}")


        if_valid_target = os.path.commonpath([working_dir_abs_path, target_dir]) == working_dir_abs_path
        if not if_valid_target:
            return (f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
        if not os.path.isfile(target_dir):
            return (f'Error: File not found or is not a regular file: {file_path}')


        with open(target_dir,'r') as f:
            content = f.read(config.MAX_CHARS)
            if f.read(1):
                content += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'

    except Exception as error:
        raise ValueError(f"Error: could not read {file_path}") from error

    return content
