import unittest

from functions.write_file import write_file


class test_write_fileFunction(unittest.TestCase):


    def test_ordinary_write(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        # print(result)
        self.assertEqual(result, """Success: Successfully wrote to "lorem.txt" (28 characters written)""")

    def test_file_write(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        # print(result)
        self.assertEqual(result,"""Success: Successfully wrote to "pkg/morelorem.txt" (26 characters written)""")

    def test_not_allowedWrite(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        # print(result)
        self.assertEqual(result,"""Error: Cannot write to "/tmp/temp.txt" as it is outside the permitted working directory""")

if __name__ == "__main__":
    unittest.main()
