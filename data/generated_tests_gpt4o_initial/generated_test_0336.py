import re
import os
import glob
from pathlib import Path
import unittest
import tempfile

def task_func(pattern, directory, extensions):
    """
    Find all files in a specific directory that contain a regex pattern in their contents in a case insensitive manner.
    
    Parameters:
    pattern (str): The regex pattern to match.
    directory (str): The directory to search in.
    extensions (list): The file extensions to consider. 
    
    Returns:
    list: A list of absolute file paths that contain the pattern.
    
    Requirements:
    - os
    - glob
    - pathlib
    - re
    """
    matched_files = []
    for ext in extensions:
        files = glob.glob(os.path.join(directory, ext))
        for file in files:
            with open(file, 'r') as f:
                content = f.read().lower()
                if re.search(pattern.lower(), content):
                    matched_files.append(Path(file).resolve())
    return matched_files

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
        # Create test files
        with open(os.path.join(self.test_dir, 'test1.txt'), 'w') as f:
            f.write('This is a sample test file.')
        with open(os.path.join(self.test_dir, 'test2.txt'), 'w') as f:
            f.write('Another test file with pattern Hello.')
        with open(os.path.join(self.test_dir, 'test3.md'), 'w') as f:
            f.write('This file does not have the keyword.')

    def tearDown(self):
        # Clean up the temporary directory and files
        for ext in ['*.txt', '*.md']:
            files = glob.glob(os.path.join(self.test_dir, ext))
            for file in files:
                os.remove(file)
        os.rmdir(self.test_dir)

    def test_match_case_sensitive(self):
        result = task_func('Hello', self.test_dir, ['*.txt'])
        self.assertEqual(len(result), 1)
        self.assertTrue(str(result[0]).endswith('test2.txt'))

    def test_match_case_insensitive(self):
        result = task_func('hello', self.test_dir, ['*.txt'])
        self.assertEqual(len(result), 1)
        self.assertTrue(str(result[0]).endswith('test2.txt'))

    def test_no_match(self):
        result = task_func('notfound', self.test_dir, ['*.txt'])
        self.assertEqual(len(result), 0)

    def test_multiple_extensions(self):
        result = task_func('test', self.test_dir, ['*.txt', '*.md'])
        self.assertEqual(len(result), 2)
        self.assertTrue(any(str(f).endswith('test1.txt') for f in result))
        self.assertTrue(any(str(f).endswith('test2.txt') for f in result))

    def test_empty_directory(self):
        empty_dir = tempfile.mkdtemp()
        try:
            result = task_func('Hello', empty_dir, ['*.txt', '*.md'])
            self.assertEqual(len(result), 0)
        finally:
            os.rmdir(empty_dir)

if __name__ == '__main__':
    unittest.main()