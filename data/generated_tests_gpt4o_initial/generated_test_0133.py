import unittest
import pandas as pd
import numpy as np
from pandas.testing import assert_frame_equal
from sklearn.preprocessing import MinMaxScaler

# Given function from the prompt
def task_func(df):
    if not isinstance(df, pd.DataFrame) or df.empty:
        raise ValueError("Input must be a non-empty DataFrame.")
    
    last_col_name = df.columns[-1]
    scaler = MinMaxScaler()
    normalized_values = scaler.fit_transform(df[[last_col_name]])
    normalized_df = df.copy()
    normalized_df[last_col_name] = normalized_values.flatten()
    
    fig, ax = plt.subplots()
    ax.plot(normalized_df.index, normalized_df[last_col_name])
    ax.set_title(f'Normalized Data of {last_col_name}')
    ax.set_xlabel("Index")
    ax.set_ylabel("Normalized Value")

    return normalized_df, ax

# Test Suite
class TestTaskFunc(unittest.TestCase):

    def test_non_dataframe_input(self):
        with self.assertRaises(ValueError):
            task_func("Not a DataFrame")

    def test_empty_dataframe(self):
        empty_df = pd.DataFrame()
        with self.assertRaises(ValueError):
            task_func(empty_df)

    def test_single_column_dataframe(self):
        df = pd.DataFrame({'A': [10, 20, 30, 40]})
        normalized_df, _ = task_func(df)
        expected_df = df.copy()
        expected_df['A'] = [0.0, 0.3333, 0.6667, 1.0]
        assert_frame_equal(normalized_df.round(4), expected_df)

    def test_multiple_columns_dataframe(self):
        df = pd.DataFrame({'A': [10, 20, 30, 40], 'B': [1, 2, 3, 4]})
        normalized_df, _ = task_func(df)
        expected_df = df.copy()
        expected_df['B'] = [0.0, 0.3333, 0.6667, 1.0]
        assert_frame_equal(normalized_df.round(4), expected_df)

    def test_plot_title(self):
        df = pd.DataFrame({'A': [10, 20, 30, 40], 'B': [5, 6, 7, 8]})
        _, ax = task_func(df)
        self.assertEqual(ax.get_title(), 'Normalized Data of B')

# Run the tests
if __name__ == "__main__":
    unittest.main()