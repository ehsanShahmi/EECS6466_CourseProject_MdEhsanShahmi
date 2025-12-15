import pandas as pd
from sklearn.cluster import KMeans
import unittest

def task_func(x_list, y_list, n_clusters=2, random_state=0):
    """
    Perform K-Means clustering on the given data by first turning it into a DataFrame with two columns "x" and "y" and then return the labels and centroids.

    Parameters:
    - x_list (list): List of data corresponding to 'x'
    - y_list (list): List of data corresponding to 'y'
    - n_clusters (int): Number of clusters to form, default to 2
    - random_state (int): Initial random state of k-means, default to 0

    Returns:
    tuple: The labels and centroids as numpy arrays.
        - kmeans.labels_: A NumPy array where each element is the cluster label assigned to each data point. 
        - kmeans.cluster_centers_: A NumPy array containing the coordinates of the cluster centers.

    Requirements:
    - pandas
    - sklearn

    Example:
    >>> df = pd.DataFrame({'x': [1, 2, 3, 4, 5, 6], 'y': [2, 3, 4, 5, 6, 7]})
    >>> labels, centroids = task_func([1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], 2, 0)
    """

    df = pd.DataFrame({'x': x_list, 'y': y_list})
    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state).fit(df)
    return kmeans.labels_, kmeans.cluster_centers_

class TestKMeansClustering(unittest.TestCase):

    def test_basic_functionality(self):
        labels, centroids = task_func([1, 2, 3, 4, 5, 6], [2, 3, 4, 5, 6, 7], 2, 0)
        expected_labels = [0, 0, 0, 1, 1, 1]  # Expected output may vary
        self.assertEqual(len(labels), 6)
        self.assertEqual(len(centroids), 2)
        self.assertTrue(all(label in [0, 1] for label in labels))

    def test_different_clusters(self):
        labels, centroids = task_func([1, 3, 5, 7], [2, 4, 6, 8], n_clusters=2)
        self.assertEqual(len(set(labels)), 2)  # Check if there are 2 unique labels

    def test_single_cluster(self):
        labels, centroids = task_func([1, 2, 3], [1, 2, 3], n_clusters=1)
        self.assertEqual(len(set(labels)), 1)  # Check if there is only 1 unique label

    def test_random_state_effect(self):
        labels1, _ = task_func([1, 2, 3, 4], [1, 2, 1, 2], n_clusters=2, random_state=42)
        labels2, _ = task_func([1, 2, 3, 4], [1, 2, 1, 2], n_clusters=2, random_state=24)
        self.assertFalse(all(label1 == label2 for label1, label2 in zip(labels1, labels2)))

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            task_func([], [])

if __name__ == '__main__':
    unittest.main()