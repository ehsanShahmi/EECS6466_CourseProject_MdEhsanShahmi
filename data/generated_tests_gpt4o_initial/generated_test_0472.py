import unittest
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def task_func(myList, n_clusters):
    """
    Cluster a list of 2D points using KMeans and visualize the clusters.

    Note: This function raises ValueError if it encounters invalid inputs.
    KMeans is performed with random_state = 42 and n_init = 10. Scatterplot
    uses red 'x' markers for cluster centers.

    Parameters:
    - myList (list): List of 2D points.
    - n_clusters (int): Number of clusters to form.

    Returns:
    - matplotlib.axes._axes.Axes: Axes object with the plotted clusters.
    """
    if not myList or n_clusters <= 0:
        raise ValueError("Invalid inputs")

    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    kmeans.fit(myList)

    fig, ax = plt.subplots()
    ax.scatter(*zip(*myList), c=kmeans.labels_)
    ax.scatter(*zip(*kmeans.cluster_centers_), marker="x", color="red")
    return ax


class TestTaskFunc(unittest.TestCase):
    
    def test_valid_input_2_clusters(self):
        myList = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
        ax = task_func(myList, 2)
        self.assertIsInstance(ax, plt.Axes)
        
    def test_valid_input_3_clusters(self):
        myList = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
        ax = task_func(myList, 3)
        self.assertIsInstance(ax, plt.Axes)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            task_func([], 2)

    def test_non_positive_cluster_count(self):
        myList = [[1, 2], [3, 4]]
        with self.assertRaises(ValueError):
            task_func(myList, 0)

    def test_invalid_point_format(self):
        myList = [[1, 2], [3]]
        with self.assertRaises(ValueError):
            task_func(myList, 2)

if __name__ == '__main__':
    unittest.main()