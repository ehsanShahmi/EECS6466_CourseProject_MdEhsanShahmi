import json
import requests
import chardet
import unittest
from unittest.mock import patch, Mock

# Constants
API_URL = "http://api.example.com/data"

def task_func(url=API_URL, from_encoding=None, to_encoding="utf8"):
    """
    Fetches data from a specified REST API URL and processes it for JSON parsing. The process involves decoding
    and re-encoding the data, handling different encoding scenarios.

    Note:
    - The function initiates an HTTP GET request to the specified URL with a 5-second timeout. It retrieves the response
    content in raw bytes.
    
    Returns:
    - dict: The JSON-parsed data after re-encoding. Returns an empty dictionary if the content is empty.
    
    Raises:
    - ValueError: "Unable to detect encoding for non-empty content", if it fails to detect the encoding for non-empty response content.
    
    Requirements:
    - json
    - requests
    - chardet
    """

    response = requests.get(url, timeout=5)
    content = response.content

    if from_encoding is None:
        detected_encoding = chardet.detect(content)["encoding"]
        if detected_encoding is None:
            if content:
                raise ValueError("Unable to detect encoding for non-empty content")
            else:
                return {}
        content = content.decode(detected_encoding)
    else:
        content = content.decode(from_encoding)

    content = content.encode(to_encoding).decode(to_encoding)
    data = json.loads(content)

    return data

class TestTaskFunc(unittest.TestCase):

    @patch('requests.get')
    def test_valid_json_response(self, mock_get):
        mock_response = Mock()
        mock_response.content = b'{"key": "value"}'
        mock_get.return_value = mock_response

        expected = {"key": "value"}
        result = task_func()
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_empty_content(self, mock_get):
        mock_response = Mock()
        mock_response.content = b''
        mock_get.return_value = mock_response

        expected = {}
        result = task_func()
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_encoding_detection(self, mock_get):
        mock_response = Mock()
        mock_response.content = b'\xe2\x98\x83'  # Snowman character
        mock_get.return_value = mock_response

        expected = {"message": "test"}  # Assuming the correct response after processing
        result = task_func()
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_invalid_json_response(self, mock_get):
        mock_response = Mock()
        mock_response.content = b'not a json'
        mock_get.return_value = mock_response
        
        with self.assertRaises(json.JSONDecodeError):
            task_func()

    @patch('requests.get')
    def test_undetectable_encoding(self, mock_get):
        mock_response = Mock()
        mock_response.content = b'\x80'  # Invalid byte sequence
        mock_get.return_value = mock_response

        with self.assertRaises(ValueError) as context:
            task_func()
        self.assertEqual(str(context.exception), "Unable to detect encoding for non-empty content")

if __name__ == '__main__':
    unittest.main()