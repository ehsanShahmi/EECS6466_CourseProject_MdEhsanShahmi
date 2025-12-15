import unittest
import numpy as np
from scipy import stats

# Here is your prompt:
import numpy as np
import random
from scipy import stats


def task_func(list_of_lists, size=5, seed=0):
    """
    Calculate the mean, median, and mode of values in a list of lists.
    If a list is empty, fill it with SIZE (default: 5) random integers between 0 and 100, 
    and then calculate the statistics.
    
    Parameters:
    list_of_lists (list): The list of lists.
    size (int, Optional): The number of random integers to generate. Default is 5.
    seed (int, Optional): Seed value for random number generation. Default is 0.
    
    Returns:
    dict: A dictionary with the mean, median, and mode of the values.
    
    Requirements:
    - numpy
    - random
    - scipy.stats
    
    Example:
    >>> task_func([[1, 2, 3], [], [4, 5, 6]])
    {'mean': 23.454545454545453, 'median': 5.0, 'mode': array([5])}
    """

    random.seed(seed)
    data = []
    for list_ in list_of_lists:
        if list_:
            data += list_
        else:
            data += [random.randint(0, 100) for _ in range(size)]
    
    return {
        'mean': np.mean(data),
        'median': np.median(data),
        'mode': stats.mode(data)[0]
    }

class TestTaskFunc(unittest.TestCase):
    def test_normal_case(self):
        result = task_func([[1, 2, 3], [4, 5, 6], []])
        expected_mean = np.mean([1, 2, 3, 4, 5, 6])
        expected_median = np.median([1, 2, 3, 4, 5, 6])
        expected_mode = stats.mode([1, 2, 3, 4, 5, 6])[0]
        self.assertEqual(result['mean'], expected_mean)
        self.assertEqual(result['median'], expected_median)
        np.testing.assert_array_equal(result['mode'], expected_mode)

    def test_empty_input(self):
        result = task_func([[], [], []], size=5, seed=1)
        self.assertEqual(len(result['mode']), 1)  # mode returns a length 1 array
        self.assertGreaterEqual(result['mean'], 0)
        self.assertLessEqual(result['mean'], 100)

    def test_seed_effect(self):
        result1 = task_func([[], []], size=5, seed=2)
        result2 = task_func([[], []], size=5, seed=2)
        self.assertEqual(result1, result2)

    def test_large_values(self):
        list_of_lists = [[100, 200], [], [300, 400]]
        result = task_func(list_of_lists)
        expected_mean = np.mean([100, 200, 300, 400])
        expected_median = np.median([100, 200, 300, 400])
        expected_mode = stats.mode([100, 200, 300, 400])[0]
        self.assertEqual(result['mean'], expected_mean)
        self.assertEqual(result['median'], expected_median)
        np.testing.assert_array_equal(result['mode'], expected_mode)

    def test_different_sizes(self):
        result = task_func([[1, 2], [], [4]], size=3, seed=0)
        self.assertGreater(len(result['mode']), 0)  # Checking mode is calculated
        self.assertTrue(np.isfinite(result['mean']))  # Mean should be a finite number

if __name__ == '__main__':
    unittest.main()