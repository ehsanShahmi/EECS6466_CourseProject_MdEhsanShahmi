import numpy as np
import pandas as pd
import unittest

# Constants
RANGE = (1, 100)

def task_func(L):
    '''
    Generates a DataFrame filled with random integers. The dimensions of the DataFrame (number of rows and columns)
    are determined by multiplying pairs of integers from nested lists within the input list of lists 'L'.
    
    Requirements:
    - numpy
    - pandas

    Parameters:
    L (list of lists): A list of lists where each sublist contains two integers.
    
    Returns:
    DataFrame: A pandas DataFrame with random integers.
    
    Example:
    >>> df = task_func([[2, 3], [5, 6]])
    >>> type(df)
    <class 'pandas.core.frame.DataFrame'>
    '''
    
    rows, columns = L[0][0] * L[0][1], L[1][0] * L[1][1]
    random_array = np.random.randint(RANGE[0], RANGE[1], size=(rows, columns))
    df = pd.DataFrame(random_array)
    
    return df

class TestTaskFunction(unittest.TestCase):
    
    def test_return_type(self):
        """Test if the function returns a DataFrame."""
        df = task_func([[2, 3], [5, 6]])
        self.assertIsInstance(df, pd.DataFrame)

    def test_dataframe_shape(self):
        """Test if the DataFrame shape is as expected."""
        df = task_func([[2, 3], [5, 6]])
        expected_shape = (2 * 3, 5 * 6)  # 6 rows and 30 columns
        self.assertEqual(df.shape, expected_shape)

    def test_value_range(self):
        """Test if all values in the DataFrame are within the specified range."""
        df = task_func([[2, 3], [5, 6]])
        self.assertTrue((df.values >= RANGE[0]).all() and (df.values < RANGE[1]).all())

    def test_empty_input(self):
        """Test if function handles an empty input list correctly."""
        with self.assertRaises(IndexError):
            task_func([])

    def test_negative_input(self):
        """Test if function handles negative integers correctly in input."""
        with self.assertRaises(ValueError):
            task_func([[2, -3], [5, 6]])

if __name__ == '__main__':
    unittest.main()