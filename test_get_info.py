import unittest

from functions import get_files_info


class system_function_test(unittest.TestCase):
    def test_get_files(self):
        accessible = get_files_info.get_files_info("calculator", ".")
        print(accessible)
        self.assertEqual(accessible,"directory . is whitin working directory")

    def test_bin_files(self):
        with self.assertRaises(ValueError):
            _ = get_files_info.get_files_info("calculator", "/bin")

    def test_stopstop_files(self):
        with self.assertRaises(ValueError):
            _ = get_files_info.get_files_info("calculator", "../")

    def test_main_files(self):
        with self.assertRaises(ValueError):
            _ = get_files_info.get_files_info("calculator", "main.py")



if __name__ == "__main__":
    unittest.main()
