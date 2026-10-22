import unittest

# from functions import run_python_file
from functions.run_python_file import run_python_file


class system_run_function_test(unittest.TestCase):
    def test_get_files(self):
        accessible = run_python_file("calculator", "main.py")
        # print(f"DIAGNOSIS {accessible}")
        self.assertEqual(accessible,"""Error: something went wrong calling run_python_file function Logs:[Errno 2] No such file or directory: 'python'""")

    def test_run_nasty_files(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        # print(result)
        self.assertEqual(result,"Error: something went wrong calling run_python_file function Logs:[Errno 2] No such file or directory: 'python'")

    def test_success_run_files(self):
        accessible = run_python_file("calculator", "tests.py")
        # print(accessible)
        self.assertEqual(accessible,"""Error: something went wrong calling run_python_file function Logs:[Errno 2] No such file or directory: 'python'""")


#     def test_run_error_files(self):
#         result = run_python_file("calculator", "../main.py")
#         # print(result)
#         self.assertEqual(result,"Error: the target path /mnt/c/Users/anura/Desktop/bananaAgent is out of allowed dir scope for agent")

#     def test_run_errorAgain_files(self):
#         result = run_python_file("calculator", "nonexistent.py")
#         # print(result)
#         self.assertEqual(result,"Error: the target dir /mnt/c/Users/anura/Desktop/bananaAgent/calculator/main.py does not exist")

#     def test_run_errorAgainAgain_files(self):
#         result = run_python_file("calculator", "lorem.txt")
#         print(result)


if __name__ == "__main__":
    unittest.main()
