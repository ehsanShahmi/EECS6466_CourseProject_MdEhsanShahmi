import unittest
from unittest.mock import patch, MagicMock
import pandas as pd

# Here is your prompt:
import requests
from bs4 import BeautifulSoup
import pandas as pd

def task_func(url='http://example.com'):
    """
    Scrape the first table from a web page and extract data into a Pandas DataFrame.
    
    (function implementation...)
    """
    pass  # The actual implementation is not provided as per the instructions.

class TestTaskFunc(unittest.TestCase):
    
    @patch('requests.get')
    def test_successful_scrape_with_table(self, mock_get):
        # Simulating a successful response with table data
        mock_response = MagicMock()
        mock_response.text = '''
            <html>
                <body>
                    <table>
                        <tr><th>Header1</th><th>Header2</th></tr>
                        <tr><td>Data1</td><td>Data2</td></tr>
                    </table>
                </body>
            </html>
        '''
        mock_get.return_value = mock_response
        
        expected_df = pd.DataFrame({'Header1': ['Data1'], 'Header2': ['Data2']})
        result_df = task_func('http://example.com')
        pd.testing.assert_frame_equal(result_df, expected_df)

    @patch('requests.get')
    def test_no_table_found(self, mock_get):
        # Simulating a response without any table
        mock_response = MagicMock()
        mock_response.text = '''
            <html>
                <body>
                    <p>No table here.</p>
                </body>
            </html>
        '''
        mock_get.return_value = mock_response
        
        with self.assertRaises(ValueError) as context:
            task_func('http://example.com')
        self.assertEqual(str(context.exception), "No table found on the page.")

    @patch('requests.get')
    def test_empty_table(self, mock_get):
        # Simulating a response with an empty table
        mock_response = MagicMock()
        mock_response.text = '''
            <html>
                <body>
                    <table>
                        <tr><th>Header1</th><th>Header2</th></tr>
                        <tr></tr>
                    </table>
                </body>
            </html>
        '''
        mock_get.return_value = mock_response
        
        with self.assertRaises(ValueError) as context:
            task_func('http://example.com')
        self.assertEqual(str(context.exception), "No data found in the table.")

    @patch('requests.get')
    def test_connection_error(self, mock_get):
        # Simulating a connection error
        mock_get.side_effect = requests.ConnectionError("Failed to connect")
        
        with self.assertRaises(ConnectionError) as context:
            task_func('http://example.com')
        self.assertEqual(str(context.exception), "Could not connect to URL: Failed to connect")

    @patch('requests.get')
    def test_http_error(self, mock_get):
        # Simulating an HTTP error
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = requests.HTTPError("HTTP Error")
        mock_get.return_value = mock_response
        
        with self.assertRaises(requests.HTTPError) as context:
            task_func('http://example.com')
        self.assertEqual(str(context.exception), "HTTP error occurred: HTTP Error")

if __name__ == '__main__':
    unittest.main()