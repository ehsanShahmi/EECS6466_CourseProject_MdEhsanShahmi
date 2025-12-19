import random
import string
from django.http import HttpResponse
import unittest
from django.conf import settings
from django.http import HttpRequest

def task_func(request, session_expire_time):
    """
    This function creates a random session key comprising letters and digits with a specific length of 20,
    then sets this key in a cookie on an HttpResponse object with the specified expiration time.

    Parameters:
    request (django.http.HttpRequest): The incoming Django HttpRequest.
    session_expire_time (int): The expiration time for the session cookie in seconds.

    Returns:
    django.http.HttpResponse: A Django HttpResponse with the session key set in a cookie.

    Raises:
    ValueError: If the session key does not contain both letters and digits or
                the session key length is not equal to 20.

    Note:
    -   The function set the response content to "Session key generated successfully." if the session key
        is valid.
    """

    session_key = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    
    has_digit = any(char.isdigit() for char in session_key)
    has_letter = any(char.isalpha() for char in session_key)
    if not (has_digit and has_letter) or len(session_key) != 20:
        raise ValueError("Session key should contain both letters and digits")

    response = HttpResponse('Session key generated successfully.')
    response.set_cookie('session_key', session_key, max_age=session_expire_time)
    return response

class TestSessionKeyGeneration(unittest.TestCase):
    
    def setUp(self):
        if not settings.configured:
            settings.configure()
        self.request = HttpRequest()
    
    def test_session_key_length(self):
        response = task_func(self.request, 60)
        self.assertEqual(len(response.cookies['session_key'].value), 20)

    def test_session_key_contains_letters_and_digits(self):
        response = task_func(self.request, 60)
        session_key = response.cookies['session_key'].value
        self.assertTrue(any(char.isdigit() for char in session_key))
        self.assertTrue(any(char.isalpha() for char in session_key))

    def test_set_cookie_expiration(self):
        response = task_func(self.request, 60)
        self.assertEqual(response.cookies['session_key']['max-age'], 60)

    def test_invalid_session_key_generation_no_letters(self):
        with self.assertRaises(ValueError):
            mock_request = HttpRequest()
            with unittest.mock.patch('random.choices', return_value=['1'] * 20):
                task_func(mock_request, 60)

    def test_invalid_session_key_generation_no_digits(self):
        with self.assertRaises(ValueError):
            mock_request = HttpRequest()
            with unittest.mock.patch('random.choices', return_value=['a'] * 20):
                task_func(mock_request, 60)

if __name__ == '__main__':
    unittest.main()