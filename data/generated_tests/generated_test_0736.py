import numpy as np
from scipy import stats
import unittest

def task_func(L):
    '''
    Calculate the mode of all elements in a nested list 'L'.
    
    Parameters:
    L (list): The nested list.
    
    Returns:
    - mode (int): The mode.
    
    Requirements:
    - numpy
    - scipy.stats

    Example:
    >>> task_func([[1,2,3],[4,5,6]])
    1
    '''
    flattened = np.hstack(L)  
    mode = stats.mode(flattened)[0][0]
    return mode

class TestTaskFunc(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(task_func([[1, 2, 2], [3, 4]]), 2)

    def test_multiple_modes(self):
        self.assertEqual(task_func([[1, 1, 2], [2, 3]]), 1)  # Assuming first mode is returned

    def test_no_elements(self):
        self.assertEqual(task_func([[], []]), np.nan)  # Assuming the behavior for no elements is to return NaN

    def test_flat_list(self):
        self.assertEqual(task_func([[2, 3, 3, 3, 4, 4]]), 3)

    def test_nested_empty_lists(self):
        self.assertEqual(task_func([[], [1, 2], [], [2, 2]]), 2)  # Should return mode of the populated elements

if __name__ == '__main__':
    unittest.main()