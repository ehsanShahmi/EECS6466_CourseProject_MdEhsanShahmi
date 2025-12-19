import unittest
from unittest.mock import patch, MagicMock
import requests
import json
import base64

# Here is your prompt:
def task_func(data, url="http://your-api-url.com"):
    """
    Convert a Python dictionary into a JSON-formatted string, encode this string in base64 format,
    and send it as a 'payload' in a POST request to an API endpoint.
    
    Parameters:
    data (dict): The Python dictionary to encode and send.
    url (str, optional): The API endpoint URL. Defaults to "http://your-api-url.com".
    
    Returns:
    requests.Response: The response object received from the API endpoint after the POST request.
    
    Requirements:
    - requests
    - json
    - base64
    
    Example:
    >>> data = {'name': 'John', 'age': 30, 'city': 'New York'}
    >>> response = task_func(data, url="http://example-api-url.com")
    >>> print(response.status_code)
    200
    """

    json_data = json.dumps(data)
    encoded_data = base64.b64encode(json_data.encode('ascii')).decode('ascii')
    response = requests.post(url, json={"payload": encoded_data})
    
    return response

class TestTaskFunc(unittest.TestCase):

    @patch('requests.post')
    def test_valid_data(self, mock_post):
        # Arrange
        test_data = {'name': 'John', 'age': 30, 'city': 'New York'}
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        # Act
        response = task_func(test_data, url="http://example-api-url.com")
        
        # Assert
        self.assertEqual(response.status_code, 200)
        mock_post.assert_called_once_with("http://example-api-url.com", json={"payload": base64.b64encode(json.dumps(test_data).encode('ascii')).decode('ascii')})

    @patch('requests.post')
    def test_empty_data(self, mock_post):
        # Arrange
        test_data = {}
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response
        
        # Act
        response = task_func(test_data)
        
        # Assert
        self.assertEqual(response.status_code, 200)
        mock_post.assert_called_once_with("http://your-api-url.com", json={"payload": base64.b64encode(json.dumps(test_data).encode('ascii')).decode('ascii')})

    @patch('requests.post')
    def test_custom_url(self, mock_post):
        # Arrange
        test_data = {'test_key': 'test_value'}
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_post.return_value = mock_response
        
        # Act
        response = task_func(test_data, url="http://custom-api-url.com")
        
        # Assert
        self.assertEqual(response.status_code, 201)
        mock_post.assert_called_once_with("http://custom-api-url.com", json={"payload": base64.b64encode(json.dumps(test_data).encode('ascii')).decode('ascii')})

    @patch('requests.post')
    def test_invalid_data_type(self, mock_post):
        # Arrange
        test_data = "This is a string, not a dictionary."
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response
        
        # Act
        with self.assertRaises(TypeError):
            task_func(test_data)

    @patch('requests.post')
    def test_response_not_ok(self, mock_post):
        # Arrange
        test_data = {'key': 'value'}
        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_post.return_value = mock_response
        
        # Act
        response = task_func(test_data)
        
        # Assert
        self.assertNotEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 500)

if __name__ == '__main__':
    unittest.main()