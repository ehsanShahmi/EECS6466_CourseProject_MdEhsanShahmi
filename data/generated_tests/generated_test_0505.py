import hashlib
import hmac
import unittest

def task_func(secret, message):
    """
    Generates an HMAC (Hash-based Message Authentication Code) signature for a given message using a secret key.
    The function uses SHA-256 as the hash function to create the HMAC signature.

    Parameters:
    secret (str): The secret key used for HMAC generation.
    message (str): The message for which the HMAC signature is to be generated.

    Returns:
    str: The HMAC signature of the message, returned as a hexadecimal string.

    Requirements:
    - hashlib
    - hmac

    Examples:
    Generate an HMAC signature for a message.
    >>> len(task_func('mysecretkey', 'Hello, world!')) == 64
    True

    Generate an HMAC for a different message with the same key.
    >>> len(task_func('mysecretkey', 'Goodbye, world!')) == 64
    True
    """
    return hmac.new(secret.encode(), message.encode(), hashlib.sha256).hexdigest()

class TestHMACGeneration(unittest.TestCase):

    def test_hmac_length(self):
        self.assertEqual(len(task_func('mysecretkey', 'Hello, world!')), 64)
    
    def test_different_message_hmac_length(self):
        self.assertEqual(len(task_func('mysecretkey', 'Goodbye, world!')), 64)
    
    def test_same_message_different_secret(self):
        self.assertNotEqual(task_func('mysecretkey1', 'Hello, world!'), task_func('mysecretkey2', 'Hello, world!'))
    
    def test_different_hmac_for_different_messages(self):
        hmac1 = task_func('mysecretkey', 'Message 1')
        hmac2 = task_func('mysecretkey', 'Message 2')
        self.assertNotEqual(hmac1, hmac2)
    
    def test_empty_message(self):
        self.assertEqual(task_func('mysecretkey', ''), 'c2f4b0c32e045261909bb6c2a1a2dc1d9ce2b55c8c2e5550fa7abc7ff5cb91f6d')

if __name__ == '__main__':
    unittest.main()