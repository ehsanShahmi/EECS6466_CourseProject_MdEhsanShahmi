import re
import json
import requests
import unittest
from unittest.mock import patch

def task_func(myString, token):
    """
    Extracts a URL from a string and sends it to a REST API via a POST request. The URL is included in the JSON payload,
    and an authorization token is used in the headers for API access. If multiple URL is in myString, then use the first one

    Parameters:
    myString (str): The string from which to extract the URL.
    token (str): The authorization token required for API access.

    Returns:
    dict: The response from the API, which varies based on the API's implementation.

    Requirements:
    - re
    - json
    - requests

    Example:
    >>> task_func('Please check: https://www.google.com', 'your_token_here')
    {'message': 'URL received'}
    """

    url = re.search(r'(https?://\S+)', myString).group()
    headers = {'Authorization': 'Bearer ' + token}
    data = {'url': url}
    response = requests.post('https://api.example.com/urls', headers=headers, data=json.dumps(data))
    return response.json()

class TestTaskFunc(unittest.TestCase):
    
    @patch('requests.post')
    def test_valid_url(self, mock_post):
        mock_post.return_value.json.return_value = {'message': 'URL received'}
        result = task_func('Please check: https://www.google.com', 'valid_token')
        self.assertEqual(result, {'message': 'URL received'})
        mock_post.assert_called_once()
        
    @patch('requests.post')
    def test_invalid_url(self, mock_post):
        mock_post.return_value.json.return_value = {'error': 'Invalid URL'}
        result = task_func('This is a test without a URL', 'valid_token')
        self.assertIsNone(result)
        mock_post.assert_not_called()
        
    @patch('requests.post')
    def test_multiple_urls(self, mock_post):
        mock_post.return_value.json.return_value = {'message': 'URL received'}
        result = task_func('Please visit: https://www.example.com and https://www.google.com', 'valid_token')
        self.assertEqual(result, {'message': 'URL received'})
        mock_post.assert_called_once()
        
    @patch('requests.post')
    def test_no_url_in_string(self, mock_post):
        mock_post.return_value.json.return_value = {'error': 'No URL found'}
        result = task_func('Just some text', 'valid_token')
        self.assertIsNone(result)
        mock_post.assert_not_called()
        
    @patch('requests.post')
    def test_api_error_response(self, mock_post):
        mock_post.return_value.json.return_value = {'error': 'Server error'}
        result = task_func('Please check: https://www.google.com', 'valid_token')
        self.assertEqual(result, {'error': 'Server error'})
        mock_post.assert_called_once()

if __name__ == '__main__':
    unittest.main()