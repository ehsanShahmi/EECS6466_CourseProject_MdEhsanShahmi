import os
import pathlib
from hashlib import md5
import unicodedata
import unittest

# The given prompt and function definition
def task_func(directory):
    """
    Processes all files within the specified directory, normalizes their filenames to ASCII,
    calculates their MD5 hashes, and retrieves their sizes. It returns a dictionary where
    each key is the normalized file name and each value is another dictionary with the file's size
    and MD5 hash. This method is useful for file integrity checks and file organization tasks.

    Parameters:
    directory (str): The directory path whose files are to be analyzed.

    Returns:
    dict: A dictionary where each key is a normalized file name, and the value is a dictionary
          containing the 'Size' (in bytes) and 'MD5 Hash' of the file.

    Requirements:
    - os
    - pathlib
    - hashlib.md5
    - unicodedata
    """

    files_info = {}

    for file_path in pathlib.Path(directory).iterdir():
        if file_path.is_file():
            normalized_file_name = unicodedata.normalize('NFKD', file_path.name).encode('ascii', 'ignore').decode()

            with open(file_path, 'rb') as file:
                file_content = file.read()
                file_hash = md5(file_content).hexdigest()

            files_info[normalized_file_name] = {'Size': os.path.getsize(file_path), 'MD5 Hash': file_hash}

    return files_info

# Test suite
class TestTaskFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a temporary directory for testing
        cls.test_dir = 'test_directory'
        pathlib.Path(cls.test_dir).mkdir(exist_ok=True)

        # Create test files
        with open(os.path.join(cls.test_dir, 'test1.txt'), 'w') as f:
            f.write('Hello, World!')

        with open(os.path.join(cls.test_dir, 'test2.txt'), 'w') as f:
            f.write('Another test file.')

    @classmethod
    def tearDownClass(cls):
        # Remove test directory and files
        for file in pathlib.Path(cls.test_dir).iterdir():
            file.unlink()
        pathlib.Path(cls.test_dir).rmdir()

    def test_return_type(self):
        info = task_func(self.test_dir)
        self.assertIsInstance(info, dict)

    def test_contains_correct_files(self):
        info = task_func(self.test_dir)
        self.assertIn('test1.txt', info)
        self.assertIn('test2.txt', info)

    def test_file_sizes(self):
        info = task_func(self.test_dir)
        self.assertEqual(info['test1.txt']['Size'], 13)  # "Hello, World!" is 13 bytes
        self.assertEqual(info['test2.txt']['Size'], 22)  # "Another test file." is 22 bytes

    def test_file_hashes(self):
        info = task_func(self.test_dir)
        hash1 = md5(b'Hello, World!').hexdigest()
        hash2 = md5(b'Another test file.').hexdigest()
        self.assertEqual(info['test1.txt']['MD5 Hash'], hash1)
        self.assertEqual(info['test2.txt']['MD5 Hash'], hash2)

    def test_normalization(self):
        # Create a file with a special character in its name
        special_file_name = 'test_ä.txt'
        with open(os.path.join(self.test_dir, special_file_name), 'w') as f:
            f.write('Special character test.')

        info = task_func(self.test_dir)
        self.assertIn('test_.txt', info)  # The special character should be normalized

if __name__ == '__main__':
    unittest.main()