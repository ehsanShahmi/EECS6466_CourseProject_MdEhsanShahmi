import pandas as pd
import numpy as np
import unittest
from sklearn.cluster import KMeans

# Here is your prompt:
def task_func(data, n_clusters=3, seed=None):
    """
    Perform K-Means clustering on the given DataFrame using the sklearn KMeans algorithm. 

    The function expects a DataFrame with numerical values, as KMeans cannot handle categorical data. 
    It applies standard KMeans clustering from the sklearn library to form clusters. The number of clusters is 
    configurable via the 'n_clusters' parameter, defaulting to 3. The Number of times the k-means algorithm is run with 
    different centroid seeds (n_init) is set to 10. The function returns an array of cluster labels 
    corresponding to each data point in the input as well as the fitted KMeans model.

    Parameters:
    data (pandas.DataFrame): A DataFrame consisting of only numerical data. Each row represents a distinct data point.
    n_clusters (int, optional): The number of clusters to form. Defaults to 3.
    seed (int, optional): The seed used for setting the random stat in the KMeans clustering algorith.
                          Used for making results reproducable.

    Returns:
    numpy.ndarray: An array of integers (cluster labels) corresponding to the input data. Each label is an integer 
                   representing the cluster to which a row of data has been assigned.
    sklearn.cluster.KMeans: The fitted KMeans Model.

    Raises:
    - ValueError: If the DataFrame contains non numeric entries.
    """

    if not data.apply(lambda s: pd.to_numeric(s, errors='coerce').notnull().all()).all():
        raise ValueError("DataFrame should only contain numeric values.")

    kmeans = KMeans(n_clusters=n_clusters, random_state=seed, n_init=10)
    kmeans.fit(data)

    return kmeans.labels_, kmeans

class TestKMeansClustering(unittest.TestCase):

    def setUp(self):
        self.data_numeric = pd.DataFrame(np.random.rand(10, 3), columns=['A', 'B', 'C'])
        self.data_numeric_large = pd.DataFrame(np.random.randint(0, 100, size=(100, 4)), columns=list('ABCD'))

    def test_kmeans_output_shape(self):
        labels, _ = task_func(self.data_numeric, n_clusters=3)
        self.assertEqual(labels.shape, (10,))

    def test_kmeans_default_n_clusters(self):
        labels, model = task_func(self.data_numeric)
        self.assertEqual(model.n_clusters, 3)

    def test_kmeans_custom_n_clusters(self):
        labels, model = task_func(self.data_numeric, n_clusters=5)
        self.assertEqual(model.n_clusters, 5)

    def test_kmeans_non_numeric_data(self):
        data_non_numeric = pd.DataFrame({
            'A': [1, 2, 3],
            'B': ['a', 'b', 'c']
        })
        with self.assertRaises(ValueError) as context:
            task_func(data_non_numeric)
        self.assertEqual(str(context.exception), "DataFrame should only contain numeric values.")

    def test_kmeans_seed_reproducibility(self):
        np.random.seed(12)
        labels1, model1 = task_func(self.data_numeric_large, n_clusters=4, seed=12)
        np.random.seed(12)
        labels2, model2 = task_func(self.data_numeric_large, n_clusters=4, seed=12)
        np.array_equal(labels1, labels2)

if __name__ == '__main__':
    unittest.main()