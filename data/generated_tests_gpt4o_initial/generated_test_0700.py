import pandas as pd
import numpy as np
import unittest

# Here is your prompt:
def task_func(data, cols):
    """
    Turn the provided data into a DataFrame and then calculate the correlation matrix of numeric columns.
    
    Parameters:
    - data (list): List of lists with the data, where the length of the inner list equals the number of columns
    - cols (list): List of column names
    
    Returns:
    - correlation_matrix (pd.DataFrame): The correlation matrix.

    Requirements:
    - pandas
    - numpy
    
    Example:
    >>> correlation_matrix = task_func([[5.1, 3.5, 1.4], [4.9, 3.0, 1.4], [4.7, 3.2, 1.3]], ['x', 'y', 'z'])
    >>> print(correlation_matrix)
              x         y         z
    x  1.000000  0.596040  0.866025
    y  0.596040  1.000000  0.114708
    z  0.866025  0.114708  1.000000
    """

    df = pd.DataFrame(data, columns=cols)
    
    df_np = np.array(df)
    df = pd.DataFrame(df_np, columns=cols)
    
    correlation_matrix = df.corr()
    return correlation_matrix


class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        data = [[5.1, 3.5, 1.4], [4.9, 3.0, 1.4], [4.7, 3.2, 1.3]]
        cols = ['x', 'y', 'z']
        result = task_func(data, cols)
        expected = pd.DataFrame([[1.000000, 0.596040, 0.866025],
                                  [0.596040, 1.000000, 0.114708],
                                  [0.866025, 0.114708, 1.000000]], 
                                columns=cols, index=cols)
        pd.testing.assert_frame_equal(result.round(6), expected.round(6))

    def test_empty_input(self):
        data = []
        cols = []
        result = task_func(data, cols)
        expected = pd.DataFrame(columns=cols, index=cols)
        pd.testing.assert_frame_equal(result, expected)

    def test_single_column(self):
        data = [[1], [2], [3]]
        cols = ['a']
        result = task_func(data, cols)
        expected = pd.DataFrame([[1]], columns=cols, index=cols)
        pd.testing.assert_frame_equal(result, expected)

    def test_no_correlation(self):
        data = [[1, 2], [2, 4], [3, 6]]
        cols = ['x', 'y']
        result = task_func(data, cols)
        expected = pd.DataFrame([[1, 1], [1, 1]], columns=cols, index=cols)
        pd.testing.assert_frame_equal(result, expected)

    def test_non_numeric_data(self):
        data = [[1, 2], [2, 'a'], [3, 4]]
        cols = ['x', 'y']
        with self.assertRaises(TypeError):
            task_func(data, cols)

# To run the tests
if __name__ == '__main__':
    unittest.main()