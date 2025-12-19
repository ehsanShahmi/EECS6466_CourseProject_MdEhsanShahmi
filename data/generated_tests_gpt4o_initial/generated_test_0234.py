import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import unittest

# Here is your prompt:
# (The task_func is not provided as per the instructions)

class TestTaskFunction(unittest.TestCase):

    def test_valid_input(self):
        data = pd.DataFrame([{'Name': 'Alice', 'Age': 20, 'Score': 70}, 
                             {'Name': 'Bob', 'Age': 25, 'Score': 75}, 
                             {'Name': 'Eve', 'Age': 30, 'Score': 80}])
        plt, ax = task_func(data)
        self.assertIsNotNone(ax)
        self.assertEqual(ax.lines[0].get_xdata()[0], 20)

    def test_duplicate_names(self):
        data = pd.DataFrame([{'Name': 'Alice', 'Age': 20, 'Score': 70}, 
                             {'Name': 'Alice', 'Age': 25, 'Score': 75}, 
                             {'Name': 'Eve', 'Age': 30, 'Score': 80}])
        plt, ax = task_func(data)
        self.assertEqual(len(ax.collections[0].get_offsets()), 2)

    def test_empty_dataframe(self):
        data = pd.DataFrame(columns=['Name', 'Age', 'Score'])
        with self.assertRaises(ValueError):
            task_func(data)

    def test_non_dataframe_input(self):
        with self.assertRaises(ValueError):
            task_func("This is not a DataFrame")

    def test_plot_properties(self):
        data = pd.DataFrame([{'Name': 'Alice', 'Age': 20, 'Score': 70}, 
                             {'Name': 'Bob', 'Age': 25, 'Score': 75}, 
                             {'Name': 'Eve', 'Age': 30, 'Score': 80}])
        plt, ax = task_func(data)
        self.assertEqual(ax.get_xlabel(), 'Age')
        self.assertEqual(ax.get_ylabel(), 'Score')
        self.assertEqual(ax.get_title(), 'Linear Regression')

if __name__ == '__main__':
    unittest.main()