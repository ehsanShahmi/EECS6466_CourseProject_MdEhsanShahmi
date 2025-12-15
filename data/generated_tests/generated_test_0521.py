import unittest
import pandas as pd
import matplotlib.pyplot as plt

class TestTaskFunc(unittest.TestCase):

    def test_valid_input(self):
        data = [{'John': 5, 'Jane': 10}, {'John': 6, 'Jane': 8}, {'John': 5, 'Jane': 9}]
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)

    def test_single_student(self):
        data = [{'Alice': 7}, {'Alice': 8}, {'Alice': 9}]
        ax = task_func(data)
        self.assertEqual(len(ax.lines), 1)
        self.assertEqual(ax.lines[0].get_label(), 'Alice')

    def test_multiple_students(self):
        data = [{'Amy': 15, 'Bob': 20}, {'Amy': 18, 'Bob': 19}, {'Amy': 16}]
        ax = task_func(data)
        self.assertEqual(len(ax.lines), 2)
        self.assertEqual(ax.lines[0].get_label(), 'Amy')
        self.assertEqual(ax.lines[1].get_label(), 'Bob')

    def test_missing_scores(self):
        data = [{'Charlie': 14}, {'Charlie': None}, {'Charlie': 16}]
        ax = task_func(data)
        self.assertEqual(len(ax.lines), 1)
        self.assertEqual(ax.lines[0].get_label(), 'Charlie')
        # Check if the second point is None (missing)
        self.assertTrue(pd.isna(ax.lines[0].get_xydata()[1][1]))

    def test_empty_input(self):
        data = []
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.lines), 0)  # No lines for empty input

if __name__ == '__main__':
    unittest.main()