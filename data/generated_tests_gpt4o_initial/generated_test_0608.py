import unittest
import pandas as pd
import numpy as np
from random import sample

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

def task_func(df, tuples, n_plots):
    """
    Remove rows from a dataframe based on values of multiple columns, and then create n random pairs of two columns 
    against each other to generate pairplots.

    Parameters:
    df (DataFrame): The pandas DataFrame.
    tuples (list of tuple): A list of tuples, where each tuple represents a row to be removed based on its values.
    n_plots (int): The number of pairplots to be generated using randomly selected column pairs.

    Returns:
    tuple: A tuple containing:
        - DataFrame: The modified DataFrame after removing specified rows.
        - list of Axes: A list containing the generated pairplots.
    """

    if not df.empty:
        df = df[~df.apply(tuple, axis=1).isin(tuples)]

    plots = []
    if n_plots > 0 and not df.empty:
        available_columns = df.columns.tolist()
        for _ in range(min(n_plots, len(available_columns) // 2)):  # Ensure we have enough columns
            # Randomly select two columns for pairplot
            selected_columns = sample(available_columns, 2)
            plot = sns.pairplot(df, vars=selected_columns)
            plots.append(plot)

    return df, plots


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame(np.random.randint(0, 100, size=(100, 5)), columns=COLUMNS)

    def test_empty_dataframe(self):
        result_df, plots = task_func(pd.DataFrame(), [(1, 2, 3, 4, 5)], 3)
        self.assertTrue(result_df.empty)
        self.assertEqual(plots, [])

    def test_no_rows_to_remove(self):
        result_df, plots = task_func(self.df, [], 3)
        self.assertEqual(result_df.shape, self.df.shape)
        self.assertGreaterEqual(len(plots), 0)

    def test_removed_rows(self):
        tuples_to_remove = [tuple(self.df.iloc[i]) for i in range(5)]
        result_df, plots = task_func(self.df, tuples_to_remove, 3)
        self.assertEqual(result_df.shape[0], self.df.shape[0] - len(tuples_to_remove))

    def test_n_plots_greater_than_available(self):
        result_df, plots = task_func(self.df, [], 10)
        self.assertLessEqual(len(plots), len(self.df.columns) // 2)

    def test_n_plots_equals_zero(self):
        result_df, plots = task_func(self.df, [], 0)
        self.assertEqual(len(plots), 0)

if __name__ == '__main__':
    unittest.main()