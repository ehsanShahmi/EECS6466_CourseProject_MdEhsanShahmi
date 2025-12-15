import unittest
import json
import os
from unittest.mock import patch, mock_open
from datetime import datetime

class TestTaskFunc(unittest.TestCase):

    @patch('requests.get')
    def test_download_file(self, mock_get):
        # Mock the response of requests.get
        mock_get.return_value.content = b'This is a test file content.'
        
        json_str = '{"unknown": "https://example.com/file.txt"}'
        unknown_key = 'unknown'
        
        # Call the task_func (implementation not included)
        file_path = task_func(json_str, unknown_key)

        # Check if the file is created in the expected location
        self.assertTrue(os.path.isfile(file_path))
        with open(file_path, 'rb') as f:
            content = f.read()
        self.assertEqual(content, b'This is a test file content.')

    @patch('requests.get')
    def test_invalid_json(self, mock_get):
        json_str = '{"unknown": "https://example.com/file.txt"'
        unknown_key = 'unknown'
        
        # Test for ValueError with invalid JSON
        with self.assertRaises(ValueError):
            task_func(json_str, unknown_key)

    @patch('requests.get')
    def test_key_not_found(self, mock_get):
        mock_get.return_value.content = b'This is a test file content.'
        
        json_str = '{"other_key": "https://example.com/file.txt"}'
        unknown_key = 'unknown'
        
        # Test KeyError for a missing key in JSON
        with self.assertRaises(KeyError):
            task_func(json_str, unknown_key)

    @patch('requests.get')
    def test_custom_save_directory(self, mock_get):
        mock_get.return_value.content = b'This is a test file content.'
        
        json_str = '{"unknown": "https://example.com/file.txt"}'
        unknown_key = 'unknown'
        save_dir = './test_dir'
        os.makedirs(save_dir, exist_ok=True)  # Create a test directory if it does not exist

        # Call the task_func (implementation not included)
        file_path = task_func(json_str, unknown_key, save_dir)

        # Check if the file is created in the expected directory
        self.assertTrue(os.path.isfile(file_path))
        self.assertIn(save_dir, file_path)

    @patch('requests.get')
    def test_file_naming_convention(self, mock_get):
        mock_get.return_value.content = b'This is a test file content.'
        
        json_str = '{"unknown": "https://example.com/file.txt"}'
        unknown_key = 'unknown'
        
        # Call the task_func (implementation not included)
        file_path = task_func(json_str, unknown_key)

        # Check if the filename matches the expected naming convention
        expected_timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        self.assertTrue(file_path.startswith(f"{unknown_key}_{expected_timestamp}"))

if __name__ == '__main__':
    unittest.main()