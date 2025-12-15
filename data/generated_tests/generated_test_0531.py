import unittest
import pandas as pd
from collections import Counter
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

from your_module import task_func  # Replace 'your_module' with the name of your Python file

class TestTaskFunc(unittest.TestCase):

    def test_no_duplicates(self):
        df = pd.DataFrame({
            'x': [1, 2, 3],
            'y': [1, 2, 3]
        })
        duplicates, df_clustered, ax = task_func(df)
        expected_duplicates = Counter()
        expected_df = pd.DataFrame({'x': [1, 2, 3], 'y': [1, 2, 3], 'cluster': [0, 1, 2]})
        
        self.assertEqual(duplicates, expected_duplicates)
        pd.testing.assert_frame_equal(df_clustered.reset_index(drop=True), expected_df.reset_index(drop=True))

    def test_with_duplicates(self):
        df = pd.DataFrame({
            'x': [1, 2, 2, 3],
            'y': [1, 1, 1, 3]
        })
        duplicates, df_clustered, ax = task_func(df)
        expected_duplicates = Counter({(2, 1): 2})
        expected_df = pd.DataFrame({'x': [1, 2, 3], 'y': [1, 1, 3], 'cluster': [1, 0, 2]})
        
        self.assertEqual(duplicates, expected_duplicates)
        pd.testing.assert_frame_equal(df_clustered.reset_index(drop=True), expected_df.reset_index(drop=True))

    def test_more_clusters_than_points(self):
        df = pd.DataFrame({
            'x': [1, 2],
            'y': [1, 2]
        })
        duplicates, df_clustered, ax = task_func(df, n_clusters=4)
        expected_duplicates = Counter()
        expected_df = pd.DataFrame({'x': [1, 2], 'y': [1, 2], 'cluster': [0, 1]})
        
        self.assertEqual(duplicates, expected_duplicates)
        pd.testing.assert_frame_equal(df_clustered.reset_index(drop=True), expected_df.reset_index(drop=True))

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['x', 'y'])
        duplicates, df_clustered, ax = task_func(df)
        expected_duplicates = Counter()
        expected_df = pd.DataFrame(columns=['x', 'y', 'cluster'])

        self.assertEqual(duplicates, expected_duplicates)
        pd.testing.assert_frame_equal(df_clustered.reset_index(drop=True), expected_df.reset_index(drop=True))

    def test_random_state_effect(self):
        df = pd.DataFrame({
            'x': [1, 1, 1, 1],
            'y': [1, 2, 3, 4]
        })
        duplicates1, df_clustered1, ax1 = task_func(df, random_state=42)
        duplicates2, df_clustered2, ax2 = task_func(df, random_state=24)

        # Expect different cluster assignments due to different random states
        self.assertNotEqual(df_clustered1['cluster'].tolist(), df_clustered2['cluster'].tolist())

if __name__ == '__main__':
    unittest.main()