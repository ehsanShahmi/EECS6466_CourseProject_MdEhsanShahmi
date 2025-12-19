import unittest
from ipaddress import IPv4Network

# Here is your prompt:
import subprocess
from ipaddress import IPv4Network

def task_func(ip_range):
    """
    Scans the specified IP address range and pings each IP to check if it is active.
    The function returns a dictionary with IP addresses as keys and a boolean value indicating
    their active status (True if the ping is successful, False otherwise).

    Parameters:
        ip_range (str): The IP range to scan, in CIDR notation (e.g., '192.168.0.0/24').

    Requirements:
    - ipaddress
    - subprocess

    Returns:
        dict: A dictionary mapping IP addresses to their active status.

    Raises:
        subprocess.CalledProcessError: If a ping command fails due to a subprocess error.

    Examples:
    >>> result = task_func('192.168.1.0/24')
    >>> isinstance(result, dict)
    True
    >>> all(isinstance(key, str) and isinstance(value, bool) for key, value in result.items())
    True
    """

    active_ips = {}

    for ip in IPv4Network(ip_range):
        try:
            subprocess.check_output(f'ping -c 1 {ip}', shell=True)
            active_ips[str(ip)] = True
        except subprocess.CalledProcessError:
            active_ips[str(ip)] = False

    return active_ips

class TestTaskFunc(unittest.TestCase):

    def test_valid_cidr_range(self):
        """ Test a valid CIDR range and check if the return type is a dictionary. """
        result = task_func('192.168.1.0/24')
        self.assertIsInstance(result, dict)

    def test_empty_cidr_range(self):
        """ Test an empty CIDR range and expect an empty dictionary. """
        result = task_func('192.168.1.0/32')
        self.assertEqual(result, {'192.168.1.0': False})  # Assuming no devices are active

    def test_invalid_cidr_range_format(self):
        """ Test an invalid CIDR notation and expect a value error to be raised. """
        with self.assertRaises(ValueError):
            task_func('192.168.1.0/33')

    def test_ip_addresses_in_cidr(self):
        """ Test that the generated IP addresses from a CIDR range are correct. """
        result = task_func('192.168.1.0/29')
        self.assertTrue(set(result.keys()).issubset({
            '192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.3', 
            '192.168.1.4', '192.168.1.5', '192.168.1.6', '192.168.1.7'
        }))

    def test_ping_command_success(self):
        """ 
        This test assumes that a specific IP address (localhost) is always active,
        given the environment that this test code is being executed.
        """
        result = task_func('127.0.0.0/30')
        self.assertTrue(result['127.0.0.1'])  # localhost should be active

if __name__ == '__main__':
    unittest.main()