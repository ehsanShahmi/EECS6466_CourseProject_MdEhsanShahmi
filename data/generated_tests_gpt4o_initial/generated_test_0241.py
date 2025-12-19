import numpy as np
import unittest
import matplotlib.pyplot as plt
from sklearn import preprocessing

# Here is your prompt:
def task_func(original):
    """
    Create a numeric array from the "original" list, normalize the array, and draw the original and normalized arrays.
    
    The function will plot the original and normalized arrays using matplotlib.

    Parameters:
    original (list): The original list with tuples to be unzipped into a numpy array.

    Returns:
    np.array: A numpy array for the original data.
    np.array: Normalized array.
    matplotlib.axes.Axes: Axes object with the plotted data.
    
    Requirements:
    - numpy
    - matplotlib.pyplot
    - sklearn.preprocessing

    Example:
    >>> original = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
    >>> arr, norm_arr, ax = task_func(original)
    >>> print(arr)
    [1 2 3 4]
    >>> print(norm_arr)
    [0.18257419 0.36514837 0.54772256 0.73029674]
    """

    arr = np.array([b for (a, b) in original])
    
    # Check if the array is empty to avoid normalization error
    if arr.size == 0:
        norm_arr = arr
    else:
        norm_arr = preprocessing.normalize([arr])[0]
    
    # Plotting the data
    fig, ax = plt.subplots()
    ax.plot(arr, label='Original')
    ax.plot(norm_arr, label='Normalized')
    ax.legend()
    ax.set_title("Original vs. Normalized Data")
    
    return arr, norm_arr, ax

class TestTaskFunc(unittest.TestCase):

    def test_normal_case(self):
        original = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
        arr, norm_arr, ax = task_func(original)
        expected_arr = np.array([1, 2, 3, 4])
        self.assertTrue(np.array_equal(arr, expected_arr))
        self.assertAlmostEqual(norm_arr[0], 0.18257419)
        self.assertAlmostEqual(norm_arr[1], 0.36514837)
        self.assertAlmostEqual(norm_arr[2], 0.54772256)
        self.assertAlmostEqual(norm_arr[3], 0.73029674)

    def test_empty_input(self):
        original = []
        arr, norm_arr, ax = task_func(original)
        expected_arr = np.array([])
        self.assertTrue(np.array_equal(arr, expected_arr))
        self.assertTrue(np.array_equal(norm_arr, expected_arr))

    def test_single_value_input(self):
        original = [('a', 5)]
        arr, norm_arr, ax = task_func(original)
        expected_arr = np.array([5])
        self.assertTrue(np.array_equal(arr, expected_arr))
        self.assertAlmostEqual(norm_arr[0], 1.0)

    def test_duplicate_values(self):
        original = [('a', 2), ('b', 2), ('c', 2)]
        arr, norm_arr, ax = task_func(original)
        expected_arr = np.array([2, 2, 2])
        self.assertTrue(np.array_equal(arr, expected_arr))
        self.assertAlmostEqual(norm_arr[0], 1/np.sqrt(3))
        self.assertAlmostEqual(norm_arr[1], 1/np.sqrt(3))
        self.assertAlmostEqual(norm_arr[2], 1/np.sqrt(3))

    def test_negative_values(self):
        original = [('a', -1), ('b', -2), ('c', -3)]
        arr, norm_arr, ax = task_func(original)
        expected_arr = np.array([-1, -2, -3])
        self.assertTrue(np.array_equal(arr, expected_arr))
        self.assertAlmostEqual(norm_arr[0], -1/np.sqrt(14))
        self.assertAlmostEqual(norm_arr[1], -2/np.sqrt(14))
        self.assertAlmostEqual(norm_arr[2], -3/np.sqrt(14))

if __name__ == '__main__':
    unittest.main()