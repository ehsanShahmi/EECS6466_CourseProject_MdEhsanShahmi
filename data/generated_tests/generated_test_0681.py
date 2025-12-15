import pandas as pd
import json
import unittest
from unittest.mock import mock_open, patch


class TestTaskFunc(unittest.TestCase):
    
    def test_valid_json_with_key(self):
        mock_data = json.dumps([{"name": "Alice", "age": 30, "ele": "value1"},
                                 {"name": "Bob", "age": 25, "ele": "value2"}])
        expected_data = json.dumps([{"name": "Alice", "age": 30},
                                    {"name": "Bob", "age": 25}])
        
        with patch("builtins.open", mock_open(read_data=mock_data)) as mock_file:
            df = task_func("mock_file_path.json", "ele")
            mock_file().write.assert_called_once_with(expected_data)
            self.assertEqual(len(df.columns), 2)
            self.assertIn("name", df.columns)
            self.assertIn("age", df.columns)

    def test_json_without_key(self):
        mock_data = json.dumps([{"name": "Alice", "age": 30},
                                 {"name": "Bob", "age": 25}])
        
        with patch("builtins.open", mock_open(read_data=mock_data)) as mock_file:
            df = task_func("mock_file_path.json", "ele")
            mock_file().write.assert_called_once_with(mock_data)
            self.assertEqual(len(df.columns), 2)
            self.assertIn("name", df.columns)
            self.assertIn("age", df.columns)

    def test_invalid_key_removal(self):
        mock_data = json.dumps([{"name": "Alice", "age": 30}])
        
        with patch("builtins.open", mock_open(read_data=mock_data)) as mock_file:
            df = task_func("mock_file_path.json", "non_existing_key")
            mock_file().write.assert_called_once_with(mock_data)
            self.assertEqual(len(df.columns), 2)
            self.assertIn("name", df.columns)

    def test_empty_json(self):
        mock_data = json.dumps([])
        
        with patch("builtins.open", mock_open(read_data=mock_data)) as mock_file:
            df = task_func("mock_file_path.json", "ele")
            mock_file().write.assert_called_once_with(json.dumps([]))
            self.assertEqual(len(df), 0)

    def test_invalid_json_format(self):
        invalid_json_data = "{name: 'Alice', age: 30}"  # Invalid JSON
        
        with patch("builtins.open", mock_open(read_data=invalid_json_data)):
            with self.assertRaises(json.JSONDecodeError):
                task_func("mock_file_path.json", "ele")


if __name__ == "__main__":
    unittest.main()