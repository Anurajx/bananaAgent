import unittest

# from functions import get_files_info
from functions.get_files_info import get_files_info


class system_get_function_test(unittest.TestCase):
    def test_get_files(self):
        accessible = get_files_info("calculator", ".")
        # print(f"DIAGNOSIS {accessible}")
        self.assertEqual(accessible,"""
result for .:
 - lorem.txt: File Size=20928bytes, is_dir=False
 - main.py: File Size=754bytes, is_dir=False
 - pkg: File Size=512bytes, is_dir=True
 - tests.py: File Size=1458bytes, is_dir=False""")

    def test_bin_files(self):
        result = get_files_info("calculator", "/bin")
        # print(result)
        self.assertEqual(result,"Error: the target path /bin is out of allowed dir scope for agent")

    def test_pkg_files(self):
        accessible = get_files_info("calculator", "pkg")
        print(accessible)
        self.assertEqual(accessible,"""
result for pkg:
 - calculator.py: File Size=2021bytes, is_dir=False
 - morelorem.txt: File Size=512bytes, is_dir=True
 - render.py: File Size=420bytes, is_dir=False
 - __pycache__: File Size=512bytes, is_dir=True""")


    def test_stopstop_files(self):
        result = get_files_info("calculator", "../")
        # print(result)
        self.assertEqual(result,"Error: the target path /mnt/c/Users/anura/Desktop/bananaAgent is out of allowed dir scope for agent")

    def test_main_files(self):
        result = get_files_info("calculator", "main.py")
        # print(result)
        self.assertEqual(result,"Error: the target dir /mnt/c/Users/anura/Desktop/bananaAgent/calculator/main.py does not exist")



if __name__ == "__main__":
    unittest.main()
