import unittest
import pandas as pd
import numpy as np

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

# Here is your prompt:
def task_func(df, tuples, n_plots):
    """
    Removes rows from a DataFrame based on values of multiple columns, 
    and then create n random line plots of two columns against each other.

    Parameters:
    - df (pd.DataFrame): The input pandas DataFrame.
    - tuples (list of tuple): A list of tuples, each tuple represents values in a row to be removed.
    - n_plots (int): The number of line plots to generate.

    Returns:
    - (pd.DataFrame, list): A tuple containing the modified DataFrame and a list of plot details.
      Each entry in the plot details list is a tuple containing the two columns plotted against each other.

    Requirements:
    - matplotlib.pyplot
    - random

    Example:
    >>> import numpy as np, pandas as pd
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=list('ABCDE'))
    >>> tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
    >>> modified_df, plot_details = task_func(df, tuples, 3)
    """
    mask = df.apply(tuple, axis=1).isin(tuples)
    df = df[~mask]

    plot_details = []
    for _ in range(min(n_plots, len(df))):
        selected_columns = sample(COLUMNS, 2)
        df.plot(x=selected_columns[0], y=selected_columns[1], kind='line')
        plot_details.append((selected_columns[0], selected_columns[1]))

    plt.show()

    return df, plot_details

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create a sample DataFrame for testing."""
        self.df = pd.DataFrame(np.random.randint(0, 100, size=(100, 5)), columns=COLUMNS)
        self.tuples_to_remove = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]

    def test_remove_rows(self):
        """Test if the function correctly removes specified rows."""
        original_size = self.df.shape[0]
        modified_df, _ = task_func(self.df, self.tuples_to_remove, 0)
        self.assertLess(modified_df.shape[0], original_size, "Rows were not removed as expected.")

    def test_plot_count(self):
        """Test if the correct number of plots are generated based on input."""
        n_plots = 3
        _, plot_details = task_func(self.df, self.tuples_to_remove, n_plots)
        self.assertEqual(len(plot_details), min(n_plots, self.df.shape[0]), "The number of plots generated is incorrect.")

    def test_plot_columns(self):
        """Test if the plot details contains valid column names."""
        _, plot_details = task_func(self.df, self.tuples_to_remove, 3)
        for col1, col2 in plot_details:
            self.assertIn(col1, COLUMNS, f"Column {col1} is not valid.")
            self.assertIn(col2, COLUMNS, f"Column {col2} is not valid.")

    def test_return_types(self):
        """Test if the function returns a tuple of (DataFrame, list)."""
        result = task_func(self.df, self.tuples_to_remove, 1)
        self.assertIsInstance(result, tuple, "Return type is not a tuple.")
        self.assertIsInstance(result[0], pd.DataFrame, "First element is not a DataFrame.")
        self.assertIsInstance(result[1], list, "Second element is not a list.")

    def test_empty_dataframe(self):
        """Test function with an empty DataFrame."""
        empty_df = pd.DataFrame(columns=COLUMNS)
        modified_df, plot_details = task_func(empty_df, self.tuples_to_remove, 3)
        self.assertTrue(modified_df.empty, "Modified DataFrame is not empty for an empty input DataFrame.")
        self.assertEqual(plot_details, [], "Plot details should be empty for an empty DataFrame.")

if __name__ == "__main__":
    unittest.main()