import numpy as np
import pandas as pd
import random
import unittest

def task_func(rows=3, cols=2, min_val=0, max_val=100, seed=0):
    """
    Creates a matrix of specified dimensions with random integers within a given range,
    and then converts it into a pandas DataFrame.
    
    Parameters:
    - rows (int): Number of rows in the matrix. Default is 3.
    - cols (int): Number of columns in the matrix. Default is 2.
    - min_val (int): Minimum integer value for the random integers. Default is 0.
    - max_val (int): Maximum integer value for the random integers. Default is 100.
    
    Returns:
    DataFrame: A pandas DataFrame containing random integers within the specified range.
    
    Requirements:
    - numpy
    - pandas
    - random

    Example:
    >>> df = task_func(3, 2, 0, 100)
    >>> print(type(df))
    <class 'pandas.core.frame.DataFrame'>
    >>> print(df.shape)
    (3, 2)
    """

    random.seed(seed)
    if min_val == max_val:
        matrix = np.full((rows, cols), min_val)
    else:
        matrix = np.array([[random.randrange(min_val, max_val) for j in range(cols)] for i in range(rows)])
    df = pd.DataFrame(matrix)
    return df

class TestTaskFunc(unittest.TestCase):
    
    def test_default_parameters(self):
        df = task_func()
        self.assertEqual(df.shape, (3, 2))
        self.assertTrue(isinstance(df, pd.DataFrame))

    def test_custom_dimensions(self):
        df = task_func(rows=5, cols=4)
        self.assertEqual(df.shape, (5, 4))

    def test_fixed_value_matrix(self):
        df = task_func(rows=3, cols=3, min_val=5, max_val=5)
        expected_matrix = np.full((3, 3), 5)
        pd.testing.assert_frame_equal(df, pd.DataFrame(expected_matrix))

    def test_min_max_range(self):
        df = task_func(rows=2, cols=2, min_val=10, max_val=20)
        self.assertTrue((df.values >= 10).all() and (df.values < 20).all())
        
    def test_seed_consistency(self):
        random.seed(0)
        df1 = task_func(seed=0)
        random.seed(0)
        df2 = task_func(seed=0)
        pd.testing.assert_frame_equal(df1, df2)

if __name__ == '__main__':
    unittest.main()