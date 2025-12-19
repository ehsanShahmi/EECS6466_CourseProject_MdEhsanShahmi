import re
import json
import requests
import unittest
from unittest.mock import MagicMock, patch


class TestTaskFunc(unittest.TestCase):
    
    @patch('requests.get')
    def test_valid_response_with_names(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"names": ["John", "[Adam]", "Eve"]}
        mock_get.return_value = mock_response
        
        result = task_func("https://api.example.com/other_data")
        self.assertEqual(result, ['John', 'Eve'])
    
    @patch('requests.get')
    def test_empty_names_list(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"names": []}
        mock_get.return_value = mock_response
        
        result = task_func("https://api.example.com/other_data")
        self.assertEqual(result, [])
    
    @patch('requests.get')
    def test_no_names_outside_brackets(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"names": ["[Adam]", "[Eve]"]}
        mock_get.return_value = mock_response
        
        result = task_func("https://api.example.com/other_data")
        self.assertEqual(result, [])

    @patch('requests.get')
    def test_exception_handling(self, mock_get):
        mock_get.side_effect = Exception("Some error")
        
        result = task_func("https://api.example.com/other_data")
        self.assertEqual(result, "Invalid url input")
    
    @patch('requests.get')
    def test_invalid_json_structure(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"wrong_key": []}
        mock_get.return_value = mock_response
        
        result = task_func("https://api.example.com/other_data")
        self.assertEqual(result, [])

        
if __name__ == '__main__':
    unittest.main()