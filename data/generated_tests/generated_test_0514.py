import unittest
import pandas as pd
import matplotlib.pyplot as plt

# Here is your prompt:
def task_func(array):
    """
    Create a Pandas DataFrame from a 2D list and plot the sum of each column.

    Parameters:
    array (list of list of int): The 2D list representing the data.

    Returns:
    DataFrame, Axes: A pandas DataFrame with the data and a matplotlib Axes object showing the sum of each column.

    Requirements:
    - pandas
    - matplotlib.pyplot

    Internal Constants:
    COLUMNS: List of column names used for the DataFrame ['A', 'B', 'C', 'D', 'E']

    Example:
    >>> df, ax = task_func([[1,2,3,4,5], [6,7,8,9,10]])
    >>> print(df)
       A  B  C  D   E
    0  1  2  3  4   5
    1  6  7  8  9  10
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """

    # Internal Constants
    COLUMNS = ["A", "B", "C", "D", "E"]

    df = pd.DataFrame(array, columns=COLUMNS)
    sums = df.sum()

    fig, ax = plt.subplots()
    sums.plot(kind="bar", ax=ax)

    return df, ax


class TestTaskFunc(unittest.TestCase):
    def test_dataframe_shape(self):
        df, _ = task_func([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        self.assertEqual(df.shape, (2, 5), "The DataFrame should have 2 rows and 5 columns.")

    def test_dataframe_columns(self):
        df, _ = task_func([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        expected_columns = ["A", "B", "C", "D", "E"]
        self.assertListEqual(list(df.columns), expected_columns, "The DataFrame should have the correct column names.")

    def test_column_sum(self):
        df, _ = task_func([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        expected_sums = pd.Series([7, 9, 11, 13, 15], index=["A", "B", "C", "D", "E"])
        self.assertTrue(df.sum().equals(expected_sums), "The sum of the columns in the DataFrame is incorrect.")

    def test_plot_creation(self):
        _, ax = task_func([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
        self.assertIsInstance(ax, plt.Axes, "The returned object should be a matplotlib Axes object.")

    def test_empty_input(self):
        df, _ = task_func([])
        self.assertTrue(df.empty, "The DataFrame should be empty for an empty input list.")


if __name__ == '__main__':
    unittest.main()