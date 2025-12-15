import pandas as pd
from sklearn.cluster import DBSCAN
import unittest

# Here is your prompt:
def task_func(data, cols):
    """
    Perform DBSCAN clustering on the data by transforming it into a DataFrame and recording the clusters in a new column named 'Cluster'.
    Please choose the parameters eps=3 and min_samples=2.
    
    Parameters:
    - data (list): List of lists with the data, where the length of the inner list equals the number of columns
    - cols (list): List of column names
    
    Returns:
    - df (DataFrame): The DataFrame with a new 'Cluster' column.
    
    Requirements:
    - pandas
    - sklearn
    """
    df = pd.DataFrame(data, columns=cols)
    dbscan = DBSCAN(eps=3, min_samples=2)
    df['Cluster'] = dbscan.fit_predict(df)
    return df

class TestTaskFunc(unittest.TestCase):

    def test_basic_clustering(self):
        data = [[5.1, 3.5], [4.9, 3.0], [4.7, 3.2]]
        cols = ['x', 'y']
        df = task_func(data, cols)
        expected_clusters = [0, 0, 0]
        pd.testing.assert_series_equal(df['Cluster'], pd.Series(expected_clusters))

    def test_two_clusters(self):
        data = [[1, 1], [1, 2], [5, 5], [5, 6]]
        cols = ['x', 'y']
        df = task_func(data, cols)
        cluster_values = df['Cluster'].unique()
        self.assertEqual(len(cluster_values), 2)

    def test_single_point(self):
        data = [[1, 1]]
        cols = ['x', 'y']
        df = task_func(data, cols)
        expected_clusters = [-1]  # Single point should be in noise
        pd.testing.assert_series_equal(df['Cluster'], pd.Series(expected_clusters))

    def test_empty_data(self):
        data = []
        cols = ['x', 'y']
        df = task_func(data, cols)
        self.assertTrue(df.empty)

    def test_all_points_noise(self):
        data = [[10, 10], [12, 12], [14, 14]]
        cols = ['x', 'y']
        df = task_func(data, cols)
        expected_clusters = [-1, -1, -1]  # All points should be classified as noise
        pd.testing.assert_series_equal(df['Cluster'], pd.Series(expected_clusters))

# To run the tests
if __name__ == '__main__':
    unittest.main()