import collections
import string
import random
import unittest

def task_func(length, seed=0):
    """
    Generate a random string of a given length using ASCII letters and calculate the frequency of each character.​

    Parameters:
    length (int): The length of the random string to be generated.
    seed (int, Optional): The seed to be used for the random number generator. Default is 0.

    Returns:
    dict: A dictionary with the frequency of each character in the generated string.

    Requirements:
    - The function uses the 'collections', 'string', and 'random' modules from the Python standard library.
    - The generated string consists only of ASCII letters.

    Example:
    >>> result = task_func(4)
    >>> isinstance(result, dict)  # The result should be a dictionary
    True
    >>> all(key in string.ascii_letters for key in result.keys())  # All keys should be ASCII letters
    True
    >>> task_func(5, 0)  # The result should be deterministic for a given seed
    {'y': 1, 'W': 1, 'A': 1, 'c': 1, 'q': 1}
    """

    random.seed(seed)
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))

    char_freq = collections.Counter(random_string)

    return dict(char_freq)

class TestTaskFunc(unittest.TestCase):

    def test_output_type(self):
        result = task_func(4)
        self.assertIsInstance(result, dict, "The result should be a dictionary")

    def test_character_keys(self):
        result = task_func(10)
        for key in result.keys():
            self.assertIn(key, string.ascii_letters, "All keys should be ASCII letters")

    def test_fixed_seed_determinism(self):
        result1 = task_func(5, 0)
        result2 = task_func(5, 0)
        self.assertEqual(result1, result2, "The results should be the same for the same seed")

    def test_non_zero_length(self):
        result = task_func(0)
        self.assertEqual(result, {}, "The result should be an empty dictionary when length is 0")

    def test_randomness(self):
        result1 = task_func(6, 1)
        result2 = task_func(6, 2)
        self.assertNotEqual(result1, result2, "The results should be different for different seeds")

if __name__ == '__main__':
    unittest.main()