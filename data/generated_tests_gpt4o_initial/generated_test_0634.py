import unittest
import numpy as np
from scipy import stats

# Here is your prompt:
import itertools
from typing import Any


def task_func(input_list: list, repetitions: int) -> Any:
    """
    Calculate the mode of a list of elements with multiple repetitions of the original list.
    
    Functionality: 
    - Takes a list and a repetition count as input.
    - Flattens the list with multiple repetitions.
    - Calculates the mode of the flattened list.
    
    Parameters:
    - input_list (list): A list containing elements (can be of any hashable type).
    - repetitions (int): The number of times the original list should be repeated.

    Requirements:
    - typing
    - itertools
    - scipy

    Returns:
    - scipy.stats.ModeResult: An object containing the mode(s) and count(s) of the most frequently occurring element(s) in the flattened list.
    
    Examples:
    >>> task_func(['A', 'B', 'C'], 10)
    ModeResult(mode=array(['A'], dtype='<U1'), count=array([10]))
    
    >>> task_func([1, 2, 3], 5)
    ModeResult(mode=array([1]), count=array([5]))
    """
               # Flattening the list with multiple repetitions
    flattened_list = np.array(list(itertools.chain(*[input_list for _ in range(repetitions)])))
    
    # Calculating the mode
    mode = stats.mode(flattened_list)
    
    return mode


class TestTaskFunc(unittest.TestCase):
    
    def test_repeated_elements(self):
        result = task_func(['A', 'B', 'A'], 5)
        expected_mode = np.array(['A'])
        expected_count = np.array([10])
        self.assertTrue(np.array_equal(result.mode, expected_mode))
        self.assertTrue(np.array_equal(result.count, expected_count))

    def test_unique_elements(self):
        result = task_func([1, 2, 3], 4)
        expected_mode = np.array([1])
        expected_count = np.array([4])
        self.assertTrue(np.array_equal(result.mode, expected_mode))
        self.assertTrue(np.array_equal(result.count, expected_count))

    def test_single_element(self):
        result = task_func(['X'], 3)
        expected_mode = np.array(['X'])
        expected_count = np.array([3])
        self.assertTrue(np.array_equal(result.mode, expected_mode))
        self.assertTrue(np.array_equal(result.count, expected_count))

    def test_mixed_elements(self):
        result = task_func([1, 2, 1, 3, 1, 2], 2)
        expected_mode = np.array([1])
        expected_count = np.array([6])
        self.assertTrue(np.array_equal(result.mode, expected_mode))
        self.assertTrue(np.array_equal(result.count, expected_count))

    def test_mode_with_ties(self):
        result = task_func(['A', 'B', 'A', 'B'], 3)
        expected_modes = np.array(['A', 'B'])
        expected_count = np.array([6, 6])
        self.assertTrue(np.array_equal(result.mode, expected_modes))
        self.assertTrue(np.array_equal(result.count, expected_count))


if __name__ == '__main__':
    unittest.main()