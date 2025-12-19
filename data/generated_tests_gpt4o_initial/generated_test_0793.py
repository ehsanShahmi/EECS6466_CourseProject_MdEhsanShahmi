import unittest
import numpy as np
import random

# Constants
ELEMENTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

def task_func(l=None):
    """
    Create a numeric array from a list "l" and move the first 3 elements to the end of the array.

    Parameters:
    - l (list): A list of elements to be processed.

    Returns:
    - arr (numpy.ndarray): The processed array with the first three elements moved to the end.

    Requirements:
    - numpy
    - random

    Example:
    >>> random.seed(42)
    >>> task_func()
    array(['I', 'F', 'G', 'J', 'E', 'A', 'B', 'H', 'D', 'C'], dtype='<U1')
    """
    if l is None:
        l = ELEMENTS.copy()  # Use a copy to avoid modifying the original list
    random.shuffle(l)
    arr = np.array(l)
    arr = np.concatenate((arr[3:], arr[:3]))
    return arr

class TestTaskFunc(unittest.TestCase):

    def test_return_type(self):
        """Test if the returned value is a numpy array."""
        result = task_func()
        self.assertIsInstance(result, np.ndarray)

    def test_array_length(self):
        """Test if the length of the output array is the same as the input list."""
        result = task_func()
        self.assertEqual(len(result), len(ELEMENTS))

    def test_shuffling_effect(self):
        """Test if the first three elements are moved to the end after shuffling."""
        random.seed(1)  # Set seed for reproducibility
        test_list = ELEMENTS.copy()
        shuffled_list = test_list.copy()
        random.shuffle(shuffled_list)
        result = task_func(shuffled_list)
        self.assertEqual(result.tolist(), shuffled_list[3:] + shuffled_list[:3])

    def test_default_behavior(self):
        """Test if the function works correctly with no input."""
        random.seed(42)  # Set seed for reproducibility
        expected_result = np.array(['I', 'F', 'G', 'J', 'E', 'A', 'B', 'H', 'D', 'C'], dtype='<U1')
        np.testing.assert_array_equal(task_func(), expected_result)

    def test_custom_list_input(self):
        """Test if the function correctly processes a custom input list."""
        custom_input = ['X', 'Y', 'Z', 'L', 'M', 'N']
        expected_output = ['L', 'M', 'N', 'X', 'Y', 'Z']
        result = task_func(custom_input)
        np.testing.assert_array_equal(result.tolist(), expected_output)

if __name__ == '__main__':
    unittest.main()