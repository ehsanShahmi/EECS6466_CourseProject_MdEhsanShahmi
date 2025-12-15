import unittest
import numpy as np
import secrets
import hashlib
import base64

def task_func(num, from_base, to_base, alphabet):
    """
    Converts a number from one base to another, adds a random salt, hashes the result using SHA-256,
    and then encodes the hash in base64 using a custom alphabet. The function also returns the used salt.
    
    Parameters:
    num (str): The number to be converted, represented as a string.
    from_base (int): The base of the number to be converted.
    to_base (int): The base to convert the number to.
    alphabet (str): The custom alphabet to be used for base64 encoding.
    
    Returns:
    tuple: A tuple containing the base64-encoded hash of the converted number and the used salt.

    Raises:
    ValueError: If `from_base` or `to_base` is less than 2, indicating an invalid base for conversion.
    ValueError: If the `num` string contains characters not valid in the `from_base` specified, indicating an invalid number format for conversion.
    """

    base64_table = np.array(list(alphabet))
    n = int(num, from_base)
    new_num = ''

    if to_base < 2:
        raise ValueError("to_base must be >= 2.")

    while n > 0:
        n, m = divmod(n, to_base)
        new_num += base64_table[m]

    num = new_num[::-1]
    salt = secrets.token_hex(16)
    hashed_num = hashlib.pbkdf2_hmac('sha256', bytes(num, 'utf-8'), bytes(salt, 'utf-8'), 100000)
    base64_encoded = base64.b64encode(hashed_num)

    return base64_encoded.decode(), salt

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
    
    def test_conversion_hex_to_octal(self):
        encoded, salt = task_func('A1', 16, 8, self.alphabet)
        self.assertIsInstance(encoded, str)
        self.assertIsInstance(salt, str)

    def test_invalid_from_base(self):
        with self.assertRaises(ValueError):
            task_func('A1', 1, 8, self.alphabet)

    def test_invalid_to_base(self):
        with self.assertRaises(ValueError):
            task_func('A1', 16, 1, self.alphabet)

    def test_invalid_num_format(self):
        with self.assertRaises(ValueError):
            task_func('G1', 16, 8, self.alphabet)

    def test_different_results_with_same_input(self):
        result1, salt1 = task_func('FF', 16, 8, self.alphabet)
        result2, salt2 = task_func('FF', 16, 8, self.alphabet)
        self.assertNotEqual(result1, result2)

if __name__ == '__main__':
    unittest.main()