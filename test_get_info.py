import unittest

from functions import get_files_info


class system_function_test(unittest.TestCase):
    def test_get_files(self):
        accessible = get_files_info.get_files_info("calculator", ".")
        print(accessible)
        self.assertEqual(accessible,"directory . is whitin working directory")


if __name__ == "__main__":
    unittest.main()
