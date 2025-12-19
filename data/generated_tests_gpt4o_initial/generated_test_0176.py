import unittest
import socket
from unittest.mock import patch

# Here is your prompt:
import re
import socket

def task_func(ip_addresses: list) -> dict:
    """
    Given a list of IP addresses, this function returns a dictionary mapping each valid IP address to its 
    respective hostname. If the hostname cannot be determined, the value will be None.
    
    Parameters:
    ip_addresses (list): A list of IP addresses.
    
    Returns:
    dict: A dictionary with IP addresses as keys and their hostnames as values. If the hostname cannot be determined,
          the value will be None.
    
    Requirements:
    - re
    - socket
    
    Example:
    >>> task_func(['8.8.8.8', '8.8.4.4'])
    {'8.8.8.8': 'dns.google', '8.8.4.4': 'dns.google'}
    """

    IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'
    hostnames = {}
    for ip in ip_addresses:
        if re.match(IP_REGEX, ip):
            try:
                hostname = socket.gethostbyaddr(ip)[0]
                hostnames[ip] = hostname
            except (socket.herror, socket.gaierror):
                hostnames[ip] = None
    return hostnames


class TestTaskFunc(unittest.TestCase):

    @patch('socket.gethostbyaddr')
    def test_valid_ip_addresses(self, mock_gethostbyaddr):
        mock_gethostbyaddr.side_effect = [('dns.google', None, None), ('dns.google', None, None)]
        result = task_func(['8.8.8.8', '8.8.4.4'])
        expected = {'8.8.8.8': 'dns.google', '8.8.4.4': 'dns.google'}
        self.assertEqual(result, expected)

    @patch('socket.gethostbyaddr')
    def test_valid_ip_address_with_none_hostname(self, mock_gethostbyaddr):
        mock_gethostbyaddr.side_effect = socket.herror
        result = task_func(['8.8.8.8'])
        expected = {'8.8.8.8': None}
        self.assertEqual(result, expected)

    @patch('socket.gethostbyaddr')
    def test_partial_valid_ip_addresses(self, mock_gethostbyaddr):
        mock_gethostbyaddr.side_effect = [('example.com', None, None), socket.herror]
        result = task_func(['192.168.0.1', '256.256.256.256'])
        expected = {'192.168.0.1': 'example.com', '256.256.256.256': None}
        self.assertEqual(result, expected)

    def test_invalid_ip_addresses(self):
        result = task_func(['invalid_ip', '192.168.1.100'])
        expected = {'invalid_ip': None, '192.168.1.100': None}
        self.assertEqual(result, expected)

    @patch('socket.gethostbyaddr')
    def test_empty_ip_list(self, mock_gethostbyaddr):
        result = task_func([])
        expected = {}
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()