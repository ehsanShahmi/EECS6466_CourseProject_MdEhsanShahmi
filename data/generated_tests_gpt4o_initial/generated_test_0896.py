import unittest
from collections import Counter
import random

# Here is your prompt:
from collections import Counter
import random
import itertools

def task_func(length, count, seed=0):
    """
    Generate a number of random strings with a specified length from a fixed set of letters ('a', 'b', 'c', 'd', 'e'),
    and analyze the frequency of each letter in the generated strings.
    
    Parameters:
    - length (int): The length of each string to be generated. Should be a non-negative integer.
    - count (int): The number of random strings to generate. Should be a non-negative integer.
    - seed (int, optional): A seed for the random number generator to ensure reproducibility.
    
    Requirements:
    - collections.Counter
    - random
    - itertools
    
    Returns:
    - Counter: A collections.Counter object containing the frequency of each letter in the generated strings.
    
    Example:
    >>> task_func(5, 2, seed=1)
    Counter({'a': 3, 'd': 3, 'c': 2, 'e': 1, 'b': 1})
    >>> task_func(0, 100, seed=2)
    Counter()
    """

    random.seed(seed)
    strings = [''.join(random.choices(['a', 'b', 'c', 'd', 'e'], k=length)) for _ in range(count)]
    letter_frequency = Counter(itertools.chain(*strings))
    
    return letter_frequency


class TestTaskFunction(unittest.TestCase):

    def test_zero_length_and_positive_count(self):
        """ Test with length 0 and positive count; expecting empty Counter. """
        result = task_func(0, 100, seed=2)
        self.assertEqual(result, Counter())

    def test_positive_length_and_zero_count(self):
        """ Test with positive length and zero count; expecting empty Counter. """
        result = task_func(5, 0, seed=1)
        self.assertEqual(result, Counter())

    def test_specific_seed_reproducibility(self):
        """ Test reproducibility with the same parameters and seed. """
        result1 = task_func(5, 2, seed=1)
        result2 = task_func(5, 2, seed=1)
        self.assertEqual(result1, result2)

    def test_letter_frequency_distribution(self):
        """ Test if the generated letters are from the expected set and analyze distribution. """
        result = task_func(5, 10, seed=1)
        total = sum(result.values())
        for letter in ['a', 'b', 'c', 'd', 'e']:
            self.assertIn(letter, result)  # Check if all letters are keys
        self.assertEqual(total, 50)  # Since length=5 and count=10

    def test_negative_length(self):
        """ Test with negative length; expecting an empty Counter. """
        with self.assertRaises(ValueError):
            task_func(-5, 10)

if __name__ == '__main__':
    unittest.main()