import unittest
import pandas as pd
import matplotlib.pyplot as plt

COLUMNS = ['col1', 'col2', 'col3']

class TestTaskFunc(unittest.TestCase):

    def test_empty_data(self):
        """ Test with empty data """
        data = []
        analyzed_df, ax = task_func(data)
        self.assertTrue(analyzed_df.empty)
        self.assertIsInstance(ax, plt.Axes)

    def test_single_row_data(self):
        """ Test with a single row of data """
        data = [[1, 2, 3]]
        analyzed_df, ax = task_func(data)
        self.assertEqual(analyzed_df.shape[0], 1)
        self.assertEqual(analyzed_df.iloc[0]['col1'], 1)
        self.assertEqual(analyzed_df.iloc[0]['col2'], 2)
        self.assertEqual(analyzed_df.iloc[0]['col3'], 3)
        self.assertIsInstance(ax, plt.Axes)

    def test_duplicate_rows(self):
        """ Test with duplicate rows in the data """
        data = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        analyzed_df, ax = task_func(data)
        self.assertEqual(analyzed_df.shape[0], 1)  # Should only return one unique combination
        self.assertEqual(analyzed_df.iloc[0]['col3'], 3)
        self.assertIsInstance(ax, plt.Axes)
    
    def test_multiple_groups(self):
        """ Test with multiple groups in the data """
        data = [[1, 1, 1], [1, 1, 2], [2, 1, 1], [2, 2, 3]]
        analyzed_df, ax = task_func(data)
        self.assertEqual(analyzed_df.shape[0], 3)  # 3 unique combinations of col1 and col2
        self.assertIsInstance(ax, plt.Axes)

    def test_plot_labels(self):
        """ Test if the plot has correct labels """
        data = [[1, 1, 1], [2, 1, 2], [1, 2, 3]]
        analyzed_df, ax = task_func(data)
        self.assertEqual(ax.get_xlabel(), 'col1-col2')  # x-label should be 'col1-col2'
        self.assertEqual(ax.get_ylabel(), 'col3')        # y-label should be 'col3' 

if __name__ == '__main__':
    unittest.main()