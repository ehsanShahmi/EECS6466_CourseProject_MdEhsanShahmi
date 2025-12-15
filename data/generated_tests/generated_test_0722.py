import unittest
import os
import urllib.request
from unittest.mock import patch, mock_open

# Here is your prompt:
import urllib.request
import os
import re

# Constants
TARGET_FILE = 'downloaded_file.txt'
SEARCH_PATTERN = r'\bERROR\b'

def task_func(url):
    """
    Download a text file from the specified url and search for occurrences of the word "ERROR."

    Parameters:
    - url (str): The url of the text file to be downloaded.

    Returns:
    - occurrences (int): The number of occurrences of the word 'ERROR'.

    Requirements:
    - urllib
    - os
    - re

    Example:
    >>> task_func('http://example.com/log.txt')
    5 # Assuming there are 5 occurrences of 'ERROR' in the file
    """

    TARGET_FILE = 'downloaded_file.txt'
    SEARCH_PATTERN = r'\bERROR\b'

    urllib.request.urlretrieve(url, TARGET_FILE)

    with open(TARGET_FILE, 'r') as f:
        data = f.read()
    occurrences = len(re.findall(SEARCH_PATTERN, data))

    os.remove(TARGET_FILE)

    return occurrences


class TestTaskFunc(unittest.TestCase):
    
    @patch('urllib.request.urlretrieve')
    @patch('builtins.open', new_callable=mock_open, read_data='ERROR\nINFO\nERROR\n')
    def test_two_occurrences(self, mock_file, mock_urlretrieve):
        url = 'http://example.com/log.txt'
        result = task_func(url)
        self.assertEqual(result, 2)
    
    @patch('urllib.request.urlretrieve')
    @patch('builtins.open', new_callable=mock_open, read_data='No errors here.\nINFO\n')
    def test_no_occurrences(self, mock_file, mock_urlretrieve):
        url = 'http://example.com/log.txt'
        result = task_func(url)
        self.assertEqual(result, 0)
    
    @patch('urllib.request.urlretrieve')
    @patch('builtins.open', new_callable=mock_open, read_data='ERROR\nERROR\nERROR\nERROR\n')
    def test_four_occurrences(self, mock_file, mock_urlretrieve):
        url = 'http://example.com/log.txt'
        result = task_func(url)
        self.assertEqual(result, 4)

    @patch('urllib.request.urlretrieve')
    @patch('builtins.open', new_callable=mock_open, read_data='Error\nerror\nERROR\nerror\n')
    def test_case_sensitive_occurrences(self, mock_file, mock_urlretrieve):
        url = 'http://example.com/log.txt'
        result = task_func(url)
        self.assertEqual(result, 1)
    
    @patch('urllib.request.urlretrieve')
    def test_file_download_called(self, mock_urlretrieve):
        url = 'http://example.com/log.txt'
        task_func(url)
        mock_urlretrieve.assert_called_once_with(url, 'downloaded_file.txt')


if __name__ == '__main__':
    unittest.main()