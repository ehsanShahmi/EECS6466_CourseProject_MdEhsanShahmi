import unittest
from unittest.mock import patch, Mock
import pandas as pd

class TestTaskFunc(unittest.TestCase):

    @patch('requests.get')
    def test_valid_url_and_sort_by_title(self, mock_get):
        # Mock the response from requests.get
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.text = "id,title,price\n1,Apple,0.3\n2,Banana,0.5\n3,Cherry,0.2"
        
        result = task_func({"URL": "http://example.com/data.csv"}, "title")
        expected_data = {
            'id': [1, 2, 3],
            'title': ['Apple', 'Banana', 'Cherry'],
            'price': [0.3, 0.5, 0.2]
        }
        expected_df = pd.DataFrame(expected_data)
        expected_df = expected_df.sort_values(by='title').reset_index(drop=True)
        
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)

    @patch('requests.get')
    def test_valid_url_and_sort_by_price(self, mock_get):
        mock_get.return_value = Mock(ok=True)
        mock_get.return_value.text = "id,title,price\n1,Apple,0.3\n2,Banana,0.5\n3,Cherry,0.2"
        
        result = task_func({"URL": "http://example.com/data.csv"}, "price")
        expected_data = {
            'id': [3, 1, 2],
            'title': ['Cherry', 'Apple', 'Banana'],
            'price': [0.2, 0.3, 0.5]
        }
        expected_df = pd.DataFrame(expected_data)
        expected_df = expected_df.sort_values(by='price').reset_index(drop=True)
        
        pd.testing.assert_frame_equal(result.reset_index(drop=True), expected_df)

    def test_empty_dictionary(self):
        with self.assertRaises(ValueError):
            task_func({}, "title")

    def test_missing_url_key(self):
        with self.assertRaises(ValueError):
            task_func({"not_url": "http://example.com/data.csv"}, "title")

    @patch('requests.get')
    def test_invalid_http_response(self, mock_get):
        mock_get.return_value = Mock(ok=False)
        with self.assertRaises(requests.exceptions.HTTPError):
            task_func({"URL": "http://example.com/nonexistent.csv"}, "title")

if __name__ == '__main__':
    unittest.main()