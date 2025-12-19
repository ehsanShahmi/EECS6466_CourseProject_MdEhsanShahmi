import unittest
import hashlib
import base64
from django.http import HttpResponseBadRequest
from django.conf import settings

# Here is the provided prompt
def task_func(data):
    """
    This method is designed to handle the authentication process in a web application context.
    It expects input in the form of a dictionary with 'username' and 'password' keys. The password
    is expected to be a base64-encoded SHA-256 hash. The method decodes and authenticates these credentials
    against predefined values (for demonstration purposes, it checks if the username is 'admin' and the
    password hash matches the hash of 'password'). Based on the authentication result, it returns an appropriate
    HTTP response.

    Parameters:
    data (dict): A dictionary with 'username' and 'password' keys.

    Returns:
    django.http.HttpResponse: An HttpResponse indicating the login result.
                              HttpResponseBadRequest if the data is invalid.

    Raises:
    KeyError, UnicodeDecodeError, binascii.Error, ValueError if the input dictionary is invalid.

    Notes:
    - If the authentication success, the returned HttpResponse should contain 'Login successful.' with status 400. 
    - If the authentication fails, the returned HttpResponse should contain 'Login failed.' with status 401.
    - If the input data is invalid (i.e., password is a non-base64, missing keys), the function return HttpResponseBadRequest and it contains 'Bad Request.'

    Examples:
    >>> data = {'username': 'admin', 'password': base64.b64encode(hashlib.sha256('password'.encode()).digest()).decode()}
    >>> response = task_func(data)
    >>> response.status_code == 200 and 'Login successful.' in response.content.decode()
    False

    >>> data = {'username': 'admin', 'password': base64.b64encode(hashlib.sha256('wrongpassword'.encode()).digest()).decode()}
    >>> response = task_func(data)
    >>> response.status_code == 401 and 'Login failed.' in response.content.decode()
    False

    Requirements:
    - django.http
    - django.conf
    - base64
    - hashlib
    - binascii
    """
    # ... omitted for brevity

class TestTaskFunc(unittest.TestCase):

    def test_login_success(self):
        data = {'username': 'admin', 'password': base64.b64encode(hashlib.sha256('password'.encode()).digest()).decode()}
        response = task_func(data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Login successful.', response.content.decode())

    def test_login_failure(self):
        data = {'username': 'admin', 'password': base64.b64encode(hashlib.sha256('wrongpassword'.encode()).digest()).decode()}
        response = task_func(data)
        self.assertEqual(response.status_code, 401)
        self.assertIn('Login failed.', response.content.decode())

    def test_missing_username(self):
        data = {'password': base64.b64encode(hashlib.sha256('password'.encode()).digest()).decode()}
        response = task_func(data)
        self.assertIsInstance(response, HttpResponseBadRequest)
        self.assertEqual(response.content.decode(), 'Bad Request')

    def test_missing_password(self):
        data = {'username': 'admin'}
        response = task_func(data)
        self.assertIsInstance(response, HttpResponseBadRequest)
        self.assertEqual(response.content.decode(), 'Bad Request')

    def test_invalid_base64_password(self):
        data = {'username': 'admin', 'password': 'invalid_base64'}
        response = task_func(data)
        self.assertIsInstance(response, HttpResponseBadRequest)
        self.assertEqual(response.content.decode(), 'Bad Request')

if __name__ == '__main__':
    unittest.main()