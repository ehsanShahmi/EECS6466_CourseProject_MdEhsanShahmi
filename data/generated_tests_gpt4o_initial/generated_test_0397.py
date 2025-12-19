import unittest
from unittest.mock import patch, MagicMock
import json

class TestTaskFunc(unittest.TestCase):

    @patch('urllib.request.urlopen')
    def test_valid_ip_address(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({'ip': '192.168.1.1'}).encode('utf-8')
        mock_urlopen.return_value = mock_response
        
        result = task_func('https://api.ipify.org?format=json')
        self.assertEqual(result, '192.168.1.1')

    @patch('urllib.request.urlopen')
    def test_invalid_ip_address_format(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({'ip': '999.999.999.999'}).encode('utf-8')
        mock_urlopen.return_value = mock_response
        
        result = task_func('https://api.ipify.org?format=json')
        self.assertEqual(result, 'Invalid IP address received')

    @patch('urllib.request.urlopen')
    def test_api_failure(self, mock_urlopen):
        mock_urlopen.side_effect = Exception('API request failed')
        
        result = task_func('https://api.ipify.org?format=json')
        self.assertEqual(result, 'API request failed')

    @patch('urllib.request.urlopen')
    def test_empty_response(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = json.dumps({'ip': ''}).encode('utf-8')
        mock_urlopen.return_value = mock_response
        
        result = task_func('https://api.ipify.org?format=json')
        self.assertEqual(result, 'Invalid IP address received')

    @patch('urllib.request.urlopen')
    def test_invalid_json_response(self, mock_urlopen):
        mock_response = MagicMock()
        mock_response.read.return_value = b'not a json'
        mock_urlopen.return_value = mock_response
        
        result = task_func('https://api.ipify.org?format=json')
        self.assertTrue('Expecting value' in result)  # Expecting a JSONDecodeError message

if __name__ == '__main__':
    unittest.main()