import unittest
import os

# Here is your prompt:
import hashlib
import io
import os

def task_func(file_path1, file_path2):
    """
    Compares two files to determine if they are identical by computing and comparing their MD5 hash values.
    This method is effective for checking if two files have exactly the same content.

    Parameters:
    file_path1 (str): The file path of the first file.
    file_path2 (str): The file path of the second file.

    Returns:
    bool: Returns True if the MD5 hashes of the files match (indicating identical content), False otherwise.

    Raises:
    FileNotFoundError: if either file_path1 or file_path2 does not exist.

    Requirements:
    - hashlib
    - io
    - os

    Examples:
    Assuming 'file1.gz' and 'file2.gz' contain the same content,
    >>> task_func('file1.gz', 'file2.gz')
    True

    Assuming 'file1.gz' and 'file3.txt' contain different content,
    >>> task_func('file1.gz', 'file3.txt')
    False
    """

    if not os.path.exists(file_path1) or not os.path.exists(file_path2):
        raise FileNotFoundError("File not found! Please specify a valid filepath")

    with io.open(file_path1, 'rb') as file1, io.open(file_path2, 'rb') as file2:
        file1_hash = hashlib.md5(file1.read()).hexdigest()
        file2_hash = hashlib.md5(file2.read()).hexdigest()

    return file1_hash == file2_hash


class TestFileComparison(unittest.TestCase):

    def setUp(self):
        # Create temporary files for testing
        self.file1_path = 'test_file1.txt'
        self.file2_path = 'test_file2.txt'
        self.file3_path = 'test_file3.txt'
        
        with open(self.file1_path, 'w') as f:
            f.write('Hello, World!')
        with open(self.file2_path, 'w') as f:
            f.write('Hello, World!')
        with open(self.file3_path, 'w') as f:
            f.write('Goodbye, World!')

    def tearDown(self):
        # Remove temporary files after testing
        os.remove(self.file1_path)
        os.remove(self.file2_path)
        os.remove(self.file3_path)

    def test_identical_files(self):
        # Test with two identical files
        result = task_func(self.file1_path, self.file2_path)
        self.assertTrue(result)

    def test_different_files(self):
        # Test with two different files
        result = task_func(self.file1_path, self.file3_path)
        self.assertFalse(result)

    def test_nonexistent_file1(self):
        # Test with a nonexistent first file
        with self.assertRaises(FileNotFoundError):
            task_func('nonexistent_file.txt', self.file2_path)

    def test_nonexistent_file2(self):
        # Test with a nonexistent second file
        with self.assertRaises(FileNotFoundError):
            task_func(self.file1_path, 'nonexistent_file.txt')

    def test_empty_files(self):
        # Test with two empty files
        empty_file1 = 'empty_file1.txt'
        empty_file2 = 'empty_file2.txt'
        with open(empty_file1, 'w') as f:
            pass
        with open(empty_file2, 'w') as f:
            pass
        
        result = task_func(empty_file1, empty_file2)
        self.assertTrue(result)

        os.remove(empty_file1)
        os.remove(empty_file2)


if __name__ == '__main__':
    unittest.main()