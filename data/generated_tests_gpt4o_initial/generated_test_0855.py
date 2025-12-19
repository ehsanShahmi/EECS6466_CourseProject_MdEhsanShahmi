import random
import string
import collections
import unittest

# Constants
VALID_CHARACTERS = string.ascii_letters + string.digits

def task_func(n_strings, string_length):
    """
    Generate n random strings of a specified length, count the frequency of each character across all strings, and return the result as a dictionary.

    Parameters:
    - n_strings (int): The number of random strings to generate.
    - string_length (int): The length of each random string.

    Returns:
    - dict: A dictionary containing character counts with characters as keys and their frequencies as values.
    """
    strings = [''.join(random.choice(VALID_CHARACTERS) for _ in range(string_length)) for _ in range(n_strings)]
    character_counts = collections.Counter(''.join(strings))
    return dict(character_counts)

class TestTaskFunc(unittest.TestCase):

    def test_zero_strings(self):
        """Test when no strings are generated."""
        result = task_func(0, 5)
        self.assertEqual(result, {})

    def test_zero_length_strings(self):
        """Test when strings of zero length are generated."""
        result = task_func(5, 0)
        self.assertEqual(result, {})

    def test_single_string(self):
        """Test generating a single string of specified length."""
        random.seed(42)  # for reproducibility
        result = task_func(1, 3)
        self.assertEqual(len(result), 3)  # expect 3 characters
        self.assertTrue(all(char in VALID_CHARACTERS for char in result))

    def test_multiple_strings(self):
        """Test generating multiple strings."""
        random.seed(42)  # for reproducibility
        result = task_func(2, 3)
        self.assertTrue(isinstance(result, dict))
        self.assertTrue(all(char in VALID_CHARACTERS for char in result))

    def test_character_count(self):
        """Test that character counts are accurate."""
        random.seed(42)  # for reproducibility
        result = task_func(2, 3)
        expected_output = {'O': 1, 'h': 1, 'b': 1, 'V': 1, 'r': 1, 'p': 1}
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()