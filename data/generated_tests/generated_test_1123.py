import unittest
from datetime import datetime

# Here is your prompt:
import re
import urllib.parse
import ssl
import socket

def task_func(myString):
    """
    Extracts all URLs from a string and retrieves the domain and the expiration date of the SSL certificate 
    for each HTTPS URL. Only HTTPS URLs are processed; HTTP URLs are ignored. The function handles SSL errors 
    by ignoring any HTTPS URLs where the SSL certificate cannot be retrieved due to such errors, and these domains 
    are not included in the returned dictionary.

    Parameters:
    myString (str): The string from which to extract URLs.
    
    Returns:
    dict: A dictionary with domains as keys and SSL certificate expiry dates in UTC format as values. 
          The dictionary includes only those HTTPS URLs for which the SSL certificate was successfully retrieved.
          Domains with SSL errors are excluded.

    Requirements:
    - re
    - urllib.parse
    - ssl
    - socket
    
    Example:
    >>> task_func("Check these links: https://www.google.com, https://www.python.org")
    {'www.google.com': '2023-06-15 12:00:00', 'www.python.org': '2023-07-20 12:00:00'}
    """

    urls = re.findall(r'https://[^\s,]+', myString)
    ssl_expiry_dates = {}

    for url in urls:
        try:
            domain = urllib.parse.urlparse(url).netloc
            context = ssl.create_default_context()
            with socket.create_connection((domain, 443)) as sock:
                with context.wrap_socket(sock, server_hostname=domain) as ssock:
                    ssl_expiry_dates[domain] = ssock.getpeercert()['notAfter']
        except ssl.SSLError:
            continue  # Ignore SSL errors or log them if necessary

    return ssl_expiry_dates


class TestTaskFunc(unittest.TestCase):

    def test_single_https_url(self):
        result = task_func("Check this link: https://www.google.com")
        self.assertIn('www.google.com', result)

    def test_multiple_https_urls(self):
        result = task_func("Check these links: https://www.google.com, https://www.python.org")
        self.assertEqual(len(result), 2)
        self.assertIn('www.google.com', result)
        self.assertIn('www.python.org', result)

    def test_no_https_urls(self):
        result = task_func("Check this link: http://www.example.com")
        self.assertEqual(result, {})

    def test_mixed_urls(self):
        result = task_func("Links: https://www.google.com and http://www.example.com")
        self.assertIn('www.google.com', result)
        self.assertEqual(len(result), 1)

    def test_invalid_https_url(self):
        result = task_func("This is an invalid URL: https://invalid.url")
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()