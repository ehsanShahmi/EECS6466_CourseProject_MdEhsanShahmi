import numpy as np
from scipy.stats import iqr
import unittest

def task_func(L):
    """
    Calculate the interquartile range of all elements in a nested list 'L'.
    
    Parameters:
    - L (list): The nested list.
    
    Returns:
    - iqr_value (float): The interquartile range.
    
    Requirements:
    - numpy
    - scipy.stats

    Example:
    >>> task_func([[1,2,3],[4,5,6]])
    2.5
    """

    flattened = np.array(L).flatten()
    iqr_value = iqr(flattened)
    
    return iqr_value

class TestTaskFunc(unittest.TestCase):

    def test_basic_case(self):
        self.assertAlmostEqual(task_func([[1, 2, 3], [4, 5, 6]]), 2.5)

    def test_empty_nested_list(self):
        self.assertEqual(task_func([]), 0.0)  # Assuming IQR of an empty list is 0

    def test_single_element(self):
        self.assertAlmostEqual(task_func([[5]]), 0.0)  # Single element, IQR is 0

    def test_identical_elements(self):
        self.assertAlmostEqual(task_func([[7, 7, 7], [7, 7]]), 0.0)  # All elements are identical

    def test_large_numbers(self):
        self.assertAlmostEqual(task_func([[1000, 2000], [3000, 4000]]), 2000.0)  # Test with large numbers

if __name__ == '__main__':
    unittest.main()