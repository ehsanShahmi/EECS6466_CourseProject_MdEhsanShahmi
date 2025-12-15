from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import unittest

def task_func(df, age: int, height: int):
    """
    Filters the input DataFrame based on specified 'Age' and 'Height' conditions and applies KMeans clustering.
    - If the filtered dataframe has less than 3  columns, add to it a column 'Cluster' with 0 for each row.
    - Otherwise, do a KMeans clustering (by Age and Height) with 3 clusters and add a column 'Cluster' to the dataframe which corresponds to the cluster
    index of the cluster to which each row belongs to.
    - Plot a scatter plot of the 'Age' and 'height' and colored by the cluster indices.
    - the xlabel should be 'Age', the ylabel 'Height' and the title 'KMeans Clustering based on Age and Height'.

    Parameters:
    df (DataFrame): The text to analyze.
    age (int): Filter out the rows of the dataframe which 'Age' value is less than or equal to this value.
    height (int): Filter out the rows of the dataframe which 'Height' value is greater than or equal to this value.

    Returns:
    DataFrame: The filtered dataframe with the new column.
    matplotlib.axes.Axes: The Axes object of the plotted data. If no KMeans was done, returns None.

    Requirements:
    - sklearn
    - matplotlib

    Example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({
    ...     'Age': [30, 45, 60, 75],
    ...     'Height': [160, 170, 165, 190],
    ...     'Weight': [55, 65, 75, 85]
    ... })
    >>> selected_df, ax = task_func(df, 50, 180)
    >>> print(selected_df)
       Age  Height  Weight  Cluster
    2   60     165      75        0
    """

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.df = pd.DataFrame({
            'Age': [30, 45, 60, 75],
            'Height': [160, 170, 165, 190],
            'Weight': [55, 65, 75, 85]
        })

    def test_empty_dataframe(self):
        empty_df = pd.DataFrame(columns=['Age', 'Height', 'Weight'])
        result_df, ax = task_func(empty_df, 20, 200)
        self.assertTrue(result_df.empty)
        self.assertIsNone(ax)

    def test_no_rows_meeting_criteria(self):
        result_df, ax = task_func(self.df, 80, 150)
        self.assertEqual(len(result_df), 0)
        self.assertIsNone(ax)

    def test_few_rows_meeting_criteria(self):
        result_df, ax = task_func(self.df, 50, 180)
        self.assertEqual(len(result_df), 1)
        self.assertEqual(result_df["Cluster"].iloc[0], 0)
        self.assertIsNone(ax)

    def test_kmeans_clustering(self):
        result_df, ax = task_func(self.df, 25, 180)
        self.assertGreater(len(result_df), 1)
        self.assertIn("Cluster", result_df.columns)
        self.assertIsNotNone(ax)

    def test_plot_labels(self):
        result_df, ax = task_func(self.df, 20, 180)
        self.assertEqual(ax.get_xlabel(), "Age")
        self.assertEqual(ax.get_ylabel(), "Height")
        self.assertEqual(ax.get_title(), "KMeans Clustering based on Age and Height")


if __name__ == '__main__':
    unittest.main()