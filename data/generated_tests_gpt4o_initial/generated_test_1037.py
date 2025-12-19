import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import unittest

# Here is your prompt:
def task_func(s1, s2, n_clusters=3):
    """
    Perform K-Means clustering on data points from two pandas Series and visualize the clusters.

    Parameters:
    - s1 (pandas.Series): The first series of data. Each value in the series represents a data point's coordinate along one dimension.
    - s2 (pandas.Series): The second series of data. Each value corresponds to a data point's coordinate along another dimension. The length of s2 must match that of s1.
    - n_clusters (int, optional): The number of clusters to form as well as the number of centroids to generate. Defaults to 3.

    Returns:
    - tuple: A tuple containing the following elements:
        - ndarray: An array of cluster labels indicating the cluster each data point belongs to.
        - matplotlib.axes.Axes: The Axes object of the plot, which shows the data points colored according to their cluster labels.

    Raises:
    - ValueError: If either s1 or s2 is not a pandas Series, raise "s1 and s2 must be pandas Series"
    - ValueError: If s1 and s2 have different lengths, raise "s1 and s2 must have the same length"

    Requirements:
    - pandas
    - scikit-learn
    - matplotlib

    Notes:
    - The function needs to ensure that s1 and s2 are pandas Series of equal length. 
    - It then performs K-Means clustering on the combined data points from s1 and s2. 
    - After clustering, it creates a scatter plot where each cluster is visualized with a different color. 
    - The plot title is set to "K-Means Clustering" to describe the visualization technique. 
    - A legend is added, which uses elements from the scatter plot to describe each cluster.
        
    Example:
    >>> s1 = pd.Series(np.random.rand(100), name='feature1')
    >>> s2 = pd.Series(np.random.rand(100), name='feature2')
    >>> labels, ax = task_func(s1, s2, n_clusters=4)
    >>> print(ax.get_title())
    K-Means Clustering

    """
    if not isinstance(s1, pd.Series) or not isinstance(s2, pd.Series):
        raise ValueError("s1 and s2 must be pandas Series")

    if len(s1) != len(s2):
        raise ValueError("s1 and s2 must have the same length")

    # Create a DataFrame from the series
    df = pd.concat([s1, s2], axis=1)

    # Perform K-Means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = kmeans.fit_predict(df)

    # Visualize the clusters
    _, ax = plt.subplots()
    scatter = ax.scatter(df[s1.name], df[s2.name], c=labels)
    ax.set_xlabel(s1.name)
    ax.set_ylabel(s2.name)
    ax.set_title("K-Means Clustering")
    plt.legend(*scatter.legend_elements(), title="Clusters")

    return labels, ax


class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        self.s1_valid = pd.Series([1, 2, 3, 4, 5], name='feature1')
        self.s2_valid = pd.Series([5, 4, 3, 2, 1], name='feature2')
        self.s1_invalid = [1, 2, 3, 4, 5]
        self.s2_invalid = pd.Series([5, 4, 3])

    def test_valid_input(self):
        labels, ax = task_func(self.s1_valid, self.s2_valid, n_clusters=2)
        self.assertEqual(len(labels), len(self.s1_valid))
        self.assertEqual(ax.get_title(), "K-Means Clustering")

    def test_invalid_series_type(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.s1_invalid, self.s2_valid)
        self.assertEqual(str(context.exception), "s1 and s2 must be pandas Series")

    def test_different_length_series(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.s1_valid, self.s2_invalid)
        self.assertEqual(str(context.exception), "s1 and s2 must have the same length")

    def test_default_clusters(self):
        labels, ax = task_func(self.s1_valid, self.s2_valid)
        self.assertEqual(labels.max() + 1, 3)  # Check number of clusters (default is 3)

    def test_custom_clusters(self):
        n_clusters = 4
        labels, ax = task_func(self.s1_valid, self.s2_valid, n_clusters=n_clusters)
        self.assertEqual(labels.max() + 1, n_clusters)  # Check number of clusters matches input


if __name__ == '__main__':
    unittest.main()