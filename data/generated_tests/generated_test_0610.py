import unittest
import pandas as pd
from random import sample
import seaborn as sns

# Constants
COLUMNS = ['A', 'B', 'C', 'D', 'E']

# Test suite for task_func function
class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up a sample DataFrame for testing."""
        self.df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': [100, 200, 300, 400, 500],
            'D': [1000, 2000, 3000, 4000, 5000],
            'E': [10000, 20000, 30000, 40000, 50000]
        })

    def test_remove_existing_rows(self):
        """Test removing existing rows."""
        tuples = [(1, 10, 100, 1000, 10000)]
        modified_df, plots = task_func(self.df, tuples, 0)
        self.assertEqual(len(modified_df), 4)  # One row should be removed

    def test_no_rows_removed(self):
        """Test that no rows are removed when no matching tuples are provided."""
        tuples = [(6, 70, 800, 9000, 100000)]
        modified_df, plots = task_func(self.df, tuples, 0)
        self.assertEqual(len(modified_df), 5)  # No rows should be removed

    def test_empty_dataframe(self):
        """Test behavior with an empty DataFrame."""
        empty_df = pd.DataFrame(columns=COLUMNS)
        tuples = [(1, 10, 100, 1000, 10000)]
        modified_df, plots = task_func(empty_df, tuples, 3)
        self.assertTrue(modified_df.empty)  # DataFrame should be empty
        self.assertEqual(len(plots), 0)  # No plots should be generated

    def test_generate_plots(self):
        """Test that plots are generated when DataFrame is not empty."""
        tuples = [(1, 10, 100, 1000, 10000)]
        modified_df, plots = task_func(self.df, tuples, 3)
        self.assertEqual(len(plots), 3)  # Three plots should be generated

    def test_invalid_tuples(self):
        """Test that invalid tuples do not crash the function."""
        tuples = [(6, 70, 800, 9000, 100000)]
        modified_df, plots = task_func(self.df, tuples, 3)
        self.assertEqual(len(modified_df), 5)  # All original rows should remain
        self.assertEqual(len(plots), 3)  # Three plots should still be generated

if __name__ == '__main__':
    unittest.main()