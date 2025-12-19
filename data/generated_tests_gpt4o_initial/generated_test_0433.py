import base64
import hashlib
import hmac
import binascii
import unittest

def task_func(s, signature, secret_key):
    """
    Validates the HMAC SHA-1 signature of a base64-encoded message against a provided signature using a specified secret key.
    This function first decodes the base64-encoded message, then computes its HMAC SHA-1 hash using the provided secret key,
    and finally compares this computed hash with the provided signature.

    Parameters:
    s (str): The base64-encoded message to validate.
    signature (str): The HMAC SHA-1 signature to compare against.
    secret_key (str): The secret key used to compute the HMAC SHA-1 hash.

    Returns:
    bool: Returns True if the provided signature matches the computed signature, False otherwise.
    """
    decoded_msg = base64.b64decode(s).decode()
    computed_signature = hmac.new(secret_key.encode(), decoded_msg.encode(), hashlib.sha1)
    return binascii.hexlify(computed_signature.digest()).decode() == signature


class TestTaskFunc(unittest.TestCase):

    def test_valid_signature(self):
        self.assertTrue(task_func('SGVsbG8gV29ybGQ=', 'c47c23299efca3c220f4c19a5f2e4ced14729322', 'my_secret_key'))

    def test_invalid_signature(self):
        self.assertFalse(task_func('SGVsbG8gV29ybGQ=', 'incorrect_signature', 'my_secret_key'))

    def test_empty_message(self):
        self.assertFalse(task_func('', '69a6b1174e554c7af8018ad931a1ccc916f49f7c', 'my_secret_key'))

    def test_different_secret_key(self):
        self.assertFalse(task_func('SGVsbG8gV29ybGQ=', 'c47c23299efca3c220f4c19a5f2e4ced14729322', 'different_key'))

    def test_base64_decode_error(self):
        with self.assertRaises(binascii.Error):
            task_func('InvalidBase64String', 'SomeSignature', 'my_secret_key')


if __name__ == '__main__':
    unittest.main()