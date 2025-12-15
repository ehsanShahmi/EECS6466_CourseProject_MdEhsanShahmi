import unittest
import hashlib
import random
import struct

KEYS = ['470FC614', '4A0FC614', '4B9FC614', '4C8FC614', '4D7FC614']

def task_func(hex_keys=KEYS, seed=42):
    """
    Given a list of hexadecimal string keys, this function selects one at random,
    converts it into a floating-point number, and then computes its MD5 hash. An optional
    seed parameter allows for deterministic random choices for testing purposes.

    Parameters:
    hex_keys (list of str): A list of hexadecimal strings to choose from.
    seed (int, optional): A seed for the random number generator to ensure deterministic behavior.

    Returns:
    str: The MD5 hash of the floating-point number derived from the randomly selected hexadecimal string.

    Raises:
    ValueError: If contains invalid hexadecimal strings.

    Requirements:
    - struct
    - hashlib
    - random

    Example:
    >>> task_func(['1a2b3c4d', '5e6f7g8h'])
    '426614caa490f2c185aebf58f1d4adac'
    """

    random.seed(seed)
    hex_key = random.choice(hex_keys)

    try:
        float_num = struct.unpack('!f', bytes.fromhex(hex_key))[0]
    except ValueError as e:
        raise ValueError("Invalid hexadecimal string in hex_keys.") from e

    hashed_float = hashlib.md5(str(float_num).encode()).hexdigest()
    return hashed_float


class TestTaskFunc(unittest.TestCase):
    
    def test_valid_hex_keys(self):
        expected_hash = '5e3c9ed58bb0b1633d3fdbafe4db82fd'  # hash of struct.unpack('!f', bytes.fromhex('470FC614'))[0]
        self.assertEqual(task_func(['470FC614'], seed=0), expected_hash)

    def test_random_choice(self):
        # The random choice depends on the seed, ensuring that we can predict the value
        expected_hash = '5ee2e846d2cfb1518e3796c74de0b229'  # hash of struct.unpack('!f', bytes.fromhex('4A0FC614'))[0]
        self.assertEqual(task_func(seed=1), expected_hash)

    def test_invalid_hex_key(self):
        with self.assertRaises(ValueError):
            task_func(['ZZZZZZZZ'])

    def test_multiple_keys(self):
        # This test checks that we get one of the hashes from the provided keys
        valid_hashes = {
            '5e3c9ed58bb0b1633d3fdbafe4db82fd',  # hash of '470FC614'
            '5ee2e846d2cfb1518e3796c74de0b229',  # hash of '4A0FC614'
            '0ba2d70d5c2927b5e0f6b08e9792bbbb',  # hash of '4B9FC614'
            '574d59f41cc73bed666ba9e4707cfc66',  # hash of '4C8FC614'
            '89ea8a70e69db6045ae790bc28161e03'   # hash of '4D7FC614'
        }
        for i in range(5):
            hash_output = task_func(seed=i)
            self.assertIn(hash_output, valid_hashes)

    def test_deterministic_output_with_seed(self):
        self.assertEqual(task_func(seed=10), task_func(seed=10))  # same seed should always yield the same result


if __name__ == '__main__':
    unittest.main()