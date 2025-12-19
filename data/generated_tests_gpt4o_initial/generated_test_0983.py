import unittest
import pandas as pd
import numpy as np
import seaborn as sns

# Here is your prompt:
def task_func(df):
    """
    Generates a pair plot from a numeric DataFrame and calculates its covariance matrix.

    Parameters:
    - df (pandas.DataFrame): A pandas DataFrame with only numeric columns.

    Returns:
    - tuple:
        - covariance_df (pandas.DataFrame): The covariance matrix of the input DataFrame.
        - pair_plot (sns.axisgrid.PairGrid): Pair plot of the input DataFrame.

    Raises:
    - ValueError: If the DataFrame is empty.
    - TypeError: If the DataFrame contains non-numeric data types.

    Requirements:
    - numpy
    - seaborn

    Examples:
    >>> import pandas as pd
    >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
    >>> covariance_df, ax = task_func(df)
    >>> type(ax)
    <class 'seaborn.axisgrid.PairGrid'>
    >>> covariance_df
         A    B    C
    A  1.0  1.0  1.0
    B  1.0  1.0  1.0
    C  1.0  1.0  1.0
    """

    if df.empty:
        raise ValueError("DataFrame is empty. Non-empty DataFrame required.")
    if not all(df.dtypes.apply(lambda x: np.issubdtype(x, np.number))):
        raise TypeError(
            "DataFrame contains non-numeric data. Only numeric data types are supported."
        )
    covariance_df = df.cov()
    pair_plot = sns.pairplot(df)

    return covariance_df, pair_plot

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        """Set up for all tests"""
        self.numeric_df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [4, 5, 6],
            'C': [7, 8, 9]
        })
        
        self.empty_df = pd.DataFrame()
        
        self.non_numeric_df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c'],
            'C': [7.0, 8.0, 9.0]
        })

    def test_task_func_with_numeric_df(self):
        """Test with a valid numeric DataFrame"""
        covariance_df, pair_plot = task_func(self.numeric_df)
        self.assertIsInstance(covariance_df, pd.DataFrame)
        self.assertIsInstance(pair_plot, sns.axisgrid.PairGrid)
        expected_covariance = np.array([[1.0, 1.0, 1.0],
                                         [1.0, 1.0, 1.0],
                                         [1.0, 1.0, 1.0]])
        pd.testing.assert_frame_equal(covariance_df.values, expected_covariance)

    def test_task_func_with_empty_df(self):
        """Test with an empty DataFrame"""
        with self.assertRaises(ValueError):
            task_func(self.empty_df)

    def test_task_func_with_non_numeric_df(self):
        """Test with a DataFrame containing non-numeric data"""
        with self.assertRaises(TypeError):
            task_func(self.non_numeric_df)

    def test_task_func_with_single_numeric_column(self):
        """Test with a DataFrame having a single numeric column"""
        single_numeric_df = pd.DataFrame({'A': [2, 4, 6]})
        covariance_df, pair_plot = task_func(single_numeric_df)
        self.assertIsInstance(covariance_df, pd.DataFrame)
        self.assertEqual(covariance_df.shape, (1, 1))  # 1x1 covariance matrix for single column

    def test_task_func_with_all_zero_values(self):
        """Test with a DataFrame containing all zero values"""
        zero_df = pd.DataFrame({
            'A': [0, 0, 0],
            'B': [0, 0, 0]
        })
        covariance_df, pair_plot = task_func(zero_df)
        self.assertIsInstance(covariance_df, pd.DataFrame)
        self.assertTrue((covariance_df == 0).all().all())  # All values should be zero

if __name__ == '__main__':
    unittest.main()