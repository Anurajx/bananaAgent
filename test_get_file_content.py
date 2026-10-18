import unittest

from functions.get_file_content import get_file_content


class system_file_content_function(unittest.TestCase):
    def test_lorem_text(self):
        result = get_file_content("calculator", "lorem.txt")
        print(f"lorem.txt length: {len(result)}")
        print(f"lorem.txt truncated: {'truncated' in result}")

    def test_calc_mainpy(self):
        result = get_file_content("calculator", "main.py")
        print(result)

    def test_calc_pkg_calcpy(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)

    def test_err_calc_bin(self):
        result = get_file_content("calculator", "/bin/cat")
        self.assertEqual(result,"""Error: Cannot read "/bin/cat" as it is outside the permitted working directory""")

    def test_err_pkg_notExist(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        self.assertEqual(result,"""Error: File not found or is not a regular file: pkg/does_not_exist.py""")


if __name__ == "__main__":
    unittest.main()
