import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
import json

# Here is your prompt:
import re
import requests
import json
import csv
import os  

# Constants
API_URL = 'https://api.example.com/data'

def task_func(pattern):
    """
    Make a GET request to an API, extract data that matches a RegEx pattern, and write it to a CSV file.

    Parameters:
    pattern (str): The regex pattern to match.

    Returns:
    str: The absolute path to the CSV file containing matched data. If no data is matched, the file will be empty.

    Note:
    - The CSV file generated name is "matched_data.csv"
    - The JSON response from the GET request in the API contains a key named "data", from which the data is extracted.

    Requirements:
    - requests
    - json
    - csv
    - re
    - os

    Example:
    >>> task_func(r'\\\\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\\\\.[A-Z]{2,}\\\\b')
    '/absolute/path/to/matched_data.csv'
    >>> task_func(r'\\\\d{3}-\\\\d{2}-\\\\d{4}')  # For matching SSN format
    '/absolute/path/to/matched_data.csv'
    """


    response = requests.get(API_URL)
    data = json.loads(response.text)
    matched_data = [re.findall(pattern, str(item)) for item in data['data']]
    with open('matched_data.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(matched_data)
    return os.path.abspath('matched_data.csv')


class TestTaskFunction(unittest.TestCase):
    
    @patch('requests.get')
    def test_task_func_valid_email_pattern(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = json.dumps({'data': ['test@example.com']})
        mock_get.return_value = mock_response
        
        pattern = r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b'
        result = task_func(pattern)
        
        self.assertTrue(os.path.isfile('matched_data.csv'))
        self.assertIn('matched_data.csv', result)

    @patch('requests.get')
    def test_task_func_ssn_pattern(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = json.dumps({'data': ['123-45-6789']})
        mock_get.return_value = mock_response
        
        pattern = r'\d{3}-\d{2}-\d{4}'
        result = task_func(pattern)
        
        self.assertTrue(os.path.isfile('matched_data.csv'))
        self.assertIn('matched_data.csv', result)

    @patch('requests.get')
    def test_task_func_no_matches(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = json.dumps({'data': ['sample text without match']})
        mock_get.return_value = mock_response
        
        pattern = r'\d{3}-\d{2}-\d{4}'
        result = task_func(pattern)
        
        self.assertTrue(os.path.isfile('matched_data.csv'))
        
        with open('matched_data.csv', 'r') as f:
            content = f.read()
            self.assertEqual(content, '')

    @patch('requests.get')
    def test_task_func_invalid_url(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Invalid URL")
        
        pattern = r'\d{3}-\d{2}-\d{4}'
        
        with self.assertRaises(requests.exceptions.RequestException):
            task_func(pattern)

    @patch('requests.get')
    def test_task_func_empty_api_data(self, mock_get):
        mock_response = MagicMock()
        mock_response.text = json.dumps({'data': []})
        mock_get.return_value = mock_response
        
        pattern = r'\d{3}-\d{2}-\d{4}'
        result = task_func(pattern)
        
        self.assertTrue(os.path.isfile('matched_data.csv'))
        
        with open('matched_data.csv', 'r') as f:
            content = f.read()
            self.assertEqual(content, '')


if __name__ == '__main__':
    unittest.main()