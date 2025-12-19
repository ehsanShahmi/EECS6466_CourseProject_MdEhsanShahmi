import unittest
from unittest.mock import patch, mock_open, MagicMock
import os

# Here is your prompt:
import re
import os
import glob

def task_func(dir_path):
    """
    Search for occurrences of the word "error" in all text files within a 
    specified directory and its subdirectories.
    
    Parameters:
    dir_path (str): The path of the directory.
    
    Returns:
    dict: A dictionary with relative file paths as keys and the count of 
            occurrences of the word "error" as values.
    
    Raises:
    - ValueError: If directory in dir_path does not exist.

    Requirements:
    - re: For regex pattern matching.
    - os: For retrieving relative file paths.
    - glob: For fetching all text file paths in the directory.
    
    The function specifically searches for the word "error" in text files
    (with the extension ".txt").
    This function is NOT case sensitive, e.g. also "ERROr" will be counted.
    
    Example:
    >>> task_func("/path/to/directory")
    {'file1.txt': 2, 'subdir/file2.txt': 1}
    """

           
    if not os.path.isdir(dir_path):
        raise ValueError("Specified directory does not exist.")

    result = {}
    file_paths = glob.glob(f'{dir_path}/**/*.txt', recursive=True)
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            content = file.read()
        matches = re.findall(r'\berror\b', content, re.IGNORECASE)
        # Always set the file's count in the result dictionary, even if it's 0
        result[os.path.relpath(file_path, dir_path)] = len(matches)

    return result

class TestTaskFunc(unittest.TestCase):

    @patch('os.path.isdir')
    @patch('glob.glob')
    @patch('builtins.open', new_callable=mock_open, read_data='This is an error. Another ERROR here.')
    def test_count_errors_in_text_file(self, mock_file, mock_glob, mock_isdir):
        mock_isdir.return_value = True
        mock_glob.return_value = ['file.txt']
        
        expected_output = {'file.txt': 2}
        result = task_func('/mock/directory')
        
        self.assertEqual(result, expected_output)

    @patch('os.path.isdir')
    @patch('glob.glob')
    @patch('builtins.open', new_callable=mock_open, read_data='No errors here.')
    def test_no_errors_in_text_file(self, mock_file, mock_glob, mock_isdir):
        mock_isdir.return_value = True
        mock_glob.return_value = ['file.txt']
        
        expected_output = {'file.txt': 0}
        result = task_func('/mock/directory')
        
        self.assertEqual(result, expected_output)

    @patch('os.path.isdir')
    def test_directory_not_exist(self, mock_isdir):
        mock_isdir.return_value = False
        
        with self.assertRaises(ValueError):
            task_func('/invalid/directory')

    @patch('os.path.isdir')
    @patch('glob.glob')
    def test_multiple_text_files(self, mock_glob, mock_isdir):
        mock_isdir.return_value = True
        mock_glob.return_value = ['file1.txt', 'file2.txt']
        
        with patch('builtins.open', new_callable=mock_open, read_data='error here.\n\nerroR again\n'):
            result = task_func('/mock/directory')
            expected_output = {'file1.txt': 2, 'file2.txt': 2}
            self.assertEqual(result, expected_output)

    @patch('os.path.isdir')
    @patch('glob.glob')
    @patch('builtins.open', new_callable=mock_open, read_data='')
    def test_empty_file(self, mock_file, mock_glob, mock_isdir):
        mock_isdir.return_value = True
        mock_glob.return_value = ['empty.txt']
        
        expected_output = {'empty.txt': 0}
        result = task_func('/mock/directory')
        
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()