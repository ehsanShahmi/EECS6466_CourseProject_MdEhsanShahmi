import pandas as pd
import numpy as np
import unittest
import matplotlib.pyplot as plt

# Here is the provided prompt:
def task_func(data, column="c"):
    """
    Remove a column from a data dictionary if it exists, and then plot the remaining data
    if it contains numeric data.

    Parameters:
    - data (dict): The input data dictionary.
    - column (str): Name of column to remove. Defaults to "c".

    Returns:
    - df (pd.DataFrame): The modified DataFrame after removing the specified column.
    - ax (matplotlib.axes._axes.Axes or None): The plot of the modified DataFrame if there's
      numeric data to plot, otherwise None.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
    >>> modified_df, ax = task_func(data)
    >>> ax
    <Axes: >
    >>> modified_df
       a  b
    0  1  4
    1  2  5
    2  3  6
    """

    df = pd.DataFrame(data)
    if column in df.columns:
        df = df.drop(columns=column)

    # If there's no numeric data, return None for the plot.
    if df.empty or not np.any(df.dtypes.apply(pd.api.types.is_numeric_dtype)):
        return df, None

    ax = df.plot()
    return df, ax

class TestTaskFunc(unittest.TestCase):

    def test_remove_column(self):
        data = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
        expected_df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
        modified_df, ax = task_func(data)
        pd.testing.assert_frame_equal(modified_df, expected_df)
        self.assertIsNotNone(ax)

    def test_no_numeric_data(self):
        data = {'a': ['x', 'y', 'z'], 'b': ['u', 'v', 'w'], 'c': [1, 2, 3]}
        expected_df = pd.DataFrame({'a': ['x', 'y', 'z'], 'b': ['u', 'v', 'w']})
        modified_df, ax = task_func(data)
        pd.testing.assert_frame_equal(modified_df, expected_df)
        self.assertIsNone(ax)

    def test_empty_data(self):
        data = {}
        expected_df = pd.DataFrame()
        modified_df, ax = task_func(data)
        pd.testing.assert_frame_equal(modified_df, expected_df)
        self.assertIsNone(ax)

    def test_column_not_present(self):
        data = {'a': [1, 2], 'b': [3, 4]}
        expected_df = pd.DataFrame({'a': [1, 2], 'b': [3, 4]})
        modified_df, ax = task_func(data, column='c')
        pd.testing.assert_frame_equal(modified_df, expected_df)
        self.assertIsNotNone(ax)

    def test_numeric_data_only_column_removed(self):
        data = {'a': [1, 2, 3], 'b': ['x', 'y', 'z'], 'c': [7, 8, 9]}
        expected_df = pd.DataFrame({'a': [1, 2, 3]})
        modified_df, ax = task_func(data)
        pd.testing.assert_frame_equal(modified_df, expected_df)
        self.assertIsNotNone(ax)

# To run the test suite
if __name__ == '__main__':
    unittest.main()