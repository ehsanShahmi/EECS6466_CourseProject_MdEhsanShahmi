import unittest
import numpy as np
from itertools import product
import string

# Here is your prompt:
def task_func(length, seed=None, alphabets=list(string.ascii_lowercase)):
    """
    Generate a list of 10 randomly picked strings from all possible strings of a given
    length from the provided series of characters, using a specific seed for
    reproducibility.

    Parameters:
    length (int): The length of the strings to generate.
    seed (int): The seed for the random number generator. Default is None.
    alphabets (list, optional): The series of characters to generate the strings from. 
                Default is lowercase English alphabets.

    Returns:
    list: A list of generated strings.

    Requirements:
    - numpy
    - itertools.product
    - string

    Example:
    >>> task_func(2, 123)
    ['tq', 'ob', 'os', 'mk', 'du', 'ar', 'wx', 'ec', 'et', 'vx']

    >>> task_func(2, 123, alphabets=['x', 'y', 'z'])
    ['xz', 'xz', 'zx', 'xy', 'yx', 'zx', 'xy', 'xx', 'xy', 'xx']
    """

    np.random.seed(seed)
    all_combinations = [''.join(p) for p in product(alphabets, repeat=length)]
    return np.random.choice(all_combinations, size=10).tolist()


class TestTaskFunc(unittest.TestCase):
    
    def test_length_two_with_default_alphabets(self):
        result = task_func(2, seed=123)
        expected = ['tq', 'ob', 'os', 'mk', 'du', 'ar', 'wx', 'ec', 'et', 'vx']
        self.assertEqual(result, expected)

    def test_length_two_with_custom_alphabets(self):
        result = task_func(2, seed=123, alphabets=['x', 'y', 'z'])
        expected = ['xz', 'xz', 'zx', 'xy', 'yx', 'zx', 'xy', 'xx', 'xy', 'xx']
        self.assertEqual(result, expected)

    def test_length_three_with_default_alphabets(self):
        result = task_func(3, seed=42)
        self.assertEqual(len(result), 10)
        for r in result:
            self.assertEqual(len(r), 3)

    def test_length_one_with_empty_alphabets(self):
        result = task_func(1, seed=10, alphabets=[])
        self.assertEqual(result, [])

    def test_reproducibility_with_same_seed(self):
        result1 = task_func(4, seed=100)
        result2 = task_func(4, seed=100)
        self.assertEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()