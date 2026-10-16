import os

def get_file_contnet(working_directory: str, file_path: str) -> str:
    try:
        working_dir_abs_path = os.path.abspath(working_directory) #Deduces absolute path starting from root
    except Exception as Error:
        raise ValueError(f"Error: failed to get absolute path of {working_directory}") from Error

    try:
        target_dir =  os.path.normpath(os.path.join(working_dir_abs_path, file_path)) # join file path and the absolute dir path then format it to norm path
    except Exception as Error:
        raise ValueError(f"Error: failed to resolve target directory {file_path}") from Error


    if_valid_target = os.path.commonpath([working_dir_abs_path, target_dir]) == working_dir_abs_path
    if not if_valid_target:
        raise ValueError(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    if not os.path.isdir(target_dir):
        raise ValueError(f'Error: File not found or is not a regular file: "{file_path}"')
    return ""
