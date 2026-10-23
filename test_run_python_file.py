import unittest

# from functions import run_python_file
from functions.run_python_file import run_python_file


class system_run_function_test(unittest.TestCase):
    def test_get_files(self):
        accessible = run_python_file("calculator", "main.py")
        # print(f"{accessible}")
        self.assertEqual(accessible,"""STDERR: and STDOUT:Calculator App
Usage: python main.py "<expression>"
Example: python main.py "3 + 5"
 Done""")

    def test_run_nasty_files(self):
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        # print(result)
        self.assertEqual(result,'STDERR: and STDOUT:{\n'
                '  "expression": "3 + 5",\n'
                '  "result": 8\n'
                '}\n'
                ' Done')

    def test_success_run_files(self):
        accessible = run_python_file("calculator", "tests.py")
        # print(accessible)
        self.assertIn("STDERR:.........", accessible)
        self.assertIn("OK", accessible)
        self.assertTrue(accessible.endswith(" and STDOUT: Done"))


    def test_run_error_files(self):
        result = run_python_file("calculator", "../main.py")
        # print(result)
        self.assertEqual(result,"""Error: Cannot write to "../main.py" as it is outside the permitted working directory""")

    def test_run_errorAgain_files(self):
        result = run_python_file("calculator", "nonexistent.py")
        # print(result)
        self.assertEqual(result,"""Error: "nonexistent.py" does not exist or is not a regular file""")

    def test_run_errorAgainAgain_files(self):
        result = run_python_file("calculator", "lorem.txt")
        # print(result)
        self.assertEqual(result,"""Error: "lorem.txt" is not a Python file""")


if __name__ == "__main__":
    unittest.main()
