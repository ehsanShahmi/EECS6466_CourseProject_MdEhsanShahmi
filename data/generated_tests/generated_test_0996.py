import unittest
from unittest.mock import patch, mock_open, MagicMock
import requests

class TestTaskFunc(unittest.TestCase):
    
    @patch('requests.get')
    def test_valid_url_title(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, text='<html><head><title>Test Title</title></head></html>')
        with patch('builtins.open', mock_open()) as mocked_file:
            from task import task_func  # Assuming task_func is defined in task.py
            result = task_func("http://example.com")
            mocked_file.assert_called_once_with("Output.txt", "a", encoding="utf-8")
            mocked_file().write.assert_called_once_with('{"title": "Test Title"}\n')
            self.assertEqual(result, "Output.txt")

    @patch('requests.get')
    def test_valid_url_no_title(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, text='<html><head></head></html>')
        with patch('builtins.open', mock_open()) as mocked_file:
            from task import task_func
            result = task_func("http://example.com")
            mocked_file.assert_called_once_with("Output.txt", "a", encoding="utf-8")
            mocked_file().write.assert_called_once_with('{"title": null}\n')
            self.assertEqual(result, "Output.txt")

    @patch('requests.get')
    def test_nonexistent_url(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Connection Error")
        with patch('builtins.open', mock_open()) as mocked_file:
            from task import task_func
            with self.assertRaises(requests.exceptions.RequestException):
                task_func("http://nonexistent.url")
            mocked_file.assert_not_called()

    @patch('requests.get')
    def test_append_to_existing_file(self, mock_get):
        mock_get.return_value = MagicMock(status_code=200, text='<html><head><title>New Title</title></head></html>')
        with patch('builtins.open', mock_open(read_data='{"title": "Old Title"}\n')) as mocked_file:
            from task import task_func
            result = task_func("http://example.com", "ExistingOutput.txt")
            mocked_file.assert_called_once_with("ExistingOutput.txt", "a", encoding="utf-8")
            mocked_file().write.assert_called_once_with('{"title": "New Title"}\n')
            self.assertEqual(result, "ExistingOutput.txt")

    @patch('requests.get')
    def test_invalid_url_format(self, mock_get):
        with patch('builtins.open', mock_open()) as mocked_file:
            from task import task_func
            with self.assertRaises(ValueError):
                task_func("invalid-url")
            mocked_file.assert_not_called()

if __name__ == '__main__':
    unittest.main()