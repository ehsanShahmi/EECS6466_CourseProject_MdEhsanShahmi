import difflib
import gzip
import unittest

def task_func(file_path1, file_path2):
    """
    Compares the contents of two gzip files and returns a string describing the differences between them.
    It reads the contents of each file, then uses difflib to compute and return the differences. 
    Only differences are returned, with an empty string indicating no differences.

    Parameters:
    file_path1 (str): The file path of the first gzip file.
    file_path2 (str): The file path of the second gzip file.

    Returns:
    str: A string describing the differences between the two files' contents.

    Requirements:
    - difflib
    - gzip

    Examples:
    Assuming 'file1.gz' and 'file2.gz' contain slightly different text,
    >>> result = task_func('file1.gz', 'file2.gz')
    >>> len(result) > 0
    True

    Assuming 'file1.gz' and 'file1.gz' are identical,
    >>> task_func('file1.gz', 'file1.gz')
    ''
    """
    with gzip.open(file_path1, 'rt') as file1, gzip.open(file_path2, 'rt') as file2:
        file1_content = file1.readlines()
        file2_content = file2.readlines()
        diff = difflib.ndiff(file1_content, file2_content)
        diff = [line for line in diff if line.startswith('+ ') or line.startswith('- ')]

    return ''.join(diff)

class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        # Create example gzip files for testing
        self.file1_path = 'file1.gz'
        self.file2_path = 'file2.gz'
        with gzip.open(self.file1_path, 'wt') as f:
            f.write("Hello World\nThis is a test file.\nGoodbye!")
        with gzip.open(self.file2_path, 'wt') as f:
            f.write("Hello World\nThis is a test text file.\nGoodbye!")

    def test_identical_files(self):
        result = task_func(self.file1_path, self.file1_path)
        self.assertEqual(result, '', "Identical files should return an empty string.")

    def test_different_files(self):
        result = task_func(self.file1_path, self.file2_path)
        self.assertNotEqual(result, '', "Different files should return a non-empty string.")

    def test_gzip_read(self):
        with gzip.open(self.file1_path, 'rt') as f:
            content = f.read()
        self.assertIn("Hello World", content, "File 1 content should include 'Hello World'.")

    def test_empty_file_comparison(self):
        empty_file_path = 'empty.gz'
        with gzip.open(empty_file_path, 'wt') as f:
            f.write("")
        result = task_func(empty_file_path, empty_file_path)
        self.assertEqual(result, '', "Comparing two empty files should return an empty string.")

    def tearDown(self):
        import os
        os.remove(self.file1_path)
        os.remove(self.file2_path)
        os.remove('empty.gz')

if __name__ == '__main__':
    unittest.main()