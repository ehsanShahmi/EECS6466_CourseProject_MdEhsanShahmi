import unittest
import numpy as np
from sklearn.cluster import KMeans

def task_func(data, n_clusters):
    """
    Apply KMeans clustering to a 2D numeric array and find the indices of the data points in each cluster.

    Parameters:
    data (numpy array): The 2D numpy array for clustering.
    n_clusters (int): The number of clusters to form.

    Returns:
    dict: A dictionary where keys are cluster labels and values are lists of indices for data points in the cluster.
    """
    kmeans = KMeans(n_clusters=n_clusters).fit(data)
    labels = kmeans.labels_
    clusters = {i: np.where(labels == i)[0] for i in range(n_clusters)}
    return clusters

class TestTaskFunc(unittest.TestCase):
    
    def test_two_clusters(self):
        data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        cluster = task_func(data, 2)
        cluster_list = list(cluster.values())
        cluster_list.sort(key=lambda x: x[0])
        expected = [np.array([0, 1]), np.array([2, 3])]
        self.assertEqual(cluster_list, expected)

    def test_two_clusters_same_points(self):
        data = np.array([[1, 1], [2, 2]])
        cluster = task_func(data, 2)
        cluster_list = list(cluster.values())
        cluster_list.sort(key=lambda x: x[0])
        expected = [np.array([0]), np.array([1])]
        self.assertEqual(cluster_list, expected)
        
    def test_more_clusters_than_points(self):
        data = np.array([[1, 1], [2, 2], [3, 3]])
        cluster = task_func(data, 5)
        cluster_list = list(cluster.values())
        expected = [np.array([0]), np.array([1]), np.array([2])]
        self.assertEqual(sorted(cluster_list, key=lambda x: x[0]), expected)

    def test_single_cluster(self):
        data = np.array([[1, 1], [1, 1], [1, 1]])
        cluster = task_func(data, 1)
        self.assertEqual(list(cluster.values()), [np.array([0, 1, 2])])

    def test_high_dimensional_data(self):
        data = np.array([[1, 2, 3], [1, 2, 4], [10, 10, 10], [10, 10, 11]])
        cluster = task_func(data, 2)
        cluster_list = list(cluster.values())
        self.assertEqual(len(cluster_list), 2)

if __name__ == '__main__':
    unittest.main()