import unittest
import pandas as pd
import numpy as np

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Sample DataFrame for testing
        self.df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
        self.tuples = [(self.df.iloc[0]['A'], self.df.iloc[0]['B'], self.df.iloc[0]['C'], self.df.iloc[0]['D'], self.df.iloc[0]['E'])]

    def test_remove_rows(self):
        modified_df, _ = task_func(self.df, self.tuples, 3)
        # Check that the row that was supposed to be removed is no longer in the DataFrame
        self.assertFalse(any((self.df.iloc[0].values == row).all() for row in modified_df.values), "Row not removed correctly.")

    def test_plot_count(self):
        modified_df, plots = task_func(self.df, self.tuples, 3)
        # Check that the number of plots generated is less than or equal to the specified number
        self.assertLessEqual(len(plots), 3, "Number of plots generated exceeds n_plots.")

    def test_columns_exist_in_plots(self):
        modified_df, plots = task_func(self.df, self.tuples, 3)
        # Ensure that the column names in each plot exist in the modified DataFrame
        for (x_col, y_col), _ in plots:
            self.assertIn(x_col, modified_df.columns, f"Column {x_col} not in DataFrame after removal.")
            self.assertIn(y_col, modified_df.columns, f"Column {y_col} not in DataFrame after removal.")

    def test_no_rows_removed_with_empty_tuples(self):
        modified_df, _ = task_func(self.df, [], 3)
        # Check that no rows are removed if no tuples are provided
        pd.testing.assert_frame_equal(modified_df, self.df, "Rows should not be removed with empty tuples.")

    def test_return_types(self):
        modified_df, plots = task_func(self.df, self.tuples, 3)
        # Check that the function returns the correct types
        self.assertIsInstance(modified_df, pd.DataFrame, "Return type should be a DataFrame.")
        self.assertIsInstance(plots, list, "Return type should include a list of plots.")

if __name__ == '__main__':
    unittest.main()