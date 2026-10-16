import unittest

# from functions import get_files_info
from functions.get_files_info import get_files_info


class system_function_test(unittest.TestCase):
    def test_get_files(self):
        accessible = get_files_info("calculator", ".")
        # print(f"DIAGNOSIS {accessible}")
        self.assertEqual(accessible,"""
result for .:
 - main.py: File Size=754bytes, is_dir=False
 - pkg: File Size=512bytes, is_dir=True
 - tests.py: File Size=1458bytes, is_dir=False""")

    def test_bin_files(self):
        with self.assertRaises(ValueError):
            _ = get_files_info("calculator", "/bin")

    def test_pkg_files(self):
        accessible = get_files_info("calculator", "pkg")
        self.assertEqual(accessible,"""
result for pkg:
 - calculator.py: File Size=2021bytes, is_dir=False
 - render.py: File Size=420bytes, is_dir=False
 - __pycache__: File Size=512bytes, is_dir=True""")


    def test_stopstop_files(self):
        with self.assertRaises(ValueError):
            _ = get_files_info("calculator", "../")

    def test_main_files(self):
        with self.assertRaises(ValueError):
            _ = get_files_info("calculator", "main.py")



if __name__ == "__main__":
    unittest.main()
