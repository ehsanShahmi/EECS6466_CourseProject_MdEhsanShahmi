import numpy as np
import random
import unittest

def task_func(length=10000, seed=0):
    """
    Generates a random walk of a specified length. A random walk is a path that consists of a series of random steps
    on some mathematical space. In this case, the steps are either +1 or -1, chosen with equal probability.

    Parameters:
    - length (int): The number of steps in the random walk. Must be a non-negative integer. Default is 10000.
    - seed (int, optional): An optional seed value to initialize the random number generator. Use this for reproducible results.
    
    Requirements:
    - numpy
    - random
    
    Returns:
    - np.array: A numpy array representing the positions of the walk at each step. Starts at 0.

    Raises:
    - ValueError: If `length` is negative.
    
    Example:
    >>> random.seed(0)     # For reproducibility in doctest
    >>> walk = task_func(5)
    >>> walk.tolist()
    [0, 1, 2, 1, 0, 1]
    """

    if length < 0:
        raise ValueError("length must be a non-negative integer")
    random.seed(seed)
    steps = [1 if random.random() > 0.5 else -1 for _ in range(length)]
    walk = np.cumsum([0] + steps)  # Starts at 0
    return walk

class TestRandomWalk(unittest.TestCase):

    def test_default_walk_length(self):
        walk = task_func()
        self.assertEqual(len(walk), 10001)  # Length should be 10001 (10000 steps + initial position)

    def test_zero_length_walk(self):
        walk = task_func(length=0)
        self.assertEqual(walk.tolist(), [0])  # Only starting point

    def test_negative_length_raises_value_error(self):
        with self.assertRaises(ValueError):
            task_func(length=-5)

    def test_random_walk_reproducibility(self):
        random.seed(0)
        walk1 = task_func(length=5)
        random.seed(0)
        walk2 = task_func(length=5)
        np.testing.assert_array_equal(walk1, walk2)  # Walks should be the same due to the same seed

    def test_walk_minimum_position(self):
        walk = task_func(length=10000, seed=1)
        self.assertTrue(np.all(walk >= -10000))  # Minimum position can't be less than -length

if __name__ == "__main__":
    unittest.main()