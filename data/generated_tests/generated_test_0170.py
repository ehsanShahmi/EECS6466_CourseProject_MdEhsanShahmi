import pandas as pd
import requests
from io import StringIO
import unittest
from unittest.mock import patch, Mock

class TestTaskFunc(unittest.TestCase):

    @patch('requests.get')
    def test_valid_response_sorted_by_title(self, mock_get):
        # Mock a valid CSV response
        mock_get.return_value = Mock(status_code=200, text='id,title,price\n1,Apple,0.3\n2,Banana,0.5\n3,Cherry,0.2\n')
        
        expected_output = pd.DataFrame({
            'id': [1, 2, 3],
            'title': ['Apple', 'Banana', 'Cherry'],
            'price': [0.3, 0.5, 0.2]
        }).sort_values(by='title')
        
        result = task_func("http://example.com/data.csv", sort_by_column="title")
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_output.reset_index(drop=True)

    @patch('requests.get')
    def test_valid_response_sorted_by_price(self, mock_get):
        # Mock a valid CSV response
        mock_get.return_value = Mock(status_code=200, text='id,title,price\n1,Apple,0.3\n2,Banana,0.5\n3,Cherry,0.2\n')
        
        expected_output = pd.DataFrame({
            'id': [3, 1, 2],
            'title': ['Cherry', 'Apple', 'Banana'],
            'price': [0.2, 0.3, 0.5]
        }).sort_values(by='price')
        
        result = task_func("http://example.com/data.csv", sort_by_column="price")
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_output.reset_index(drop=True)

    @patch('requests.get')
    def test_invalid_response_status_code(self, mock_get):
        # Mock an invalid response status code
        mock_get.return_value = Mock(status_code=404)
        
        with self.assertRaises(Exception):
            task_func("http://example.com/data.csv", sort_by_column="title")

    @patch('requests.get')
    def test_response_content_does_not_contain_csv(self, mock_get):
        # Mock a valid response but with invalid CSV format
        mock_get.return_value = Mock(status_code=200, text='Not a CSV format')
        
        with self.assertRaises(pd.errors.ParserError):
            task_func("http://example.com/data.csv", sort_by_column="title")

    @patch('requests.get')
    def test_empty_csv_response(self, mock_get):
        # Mock an empty CSV response
        mock_get.return_value = Mock(status_code=200, text='id,title,price\n')
        
        expected_output = pd.DataFrame(columns=['id', 'title', 'price'])
        
        result = task_func("http://example.com/data.csv", sort_by_column="title")
        pd.testing.assert_frame_equal(result, expected_output)

if __name__ == '__main__':
    unittest.main()