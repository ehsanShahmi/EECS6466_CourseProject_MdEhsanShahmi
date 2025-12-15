import os
import unittest
from unittest.mock import patch, mock_open

# Here is your prompt:
import os
import re

def task_func(pattern: str, replacement: str, directory: str) -> bool:
    """
    Renames all files in a directory that match a particular pattern with a given replacement string.
    
    Parameters:
        - pattern (str): The pattern to search for in the filenames.
        - replacement (str): The string to replace the pattern with.
        - directory (str): The directory in which to search for files.
        
    Returns:
    - Returns a boolean value. True if the operation was successful, otherwise False.
    
    Requirements:
    - re
    - os

    Examples:
    >>> task_func('draft', 'final', '/home/user/documents')
    True
    >>> task_func('tmp', 'temp', '/home/user/downloads')
    False
    """

    try:
        for file in os.listdir(directory):
            if re.search(pattern, file):
                new_filename = re.sub(pattern, replacement, file)
                os.rename(os.path.join(directory, file), os.path.join(directory, new_filename))
        return True
    except Exception as e:
        return False

class TestTaskFunc(unittest.TestCase):

    @patch('os.listdir')
    @patch('os.rename')
    def test_rename_success(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['draft_document.txt', 'final_report.docx']
        result = task_func('draft', 'final', '/mock/directory')
        self.assertTrue(result)
        mock_rename.assert_called_once_with('/mock/directory/draft_document.txt', '/mock/directory/final_document.txt')

    @patch('os.listdir')
    @patch('os.rename')
    def test_rename_multiple_files(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['draft1.txt', 'draft2.txt', 'final_report.doc']
        result = task_func('draft', 'final', '/mock/directory')
        self.assertTrue(result)
        self.assertEqual(mock_rename.call_count, 2)

    @patch('os.listdir')
    @patch('os.rename')
    def test_no_files_matched(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['report.txt', 'presentation.pptx']
        result = task_func('draft', 'final', '/mock/directory')
        self.assertTrue(result)
        mock_rename.assert_not_called()

    @patch('os.listdir')
    @patch('os.rename')
    def test_empty_directory(self, mock_rename, mock_listdir):
        mock_listdir.return_value = []
        result = task_func('draft', 'final', '/mock/directory')
        self.assertTrue(result)
        mock_rename.assert_not_called()

    @patch('os.listdir')
    @patch('os.rename')
    def test_rename_with_exception(self, mock_rename, mock_listdir):
        mock_listdir.return_value = ['draft.txt']
        mock_rename.side_effect = Exception("Rename failed")
        result = task_func('draft', 'final', '/mock/directory')
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()