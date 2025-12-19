import pandas as pd
import unittest
from random import sample
import numpy as np
import matplotlib.pyplot as plt

# Constants for column names to use in plots
COLUMNS = ['A', 'B', 'C', 'D', 'E']

# Provided function that we are going to test
def task_func(df: pd.DataFrame, tuples: list, n_plots: int) -> (pd.DataFrame, list):
    '''
    Remove rows from a dataframe based on column values and generate random scatter plots.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame to be modified.
    - tuples (list): A list of tuples, each representing a row's values for removal.
    - n_plots (int): Number of scatter plots to generate from random pairs of columns.

    Returns:
    - pd.DataFrame: The DataFrame after removal of specified rows.
    - list: A list containing matplotlib Axes objects of the generated plots.
    
    Requirements:
    - pandas
    - matplotlib.pyplot
    - random
    
    Example:
    >>> df = pd.DataFrame(np.random.randint(0,100,size=(100, 5)), columns=COLUMNS)
    >>> tuples = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
    >>> modified_df, plots = task_func(df, tuples, 3)
    '''
    df = df[~df.apply(tuple, axis=1).isin(tuples)]
    plots = []
    for _ in range(n_plots):
        selected_columns = sample(COLUMNS, 2)
        ax = df.plot(x=selected_columns[0], y=selected_columns[1], kind='scatter')
        plots.append(ax)

    plt.show()
    return df, plots

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Set up a sample DataFrame for testing
        self.df = pd.DataFrame(np.random.randint(0, 100, size=(100, 5)), columns=COLUMNS)

    def test_remove_no_tuples(self):
        # Test removing no rows when no tuples are provided
        original_count = len(self.df)
        modified_df, _ = task_func(self.df, [], 3)
        self.assertEqual(len(modified_df), original_count)

    def test_remove_specific_rows(self):
        # Test that specific rows can be removed
        rows_to_remove = [(10, 20, 30, 40, 50), (60, 70, 80, 90, 100)]
        for row in rows_to_remove:
            self.df.loc[len(self.df)] = row  # Add rows to the DataFrame
        modified_df, _ = task_func(self.df, rows_to_remove, 3)
        self.assertEqual(len(modified_df), len(self.df) - len(rows_to_remove))

    def test_plot_creation(self):
        # Test the number of plots created is as specified
        n_plots = 5
        modified_df, plots = task_func(self.df, [], n_plots)
        self.assertEqual(len(plots), n_plots)

    def test_random_column_selection(self):
        # Test that at least one plot contains expected column names
        n_plots = 3
        modified_df, plots = task_func(self.df, [], n_plots)
        selected_columns = [plot.get_title().split(' ')[1] for plot in plots]
        for col in selected_columns:
            self.assertIn(col, COLUMNS)

    def test_empty_dataframe(self):
        # Test behavior with an empty DataFrame
        empty_df = pd.DataFrame(columns=COLUMNS)
        modified_df, plots = task_func(empty_df, [], 3)
        self.assertTrue(modified_df.empty)
        self.assertEqual(len(plots), 0)

if __name__ == '__main__':
    unittest.main()