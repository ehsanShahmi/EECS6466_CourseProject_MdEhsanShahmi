import pandas as pd
import matplotlib.pyplot as plt
from unittest import TestCase, main

class TestTaskFunction(TestCase):

    def test_basic_functionality(self):
        """Test basic functionality with simple numeric DataFrame."""
        input_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        expected_output = pd.DataFrame({'A': [1, 3, 6], 'B': [4, 9, 15]})
        output_df, fig = task_func(input_df)
        
        pd.testing.assert_frame_equal(output_df, expected_output)
        self.assertIsInstance(fig, plt.Figure)

    def test_empty_dataframe(self):
        """Test with an empty DataFrame, which should raise ValueError."""
        input_df = pd.DataFrame()
        with self.assertRaises(ValueError):
            task_func(input_df)

    def test_non_numeric_dataframe(self):
        """Test with a DataFrame that contains non-numeric data."""
        input_df = pd.DataFrame({'A': [1, 'text', 3], 'B': [4, 5, 6]})
        with self.assertRaises(ValueError):
            task_func(input_df)

    def test_dataframe_with_nan(self):
        """Test with a DataFrame that includes NaN values."""
        input_df = pd.DataFrame({'A': [1, 2, None], 'B': [4, None, 6]})
        expected_output = pd.DataFrame({'A': [1, 3, 3], 'B': [4, 4, 10]})
        output_df, fig = task_func(input_df)
        
        pd.testing.assert_frame_equal(output_df, expected_output)
        self.assertIsInstance(fig, plt.Figure)

    def test_correct_plot_attributes(self):
        """Test that the plot has the correct title and labels."""
        input_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        output_df, fig = task_func(input_df)
        
        ax = fig.axes[0]
        self.assertEqual(ax.get_title(), "Cumulative Sum per Column")
        self.assertEqual(ax.get_xlabel(), "Index")
        self.assertEqual(ax.get_ylabel(), "Cumulative Sum")
        self.assertTrue(ax.get_legend() is not None)

if __name__ == "__main__":
    main()