from datetime import datetime
import pandas as pd
import numpy as np
import unittest
import matplotlib.pyplot as plt

# Here is your prompt:
# ... (the prompt content remains unchanged) ...

class TestTaskFunction(unittest.TestCase):

    def test_valid_case(self):
        """Test the function with valid inputs."""
        ax = task_func(0, 10000, 100, 0.01)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_ylabel(), "Value")

    def test_start_time_after_end_time(self):
        """Test ValueError when start_time is greater than end_time."""
        with self.assertRaises(ValueError) as context:
            task_func(10000, 0, 100, 0.01)
        self.assertEqual(str(context.exception), "Start time must be before end time")

    def test_invalid_step_value_zero(self):
        """Test ValueError when step value is zero."""
        with self.assertRaises(ValueError) as context:
            task_func(0, 10000, 0, 0.01)
        self.assertEqual(str(context.exception), "Invalid step value.")

    def test_invalid_step_value_negative(self):
        """Test ValueError when step value is negative."""
        with self.assertRaises(ValueError) as context:
            task_func(0, 10000, -100, 0.01)
        self.assertEqual(str(context.exception), "Invalid step value.")

    def test_plot_labels(self):
        """Test that plot labels are correct."""
        ax = task_func(0, 10000, 100, 0.01)
        self.assertEqual(ax.get_xlabel(), "Time")
        self.assertEqual(ax.get_ylabel(), "Value")

if __name__ == '__main__':
    unittest.main()