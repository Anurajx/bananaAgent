import os


def get_files_info(working_directory: str, directory: str = ".") -> str:
     try:
         working_dir_abs_path = os.path.abspath(working_directory)
         if not working_dir_abs_path:
             return (f"Error: failed to get absolute path of {working_directory}")

         target_dir =  os.path.normpath(os.path.join(working_dir_abs_path, directory))
         if not target_dir:
             return (f"Error: failed to resolve target directory {directory}")

         if_valid_target = os.path.commonpath([working_dir_abs_path, target_dir]) == working_dir_abs_path
         if not if_valid_target:
             return (f"Error: the target path {target_dir} is out of allowed dir scope for agent")

         if not os.path.isdir(target_dir):
             return (f"Error: the target dir {target_dir} does not exist")
     # return f"directory {directory} is within working directory"
     #
     # result = f"result for {directory} is -"

         content = os.listdir(target_dir)
     except OSError as error:
         return (f"Error: could not list content of {directory} Logs: {error}")

     # print(f"CONTENT IS {content}")

     final_array= [f"\nresult for {directory}:"]
     for i in content:
         full_path = os.path.join(target_dir, i)
         # print(f"FULL PATH IS {full_path}")

         # print(i)
         try:
             size = os.path.getsize(full_path)
             if not size:
                 return(f"Error: Could not deduce size of file or dir {i}")
         # print(f"SIZE IS: {size}")
             is_dir = os.path.isdir(full_path)
         except OSError as error:
             return (f"Error: could not find information of {i} Logs:{error}")

         # print(f"file {i} is {is_dir}")
         result = f" - {i}: File Size={size}bytes, is_dir={is_dir}"
         final_array.append(result)

     final_string = "\n".join(final_array)
     # print(f"{final_string}")
     return final_string
