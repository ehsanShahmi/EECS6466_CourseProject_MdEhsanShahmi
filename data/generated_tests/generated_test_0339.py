import json
import urllib.parse
import hmac
import hashlib
import unittest

def task_func(req_data, secret_key):
    """
    Signs the specified request data with a secret key using HMAC SHA256, then URL encodes the signature and replace spaces with '+'.

    Parameters:
        req_data (dict): The request data to be signed. It should be a dictionary.
        secret_key (str): The secret key used for signing the request data.

    Returns:
        str: The URL encoded HMAC signature of the request data.

    Raises:
        TypeError: If `req_data` is not a dictionary.

    Requirements:
    - json
    - urllib.parse
    - hmac
    - hashlib

    Examples:
    >>> secret_key = 'my_secret_key'
    >>> isinstance(task_func({'test': 'just a test'}, secret_key), str)
    True
    >>> isinstance(task_func({'another': 'data', 'key': 123}, secret_key), str)
    True
    """

    if not isinstance(req_data, dict):
        raise TypeError("req_data must be a dictionary")
    # Convert request data to json string
    json_req_data = json.dumps(req_data)
    # Create a new hmac object with the secret key and the json string as the message
    hmac_obj = hmac.new(secret_key.encode(), json_req_data.encode(), hashlib.sha256)
    # Get the hmac signature
    hmac_signature = hmac_obj.hexdigest()  # Use hexdigest for a hexadecimal representation
    # URL encode the hmac signature
    url_encoded_signature = urllib.parse.quote_plus(hmac_signature)

    return url_encoded_signature


class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.secret_key = 'my_secret_key'
        
    def test_standard_dict(self):
        req_data = {'test': 'just a test'}
        result = task_func(req_data, self.secret_key)
        self.assertIsInstance(result, str)

    def test_another_standard_dict(self):
        req_data = {'another': 'data', 'key': 123}
        result = task_func(req_data, self.secret_key)
        self.assertIsInstance(result, str)
        
    def test_dict_with_special_characters(self):
        req_data = {'special characters': '!@#$%^&*()_+'}
        result = task_func(req_data, self.secret_key)
        self.assertIsInstance(result, str)

    def test_empty_dict(self):
        req_data = {}
        result = task_func(req_data, self.secret_key)
        self.assertIsInstance(result, str)

    def test_invalid_req_data_type(self):
        req_data = "this is not a dict"
        with self.assertRaises(TypeError) as context:
            task_func(req_data, self.secret_key)
        self.assertEqual(str(context.exception), "req_data must be a dictionary")


if __name__ == '__main__':
    unittest.main()