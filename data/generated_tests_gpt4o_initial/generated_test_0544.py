import struct
import zlib
import unittest

# Constants
KEY = '470FC614'

def task_func(hex_string=KEY):
    """
    Converts a given hex string to a float number and then compresses the binary32 float number.

    Parameters:
    hex_string (str, optional): The hex string to be converted. Defaults to 470FC614.

    Returns:
    bytes: The compressed float number.

    Requirements:
    - struct
    - zlib

    Example:
    >>> task_func("470FC614")
    b'x\\x9c\\xf3\\xeb\\x93\\xef\\x01\\x00\\x03\\xb0\\x01\\x88'
    >>> task_func("ABCD1234")
    b'x\\x9c\\xf3\\xd7>+\\x04\\x00\\x03m\\x01Z'
    """
    
    binary_float = struct.pack('!f', int(hex_string, 16))
    compressed_data = zlib.compress(binary_float)
    return compressed_data

class TestTaskFunc(unittest.TestCase):
    
    def test_default_key(self):
        expected = b'x\x9c\xf3\xeb\x93\xef\x01\x00\x03\xb0\x01\x88'
        result = task_func()  # Using the default key
        self.assertEqual(result, expected)

    def test_abcd_hex_string(self):
        expected = b'x\x9c\xf3\xd7>+\x04\x00\x03m\x01Z'
        result = task_func("ABCD1234")
        self.assertEqual(result, expected)

    def test_zero_hex_string(self):
        expected = b'x\x9c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        result = task_func("00000000")
        self.assertEqual(result, expected)

    def test_negative_hex_string(self):
        expected = b'x\x9c\xcb\xcc\xcc\xcc\xcc\xcc\xcc\xcc\xcc\x03'
        result = task_func("B2B2B2B2")  # This should yield a negative float
        self.assertEqual(result, expected)

    def test_large_hex_string(self):
        expected = b'x\x9c\xfa[\xce\xec6\x04\x00\x0b\x06\x01\xff'
        result = task_func("FFFFFFFF")
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()