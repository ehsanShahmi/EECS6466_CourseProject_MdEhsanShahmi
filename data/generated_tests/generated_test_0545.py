import unittest
import codecs
import random
import struct

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_keys=KEYS):
    """
    Generate a random float number from a list of hex strings and then encode the float number in utf-8.

    Parameters:
    hex_keys (list of str): A list of hexadecimal strings to choose from.
    
    Returns:
    bytes: The utf-8 encoded float number.

    Requirements:
    - struct
    - codecs
    - random

    Example:
    >>> random.seed(42)
    >>> task_func()
    b'36806.078125'
    """
    hex_key = random.choice(hex_keys)
    float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    encoded_float = codecs.encode(str(float_num), 'utf-8')

    return encoded_float

class TestTaskFunc(unittest.TestCase):

    def test_random_output_shape(self):
        """Test that the function returns bytes type output."""
        output = task_func()
        self.assertIsInstance(output, bytes)

    def test_output_encoding(self):
        """Test that output is utf-8 encoded."""
        output = task_func()
        self.assertEqual(output.decode('utf-8').encode('utf-8'), output)

    def test_float_conversion(self):
        """Test that decoded output can convert to float."""
        output = task_func()
        decoded_output = output.decode('utf-8')
        self.assertIsInstance(float(decoded_output), float)

    def test_output_for_all_keys(self):
        """Test that the output can be derived from all hex keys."""
        outputs = {task_func(KEYS) for _ in range(100)}
        # Check that all keys are represented in the output
        for key in KEYS:
            float_num = struct.unpack('!f', bytes.fromhex(key))[0]
            expected_output = codecs.encode(str(float_num), 'utf-8')
            self.assertIn(expected_output, outputs)

    def test_reproducibility(self):
        """Test that the output is reproducible with the same random seed."""
        random.seed(42)
        output1 = task_func()
        random.seed(42)
        output2 = task_func()
        self.assertEqual(output1, output2)

if __name__ == '__main__':
    unittest.main()