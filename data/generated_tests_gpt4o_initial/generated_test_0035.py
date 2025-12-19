import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Here is your prompt:
def task_func(df, target_values=[1, 3, 4]):
    """
    Replace all elements in DataFrame columns that do not exist in the target_values array with zeros, and then output the distribution of each column after replacing.
    - label each plot as the name of the column it corresponds to.

    Parameters:
    - df (DataFrame): The input pandas DataFrame.
    - target_values (list) : Array of values not to replace by zero.

    Returns:
    - matplotlib.axes.Axes: The Axes object of the plotted data.

    Requirements:
    - seaborn
    - matplotlib.pyplot

    Example:
    >>> import pandas as pd
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> df = pd.DataFrame(np.random.randint(0,10,size=(100, 5)), columns=list('ABCDE'))
    >>> print(df.head(2))
       A  B  C  D  E
    0  6  3  7  4  6
    1  9  2  6  7  4
    >>> df1, ax = task_func(df)
    >>> print(ax)
    Axes(0.125,0.11;0.775x0.77)
    """
    df = df.applymap(lambda x: x if x in target_values else 0)
    plt.figure(figsize=(10, 5))
    for column in df.columns:
        sns.kdeplot(df[column], label=column, warn_singular=False)
    plt.legend()
    return df, plt.gca()

class TestTaskFunction(unittest.TestCase):

    def setUp(self):
        np.random.seed(42)
        self.df = pd.DataFrame(np.random.randint(0, 10, size=(100, 5)), columns=list('ABCDE'))

    def test_dataframe_shape(self):
        """Test if the shape of the DataFrame remains the same."""
        modified_df, _ = task_func(self.df)
        self.assertEqual(modified_df.shape, self.df.shape)

    def test_replacement_with_zeros(self):
        """Test if non-target values are replaced by zeros."""
        target_values = [1, 3, 4]
        modified_df, _ = task_func(self.df, target_values)
        for col in modified_df.columns:
            non_target_values = modified_df[col].unique()
            self.assertTrue(all(val in target_values or val == 0 for val in non_target_values))

    def test_target_values_preserved(self):
        """Test if the target values are preserved in the DataFrame."""
        target_values = [1, 3, 4]
        modified_df, _ = task_func(self.df, target_values)
        for col in modified_df.columns:
            preserved_values = modified_df[col][modified_df[col].nonzero()[0]].unique()
            self.assertTrue(all(val in target_values for val in preserved_values))

    def test_empty_dataframe(self):
        """Test the function with an empty DataFrame."""
        empty_df = pd.DataFrame(columns=list('ABCDE'))
        modified_df, ax = task_func(empty_df)
        self.assertTrue(modified_df.empty)
        self.assertIsInstance(ax, plt.Axes)

    def test_plot_generated(self):
        """Test if a plot is generated and returned."""
        modified_df, ax = task_func(self.df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())

if __name__ == '__main__':
    unittest.main()