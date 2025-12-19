from sklearn.preprocessing import MinMaxScaler
import numpy as np
import unittest

def task_func(myList):
    """
    Normalize a list of numeric values to the range [0, 1] using min-max scaling.

    Parameters:
    - myList (list): List of numerical values to normalize.

    Returns:
    - ndarray: An array of normalized values.

    Requirements:
    - sklearn.preprocessing.MinMaxScaler
    - numpy

    Example:
    >>> myList = [10, 20, 30, 40, 50]
    >>> task_func(myList)
    array([0.  , 0.25, 0.5 , 0.75, 1.  ])
    """

    myList = np.array(myList).reshape(-1, 1)
    scaler = MinMaxScaler()
    normalized_list = scaler.fit_transform(myList)

    return normalized_list.flatten()

class TestTaskFunc(unittest.TestCase):

    def test_normal_case(self):
        myList = [10, 20, 30, 40, 50]
        expected = np.array([0., 0.25, 0.5, 0.75, 1.])
        np.testing.assert_array_almost_equal(task_func(myList), expected)

    def test_single_value(self):
        myList = [5]
        expected = np.array([0.])
        np.testing.assert_array_almost_equal(task_func(myList), expected)

    def test_two_values(self):
        myList = [10, 20]
        expected = np.array([0., 1.])
        np.testing.assert_array_almost_equal(task_func(myList), expected)

    def test_identical_values(self):
        myList = [7, 7, 7]
        expected = np.array([0., 0., 0.])
        np.testing.assert_array_almost_equal(task_func(myList), expected)

    def test_negative_values(self):
        myList = [-10, -5, 0, 5, 10]
        expected = np.array([0., 0.25, 0.5, 0.75, 1.])
        np.testing.assert_array_almost_equal(task_func(myList), expected)

if __name__ == '__main__':
    unittest.main()