import unittest
import pandas as pd
import numpy as np
import seaborn as sns

# Here begins the suite of test cases for the provided prompt
class TestTaskFunction(unittest.TestCase):

    def test_basic_description(self):
        df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7.0, np.nan, 9.0]], columns=["c1", "c2", "c3"])
        description, plots = task_func(df)
        self.assertEqual(description.loc['count'].sum(), 9.0)
        self.assertAlmostEqual(description.loc['mean', 'c1'], 4.0)
        self.assertAlmostEqual(description.loc['mean', 'c2'], 3.5)
        self.assertAlmostEqual(description.loc['mean', 'c3'], 6.0)

    def test_nan_handling(self):
        df = pd.DataFrame([[np.nan, np.nan, np.nan], [4, 5, 6], [7.0, np.nan, 9.0]], columns=["c1", "c2", "c3"])
        description, plots = task_func(df)
        self.assertEqual(description.loc['count', 'c1'], 2.0)
        self.assertEqual(description.loc['count', 'c2'], 2.0)
        self.assertEqual(description.loc['count', 'c3'], 2.0)

    def test_different_data_types(self):
        df = pd.DataFrame([[1, 'a', 3], [4, 'b', 6], [7.0, 'c', 9.0]], columns=["c1", "c2", "c3"])
        description, plots = task_func(df)
        self.assertIn('c1', description.index)
        self.assertIn('c3', description.index)
        self.assertNotIn('c2', description.index)

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=["c1", "c2", "c3"])
        description, plots = task_func(df)
        self.assertEqual(description.empty, True)

    def test_plot_count(self):
        df = pd.DataFrame([[1, 2, np.nan], [4, 5, 6], [7, 8, 9]], columns=["c1", "c2", "c3"])
        description, plots = task_func(df)
        self.assertEqual(len(plots), 2)  # c1 and c2 are numeric columns

# This would allow test execution
if __name__ == '__main__':
    unittest.main()