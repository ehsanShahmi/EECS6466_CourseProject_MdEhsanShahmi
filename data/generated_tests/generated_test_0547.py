import unittest
import hashlib
import os
import base64


def task_func(password: str, salt_length: int = 8) -> str:
    """
    Encrypt a password using Salt and SHA-256, then encode the result in base64.

    Parameters:
    password (str): The password to be encrypted.
    salt_length (int, optional): The length of the generated salt. Default is 8.

    Returns:
    str: The encrypted password in base64 format.

    Requirements:
    - base64
    - hashlib
    - os

    Example:
    >>> isinstance(task_func('my_password'), str)
    True
    """
    salt = os.urandom(salt_length)
    hash = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    salted_hash = salt + hash
    encrypted_password = base64.b64encode(salted_hash)

    return encrypted_password.decode('utf-8')


class TestPasswordEncryption(unittest.TestCase):
    
    def test_encryption_output_type(self):
        """Test that the output of the task_func is of type str."""
        result = task_func('test_password')
        self.assertIsInstance(result, str)

    def test_encryption_output_length(self):
        """Test that the output of the task_func has a specific length."""
        result = task_func('test_password')
        self.assertEqual(len(result),  24)  # base64 encoded results of 32 bytes (8 salt + 32 hash)

    def test_different_passwords_yield_different_results(self):
        """Test that different passwords yield different encrypted results."""
        result1 = task_func('password1')
        result2 = task_func('password2')
        self.assertNotEqual(result1, result2)

    def test_same_password_yields_same_salt_hash_length(self):
        """Test that encrypting the same password results in consistent salted hash length."""
        result1 = task_func('consistent_password')
        result2 = task_func('consistent_password')
        self.assertEqual(len(result1), len(result2))

    def test_empty_password(self):
        """Test that encrypting an empty password returns a valid base64 string."""
        result = task_func('')
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)


if __name__ == '__main__':
    unittest.main()