import json
import requests
import unittest
from unittest.mock import patch, mock_open

class TestTaskFunction(unittest.TestCase):

    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_successful_api_call(self, mock_file, mock_requests):
        # Arrange
        mock_requests.return_value.__enter__.return_value.json.return_value = {'key': 'value'}
        mock_requests.return_value.__enter__.return_value.status_code = 200
        API_URL = 'https://api.github.com/'
        endpoint = 'users'
        PREFIX = 'ME'

        # Act
        filename = task_func(API_URL, endpoint, PREFIX)

        # Assert
        mock_requests.assert_called_once_with(API_URL + endpoint)
        mock_file.assert_called_once_with('MEusers.json', 'w')
        mock_file().write.assert_called_once_with(json.dumps({'key': 'value'}))
        self.assertEqual(filename, 'MEusers.json')

    @patch('requests.get')
    def test_api_call_raises_runtime_error(self, mock_requests):
        # Arrange
        mock_requests.side_effect = requests.exceptions.HTTPError("HTTP error occurred")
        API_URL = 'https://api.github.com/'
        endpoint = 'users'
        PREFIX = 'ME'

        # Act & Assert
        with self.assertRaises(RuntimeError) as context:
            task_func(API_URL, endpoint, PREFIX)
        self.assertEqual(str(context.exception), "Error fetching data from API: HTTP error occurred")

    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_api_call_with_empty_response(self, mock_file, mock_requests):
        # Arrange
        mock_requests.return_value.__enter__.return_value.json.return_value = {}
        mock_requests.return_value.__enter__.return_value.status_code = 200
        API_URL = 'https://api.github.com/'
        endpoint = 'users'
        PREFIX = 'ME'

        # Act
        filename = task_func(API_URL, endpoint, PREFIX)

        # Assert
        mock_file().write.assert_called_once_with(json.dumps({}))
        self.assertEqual(filename, 'MEusers.json')

    @patch('requests.get')
    def test_invalid_api_url(self, mock_requests):
        # Arrange
        mock_requests.side_effect = requests.exceptions.RequestException("Invalid URL")
        API_URL = 'invalid_url'
        endpoint = 'users'
        PREFIX = 'ME'

        # Act & Assert
        with self.assertRaises(RuntimeError) as context:
            task_func(API_URL, endpoint, PREFIX)
        self.assertEqual(str(context.exception), "Error fetching data from API: Invalid URL")

    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_file_write_error(self, mock_file, mock_requests):
        # Arrange
        mock_requests.return_value.__enter__.return_value.json.return_value = {'key': 'value'}
        mock_requests.return_value.__enter__.return_value.status_code = 200
        mock_file.side_effect = IOError("File write error")
        API_URL = 'https://api.github.com/'
        endpoint = 'users'
        PREFIX = 'ME'

        # Act & Assert
        with self.assertRaises(RuntimeError) as context:
            task_func(API_URL, endpoint, PREFIX)
        self.assertEqual(str(context.exception), "Error fetching data from API: File write error")

if __name__ == '__main__':
    unittest.main()