import unittest
import numpy as np
from sklearn.cluster import KMeans

# Here is your prompt:

def task_func(data, n_clusters=2, random_state=0):
    """
    Perform KMeans clustering on a list of data points with 2D coordinates and 
    return the cluster labels.

    The function takes a list of tuples, each containing an identifier and its 
    2D coordinates. It applies KMeans clustering to categorize the points.

    Parameters:
    data (list of tuples): Each tuple contains an identifier and its 2D coordinates (e.g., ('A', 1, 1)).
    n_clusters (int): The number of clusters to form. Defaults to 2.
    random_state (int): Determines random number generation for centroid
                        initialization. Use an int for reproducible output.
                        Defaults to 0.

    Returns:
    ndarray: A numpy array with the cluster labels for each item.

    Requirements:
    - numpy
    - sklearn.cluster.KMeans

    Example:
    >>> data = [('A', 1, 1), ('B', 2, 2), ('C', 300, 300), ('D', 400, 400)]
    >>> labels = task_func(data, n_clusters=2, random_state=42)
    >>> print(labels)
    [0 0 1 1]
    
    >>> data = [('T1', 1, 1), ('T2', 1, 1.1), ('T2', 1.1, 1), ('C1', 400, 400), ('C2', 401, 401), ('B1', 35, 35)]
    >>> labels = task_func(data, n_clusters=3, random_state=42)
    >>> print(labels)
    [0 0 0 1 1 2]
    """

    items, x_values, y_values = zip(*data)
    coordinates = np.array(list(zip(x_values, y_values)))

    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state).fit(coordinates)
    labels = kmeans.labels_

    return labels

class TestTaskFunc(unittest.TestCase):

    def test_basic_clustering(self):
        data = [('A', 1, 1), ('B', 2, 2), ('C', 300, 300), ('D', 400, 400)]
        expected_labels = np.array([0, 0, 1, 1])
        labels = task_func(data, n_clusters=2, random_state=42)
        np.testing.assert_array_equal(labels, expected_labels)

    def test_multiple_clusters(self):
        data = [('T1', 1, 1), ('T2', 1, 1.1), 
                ('T3', 1.1, 1), 
                ('C1', 400, 400), ('C2', 401, 401), 
                ('B1', 35, 35)]
        expected_labels = np.array([0, 0, 0, 1, 1, 2])
        labels = task_func(data, n_clusters=3, random_state=42)
        np.testing.assert_array_equal(labels, expected_labels)

    def test_single_cluster(self):
        data = [('A', 1, 1), ('B', 1, 1), ('C', 1, 1)]
        expected_labels = np.array([0, 0, 0])
        labels = task_func(data, n_clusters=1, random_state=42)
        np.testing.assert_array_equal(labels, expected_labels)

    def test_random_state_effect(self):
        data = [('A', 1, 1), ('B', 2, 2), ('C', 3, 3)]
        labels_1 = task_func(data, n_clusters=2, random_state=42)
        labels_2 = task_func(data, n_clusters=2, random_state=0)
        self.assertFalse(np.array_equal(labels_1, labels_2), "Labels should differ with different random states.")

    def test_empty_data(self):
        data = []
        with self.assertRaises(ValueError):
            task_func(data, n_clusters=2)

if __name__ == '__main__':
    unittest.main()