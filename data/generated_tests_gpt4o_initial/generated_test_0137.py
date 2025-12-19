import unittest
import pandas as pd
import numpy as np
from scipy.stats import skew

# Here is your prompt:
def task_func(df):
    """
    Calculate the skewness of the last column of the dataframe.

    Parameters:
    df (DataFrame): The input dataframe.

    Returns:
    float: The skewness of the last column of the dataframe.

    Raises:
    ValueError: If the input is not a DataFrame or has no columns.

    Requirements:
    - pandas
    - scipy.stats
    
    Example:
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
    >>> skewness = task_func(df)
    """
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty pandas DataFrame.")

    last_col = df.columns[-1]
    skewness = skew(df[last_col].dropna())  # dropna() to handle NaN values

    return skewness


class TestTaskFunc(unittest.TestCase):

    def test_skewness_of_int_column(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))
        result = task_func(df)
        self.assertIsInstance(result, float)

    def test_skewness_of_float_column(self):
        df = pd.DataFrame(np.random.normal(loc=0.0, scale=1.0, size=(100, 4)), columns=list('ABCD'))
        result = task_func(df)
        self.assertIsInstance(result, float)

    def test_skewness_with_nan(self):
        data = {'A': [1, 2, np.nan, 4], 'B': [5, 6, 7, 8], 'C': [9, 10, 11, 12], 'D': [13, np.nan, 15, 16]}
        df = pd.DataFrame(data)
        result = task_func(df)
        self.assertIsInstance(result, float)

    def test_invalid_input_not_dataframe(self):
        with self.assertRaises(ValueError):
            task_func("not a dataframe")

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['A', 'B', 'C', 'D'])
        with self.assertRaises(ValueError):
            task_func(df)


if __name__ == '__main__':
    unittest.main()