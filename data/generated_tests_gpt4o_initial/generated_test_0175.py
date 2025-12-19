import unittest
import pandas as pd
import matplotlib.pyplot as plt
from your_module import task_func  # Replace 'your_module' with the actual module name where task_func is defined.

class TestTaskFunc(unittest.TestCase):

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['Title', 'Views', 'Likes'])
        ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.has_data(), False)

    def test_dataframe_missing_columns(self):
        df = pd.DataFrame(columns=['Title', 'Likes'])  # Missing 'Views'
        ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.has_data(), False)

    def test_no_matching_titles(self):
        data = {'Title': ['Tutorial', 'Learning Python'], 'Views': [1000, 2000], 'Likes': [100, 200]}
        df = pd.DataFrame(data)
        ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.has_data(), False)

    def test_valid_dataframe(self):
        data = {'Title': ['How to code', 'What is Python', 'Tutorial'], 'Views': [1500, 1200, 1000], 'Likes': [150, 300, 100]}
        df = pd.DataFrame(data)
        ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())
        self.assertIn('How to code', ax.get_xticks())
        self.assertIn('What is Python', ax.get_xticks())

    def test_large_values(self):
        data = {'Title': ['How to code', 'What is Python'], 'Views': [10**6, 10**6], 'Likes': [10**5, 5*10**5]}
        df = pd.DataFrame(data)
        ax = task_func(df)
        self.assertIsInstance(ax, plt.Axes)
        self.assertTrue(ax.has_data())
        self.assertAlmostEqual(ax.patches[0].get_height(), 0.1)  # Check first like ratio
        self.assertAlmostEqual(ax.patches[1].get_height(), 0.5)  # Check second like ratio

if __name__ == '__main__':
    unittest.main()