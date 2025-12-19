import pandas as pd
import re
import os
import unittest

def task_func(dir_path: str, pattern: str = '^EMP'):
    """
    Look for all ascendingly sorted files in a directory that start with a given pattern, and return the number of files against their size. You should return a pandas DataFrame with 2 columns 'File' and 'Size' with correspond to the file name and the size respectively.

    Parameters:
    - dir_path (str): The path to the directory.
    - pattern (str): The pattern to match. Default is '^EMP' (files starting with 'EMP').

    Returns:
    - pandas.DataFrame: A pandas DataFrame with file names and their sizes.

    Requirements:
    - pandas
    - re
    - os

    Example:
    >>> report = task_func('/path/to/directory')
    >>> print(report)
    """
    
    file_sizes = []
    for file in sorted(os.listdir(dir_path)):
        if re.match(pattern, file):
            file_sizes.append((file, os.path.getsize(os.path.join(dir_path, file))))

    df = pd.DataFrame(file_sizes, columns=['File', 'Size'])
    return df

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        os.mkdir('test_dir')
        
        # Create test files
        with open('test_dir/EMP1.txt', 'w') as f:
            f.write('This is a test file')
        with open('test_dir/EMP2.txt', 'w') as f:
            f.write('Another test file')
        with open('test_dir/XYZ1.txt', 'w') as f:
            f.write('Not matching file')

    def tearDown(self):
        # Clean up the created directory and files
        for file in os.listdir('test_dir'):
            os.remove(os.path.join('test_dir', file))
        os.rmdir('test_dir')

    def test_files_matching_pattern(self):
        result = task_func('test_dir')
        self.assertEqual(len(result), 2)  # Two files should match the 'EMP' pattern

    def test_file_sizes(self):
        result = task_func('test_dir')
        sizes = result['Size'].to_list()
        self.assertTrue(all(size > 0 for size in sizes))  # All sizes should be greater than 0

    def test_empty_directory(self):
        os.rmdir('test_dir')
        os.mkdir('test_dir')
        result = task_func('test_dir')
        self.assertTrue(result.empty)  # Should return an empty DataFrame

    def test_non_matching_pattern(self):
        result = task_func('test_dir', pattern='^XYZ')
        self.assertTrue(result.empty)  # No files should match the 'XYZ' pattern

    def test_sorted_file_list(self):
        result = task_func('test_dir')
        expected_files = ['EMP1.txt', 'EMP2.txt']
        self.assertListEqual(result['File'].tolist(), expected_files)  # Ensure files are sorted

if __name__ == '__main__':
    unittest.main()