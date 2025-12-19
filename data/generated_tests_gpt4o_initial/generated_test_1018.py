import unittest
from unittest.mock import patch
from task_module import task_func  # Assuming the function is in 'task_module.py'

class TestTaskFunc(unittest.TestCase):

    @patch('requests.get')
    def test_task_func_valid_url(self, mock_get):
        """ Test with a valid URL and default parameters """
        html_content = "<html><body><h1>Example Domain</h1></body></html>"
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = html_content.encode('cp1251')

        result = task_func("http://example.com")

        self.assertIsNotNone(result)
        self.assertEqual(result.h1.string, "Example Domain")

    @patch('requests.get')
    def test_task_func_invalid_url(self, mock_get):
        """ Test with an invalid URL """
        mock_get.side_effect = requests.exceptions.MissingSchema

        result = task_func("")

        self.assertIsNone(result)

    @patch('requests.get')
    def test_task_func_network_error(self, mock_get):
        """ Test network error scenario """
        mock_get.side_effect = requests.exceptions.ConnectionError

        result = task_func("http://example.com")

        self.assertIsNone(result)

    @patch('requests.get')
    def test_task_func_non_200_status_code(self, mock_get):
        """ Test with a non-200 HTTP response status code """
        mock_get.return_value.status_code = 404
        mock_get.return_value.content = b''

        result = task_func("http://example.com")

        self.assertIsNone(result)

    @patch('requests.get')
    def test_task_func_invalid_encoding(self, mock_get):
        """ Test with an invalid encoding """
        html_content = "<html><body><h1>Example Domain</h1></body></html>"
        mock_get.return_value.status_code = 200
        mock_get.return_value.content = html_content.encode('utf-8')

        result = task_func("http://example.com", from_encoding="invalid_encoding")

        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()