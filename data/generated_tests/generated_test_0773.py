import os
import re
import shutil
import unittest
from unittest.mock import patch, mock_open

# Constants
SOURCE_DIR = '/source/dir'
TARGET_DIR = '/target/dir'
FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')

def task_func():
    """
    Move all json files in a source directory to a target directory and rename them by splitting the filename the last time "-" occurs and keeping the prefix part of the filename.
    
    Parameters:
    - None

    Returns:
    - None

    Requirements:
    - os
    - re
    - shutil

    Example:
    >>> task_func()

    """

    SOURCE_DIR = '/source/dir'
    TARGET_DIR = '/target/dir'
    FILE_PATTERN = re.compile(r'^(.*?)-\d+\.json$')
    for filename in os.listdir(SOURCE_DIR):
        match = FILE_PATTERN.match(filename)
        if match is not None:
            prefix = match.group(1)
            new_filename = f'{prefix}.json'
            shutil.move(os.path.join(SOURCE_DIR, filename), os.path.join(TARGET_DIR, new_filename))

class TestTaskFunc(unittest.TestCase):

    @patch('os.listdir')
    @patch('shutil.move')
    def test_move_files_correctly(self, mock_move, mock_listdir):
        mock_listdir.return_value = ['file-1.json', 'file-2.json', 'anotherfile-3.json']
        task_func()
        expected_calls = [
            (os.path.join(SOURCE_DIR, 'file-1.json'), os.path.join(TARGET_DIR, 'file.json')),
            (os.path.join(SOURCE_DIR, 'file-2.json'), os.path.join(TARGET_DIR, 'file.json')),
            (os.path.join(SOURCE_DIR, 'anotherfile-3.json'), os.path.join(TARGET_DIR, 'anotherfile.json')),
        ]
        mock_move.assert_has_calls(expected_calls, any_order=True)

    @patch('os.listdir')
    @patch('shutil.move')
    def test_no_files_to_move(self, mock_move, mock_listdir):
        mock_listdir.return_value = []
        task_func()
        mock_move.assert_not_called()

    @patch('os.listdir')
    @patch('shutil.move')
    def test_files_without_pattern(self, mock_move, mock_listdir):
        mock_listdir.return_value = ['file.txt', 'document.pdf']
        task_func()
        mock_move.assert_not_called()

    @patch('os.listdir')
    @patch('shutil.move')
    def test_files_with_different_patterns(self, mock_move, mock_listdir):
        mock_listdir.return_value = ['test-1.json', 'example-2.json', 'random-123.json']
        task_func()
        expected_calls = [
            (os.path.join(SOURCE_DIR, 'test-1.json'), os.path.join(TARGET_DIR, 'test.json')),
            (os.path.join(SOURCE_DIR, 'example-2.json'), os.path.join(TARGET_DIR, 'example.json')),
            (os.path.join(SOURCE_DIR, 'random-123.json'), os.path.join(TARGET_DIR, 'random.json')),
        ]
        mock_move.assert_has_calls(expected_calls, any_order=True)

    @patch('os.listdir')
    @patch('shutil.move')
    def test_move_files_with_different_numberings(self, mock_move, mock_listdir):
        mock_listdir.return_value = ['file-1.json', 'file-23.json', 'file-456.json']
        task_func()
        expected_calls = [
            (os.path.join(SOURCE_DIR, 'file-1.json'), os.path.join(TARGET_DIR, 'file.json')),
            (os.path.join(SOURCE_DIR, 'file-23.json'), os.path.join(TARGET_DIR, 'file.json')),
            (os.path.join(SOURCE_DIR, 'file-456.json'), os.path.join(TARGET_DIR, 'file.json')),
        ]
        mock_move.assert_has_calls(expected_calls, any_order=True)

if __name__ == '__main__':
    unittest.main()