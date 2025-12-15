import unittest
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def task_func(list_of_lists):
    """
    Merges a predefined set of lists into a list and one-hot-encodes the elements of the list.

    Parameters:
    - list_of_lists (list): The list to be processed.

    Returns:
    - one_hot (numpy.array): The one-hot encoding of the merged list.

    Requirements:
    - numpy
    - scikit-learn

    Example:
    >>> task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    array([[1., 0., 0., 0., 0., 0., 0., 0., 0.],
           [0., 1., 0., 0., 0., 0., 0., 0., 0.],
           [0., 0., 1., 0., 0., 0., 0., 0., 0.],
           [0., 0., 0., 1., 0., 0., 0., 0., 0.],
           [0., 0., 0., 0., 1., 0., 0., 0., 0.],
           [0., 0., 0., 0., 0., 1., 0., 0., 0.],
           [0., 0., 0., 0., 0., 0., 1., 0., 0.],
           [0., 0., 0., 0., 0., 0., 0., 1., 0.],
           [0., 0., 0., 0., 0., 0., 0., 0., 1.]])
    """
    
class TestTaskFunc(unittest.TestCase):
    
    def test_basic_case(self):
        result = task_func([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        expected = np.array([[1., 0., 0., 0., 0., 0., 0., 0., 0.],
                             [0., 1., 0., 0., 0., 0., 0., 0., 0.],
                             [0., 0., 1., 0., 0., 0., 0., 0., 0.],
                             [0., 0., 0., 1., 0., 0., 0., 0., 0.],
                             [0., 0., 0., 0., 1., 0., 0., 0., 0.],
                             [0., 0., 0., 0., 0., 1., 0., 0., 0.],
                             [0., 0., 0., 0., 0., 0., 1., 0., 0.],
                             [0., 0., 0., 0., 0., 0., 0., 1., 0.],
                             [0., 0., 0., 0., 0., 0., 0., 0., 1.]])
        np.testing.assert_array_equal(result, expected)
    
    def test_empty_input(self):
        result = task_func([[], [], []])
        expected = np.empty((0, 0))
        np.testing.assert_array_equal(result, expected)
        
    def test_single_list(self):
        result = task_func([[1, 2, 3]])
        expected = np.array([[1., 0., 0.],
                             [0., 1., 0.],
                             [0., 0., 1.]])
        np.testing.assert_array_equal(result, expected)
    
    def test_non_integer_elements(self):
        result = task_func([['a', 'b'], ['c']])
        expected = np.array([[1., 0., 0.],
                             [0., 1., 0.],
                             [0., 0., 1.]])
        np.testing.assert_array_equal(result, expected)
    
    def test_repeated_elements(self):
        result = task_func([[1, 2, 2], [3, 1]])
        expected = np.array([[1., 0., 0., 0.],
                             [0., 1., 0., 0.],
                             [0., 0., 1., 0.],
                             [0., 0., 0., 1.]])
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()