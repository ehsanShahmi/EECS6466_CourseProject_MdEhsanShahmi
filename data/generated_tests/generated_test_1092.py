import unittest
from unittest.mock import patch, Mock
import ast
import requests
from bs4 import BeautifulSoup

def task_func(url):
    """
    Fetches the content of a webpage specified by its URL, parses it to find <script> tags,
    and attempts to evaluate any string within these tags as a Python dictionary.

    Parameters:
    - url (str): The URL of the webpage to scrape.

    Returns:
    - list of dict: A list containing dictionaries that were successfully evaluated from string representations
      found within <script> tags on the webpage. 
    
    Note:
    - If an error occurs during the request or if no dictionaries are found/evaluable, an empty list is returned.

    Requirements:
    - ast
    - requests
    - bs4.BeautifulSoup

    Example:
    >>> task_func('https://example.com')
    [{'key': 'value'}, ...]
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException:
        return []
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []
    for script in soup.find_all('script'):
        try:
            results.append(ast.literal_eval(script.string))
        except (ValueError, SyntaxError):
            continue

    return results

class TestTaskFunc(unittest.TestCase):
    
    @patch('requests.get')
    def test_valid_url_with_dictionaries(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.text = '<html><script>{"key1": "value1"}</script></html>'
        mock_get.return_value = mock_response
        
        result = task_func('https://example.com')
        expected = [{'key1': 'value1'}]
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_valid_url_with_multiple_dictionaries(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.text = '<html><script>{"key1": "value1"}</script><script>{"key2": "value2"}</script></html>'
        mock_get.return_value = mock_response
        
        result = task_func('https://example.com')
        expected = [{'key1': 'value1'}, {'key2': 'value2'}]
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_valid_url_with_non_dict_script(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.text = '<html><script>Not a dict</script></html>'
        mock_get.return_value = mock_response
        
        result = task_func('https://example.com')
        expected = []
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_invalid_url(self, mock_get):
        mock_get.side_effect = requests.RequestException
        
        result = task_func('https://invalid-url.com')
        expected = []
        self.assertEqual(result, expected)

    @patch('requests.get')
    def test_url_with_no_script_tags(self, mock_get):
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.text = '<html><body>No scripts here!</body></html>'
        mock_get.return_value = mock_response
        
        result = task_func('https://example.com')
        expected = []
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()