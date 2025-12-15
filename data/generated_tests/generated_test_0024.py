import base64
import hashlib
import os
import unittest

# Here is your prompt:
def task_func(password, SALT_LENGTH = 32):
    """
    Hashes a password using the PBKDF2 HMAC algorithm with SHA-256 as the hashing algorithm, 
    combined with a randomly generated salt, and returns both the salt and the hashed password, 
    each base64-encoded.

    Parameters:
    password (str): The password to be hashed.
    SALT_LENGTH (int): the length of the randomly generated salt.

    Returns:
    tuple[bytes, bytes]: A tuple containing the base64-encoded salt and the base64-encoded hashed password as byte strings.

    Raises:
    ValueError if the password is None or empty

    Requirements:
    - base64
    - hashlib
    - os

    Example:
    >>> salt, hashed_password = task_func('my_password')
    >>> isinstance(salt, bytes)
    True
    >>> isinstance(hashed_password, bytes)
    True
    """

    if not password:
        raise ValueError
    salt = os.urandom(SALT_LENGTH)
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return base64.b64encode(salt), base64.b64encode(hashed_password)


class TestTaskFunc(unittest.TestCase):
    
    def test_valid_password(self):
        password = 'my_password'
        salt, hashed_password = task_func(password)
        self.assertIsInstance(salt, bytes)
        self.assertIsInstance(hashed_password, bytes)

    def test_empty_password(self):
        with self.assertRaises(ValueError):
            task_func('')

    def test_none_password(self):
        with self.assertRaises(ValueError):
            task_func(None)

    def test_salt_length(self):
        password = 'my_password'
        salt, _ = task_func(password)
        self.assertEqual(len(base64.b64decode(salt)), 32)

    def test_hashed_password_consistency(self):
        password = 'my_password'
        salt1, hashed_password1 = task_func(password)
        salt2, hashed_password2 = task_func(password)
        self.assertNotEqual(hashed_password1, hashed_password2)


if __name__ == '__main__':
    unittest.main()