import json
import unittest
from datetime import datetime

# Here is your prompt:
# (The provided prompt functions will not be modified)
import json
import random
import hashlib
from datetime import datetime


def task_func(utc_datetime, salt='salt', password_length=10, seed=0):
    """
    Generate a random lowercase alphanumeric password of length password_length
    and then encrypt it as a JSON string. The password is hashed using SHA-256.
    The hashing uses the combination of the user provided salt and the complete 
    conventional string representation of the user provided UTC datetime. 
    
    Parameters:
    utc_datetime (datetime): The datetime in UTC.
    salt (str, optional): The salt to be used for hashing the password. Defaults to 'salt'.
    password_length (int, optional): The length of the password to be generated. Defaults to 10.
    seed (int, optional): The seed for the random number generator. Defaults to 0.
    
    Returns:
    str: The hashed password encoded as a JSON string.
    
    Requirements:
    - json
    - datetime
    - random
    - hashlib

    Raises:
    - ValueError: If the utc_datetime is not a datetime object or the salt is not a string.
    
    Example:
    >>> utc_time = datetime(2023, 6, 15, 12, 0, 0, tzinfo=pytz.UTC)
    >>> password_json_str = task_func(utc_time)
    """

    random.seed(seed)
    # Test if the utc_datetime is a datetime object and the salt is a string
    if not isinstance(utc_datetime, datetime):
        raise ValueError("Input should be a datetime object")
    if not isinstance(salt, str):
        raise ValueError("Salt should be a string")

    # Convert the datetime to a string
    utc_time_str = utc_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # Create the salted string
    salted_string = utc_time_str + salt

    # Generate a random password
    password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(password_length))
    
    # Hash the password
    hashed_password = hashlib.sha256((password + salted_string).encode('utf-8')).hexdigest()
    
    # Encode the hashed password as a JSON string
    password_json_str = json.dumps(hashed_password)
    
    return password_json_str


class TestTaskFunc(unittest.TestCase):
    
    def test_valid_input(self):
        """Test with valid datetime and default parameters."""
        utc_time = datetime(2023, 6, 15, 12, 0, 0)
        result = task_func(utc_time)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith('"') and result.endswith('"'))

    def test_custom_salt(self):
        """Test with a custom salt."""
        utc_time = datetime(2023, 6, 15, 12, 0, 0)
        salt = "custom_salt"
        result = task_func(utc_time, salt=salt)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith('"') and result.endswith('"'))

    def test_invalid_datetime(self):
        """Test with an invalid datetime input."""
        with self.assertRaises(ValueError):
            task_func("not_a_datetime")

    def test_invalid_salt(self):
        """Test with an invalid salt input."""
        utc_time = datetime(2023, 6, 15, 12, 0, 0)
        with self.assertRaises(ValueError):
            task_func(utc_time, salt=12345)

    def test_different_password_lengths(self):
        """Test with different password lengths."""
        utc_time = datetime(2023, 6, 15, 12, 0, 0)
        result = task_func(utc_time, password_length=15)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith('"') and result.endswith('"'))


if __name__ == '__main__':
    unittest.main()