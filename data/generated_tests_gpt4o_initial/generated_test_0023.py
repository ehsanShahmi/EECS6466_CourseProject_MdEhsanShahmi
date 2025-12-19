import numpy as np
from itertools import zip_longest
import unittest

# Here is your prompt:
def task_func(l1, l2, THRESHOLD=0.5):
    """
    Alternates elements from two numeric lists, calculates the absolute difference of each 
    element from a predefined threshold, and returns the element closest to this threshold.
    
    Parameters:
    l1 (list): The first input list containing numeric values.
    l2 (list): The second input list containing numeric values.
    THRESHOLD (float): The predefined constant representing a numeric value used as a reference point for comparison. Default to 0.5. 
    
    Returns:
    float: The element from the combined list that is closest to the threshold of 0.5.
    
    Requirements:
    - numpy
    - itertools.zip_longest

    Notes:
    - If l1 and l2 are of different lengths, elements from the longer list without a corresponding 
      pair in the shorter list will not be paired with 'None'. Only existing numeric elements are considered.
    - The threshold is fixed at 0.5. Adjustments to the threshold require changes to the THRESHOLD constant.
    
    Example:
    >>> l1 = [0.3, 1, 2, 3]
    >>> l2 = [0.7, 11, 12, 13]
    >>> closest = task_func(l1, l2)
    >>> print(closest)
    0.7
    """
    combined = [val for pair in zip_longest(l1, l2) for val in pair if val is not None]
    differences = np.abs(np.array(combined) - THRESHOLD)
    closest_index = np.argmin(differences)
    return combined[closest_index]

class TestTaskFunc(unittest.TestCase):
    def test_basic_case(self):
        l1 = [0.3, 1, 2, 3]
        l2 = [0.7, 11, 12, 13]
        result = task_func(l1, l2)
        self.assertEqual(result, 0.7)

    def test_empty_lists(self):
        l1 = []
        l2 = []
        result = task_func(l1, l2)
        self.assertIsNone(result)

    def test_single_element_lists(self):
        l1 = [0.2]
        l2 = [0.6]
        result = task_func(l1, l2)
        self.assertEqual(result, 0.6)

    def test_longer_first_list(self):
        l1 = [0.1, 0.4, 0.8, 1.2]
        l2 = [0.5, 0.9]
        result = task_func(l1, l2)
        self.assertEqual(result, 0.5)

    def test_longer_second_list(self):
        l1 = [1.0]
        l2 = [0.4, 0.9, 1.6]
        result = task_func(l1, l2)
        self.assertEqual(result, 0.4)

if __name__ == '__main__':
    unittest.main()