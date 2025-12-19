import unittest
import random
import math

# Here is your prompt:
def task_func(range_start=1, range_end=100, pairs_count=10, random_seed=None):
    """
    Create a generator object that generates a sequence of tuples.
    Each tuple contains two random numbers and the square root of their
    absolute difference.

    A random seed is used to have reproducability in the outputs.

    Parameters:
    - range_start (int): The start of the range for random numbers. Default is 1.
    - range_end (int): The end of the range for random numbers. Default is 100.
    - pairs_count (int): The number of pairs to generate. Default is 10.
    - random_seed (int): Seed used for rng. Default is None.
    
    Returns:
    generator: A generator object that produces tuples in the format
               (num1, num2, square root of absolute difference).

    Requirements:
    - random
    - math

    Example:
    >>> pairs = task_func(random_seed=1)
    >>> print(next(pairs))
    (18, 73, 7.416198487095663)
    
    >>> pairs = task_func(1, 3, pairs_count=25, random_seed=14)
    >>> print(next(pairs))
    (1, 3, 1.4142135623730951)
    """
    random.seed(random_seed)
    pairs = [(random.randint(range_start, range_end), random.randint(range_start, range_end)) for _ in range(pairs_count)]
    return ((x, y, math.sqrt(abs(x - y))) for x, y in pairs)

# Test suite
class TestTaskFunction(unittest.TestCase):

    def test_default_parameters(self):
        pairs = task_func()
        result = next(pairs)
        self.assertEqual(len(result), 3)
        self.assertTrue(isinstance(result[0], int))
        self.assertTrue(isinstance(result[1], int))
        self.assertTrue(isinstance(result[2], float))

    def test_custom_range(self):
        pairs = task_func(1, 10, pairs_count=5, random_seed=5)
        result = list(pairs)
        self.assertEqual(len(result), 5)
        for x, y, sqrt_diff in result:
            self.assertTrue(1 <= x <= 10)
            self.assertTrue(1 <= y <= 10)

    def test_pairs_count(self):
        pairs_count = 15
        pairs = task_func(pairs_count=pairs_count)
        result = list(pairs)
        self.assertEqual(len(result), pairs_count)

    def test_random_seed_reproducibility(self):
        pairs1 = task_func(random_seed=7)
        pairs2 = task_func(random_seed=7)
        for _ in range(5):
            self.assertEqual(next(pairs1), next(pairs2))

    def test_absolute_difference_computation(self):
        pairs = task_func(random_seed=10)
        result = next(pairs)
        x, y, sqrt_diff = result
        self.assertEqual(sqrt_diff, math.sqrt(abs(x - y)))
        
if __name__ == '__main__':
    unittest.main()