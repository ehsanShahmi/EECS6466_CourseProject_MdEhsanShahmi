import unittest
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

# Here is your prompt:

def task_func(df):
    """
    Normalize numeric columns in a DataFrame and draw a box plot for each column. Missing values are replaced by column's average.

    Parameters:
    df (DataFrame): The pandas DataFrame.

    Returns:
    DataFrame: A pandas DataFrame after normalization.
    Axes: A matplotlib Axes displaying a box plot for each column.

    Requirements:
    - pandas
    - numpy
    - sklearn.preprocessing.MinMaxScaler
    - matplotlib.pyplot

    Example:
    >>> import pandas as pd
    >>> import numpy as np
    >>> df = pd.DataFrame([[1,2,3],[4,5,6],[7.0,np.nan,9.0]], columns=["c1","c2","c3"])
    >>> df, ax = task_func(df)
    >>> print(df)
        c1   c2   c3
    0  0.0  0.0  0.0
    1  0.5  1.0  0.5
    2  1.0  0.5  1.0
    """
               df = df.fillna(df.mean(axis=0))
    scaler = MinMaxScaler()
    df[df.columns] = scaler.fit_transform(df[df.columns])
    plt.figure(figsize=(10, 5))
    df.boxplot(grid=False, vert=False, fontsize=15)
    return df, plt.gca()

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.df1 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7.0, np.nan, 9.0]], columns=["c1", "c2", "c3"])
        self.df2 = pd.DataFrame([[np.nan, 2, 3], [np.nan, 5, np.nan], [7.0, 7.0, 9.0]], columns=["c1", "c2", "c3"])
        self.df3 = pd.DataFrame([[1, 1, 1], [2, 2, 2], [3, 3, 3]], columns=["c1", "c2", "c3"])
        self.df4 = pd.DataFrame([[np.nan, np.nan, np.nan], [np.nan, np.nan, np.nan]], columns=["c1", "c2", "c3"])
    
    def test_normalization(self):
        df, _ = task_func(self.df1)
        expected_df = pd.DataFrame([[0.0, 0.0, 0.0], [0.5, 1.0, 0.5], [1.0, 0.5, 1.0]], columns=["c1", "c2", "c3"])
        pd.testing.assert_frame_equal(df, expected_df)

    def test_fillna_with_mean(self):
        df, _ = task_func(self.df2)
        expected_df = pd.DataFrame([[0.5, 0.0, 0.25], [0.5, 0.625, 0.75], [1.0, 1.0, 1.0]], columns=["c1", "c2", "c3"])
        pd.testing.assert_frame_equal(df, expected_df)

    def test_no_change_for_identical_values(self):
        df, _ = task_func(self.df3)
        expected_df = pd.DataFrame([[0.0, 0.0, 0.0], [0.5, 0.5, 0.5], [1.0, 1.0, 1.0]], columns=["c1", "c2", "c3"])
        pd.testing.assert_frame_equal(df, expected_df)

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=["c1", "c2", "c3"])
        with self.assertRaises(ValueError):
            task_func(df)

    def test_all_nan_dataframe(self):
        df, _ = task_func(self.df4)
        expected_df = pd.DataFrame(columns=["c1", "c2", "c3"])  # Should remain empty or raise a specific exception
        self.assertTrue(df.empty)

if __name__ == '__main__':
    unittest.main()