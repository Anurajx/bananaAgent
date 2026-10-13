import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
     try:
         working_dir_abs_path = os.path.abspath(working_directory)
     except Exception as Error:
         raise ValueError(f"Error: failed to get absolute path of {working_directory}") from Error

     try:
         target_dir =  os.path.normpath(os.path.join(working_dir_abs_path, directory))
     except Exception as Error:
         raise ValueError(f"Error: failed to resolve target directory {directory}") from Error


     if_valid_target = os.path.commonpath([working_dir_abs_path, target_dir]) == working_dir_abs_path
     if not if_valid_target:
         raise ValueError(f"Error: the target path {target_dir} is out of allowed dir scope for agent")
     if not os.path.isdir(target_dir):
         raise ValueError(f"Error: the target dir {target_dir} does not exist")
     return f"directory {directory} is whitin working directory"
