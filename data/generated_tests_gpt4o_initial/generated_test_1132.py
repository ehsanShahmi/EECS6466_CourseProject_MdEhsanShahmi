import os
import hashlib
import base64
import unittest

# Here is your prompt:
def task_func(password, PREFIX="ME", SALT_LENGTH=16):
    """
    Generates a hashed password by concatenating a given password with a prefix and a generated salt,
    and then hashing the combined string using SHA256. The hashed result is then encoded in base64.

    Parameters:
    - password (str): The password string to hash.
    - PREFIX (str): A prefix added to the password before hashing. Defaults to "ME".
    - SALT_LENGTH (int): The byte length of the random salt to be generated. Defaults to 16.

    Returns:
    - str: The base64 encoded SHA256 hash of the password concatenated with the prefix and salt.

    Raises:
    ValueError if the SALT_LENGTH is negative

    Requirements:
    - os
    - hashlib
    - base64

    Example:
    >>> hashed_password = task_func('password123', 'ME', 16)
    >>> isinstance(hashed_password, str)
    True
    """
    
    if SALT_LENGTH < 0:
        raise ValueError
    
    salt = os.urandom(SALT_LENGTH)
    salted_password = PREFIX + password + salt.hex()
    
    hashed_password = hashlib.sha256(salted_password.encode()).digest()

    return base64.b64encode(hashed_password).decode()

class TestTaskFunc(unittest.TestCase):

    def test_valid_password(self):
        hashed_password = task_func('password123', 'ME', 16)
        self.assertIsInstance(hashed_password, str)

    def test_prefix_variation(self):
        hashed_password1 = task_func('password123', 'ME', 16)
        hashed_password2 = task_func('password123', 'YOU', 16)
        self.assertNotEqual(hashed_password1, hashed_password2)

    def test_salt_length(self):
        hashed_password1 = task_func('password123', 'ME', 16)
        hashed_password2 = task_func('password123', 'ME', 32)
        self.assertNotEqual(hashed_password1, hashed_password2)

    def test_negative_salt_length(self):
        with self.assertRaises(ValueError):
            task_func('password123', 'ME', -1)

    def test_different_passwords(self):
        hashed_password1 = task_func('password123', 'ME', 16)
        hashed_password2 = task_func('differentpassword', 'ME', 16)
        self.assertNotEqual(hashed_password1, hashed_password2)

if __name__ == '__main__':
    unittest.main()