import unittest
from unittest.mock import patch
import json
import requests

URL = 'https://api.github.com/users/'

# Here is your prompt:
import unicodedata
import requests

def task_func(username):
    """
    Retrieves user information from the GitHub API for a given username, normalizes all string data to ASCII,
    and returns a dictionary of the normalized data. This function demonstrates data retrieval from a web API
    and handling of Unicode data normalization.

    Parameters:
    username (str): The GitHub username.

    Returns:
    dict: A dictionary with the user's data, where all string values are normalized to ASCII.

    Raises:
    requests.exceptions.HTTPError: For any HTTP response indicating an error.

    Requirements:
    - unicodedata
    - requests

    Examples:
    >>> result = task_func('torvalds')
    >>> isinstance(result, dict)
    True
    >>> 'login' in result
    True
    """

    response = requests.get(URL + username)
    try:
        response.raise_for_status()  # This will raise an HTTPError if the response was an error
        user_data = response.json()
    except requests.exceptions.HTTPError as e:
        # Optionally, log the error or handle it according to your needs
        error_msg = f"Failed to fetch user data for '{username}'. HTTP status: {e.response.status_code} - {e.response.reason}."
        raise Exception(error_msg) from e

    normalized_user_data = {}
    for key, value in user_data.items():
        if isinstance(value, str):
            normalized_value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode()
            normalized_user_data[key] = normalized_value
        else:
            normalized_user_data[key] = value

    return normalized_user_data


class TestTaskFunction(unittest.TestCase):

    @patch('requests.get')
    def test_successful_response(self, mock_get):
        mock_response = {
            "login": "torvalds",
            "id": 1024025,
            "node_id": "MDQ6VXNlcjEwMjQwMjU=",
            "avatar_url": "https://avatars.githubusercontent.com/u/1024025?v=4",
            "url": "https://api.github.com/users/torvalds"
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        expected = {
            "login": "torvalds",
            "id": 1024025,
            "node_id": "MDQ6VXNlcjEwMjQwMjU=",
            "avatar_url": "https://avatars.githubusercontent.com/u/1024025?v=4",
            "url": "https://api.github.com/users/torvalds"
        }
        result = task_func('torvalds')
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_username_with_unicode(self, mock_get):
        mock_response = {
            "login": "torvałds",
            "id": 1024025,
            "avatar_url": "https://avatars.githubusercontent.com/u/1024025?v=4",
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        expected = {
            "login": "torvalds",
            "id": 1024025,
            "avatar_url": "https://avatars.githubusercontent.com/u/1024025?v=4",
        }
        result = task_func('torvałds')
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_user_not_found(self, mock_get):
        mock_get.return_value.status_code = 404
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
        
        with self.assertRaises(Exception) as context:
            task_func('nonexistentuser')
        self.assertIn("Failed to fetch user data for 'nonexistentuser'", str(context.exception))

    @patch('requests.get')
    def test_empty_username(self, mock_get):
        with self.assertRaises(Exception) as context:
            task_func('')
        self.assertIn("Failed to fetch user data for ''", str(context.exception))

    @patch('requests.get')
    def test_invalid_response_format(self, mock_get):
        mock_response = "This is not a JSON"
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        with self.assertRaises(ValueError):
            task_func('torvalds')


if __name__ == '__main__':
    unittest.main()