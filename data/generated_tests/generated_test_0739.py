import struct
import random
import unittest

# Constants
KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_key=None):
    """
    Generate a random float number from a list of hexadecimal strings and then round the float number to 2 decimal places.

    Parameters:
    - None

    Returns:
    - rounded_float (float): The rounded float number.

    Requirements:
    - struct
    - random

    Example:
    >>> random.seed(42)
    >>> print(repr(f"{task_func():.1f}"))
    '36806.1'
    """
    if hex_key is None:
        hex_key = random.choice(KEYS)
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    rounded_float = round(float_num, 2)
    return rounded_float

class TestTaskFunc(unittest.TestCase):

    def test_return_type(self):
        """Test if the return type is a float."""
        result = task_func()
        self.assertIsInstance(result, float)

    def test_return_value_rounding(self):
        """Test if the return value is correctly rounded to 2 decimal places."""
        hex_key = '470FC614'  # Known input
        result = task_func(hex_key)
        self.assertEqual(result, round(struct.unpack('!f', bytes.fromhex(hex_key))[0], 2))

    def test_default_random_choice(self):
        """Test if the function returns a value for a random key when hex_key is None."""
        random.seed(42)  # Set seed for reproducibility
        result = task_func(None)
        expected_value = round(struct.unpack('!f', bytes.fromhex('4C8FC614'))[0], 2)
        self.assertEqual(result, expected_value)

    def test_multiple_calls(self):
        """Test multiple calls to task_func to ensure diverse outputs."""
        results = set(task_func() for _ in range(100))
        self.assertGreater(len(results), 1)  # Expect at least two different rounded values

    def test_invalid_hex_key(self):
        """Test if ValueError is raised for an invalid hex_key."""
        with self.assertRaises(ValueError):
            task_func('InvalidHexKey')

if __name__ == "__main__":
    unittest.main()