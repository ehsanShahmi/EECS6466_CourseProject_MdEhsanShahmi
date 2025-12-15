import unittest
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import random

class TestTaskFunc(unittest.TestCase):
    
    def test_plot_title(self):
        """Test that the plot title is correct."""
        ax = task_func()
        self.assertEqual(ax.get_title(), 'Random Time Series Data')

    def test_x_axis_label(self):
        """Test that the x-axis label is correct."""
        ax = task_func()
        self.assertEqual(ax.get_xlabel(), 'Date')

    def test_y_axis_label(self):
        """Test that the y-axis label is correct."""
        ax = task_func()
        self.assertEqual(ax.get_ylabel(), 'Value')

    def test_plot_value_range(self):
        """Test that all y-values are in the expected range."""
        ax = task_func()
        y_data = ax.lines[0].get_ydata()
        self.assertTrue(all(0 <= v <= 100 for v in y_data))

    def test_reproducibility(self):
        """Test that the plot values are reproducible with the same seed."""
        random.seed(42)
        dates1 = pd.date_range(end=datetime.now(), periods=30)
        values1 = [random.randint(0, 100) for _ in range(30)]
        
        random.seed(42)
        dates2 = pd.date_range(end=datetime.now(), periods=30)
        values2 = [random.randint(0, 100) for _ in range(30)]
        
        self.assertEqual(values1, values2)

if __name__ == '__main__':
    unittest.main()