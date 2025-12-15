import unittest
import numpy as np

# Here is your prompt:
import numpy as np
from itertools import chain

def task_func(L):
    """
    Calculate the mean and variance of all elements in a nested list 'L'.
    
    Parameters:
    - L (list): The nested list.
    
    Returns:
    - dict: A dictionary containing the mean and variance.
    
    Requirements:
    - numpy
    - itertools.chain

    Example:
    >>> task_func([[1,2,3],[4,5,6]])
    {'mean': 3.5, 'variance': 2.9166666666666665}
    """

    flattened = list(chain.from_iterable(L))
    mean = np.mean(flattened)
    variance = np.var(flattened)

    return {'mean': mean, 'variance': variance}

class TestTaskFunc(unittest.TestCase):

    def test_basic_nested_list(self):
        result = task_func([[1, 2, 3], [4, 5, 6]])
        expected = {'mean': 3.5, 'variance': 2.9166666666666665}
        self.assertEqual(result, expected)

    def test_empty_nested_list(self):
        result = task_func([[], []])
        expected = {'mean': 0.0, 'variance': 0.0}
        self.assertEqual(result, expected)

    def test_single_element(self):
        result = task_func([[42]])
        expected = {'mean': 42.0, 'variance': 0.0}
        self.assertEqual(result, expected)

    def test_floats_in_nested_list(self):
        result = task_func([[1.5, 2.5], [3.5, 4.5]])
        expected = {'mean': 3.0, 'variance': 1.25}
        self.assertEqual(result, expected)

    def test_large_numbers(self):
        result = task_func([[1e6, 2e6], [3e6, 4e6]])
        expected = {'mean': 2.5e6, 'variance': 2.5e12}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()