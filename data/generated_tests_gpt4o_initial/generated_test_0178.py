import unittest
import json

# Here is your prompt:
import re
from urllib import request
import json

# Constants
IP_REGEX = r'[0-9]+(?:\.[0-9]+){3}'

def task_func(ip_address):
    """
    Get the public IP address from a JSON response containing the IP address.
    
    Parameters:
    ip_address (str): JSON-formatted string containing the IP address. 

    Returns:
    str: The public IP address.
    
    Note:
    - The function needs to check whether the provided IP address is valid.
      If the IP address is not valid, the function will return 'Invalid IP address received'.

    Requirements:
    - re
    - urllib.request
    - json
    
    Example:
    >>> ip_address = '{"ip": "192.168.1.1"}'
    >>> task_func(ip_address)
    '192.168.1.1'
    """

           
    try:
        response = ip_address
        data = json.loads(response)
        ip = data['ip']
        if re.match(IP_REGEX, ip):
            return ip
        else:
            return 'Invalid IP address received'
    except Exception as e:
        return str(e)

class TestTaskFunc(unittest.TestCase):

    def test_valid_ip(self):
        ip_address = '{"ip": "192.168.1.1"}'
        result = task_func(ip_address)
        self.assertEqual(result, '192.168.1.1')

    def test_valid_public_ip(self):
        ip_address = '{"ip": "203.0.113.45"}'
        result = task_func(ip_address)
        self.assertEqual(result, '203.0.113.45')

    def test_invalid_ip_format(self):
        ip_address = '{"ip": "999.999.999.999"}'
        result = task_func(ip_address)
        self.assertEqual(result, 'Invalid IP address received')

    def test_no_ip_key(self):
        ip_address = '{"not_ip": "192.168.1.1"}'
        result = task_func(ip_address)
        self.assertTrue('KeyError' in result)

    def test_empty_string(self):
        ip_address = ''
        result = task_func(ip_address)
        self.assertTrue('Expecting value' in result)

if __name__ == '__main__':
    unittest.main()