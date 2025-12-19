import numpy as np
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
import unittest

def task_func(num, from_base, to_base, private_key, alphabet):
    """
    Converts a number from one base to another, signs it with a private RSA key,
    and encodes the signed number in base64 using a custom alphabet.

    Parameters:
    - num (str): The number to be converted, represented as a string.
    - from_base (int): The base of the number to be converted.
    - to_base (int): The base to convert the number to.
    - private_key (Any): The private RSA key for signing. The type hint is `Any` due to the dynamic nature of key objects.
    - alphabet (str): A string representing the custom alphabet for base64 encoding.

    Returns:
    - str: The base64-encoded signed number.
    """
    base64_table = np.array(list(alphabet))
    n = int(num, from_base)
    
    new_num = ''
    while n > 0:
        n, m = divmod(n, to_base)
        new_num += base64_table[m]

    num = new_num[::-1]
    data = bytes(num, 'utf-8')
    signed_num = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    base64_encoded = base64.b64encode(signed_num)

    return base64_encoded.decode()

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        self.alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
    
    def test_conversion_base_16_to_8(self):
        result = task_func('A1', 16, 8, self.private_key, self.alphabet)
        self.assertIsInstance(result, str)

    def test_conversion_base_10_to_16(self):
        result = task_func('255', 10, 16, self.private_key, self.alphabet)
        self.assertIsInstance(result, str)

    def test_conversion_base_2_to_10(self):
        result = task_func('1101', 2, 10, self.private_key, self.alphabet)
        self.assertIsInstance(result, str)

    def test_conversion_base_8_to_2(self):
        result = task_func('17', 8, 2, self.private_key, self.alphabet)
        self.assertIsInstance(result, str)

    def test_conversion_invalid_base(self):
        with self.assertRaises(ValueError):
            task_func('Z', 36, 10, self.private_key, self.alphabet)

if __name__ == '__main__':
    unittest.main()