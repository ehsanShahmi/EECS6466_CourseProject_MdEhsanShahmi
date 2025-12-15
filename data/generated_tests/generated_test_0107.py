import pandas as pd
import unittest
from sklearn.exceptions import NotFittedError
import numpy as np
import matplotlib.pyplot as plt

# Here is your prompt:
def task_func(df, n_clusters=3, random_state=0):
    """
    Convert the 'date' column of a DataFrame to ordinal, perform KMeans clustering on 'date' and 'value' columns, and plot the clusters.

    Parameters:
        df (pandas.DataFrame): The DataFrame with columns 'group', 'date', and 'value'.
        n_clusters (int): The number of clusters for KMeans. Defaults to 3.
        random_state (int): Random state for KMeans to ensure reproducibility. Defaults to 0.


    Returns:
        matplotlib.axes.Axes: The Axes object containing the scatter plot of the clusters.

    Required names:
        x: 'Date (ordinal)'
        ylabel: 'Value'
        title: 'KMeans Clustering of Value vs Date'
    
    Raises:
        ValueError: If the DataFrame is empty or lacks required columns.

    Requirements:
        - pandas
        - sklearn.cluster
        - matplotlib.pyplot

    Example:
        >>> df = pd.DataFrame({
        ...     "group": ["A", "A", "A", "B", "B"],
        ...     "date": pd.to_datetime(["2022-01-02", "2022-01-13", "2022-02-01", "2022-02-23", "2022-03-05"]),
        ...     "value": [10, 20, 16, 31, 56],
        ... })
        >>> ax = task_func(df)
    """

    if df.empty or not all(col in df.columns for col in ['group', 'date', 'value']):
        raise ValueError("DataFrame must be non-empty and contain 'group', 'date', and 'value' columns.")

    if not pd.api.types.is_datetime64_any_dtype(df['date']):
        raise ValueError("'date' column must be in datetime format.")

    df['date'] = df['date'].apply(lambda x: x.toordinal())
    X = df[['date', 'value']]

    kmeans = KMeans(n_clusters=n_clusters, random_state=random_state)
    kmeans.fit(X)
    y_kmeans = kmeans.predict(X)

    fig, ax = plt.subplots()
    ax.scatter(X['date'], X['value'], c=y_kmeans, cmap='viridis')
    ax.set_title('KMeans Clustering of Value vs Date')
    ax.set_xlabel('Date (ordinal)')
    ax.set_ylabel('Value')

    return ax

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.df_valid = pd.DataFrame({
            "group": ["A", "A", "A", "B", "B"],
            "date": pd.to_datetime(["2022-01-02", "2022-01-13", "2022-02-01", "2022-02-23", "2022-03-05"]),
            "value": [10, 20, 16, 31, 56],
        })
        
    def test_valid_input(self):
        ax = task_func(self.df_valid)
        self.assertIsInstance(ax, plt.Axes)
        
    def test_empty_dataframe(self):
        empty_df = pd.DataFrame(columns=["group", "date", "value"])
        with self.assertRaises(ValueError) as e:
            task_func(empty_df)
        self.assertEqual(str(e.exception), "DataFrame must be non-empty and contain 'group', 'date', and 'value' columns.")
        
    def test_missing_columns(self):
        df_invalid = pd.DataFrame({
            "group": ["A", "A", "A"],
            "value": [10, 20, 16],
        })
        with self.assertRaises(ValueError) as e:
            task_func(df_invalid)
        self.assertEqual(str(e.exception), "DataFrame must be non-empty and contain 'group', 'date', and 'value' columns.")
        
    def test_non_datetime_date(self):
        df_invalid_date = pd.DataFrame({
            "group": ["A", "A", "A", "B", "B"],
            "date": ["2022-01-02", "2022-01-13", "not_a_date", "2022-02-23", "2022-03-05"],
            "value": [10, 20, 16, 31, 56],
        })
        with self.assertRaises(ValueError) as e:
            task_func(df_invalid_date)
        self.assertEqual(str(e.exception), "'date' column must be in datetime format.")

    def test_plot_output(self):
        ax = task_func(self.df_valid)
        self.assertEqual(ax.get_title(), 'KMeans Clustering of Value vs Date')
        self.assertEqual(ax.get_xlabel(), 'Date (ordinal)')
        self.assertEqual(ax.get_ylabel(), 'Value')

if __name__ == '__main__':
    unittest.main()