import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import unittest

# Constants
COLUMNS = ['Date', 'Value']

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up test data."""
        self.valid_df = pd.DataFrame([
            ['2021-01-01', [8, 10, 12]],
            ['2021-01-02', [7, 9, 11]]
        ], columns=COLUMNS)

        self.empty_df = pd.DataFrame(columns=COLUMNS)

        self.invalid_df = pd.DataFrame([
            ['2021-01-01', 'Not a list'],
            ['2021-01-02', [7, 9, 11]]
        ], columns=COLUMNS)

    def test_valid_input(self):
        """Test with valid DataFrame input."""
        scaled_df, ax = task_func(self.valid_df, plot=False)
        self.assertEqual(scaled_df.shape, (2, 4))
        self.assertListEqual(list(scaled_df.columns), ['Date', 0, 1, 2])

    def test_plot_creation(self):
        """Test that plot is created when requested."""
        _, ax = task_func(self.valid_df, plot=True)
        self.assertIsInstance(ax, plt.Axes)
        plt.close()  # Close the plot to avoid display during tests

    def test_empty_dataframe(self):
        """Test with empty DataFrame."""
        with self.assertRaises(KeyError):
            task_func(self.empty_df)

    def test_invalid_value_column(self):
        """Test with invalid format in 'Value' column."""
        with self.assertRaises(ValueError):
            task_func(self.invalid_df)

    def test_nonexistent_columns(self):
        """Test with DataFrame lacking required columns."""
        df_missing_columns = pd.DataFrame([['2021-01-01', [8, 10]]], columns=['SomeDate', 'SomeValue'])
        with self.assertRaises(KeyError):
            task_func(df_missing_columns)

if __name__ == '__main__':
    unittest.main()