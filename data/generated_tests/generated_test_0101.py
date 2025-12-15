import unittest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

class TestTaskFunction(unittest.TestCase):

    def test_return_type(self):
        """Test if the function returns a matplotlib Axes object."""
        ax = task_func()
        self.assertIsInstance(ax, plt.Axes)

    def test_dataframe_shape(self):
        """Test if the shape of the DataFrame matches expected dimensions."""
        data_url = "http://lib.stat.cmu.edu/datasets/boston"
        raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
        expected_rows = len(raw_df) // 2
        expected_columns = 13  # Should include 13 features as per the prompt
        data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
        boston_df = pd.DataFrame(data=data, columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'])
        
        # Execute the function
        task_func_data = task_func().get_children()[0].get_array()
        
        self.assertEqual(task_func_data.shape, (expected_rows, expected_columns))

    def test_correlation_matrix(self):
        """Test if the correlation matrix is computed correctly."""
        data_url = "http://lib.stat.cmu.edu/datasets/boston"
        raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
        data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
        boston_df = pd.DataFrame(data=data, columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'])
        
        expected_correlation = boston_df.corr()
        
        task_func_correlation = task_func().get_children()[0].get_array()
        
        pd.testing.assert_frame_equal(pd.DataFrame(task_func_correlation), expected_correlation)

    def test_error_handling(self):
        """Test if ValueError is raised with an invalid URL."""
        with self.assertRaises(ValueError):
            task_func("invalid_url")

    def test_plot_saved(self):
        """Test if the heatmap can be successfully generated and displayed."""
        ax = task_func()
        self.assertIsNotNone(ax.get_figure())
        self.assertIsInstance(ax.collections[0], plt.collections.Collection)

if __name__ == '__main__':
    unittest.main()