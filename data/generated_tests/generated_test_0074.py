import socket
import requests
import unittest

def task_func(host):
    """
    This function resolves the IP address of the given host and then uses the IP address 
    to fetch geolocation information from the ipinfo.io API. The function is robust against
    various common errors, such as invalid hostnames, network issues, or problems with the 
    geolocation service.

    Parameters:
    host (str): The hostname to be resolved.

    Returns:
    dict: A dictionary containing the IP address and geolocation information if successful.

    Raises:
    ValueError: If 'host' is None or an empty string.
    ConnectionError: If there is a problem connecting to the geolocation service.

    Example:
    >>> result = task_func('google.com')
    >>> 'ip_address' in result and 'geolocation' in result
    True
    >>> task_func('')
    Traceback (most recent call last):
       ...
    ValueError: Host must be a non-empty string.
    
    Requirements:
    - socket
    - requests
    """

    if not host:
        raise ValueError("Host must be a non-empty string.")

    try:
        # Fetch IP address
        ip_address = socket.gethostbyname(host)

        # Fetch geolocation
        response = requests.get(f"https://ipinfo.io/{ip_address}")
        response.raise_for_status()
        geolocation = response.json()

        return {
            'ip_address': ip_address,
            'geolocation': geolocation
        }
    except (socket.gaierror, requests.HTTPError) as e:
        raise ConnectionError(f"Failed to retrieve information for {host}: {e}")

class TestTaskFunc(unittest.TestCase):

    def test_valid_host(self):
        """Test with a valid hostname."""
        result = task_func('google.com')
        self.assertIn('ip_address', result)
        self.assertIn('geolocation', result)
        self.assertIsInstance(result['ip_address'], str)

    def test_empty_hostname(self):
        """Test with an empty hostname."""
        with self.assertRaises(ValueError) as context:
            task_func('')
        self.assertEqual(str(context.exception), "Host must be a non-empty string.")

    def test_invalid_hostname(self):
        """Test with an invalid hostname."""
        with self.assertRaises(ConnectionError):
            task_func('invalid_hostname_1234')

    def test_none_hostname(self):
        """Test with a None hostname."""
        with self.assertRaises(ValueError) as context:
            task_func(None)
        self.assertEqual(str(context.exception), "Host must be a non-empty string.")

    def test_unreachable_hostname(self):
        """Test with a valid hostname but unreachable service."""
        with self.assertRaises(ConnectionError):
            task_func('localhost')

if __name__ == "__main__":
    unittest.main()