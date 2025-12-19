import unittest
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Here is your prompt:
# def task_func(df1, df2, column1="feature1", column2="feature2"):
#     """Merge datasets, perform KMeans clustering, then return cluster labels and scatterplot.
#     (Function Definition is provided in the prompt but not to be modified)
#     ...
#     """
#     df = pd.merge(df1, df2, on="id")
#     X = df[[column1, column2]]
# 
#     kmeans = KMeans(n_clusters=2, n_init=10)
#     kmeans.fit(X)
#     labels = kmeans.labels_
# 
#     _, ax = plt.subplots()
#     ax.scatter(X[column1], X[column2], c=kmeans.labels_)
#     ax.set_xlabel(column1)
#     ax.set_ylabel(column2)
# 
#     return labels, ax

class TestTaskFunc(unittest.TestCase):

    def test_return_types(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [1.2, 3.4, 5.6]})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'feature2': [2.3, 4.5, 6.7]})
        labels, ax = task_func(df1, df2)
        self.assertIsInstance(labels, np.ndarray)
        self.assertIsInstance(ax, plt.Axes)

    def test_cluster_labels_length(self):
        df1 = pd.DataFrame({'id': [1, 2, 3, 4], 'feature1': [1.2, 2.3, 3.4, 4.5]})
        df2 = pd.DataFrame({'id': [1, 2, 3, 4], 'feature2': [5.6, 6.7, 7.8, 8.9]})
        labels, _ = task_func(df1, df2)
        self.assertEqual(len(labels), 4)

    def test_default_columns(self):
        df1 = pd.DataFrame({'id': [1, 2, 3], 'feature1': [10, 20, 30]})
        df2 = pd.DataFrame({'id': [1, 2, 3], 'feature2': [15, 25, 35]})
        labels, _ = task_func(df1, df2)
        self.assertTrue(np.all(np.isin(labels, [0, 1])))

    def test_custom_columns(self):
        df1 = pd.DataFrame({'id': [1, 2], 'custom1': [1, 2]})
        df2 = pd.DataFrame({'id': [1, 2], 'custom2': [3, 4]})
        labels, _ = task_func(df1, df2, column1="custom1", column2="custom2")
        self.assertTrue(np.all(np.isin(labels, [0, 1])))

    def test_no_merge_columns(self):
        df1 = pd.DataFrame({'id': [1, 2], 'feature1': [5, 10]})
        df2 = pd.DataFrame({'id': [3, 4], 'feature2': [15, 20]})
        with self.assertRaises(ValueError):
            task_func(df1, df2)

if __name__ == '__main__':
    unittest.main()