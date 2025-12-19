import unittest
import base64
from cryptography.fernet import Fernet

# Here is your prompt:
def task_func(message, encryption_key):
    """
    Encrypts a message with a symmetric encryption key using Fernet encryption, and then encode the 
    encrypted message using base64.

    Parameters:
    message (str): The message to be encrypted and encoded.
    encryption_key (str): The key used for symmetric encryption. It should be a string, which will 
                          be encoded to bytes, then URL-safe base64 encoded to conform to the requirements 
                          for Fernet (32 bytes after encoding).

    Returns:
    str: The base64 encoded encrypted message. The message is first encrypted using Fernet encryption, 
         then the result is base64 encoded.

    Requirements:
    - base64
    - cryptography.fernet

    Example:
    >>> encrypted_message = task_func('Hello, World!', '01234567890123456789012345678901')
    >>> isinstance(encrypted_message, str)
    True
    """

    fernet = Fernet(base64.urlsafe_b64encode(encryption_key.encode()))
    encrypted_message = fernet.encrypt(message.encode())
    return base64.b64encode(encrypted_message).decode()


class TestTaskFunc(unittest.TestCase):

    def test_encrypt_empty_message(self):
        """Test encryption of an empty message"""
        encryption_key = '01234567890123456789012345678901'
        encrypted_message = task_func('', encryption_key)
        self.assertIsInstance(encrypted_message, str)
        self.assertNotEqual(encrypted_message, '')

    def test_encrypt_message(self):
        """Test encryption of a non-empty message"""
        message = 'Hello, World!'
        encryption_key = '01234567890123456789012345678901'
        encrypted_message = task_func(message, encryption_key)
        self.assertIsInstance(encrypted_message, str)
        self.assertNotEqual(encrypted_message, base64.b64encode(message.encode()).decode())

    def test_encrypt_with_different_keys(self):
        """Test encryption with different keys leads to different encrypted messages"""
        message = 'Hello, World!'
        encryption_key1 = '01234567890123456789012345678901'
        encryption_key2 = 'abcdefghijklmnopqrstuvwxyz123456'
        encrypted_message1 = task_func(message, encryption_key1)
        encrypted_message2 = task_func(message, encryption_key2)
        self.assertNotEqual(encrypted_message1, encrypted_message2)

    def test_invalid_key_length(self):
        """Test encryption with an invalid key length"""
        message = 'Hello, World!'
        encryption_key = 'short_key'  # Invalid key, less than 32 bytes
        with self.assertRaises(ValueError):
            task_func(message, encryption_key)

    def test_base64_encoded_result(self):
        """Test that the result is base64 encoded"""
        message = 'Hello, World!'
        encryption_key = '01234567890123456789012345678901'
        encrypted_message = task_func(message, encryption_key)
        self.assertTrue(base64.urlsafe_b64decode(encrypted_message).decode(errors='ignore'))


if __name__ == '__main__':
    unittest.main()