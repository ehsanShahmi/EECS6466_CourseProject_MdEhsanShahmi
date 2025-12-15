import unittest
import tempfile
import os
import mimetypes

# Here is your prompt:
import re
import os
import glob
import mimetypes

def task_func(directory, file_pattern, suffix):
    """
    Scans a specified directory for files matching a given pattern and with a certain suffix, then determines their file types.
    The function returns a dictionary with file names as keys and their corresponding MIME types as values.

    Parameters:
        directory (str): The path to the directory to scan.
        file_pattern (str): The pattern to match files against.
        suffix (str): The suffix that files must have to be included.

    Returns:
        dict: A dictionary mapping file names to their MIME types.

    Requirements:
    - re
    - os
    - glob
    - mimetypes

    Examples:
    >>> isinstance(task_func(r'dir', '*', '_suff), dict)
    True
    >>> 'example_suff.txt' in task_func(r'dir', '*_suff.txt', '_suff')
    True  # This example assumes 'example_suff.txt' is in the directory and matches the pattern and suffix
    """

    os.chdir(directory)
    files = glob.glob(file_pattern)
    file_types = {}

    for file in files:
        if re.search(suffix, file):
            file_type = mimetypes.guess_type(file)[0]
            file_types[file] = file_type

    return file_types

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        self.test_file_1 = os.path.join(self.test_dir, 'example_suff.txt')
        self.test_file_2 = os.path.join(self.test_dir, 'sample.txt')
        self.test_file_3 = os.path.join(self.test_dir, 'test_suff.doc')
        with open(self.test_file_1, 'w') as f:
            f.write("This is a test file.")
        with open(self.test_file_2, 'w') as f:
            f.write("This file does not match the suffix.")
        with open(self.test_file_3, 'w') as f:
            f.write("Another test file.")

    def tearDown(self):
        for file in (self.test_file_1, self.test_file_2, self.test_file_3):
            if os.path.exists(file):
                os.remove(file)
        os.rmdir(self.test_dir)

    def test_file_matching_suffix(self):
        result = task_func(self.test_dir, '*_suff.txt', '_suff')
        self.assertIn(self.test_file_1, result)
        self.assertEqual(result[self.test_file_1], 'text/plain')

    def test_file_not_matching_suffix(self):
        result = task_func(self.test_dir, '*.txt', '_suff')
        self.assertNotIn(self.test_file_2, result)

    def test_multiple_file_types(self):
        result = task_func(self.test_dir, '*', '_suff')
        self.assertIn(self.test_file_1, result)
        self.assertIn(self.test_file_3, result)
        self.assertEqual(result[self.test_file_1], 'text/plain')
        self.assertEqual(result[self.test_file_3], 'application/msword')

    def test_no_matching_files(self):
        result = task_func(self.test_dir, '*.txt', '_non_existent')
        self.assertEqual(result, {})

    def test_invalid_directory(self):
        with self.assertRaises(FileNotFoundError):
            task_func('invalid_directory', '*.txt', '_suff')

if __name__ == '__main__':
    unittest.main()