import pandas as pd
import numpy as np
import unittest

# Here is your prompt:
def task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=0):
    """
    Generate a Pandas DataFrame with random numeric values between 1 and 100, inclusive, and replace all occurrences of values less than 10 with -1.
    
    Requirements:
    - pandas
    - numpy
    
    Parameters:
    - data_size (int, optional): The number of rows in the DataFrame. Defaults to 1000.
    - column_names (list of str, optional): Names of the DataFrame columns. Defaults to ['A', 'B', 'C', 'D', 'E'].

    Returns:
    - DataFrame: The modified Pandas DataFrame.
    
    Examples:
    >>> df = task_func(data_size=100, column_names=['X', 'Y', 'Z'], seed=42)
    >>> df.shape
    (100, 3)
    """
    
    np.random.seed(seed)
    df = pd.DataFrame(np.random.randint(1, 101, size=(data_size, len(column_names))), columns=column_names)
    df[df < 10] = -1  # Correctly replace values less than 10 with -1
    return df

class TestTaskFunc(unittest.TestCase):
    
    def test_default_size_and_columns(self):
        df = task_func()
        self.assertEqual(df.shape, (1000, 5))
        self.assertListEqual(list(df.columns), ['A', 'B', 'C', 'D', 'E'])

    def test_custom_columns(self):
        df = task_func(column_names=['X', 'Y', 'Z'])
        self.assertEqual(df.shape[1], 3)
        self.assertListEqual(list(df.columns), ['X', 'Y', 'Z'])

    def test_value_replacement(self):
        df = task_func(data_size=100, seed=42)
        # Check if all values less than 10 have been replaced with -1
        self.assertTrue((df[df < 10] == -1).all().all())
    
    def test_randomness_with_seed(self):
        df1 = task_func(seed=0)
        df2 = task_func(seed=0)
        # With the same seed, the two dataframes should be equal
        pd.testing.assert_frame_equal(df1, df2)

    def test_shape_with_different_data_size(self):
        df = task_func(data_size=500)
        self.assertEqual(df.shape[0], 500)

if __name__ == '__main__':
    unittest.main()