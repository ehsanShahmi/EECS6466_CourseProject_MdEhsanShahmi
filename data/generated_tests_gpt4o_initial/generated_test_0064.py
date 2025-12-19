import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import unittest

# Constants
COLUMNS = ['col1', 'col2', 'col3']

def task_func(data):
    df = pd.DataFrame(data, columns=COLUMNS)
    analyzed_df = df.groupby(COLUMNS[:-1])[COLUMNS[-1]].nunique().reset_index()
    analyzed_df = analyzed_df.pivot(index=COLUMNS[0], columns=COLUMNS[1], values=COLUMNS[2])
    ax = sns.heatmap(analyzed_df, annot=True)
    plt.show()
    return analyzed_df, ax

class TestTaskFunc(unittest.TestCase):

    def test_empty_data(self):
        data = []
        analyzed_df, ax = task_func(data)
        self.assertTrue(analyzed_df.empty)
        
    def test_single_row_data(self):
        data = [[1, 1, 1]]
        analyzed_df, ax = task_func(data)
        self.assertEqual(analyzed_df.shape, (1, 1))
        self.assertEqual(analyzed_df.iloc[0, 0], 1)

    def test_multiple_rows_same_group(self):
        data = [[1, 1, 1], [1, 1, 1], [1, 1, 2]]
        analyzed_df, ax = task_func(data)
        self.assertEqual(analyzed_df.shape, (1, 1))
        self.assertEqual(analyzed_df.iloc[0, 0], 2)

    def test_multiple_groups(self):
        data = [[1, 1, 1], [1, 1, 2], [1, 2, 3], [2, 1, 1], [2, 2, 3]]
        analyzed_df, ax = task_func(data)
        self.assertEqual(analyzed_df.shape, (2, 2))
        self.assertTrue((1, 1) in analyzed_df.index)
        self.assertTrue((2, 1) in analyzed_df.index)

    def test_inconsistent_data_length(self):
        data = [[1, 1], [1, 1, 1], [1, 2, 3]]
        with self.assertRaises(ValueError):
            task_func(data)

if __name__ == '__main__':
    unittest.main()