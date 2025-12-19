import re
import requests
import unittest
from unittest.mock import patch


class TestTaskFunc(unittest.TestCase):

    @patch('requests.get')
    def test_valid_api_endpoint(self, mock_get):
        mock_get.return_value.json.return_value = {'key': 'value'}
        result = task_func('Fetch data from https://api.example.com/data')
        self.assertEqual(result, {'key': 'value'})
        mock_get.assert_called_once_with('https://api.example.com/data')

    @patch('requests.get')
    def test_invalid_url(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Invalid URL")
        with self.assertRaises(requests.exceptions.RequestException):
            task_func('Fetch data from this_is_not_a_url')

    @patch('requests.get')
    def test_no_url_in_input(self, mock_get):
        with self.assertRaises(AttributeError):
            task_func('Fetch data without a URL')
    
    @patch('requests.get')
    def test_multiple_urls_in_input(self, mock_get):
        mock_get.return_value.json.return_value = {'key': 'value'}
        result = task_func('Fetch data from multiple endpoints: https://api.example.com/data and https://api.example.com/other')
        self.assertEqual(result, {'key': 'value'})
        mock_get.assert_called_once_with('https://api.example.com/data')

    @patch('requests.get')
    def test_non_json_response(self, mock_get):
        mock_get.return_value.json.side_effect = ValueError("Response not JSON")
        with self.assertRaises(ValueError):
            task_func('Fetch data from https://api.example.com/data')


if __name__ == '__main__':
    unittest.main()