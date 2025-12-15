from scipy.stats import zscore
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import unittest

def task_func(df):
    """
    Calculate Z-scores for numeric columns in a DataFrame and draw a histogram for each column.
    - Missing values are replaced by the column's average.
    - The histograms are plotted with 10 bins.

    Parameters:
    - df (pandas.DataFrame): The input pandas DataFrame with numeric columns.

    Returns:
    - tuple:
        1. pandas.DataFrame: A DataFrame with computed z-scores.
        2. list: A list of Axes objects representing the histograms of the numeric columns.

    Requirements:
    - pandas.
    - numpy.
    - scipy.stats.zscore.
    - matplotlib.pyplot.

    Example:
    >>> import pandas as pd
    >>> import numpy as np
    >>> df_input = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7.0, np.nan, 9.0]], columns=["col1", "col2", "col3"])
    >>> zscore_output, plots = task_func(df_input)
    """

    # Fill missing values with column's average
    df = df.fillna(df.mean(axis=0))
    # Compute Z-scores
    df = df.apply(zscore)
    # Plot histograms for each numeric column
    axes = df.hist(grid=False, bins=10, layout=(1, df.shape[1]))
    plt.tight_layout()
    return df, axes

class TestTaskFunc(unittest.TestCase):
    
    def test_basic_functionality(self):
        df_input = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7.0, np.nan, 9.0]], columns=["col1", "col2", "col3"])
        zscore_output, plots = task_func(df_input)
        self.assertEqual(zscore_output.shape, (3, 3))
        self.assertIsNotNone(plots)
    
    def test_missing_values(self):
        df_input = pd.DataFrame([[1, 2, 3], [4, np.nan, 6], [7, 8, 9]], columns=["col1", "col2", "col3"])
        zscore_output, plots = task_func(df_input)
        self.assertTrue(zscore_output['col2'].isnull().sum() == 0)
        self.assertAlmostEqual(zscore_output['col2'].mean(), 0, places=5)

    def test_no_missing_values(self):
        df_input = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]], columns=["col1", "col2", "col3"])
        zscore_output, plots = task_func(df_input)
        self.assertAlmostEqual(zscore_output.values.mean(), 0, places=5)

    def test_single_column_dataframe(self):
        df_input = pd.DataFrame([[1], [2], [3], [4], [5]], columns=["col1"])
        zscore_output, plots = task_func(df_input)
        self.assertEqual(zscore_output.shape, (5, 1))
        self.assertTrue(zscore_output['col1'].isnull().sum() == 0)

    def test_empty_dataframe(self):
        df_input = pd.DataFrame(columns=["col1", "col2"])
        zscore_output, plots = task_func(df_input)
        self.assertEqual(zscore_output.shape, (0, 0))

if __name__ == '__main__':
    unittest.main()