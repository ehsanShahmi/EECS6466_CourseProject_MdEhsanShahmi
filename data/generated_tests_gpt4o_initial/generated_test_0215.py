import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import seaborn as sns

# Constants
HEADERS = {
    'accept': 'application/json'
}

# Here is your prompt:
# (The provided function from the user's prompt is not modified or included, it's only for context.)

class TestTaskFunc(unittest.TestCase):

    @patch('requests.get')
    def test_valid_response(self, mock_get):
        # Mocking a positive response with valid data
        mock_response = MagicMock()
        mock_response.text = json.dumps([{'value1': 1, 'value2': 2}, {'value1': 3, 'value2': 4}])
        mock_get.return_value = mock_response
        
        url = 'https://api.example.com/data'
        parameters = {'param1': 'value1'}
        
        df, ax = task_func(url, parameters)

        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (2, 2))
        self.assertIn('value1', df.columns)
        self.assertIn('value2', df.columns)

    @patch('requests.get')
    def test_empty_data(self, mock_get):
        # Mocking an empty response
        mock_response = MagicMock()
        mock_response.text = json.dumps([])
        mock_get.return_value = mock_response
        
        url = 'https://api.example.com/data'
        parameters = {'param1': 'value1'}

        with self.assertRaises(Exception):
            task_func(url, parameters)

    @patch('requests.get')
    def test_invalid_url(self, mock_get):
        # Simulating an invalid URL
        mock_get.side_effect = requests.exceptions.RequestException("Invalid URL")
        
        url = 'invalid_url'
        parameters = {}

        with self.assertRaises(Exception):
            task_func(url, parameters)

    @patch('requests.get')
    def test_no_numerical_data(self, mock_get):
        # Mocking a response with no numerical data
        mock_response = MagicMock()
        mock_response.text = json.dumps([{'value1': 'text', 'value2': 'more text'}, {'value1': 'another text', 'value2': 'yet another'}])
        mock_get.return_value = mock_response
        
        url = 'https://api.example.com/data'
        parameters = {'param1': 'value1'}

        with self.assertRaises(Exception):
            task_func(url, parameters)

    @patch('requests.get')
    def test_heatmap_creation(self, mock_get):
        # Mocking a positive response with valid data
        mock_response = MagicMock()
        mock_response.text = json.dumps([{'value1': 1, 'value2': 2}, {'value1': 3, 'value2': 4}])
        mock_get.return_value = mock_response
        
        url = 'https://api.example.com/data'
        parameters = {'param1': 'value1'}

        df, ax = task_func(url, parameters)

        self.assertIsNotNone(ax)  # Check that the returned Axes object is not None
        self.assertEqual(ax.get_title(), '')  # Just an example check; more specific checks can be added here

if __name__ == '__main__':
    unittest.main()