import ipaddress
import requests
import unittest

# Here is your prompt:
def task_func(ip_range, timeout):
    """
    Scans a specified IP address range and sends an HTTP GET request to each IP to verify if it is an active web server.
    The function requires an IP range in CIDR format (e.g., '192.168.0.0/16') and a timeout value in seconds.
    It returns a list of IPs where the request returned a status code of 200. If the request is not success, then ignore and continue
    to the next IP address.

    Parameters:
        ip_range (str): The IP range to scan in CIDR notation.
        timeout (int): The timeout for each HTTP GET request in seconds.

    Requirements:
        - ipaddress
        - requests

    Returns:
        list: A list of IP addresses that responded with a status code of 200.

    Raises:
        ValueError: If an invalid IP range is provided.

    Examples:
    >>> type(task_func('192.168.0.0/16', 5)) is list
    True
    >>> isinstance(task_func('192.168.0.0/16', 5), list)
    True
    """

               results = []
    try:
        network = ipaddress.IPv4Network(ip_range, strict=False)  # Note the `strict=False`
    except ValueError as e:
        raise ValueError(f"Invalid IP range: {e}")

    for ip in network:
        try:
            response = requests.get(f"http://{ip}", timeout=timeout)
            if response.status_code == 200:
                results.append(str(ip))
        except requests.exceptions.ConnectionError as e:
            pass
    return results


class TestTaskFunc(unittest.TestCase):

    def test_valid_ip_range(self):
        """ Test with a valid IP range and a short timeout """
        ip_range = '192.168.0.0/30'
        timeout = 1
        result = task_func(ip_range, timeout)
        self.assertIsInstance(result, list)

    def test_invalid_ip_range(self):
        """ Test with an invalid IP range """
        ip_range = '999.999.999.999/30'
        timeout = 1
        with self.assertRaises(ValueError):
            task_func(ip_range, timeout)

    def test_empty_ip_range(self):
        """ Test with an empty IP range """
        ip_range = ''
        timeout = 1
        with self.assertRaises(ValueError):
            task_func(ip_range, timeout)
    
    def test_no_active_servers(self):
        """ Test with a valid IP range but no active servers """
        ip_range = '192.0.2.0/30'  # This is a reserved block for documentation and should have no active servers.
        timeout = 1
        result = task_func(ip_range, timeout)
        self.assertEqual(result, [])

    def test_timeout_exceed(self):
        """ Test with a valid IP range and a timeout that is likely to cause a failure """
        ip_range = '192.168.0.0/30'
        timeout = 0.001  # Very short timeout
        result = task_func(ip_range, timeout)
        self.assertIsInstance(result, list)  # Should still return a list, even if it's empty.


if __name__ == "__main__":
    unittest.main()