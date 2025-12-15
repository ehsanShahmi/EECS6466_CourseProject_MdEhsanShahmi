import unittest
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Here is your prompt:
def task_func(df, x_column, y_column):
    """
    Draws a scatter plot for the specified columns from a pandas DataFrame and fits a linear regression model to the data.

    Parameters:
    df (DataFrame): The input pandas DataFrame.
    x_column (str): The column name for the x-axis. Data contained in column must be numeric.
    y_column (str): The column name for the y-axis. Data contained in column must be numeric.

    Returns:
    matplotlib.axes._axes.Axes: The Axes object containing the scatter plot and the linear regression line.

    Requirements:
    - matplotlib
    - sklearn

    Notes:
    - After plotting the scatterplot, this function overlays the predicted regression line on top in red on the same Axes.

    Example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4]})
    >>> ax = task_func(df, 'A', 'B')
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """

    X = df[x_column].values.reshape(-1, 1)
    Y = df[y_column].values
    reg = LinearRegression().fit(X, Y)
    Y_pred = reg.predict(X)

    fig, ax = plt.subplots()
    ax.scatter(X, Y)
    ax.plot(X, Y_pred, color="red")

    return ax


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Sample DataFrames for testing
        self.df_valid = pd.DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4]})
        self.df_invalid_column = pd.DataFrame({'A': [1, 2, 3], 'B': [2, 3, 4]})
        self.df_empty = pd.DataFrame(columns=['A', 'B'])

    def test_valid_input(self):
        ax = task_func(self.df_valid, 'A', 'B')
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.collections), 1)  # Check for scatter plot

    def test_invalid_x_column(self):
        with self.assertRaises(KeyError):
            task_func(self.df_valid, 'C', 'B')

    def test_invalid_y_column(self):
        with self.assertRaises(KeyError):
            task_func(self.df_valid, 'A', 'C')

    def test_empty_dataframe(self):
        ax = task_func(self.df_empty, 'A', 'B')
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.collections), 0)  # No points to plot

    def test_numeric_columns(self):
        with self.assertRaises(ValueError):
            task_func(pd.DataFrame({'A': [1, 2, 'three'], 'B': [2, 3, 4]}), 'A', 'B')


if __name__ == '__main__':
    unittest.main()