import random
from collections import Counter
from statistics import mode
import unittest

def task_func(list_length=1000, range_start=1, range_end=10, random_seed=None):
    """
    Generate a random list of integers within a specified range. Convert this
    list to a generator object that yields tuples. Each tuple contains a number
    from the list and its frequency. Additionally, find and return the mode of 
    the list.

    Parameters:
    - list_length (int): The length of the random list to be generated. Default is 1000.
    - range_start (int): The start of the range for random numbers. Default is 1.
    - range_end (int): The end of the range for random numbers. Default is 10.
    - random_seed (int): Seed for the rng. Default is None.

    Returns:
    tuple: A tuple containing:
    - int: The mode of the generated list.
    - generator: A generator object yielding tuples with each number from the list and its frequency.

    Requirements:
    - random
    - collections
    - statistics
    """

    random.seed(random_seed)
    random_list = [random.randint(range_start, range_end) for _ in range(list_length)]
    counter = Counter(random_list)
    numbers = ((number, count) for number, count in counter.items())
    return mode(random_list), numbers

class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        mode, numbers = task_func()
        self.assertIsInstance(mode, int)
        self.assertEqual(len(list(numbers)), len(set(range(1, 11))) - 1)

    def test_custom_range_and_list_length(self):
        mode, numbers = task_func(list_length=100, range_start=1, range_end=5)
        self.assertIsInstance(mode, int)
        self.assertTrue(all(1 <= n[0] <= 5 for n in numbers))

    def test_random_seed_consistency(self):
        random_seed = 42
        mode1, numbers1 = task_func(random_seed=random_seed)
        mode2, numbers2 = task_func(random_seed=random_seed)
        self.assertEqual(mode1, mode2)
        self.assertEqual(list(numbers1), list(numbers2))

    def test_negative_range(self):
        mode, numbers = task_func(list_length=100, range_start=-5, range_end=5)
        self.assertIsInstance(mode, int)
        self.assertTrue(all(-5 <= n[0] <= 5 for n in numbers))

    def test_empty_list(self):
        mode, numbers = task_func(list_length=0, range_start=1, range_end=10)
        with self.assertRaises(ValueError):
            _ = mode(numbers)

if __name__ == '__main__':
    unittest.main()