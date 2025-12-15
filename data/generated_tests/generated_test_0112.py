import pandas as pd
import matplotlib.pyplot as plt
import unittest

class TestTaskFunc(unittest.TestCase):

    def test_valid_dataframe(self):
        df = pd.DataFrame({'Status': ['Pending', 'Completed', 'In Progress', 'Cancelled']})
        ax = task_func(df)
        self.assertEqual(ax.get_title(), 'Status Distribution')

    def test_pie_chart_generation(self):
        df = pd.DataFrame({'Status': ['Pending', 'Completed', 'In Progress', 'Cancelled', 'Completed', 'Pending']})
        ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(len(ax.patches) > 0)  # Check that pie chart has created slices

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['Status'])
        with self.assertRaises(ValueError):
            task_func(df)

    def test_invalid_column(self):
        df = pd.DataFrame({'Other': ['Pending', 'Completed']})
        with self.assertRaises(ValueError):
            task_func(df)

    def test_non_dataframe_input(self):
        with self.assertRaises(ValueError):
            task_func("I am not a DataFrame")

if __name__ == '__main__':
    unittest.main()