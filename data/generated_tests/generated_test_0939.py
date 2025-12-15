import re
import os
import glob
import unittest

def task_func(dir_path: str) -> list:
    """
    Rename all files in the specified directory by removing all special characters,
    punctuation marks, and spaces, using regular expressions. The function keeps
    alphanumeric characters and removes the rest.

    Requirements:
    - re
    - os
    - glob

    Parameters:
    dir_path (str): The path to the directory containing the files to be renamed.

    Returns:
    list[str]: A list containing the new names of all files after renaming.

    Example:
    >>> task_func('path/to/directory')
    ['file1', 'file2', 'file3']
    >>> task_func('another/directory/path')
    ['anotherFile1', 'anotherFile2']
    """
    
    new_names = []
    for file_path in glob.glob(os.path.join(dir_path, '*')):
        base_name = os.path.basename(file_path)
        new_name = re.sub('[^A-Za-z0-9]+', '', base_name)
        new_path = os.path.join(dir_path, new_name)
        os.rename(file_path, new_path)
        new_names.append(new_name)
    return new_names

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        """Set up a temporary directory and files for testing."""
        self.test_dir = 'test_dir'
        os.makedirs(self.test_dir, exist_ok=True)
        # Create test files
        test_files = [
            'file 1.txt',
            'file@2.doc',
            'file#3.pdf',
            'file!4.jpg',
            'file(5).png'
        ]
        for file in test_files:
            open(os.path.join(self.test_dir, file), 'a').close()

    def tearDown(self):
        """Remove the temporary directory and all test files."""
        for file in glob.glob(os.path.join(self.test_dir, '*')):
            os.remove(file)
        os.rmdir(self.test_dir)

    def test_rename_files(self):
        """Test renaming of files in the test directory."""
        expected_names = ['file1', 'file2', 'file3', 'file4', 'file5']
        new_names = task_func(self.test_dir)
        self.assertListEqual(sorted(new_names), sorted(expected_names))
    
    def test_empty_directory(self):
        """Test renaming in an empty directory."""
        empty_dir = 'empty_test_dir'
        os.makedirs(empty_dir, exist_ok=True)
        try:
            new_names = task_func(empty_dir)
            self.assertEqual(new_names, [])
        finally:
            os.rmdir(empty_dir)

    def test_no_special_characters(self):
        """Test with files that have no special characters."""
        no_special_char_dir = 'no_special_dir'
        os.makedirs(no_special_char_dir, exist_ok=True)
        files = ['file1', 'file2', 'file3']
        for file in files:
            open(os.path.join(no_special_char_dir, file), 'a').close()
        try:
            new_names = task_func(no_special_char_dir)
            self.assertListEqual(sorted(new_names), sorted(files))
        finally:
            for file in glob.glob(os.path.join(no_special_char_dir, '*')):
                os.remove(file)
            os.rmdir(no_special_char_dir)

    def test_mixed_names(self):
        """Test with a mix of normal and special character files."""
        mixed_dir = 'mixed_dir'
        os.makedirs(mixed_dir, exist_ok=True)
        mixed_files = ['test file 1.txt', 'another-file_2.doc', 'yetanother#3.png']
        for file in mixed_files:
            open(os.path.join(mixed_dir, file), 'a').close()
        try:
            expected_names = ['testfile1', 'anotherfile2', 'yetanother3']
            new_names = task_func(mixed_dir)
            self.assertListEqual(sorted(new_names), sorted(expected_names))
        finally:
            for file in glob.glob(os.path.join(mixed_dir, '*')):
                os.remove(file)
            os.rmdir(mixed_dir)

if __name__ == '__main__':
    unittest.main()