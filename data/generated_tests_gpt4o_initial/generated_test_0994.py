import requests
import pandas as pd
from bs4 import BeautifulSoup
import unittest
from unittest.mock import patch, MagicMock


class TestTaskFunc(unittest.TestCase):

    @patch('requests.get')
    def test_valid_url(self, mock_get):
        # Simulating a valid response from a webpage
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '<div class="container"><h1>Test Title</h1><span class="date">2023-01-01</span><span class="author">John Doe</span></div>'
        mock_get.return_value = mock_response

        # Test the function with a valid URL
        from task_module import task_func  # Assume task_func is in task_module
        result = task_func('https://example.com/articles', 'test.csv')
        expected = [('Test Title', '2023-01-01', 'John Doe')]
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_empty_response(self, mock_get):
        # Simulating a valid response with no data
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '<div class="container"></div>'
        mock_get.return_value = mock_response

        from task_module import task_func
        result = task_func('https://example.com/articles', 'test.csv')
        expected = [('No Title', 'No Date', 'No Author')]
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_page_with_missing_elements(self, mock_get):
        # Simulating a valid response where some elements are missing
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '<div class="container"><h1>Test Title</h1><span class="author">Jane Doe</span></div>'
        mock_get.return_value = mock_response

        from task_module import task_func
        result = task_func('https://example.com/articles', 'test.csv')
        expected = [('Test Title', 'No Date', 'Jane Doe')]
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_invalid_url(self, mock_get):
        # Simulating a 404 error for an invalid URL
        mock_get.side_effect = requests.exceptions.HTTPError("404 Client Error: Not Found for url")
        
        from task_module import task_func
        with self.assertRaises(RuntimeError) as context:
            task_func('https://example.com/nonexistent', 'test.csv')
        self.assertIn("Error fetching URL:", str(context.exception))

    @patch('requests.get')
    def test_connection_error(self, mock_get):
        # Simulating a connection error
        mock_get.side_effect = requests.exceptions.ConnectionError("Connection Error")
        
        from task_module import task_func
        with self.assertRaises(RuntimeError) as context:
            task_func('https://example.com/articles', 'test.csv')
        self.assertIn("Error fetching URL:", str(context.exception))


if __name__ == '__main__':
    unittest.main()