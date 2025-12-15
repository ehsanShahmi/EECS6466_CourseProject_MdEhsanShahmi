import unittest
import numpy as np
import pandas as pd
import seaborn as sns
from scipy.stats import zscore

def task_func(data_matrix):
    """
    Calculate the Z-values of a 2D data matrix, calculate the mean value of each row and then visualize the correlation matrix of the Z-values with a heatmap.

    Parameters:
    data_matrix (numpy.array): The 2D data matrix of shape (m, n) where m is the number of rows and n is the number of columns.

    Returns:
    tuple: A tuple containing:
      - pandas.DataFrame: A DataFrame with columns 'Feature 1', 'Feature 2', ..., 'Feature n' containing the Z-scores (per matrix row).
                      There is also an additional column 'Mean' the mean of z-score per row.
      - matplotlib.axes.Axes: The Axes object of the plotted heatmap.

    Requirements:
    - pandas
    - seaborn
    - scipy.stats.zscore

    Example:
    >>> import numpy as np
    >>> data = np.array([[6, 8, 1, 3, 4], [-1, 0, 3, 5, 1]])
    >>> df, ax = task_func(data)
    >>> print(df)
       Feature 1  Feature 2  Feature 3  Feature 4  Feature 5          Mean
    0   0.662085   1.489691  -1.406930  -0.579324  -0.165521 -2.053913e-16
    1  -1.207020  -0.742781   0.649934   1.578410  -0.278543 -3.330669e-17
    """

    z_scores = zscore(data_matrix, axis=1)
    feature_columns = ["Feature " + str(i + 1) for i in range(data_matrix.shape[1])]
    df = pd.DataFrame(z_scores, columns=feature_columns)
    df["Mean"] = df.mean(axis=1)
    correlation_matrix = df.corr()
    ax = sns.heatmap(correlation_matrix, annot=True, fmt=".2f")
    return df, ax

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        data = np.array([[6, 8, 1, 3, 4], [-1, 0, 3, 5, 1]])
        df, ax = task_func(data)
        self.assertEqual(df.shape[1], 6)  # Check the number of columns (5 features + "Mean")

    def test_output_dataframe_shape(self):
        data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        df, ax = task_func(data)
        self.assertEqual(df.shape[0], 3)  # Check number of rows matches input

    def test_mean_computation(self):
        data = np.array([[1, 2, 3], [4, 5, 6]])
        df, ax = task_func(data)
        means = df['Mean'].values
        expected_means = [zscore([1, 2, 3]).mean(), zscore([4, 5, 6]).mean()]  # Calculate expected means
        np.testing.assert_almost_equal(means, expected_means, decimal=5)  # Check means are correct

    def test_columns_are_named_correctly(self):
        data = np.array([[10, 20, 30], [40, 50, 60]])
        df, ax = task_func(data)
        self.assertListEqual(list(df.columns[:-1]), ['Feature 1', 'Feature 2', 'Feature 3'])  # Check feature names

    def test_empty_data_matrix(self):
        data = np.empty((0, 5))
        df, ax = task_func(data)
        self.assertEqual(df.shape, (0, 6))  # Ensure correct shape for empty input

if __name__ == '__main__':
    unittest.main()