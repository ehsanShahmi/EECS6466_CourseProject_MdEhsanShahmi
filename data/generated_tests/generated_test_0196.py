import random
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
import unittest

def task_func(length, range_limit=100, seed=0):
    """
    Create a list of random numbers, sort them and record the distribution of the numbers in a histogram using 
    default settings in a deterministic seaborn plot. Return the axes object and the list of random numbers.

    Parameters:
    length (int): The length of the list of random numbers.
    range_limit (int, Optional): The range of the random numbers. Defaults to 100. Must be greater than 1.
    seed (int, Optional): The seed value for the random number generator. Defaults to 0.

    Returns:
    Tuple[matplotlib.axes._axes.Axes, List[int]]: The axes object with the plot and the list of random numbers.

    Requirements:
    - random
    - matplotlib.pyplot
    - seaborn
    - numpy

    Raises:
    ValueError: If range_limit is less than or equal to 1.

    Example:
    >>> import matplotlib.pyplot as plt
    >>> ax, data = task_func(1000, 100, 24) # Generate a list of 1000 random numbers between 1 and 100
    >>> isinstance(ax, plt.Axes)
    True
    """
    if range_limit <= 1:
        raise ValueError("range_limit must be greater than 1")

    random.seed(seed)
    np.random.seed(seed)

    random_numbers = [random.randint(1, range_limit) for _ in range(length)]
    random_numbers.sort()

    # Initialize a fresh plot
    plt.figure()
    plot = sns.histplot(random_numbers, kde=False)

    return plot.axes, random_numbers

class TestTaskFunction(unittest.TestCase):
    
    def test_length_of_random_numbers(self):
        ax, data = task_func(1000, 100, 24)
        self.assertEqual(len(data), 1000)
    
    def test_random_numbers_within_range(self):
        ax, data = task_func(1000, 100, 24)
        self.assertTrue(all(1 <= num <= 100 for num in data))
    
    def test_sorting_of_random_numbers(self):
        ax, data = task_func(100, 50, 24)
        self.assertEqual(data, sorted(data))

    def test_raise_value_error_on_invalid_range_limit(self):
        with self.assertRaises(ValueError):
            task_func(100, 1)

    def test_axes_object_returned(self):
        ax, data = task_func(1000, 100, 24)
        self.assertIsInstance(ax, plt.Axes)

if __name__ == "__main__":
    unittest.main()