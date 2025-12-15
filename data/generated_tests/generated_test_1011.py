import unittest
import pandas as pd
import os
import matplotlib.pyplot as plt

class TestTaskFunc(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Set up a temporary CSV file for testing
        cls.test_csv_path = "test_data.csv"
        data = {
            'column1': ['A', 'B', 'A', 'B', 'C'],
            'column2': [10, 20, 30, 40, 50]
        }
        df = pd.DataFrame(data)
        df.to_csv(cls.test_csv_path, index=False)

    @classmethod
    def tearDownClass(cls):
        # Remove the temporary file after testing
        if os.path.exists(cls.test_csv_path):
            os.remove(cls.test_csv_path)

    def test_task_func_valid_input(self):
        ax = task_func(self.test_csv_path, 'column1', 'column2')
        self.assertEqual(ax.get_title(), "Mean of column2 Grouped by column1")
        self.assertEqual(ax.get_xlabel(), 'column1')
        self.assertEqual(ax.get_ylabel(), 'Mean of column2')
        # Check that the right number of bars are present
        self.assertEqual(len(ax.patches), 3)  # 'A', 'B', 'C'

    def test_task_func_default_columns(self):
        ax = task_func(self.test_csv_path)
        self.assertEqual(ax.get_title(), "Mean of column2 Grouped by column1")
        self.assertEqual(ax.get_xlabel(), 'column1')
        self.assertEqual(ax.get_ylabel(), 'Mean of column2')

    def test_task_func_grouping(self):
        ax = task_func(self.test_csv_path, 'column1', 'column2')
        # Validate that the means are correct
        expected_means = {'A': 20.0, 'B': 30.0, 'C': 50.0}
        for patch in ax.patches:
            label = patch.get_x() + patch.get_width() / 2
            mean_value = patch.get_height()
            corresponding_group = ax.get_xticks()[int(label)]
            self.assertAlmostEqual(mean_value, expected_means[corresponding_group])

    def test_task_func_invalid_csv_path(self):
        with self.assertRaises(FileNotFoundError):
            task_func("invalid_path.csv")

    def test_task_func_missing_column(self):
        df = pd.DataFrame({'columnX': [1, 2, 3], 'columnY': [4, 5, 6]})
        df.to_csv(self.test_csv_path, index=False)
        with self.assertRaises(KeyError):
            task_func(self.test_csv_path, 'column1', 'column2')  # 'column1' doesn't exist


if __name__ == '__main__':
    unittest.main()