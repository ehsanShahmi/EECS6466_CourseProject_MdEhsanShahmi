import unittest
import numpy as np
from sklearn.cluster import KMeans

# Constants for configuration for the test
RANGE = 100
SIZE = 1000
CLUSTERS = 5

class TestTaskFunc(unittest.TestCase):

    def test_data_type(self):
        """Test to ensure that the data returned is a numpy array."""
        data, kmeans = task_func()
        self.assertIsInstance(data, np.ndarray)

    def test_data_shape(self):
        """Test to ensure that the shape of the data is (1000, 2)."""
        data, kmeans = task_func()
        self.assertEqual(data.shape, (SIZE, 2))

    def test_kmeans_instance(self):
        """Test to ensure that the kmeans object returned is an instance of KMeans."""
        data, kmeans = task_func()
        self.assertIsInstance(kmeans, KMeans)

    def test_number_of_clusters(self):
        """Test to ensure that the number of clusters is correct according to the constant."""
        data, kmeans = task_func()
        self.assertEqual(len(kmeans.cluster_centers_), CLUSTERS)

    def test_cluster_labels_length(self):
        """Test to ensure that the length of the cluster labels matches the number of data points."""
        data, kmeans = task_func()
        self.assertEqual(len(kmeans.labels_), SIZE)

# The following check allows the test suite to be run
if __name__ == '__main__':
    unittest.main()