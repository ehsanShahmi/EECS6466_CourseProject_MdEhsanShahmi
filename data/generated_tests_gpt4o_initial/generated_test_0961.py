import os
import glob
from collections import Counter
import unittest

def task_func(directory, extensions=[".txt", ".docx", ".xlsx", ".csv"], keep_zero=True):
    """
    Traverses a given directory recursively to count files by specified extensions.

    Parameters:
    - directory (str): The path of the directory to search.
    - extensions (list of str): File extensions to count. Defaults to ['.txt', '.docx', '.xlsx', '.csv'].
    - keep_zero (bool): Whether to include extensions with zero counts. Defaults to True.

    Returns:
    - Counter: An object containing counts of files for each of the specified extensions.

    Raises:
    - OSError: If the specified directory does not exist.

    Requirements:
    - os
    - glob
    - collections

    Note:
    - This function counts files in a case-sensitive manner.
    """

    if not os.path.exists(directory):
        raise OSError("directory must exist.")

    counter = Counter()

    for suffix in extensions:
        count = len(
            glob.glob(os.path.join(directory, "**", "*" + suffix), recursive=True)
        )
        if count:
            counter[suffix] += count
        else:
            if keep_zero:
                counter[suffix] += count
    return counter


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create a test directory with files for testing."""
        self.test_dir = 'test_directory'
        os.makedirs(self.test_dir, exist_ok=True)
        with open(os.path.join(self.test_dir, 'file1.txt'), 'w') as f:
            f.write("test")
        with open(os.path.join(self.test_dir, 'file2.docx'), 'w') as f:
            f.write("test")
        with open(os.path.join(self.test_dir, 'file3.xlsx'), 'w') as f:
            f.write("test")

    def tearDown(self):
        """Remove the test directory and its contents after tests."""
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_count_txt_files(self):
        """Test counting .txt files."""
        result = task_func(self.test_dir)
        self.assertEqual(result['.txt'], 1)

    def test_count_docx_files(self):
        """Test counting .docx files."""
        result = task_func(self.test_dir)
        self.assertEqual(result['.docx'], 1)

    def test_count_xlsx_files(self):
        """Test counting .xlsx files."""
        result = task_func(self.test_dir)
        self.assertEqual(result['.xlsx'], 1)

    def test_keep_zero_false(self):
        """Test with keep_zero set to False."""
        result = task_func(self.test_dir, keep_zero=False)
        self.assertNotIn('.csv', result)

    def test_nonexistent_directory(self):
        """Test handling of a nonexistent directory."""
        with self.assertRaises(OSError):
            task_func('nonexistent_directory')

if __name__ == '__main__':
    unittest.main()