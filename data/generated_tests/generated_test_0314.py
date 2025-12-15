import socket
import ssl
import http.client
import unittest

def task_func(SERVER_NAME, SERVER_PORT, path):
    """
    Makes an HTTPS GET request to a specified server and path, and retrieves the response.

    Parameters:
        SERVER_NAME (str): The name of the server to which the request is made.
        SERVER_PORT (int): The port number of the server to which the request is made.
        path (str): The path for the HTTP request.

    Returns:
        str: The response body from the server as a string.

    Raises:
        ssl.SSLError: If there is an SSL handshake error.

    Requirements:
    - socket
    - ssl
    - http.client

    Examples:
    >>> response = task_func('www.example.com', 443, '/path/to/request')
    >>> isinstance(response, str)
    True
    """

    context = ssl.create_default_context()

    with socket.create_connection((SERVER_NAME, SERVER_PORT)) as sock:
        with context.wrap_socket(sock, server_hostname=SERVER_NAME) as ssock:
            conn = http.client.HTTPSConnection(SERVER_NAME, SERVER_PORT, context=context)
            conn.request('GET', path)
            response = conn.getresponse()
            return response.read().decode()

class TestTaskFunc(unittest.TestCase):

    def test_valid_request(self):
        response = task_func('www.example.com', 443, '/')
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)
        
    def test_invalid_server(self):
        with self.assertRaises(OSError):
            task_func('invalid.server', 443, '/')

    def test_invalid_path(self):
        response = task_func('www.example.com', 443, '/nonexistent')
        self.assertIsInstance(response, str)
        self.assertIn("404", response)  # Assuming the server returns a 404 page containing '404'
        
    def test_ssl_error(self):
        with self.assertRaises(ssl.SSLError):
            task_func('self-signed.badssl.com', 443, '/')

    def test_no_connection(self):
        with self.assertRaises(OSError):
            task_func('127.0.0.1', 9999, '/')  # Assuming nothing is running on port 9999

if __name__ == '__main__':
    unittest.main()