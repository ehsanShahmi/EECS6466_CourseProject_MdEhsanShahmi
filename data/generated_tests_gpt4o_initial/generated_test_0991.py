import unittest
import binascii
import string
import random

def task_func(length):
    """
    Generate a random hexadecimal string of a given length and then attempt to decode it in ASCII.
    The resulting ASCII string may contain non-printable characters
    or be shorter than the input length.

    Parameters:
    length (int): The length of the hexadecimal string.

    Returns:
    str: The decoded ASCII string.

    Requirements:
    - binascii
    - string
    - random

    Example:
    >>> random.seed(0)
    >>> task_func(6)
    '\\x18'
    >>> task_func(8)
    'Ƥ'
    """
    HEX_CHARS = string.hexdigits.lower()
    hex_string = "".join(random.choice(HEX_CHARS) for _ in range(length))
    return binascii.unhexlify(hex_string).decode("utf-8", "ignore")

class TestTaskFunc(unittest.TestCase):

    def test_length_zero(self):
        """Test with length 0, should return an empty string."""
        self.assertEqual(task_func(0), '')

    def test_length_one(self):
        """Test with length 1, should return a single character string or non-printable char."""
        result = task_func(1)
        self.assertEqual(len(result), 1)

    def test_length_two(self):
        """Test with length 2, the result should be either a character or a non-printable character."""
        result = task_func(2)
        self.assertEqual(len(result), 1)
    
    def test_non_printable_output(self):
        """Test with length 4, check if output contains non-printable characters."""
        result = task_func(4)
        self.assertTrue(all(c in string.printable for c in result))

    def test_random_seed(self):
        """Test with fixed seed for reproducible results."""
        random.seed(0)
        self.assertEqual(task_func(6), '\x18')

if __name__ == '__main__':
    unittest.main()