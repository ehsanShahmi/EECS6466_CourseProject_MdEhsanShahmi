import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from python_http_client.exceptions import HTTPError
import unittest
from unittest.mock import patch, MagicMock

class TestTaskFunction(unittest.TestCase):

    @patch('os.listdir')
    @patch('sendgrid.SendGridAPIClient')
    def test_task_func_success(self, mock_sendgrid_client, mock_listdir):
        mock_listdir.return_value = ['file1.txt', 'file2.txt']
        mock_response = MagicMock()
        mock_response.status_code = 202
        mock_sendgrid_client.return_value.send.return_value = mock_response
        
        result = task_func('./test_directory', 'test_api_key', 'test@example.com')
        self.assertTrue(result)

    @patch('os.listdir', side_effect=FileNotFoundError)
    def test_task_func_directory_not_exist(self, mock_listdir):
        with self.assertRaises(FileNotFoundError):
            task_func('/nonexistent_directory', 'test_api_key', 'test@example.com')

    @patch('os.listdir')
    @patch('sendgrid.SendGridAPIClient')
    def test_task_func_http_error(self, mock_sendgrid_client, mock_listdir):
        mock_listdir.return_value = ['file1.txt']
        mock_sendgrid_client.return_value.send.side_effect = HTTPError("HTTP error occurred")
        
        with self.assertRaises(HTTPError):
            task_func('./test_directory', 'test_api_key', 'test@example.com')

    @patch('os.listdir')
    @patch('sendgrid.SendGridAPIClient')
    def test_task_func_other_exception(self, mock_sendgrid_client, mock_listdir):
        mock_listdir.return_value = ['file1.txt']
        mock_sendgrid_client.return_value.send.side_effect = Exception("Generic error")
        
        with self.assertRaises(Exception):
            task_func('./test_directory', 'test_api_key', 'test@example.com')

    @patch('os.listdir')
    @patch('sendgrid.SendGridAPIClient')
    def test_task_func_empty_directory(self, mock_sendgrid_client, mock_listdir):
        mock_listdir.return_value = []
        mock_response = MagicMock()
        mock_response.status_code = 202
        mock_sendgrid_client.return_value.send.return_value = mock_response
        
        result = task_func('./empty_directory', 'test_api_key', 'test@example.com')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()