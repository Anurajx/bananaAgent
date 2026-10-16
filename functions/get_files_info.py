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
     # return f"directory {directory} is within working directory"
     #
     # result = f"result for {directory} is -"
     try:
         content = os.listdir(target_dir)
     except OSError as error:
         raise ValueError(f"Error: could not list content of {target_dir}") from error

     # print(f"CONTENT IS {content}")

     final_array= [f"\nresult for {directory}:"]
     for i in content:
         full_path = os.path.join(target_dir, i)
         # print(f"FULL PATH IS {full_path}")

         # print(i)
         try:
             size = os.path.getsize(full_path)
         except OSError as error:
             raise ValueError(f"Error: Could not deduce size of file or dir {i}") from error
         # print(f"SIZE IS: {size}")
         try:
             is_dir = os.path.isdir(full_path)
         except OSError as error:
             raise ValueError(f"Error: could not find size of {i}") from error

         # print(f"file {i} is {is_dir}")
         result = f" - {i}: File Size={size}bytes, is_dir={is_dir}"
         final_array.append(result)

     final_string = "\n".join(final_array)
     # print(f"{final_string}")
     return final_string
