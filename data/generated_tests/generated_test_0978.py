import numpy as np
import pandas as pd
import unittest
from sklearn.decomposition import PCA


def task_func(array, seed=None):
    """
    Shuffles the columns of a numpy array randomly, performs Principal Component Analysis (PCA)
    to reduce the dimensionality to 2 principal components, and returns these components as a pandas DataFrame.

    Parameters:
    - array (numpy.ndarray): A 2D numpy array where each row is an observation and each column is a feature.
    - seed (int, optional): Seed for the random number generator. Defaults to None (not set).

    Returns:
    - pandas.DataFrame: DataFrame with columns 'PC1' and 'PC2' representing the two principal components.

    Raises:
    - ValueError: If the input array is not 2D.

    Requirements:
    - numpy
    - pandas
    - sklearn

    Note:
    - PCA reduction will default to the number of features if fewer than 2.
    - An named but empty DataFrame is returned for arrays without features or with empty content.

    Examples:
    >>> array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    >>> df = task_func(array, seed=42)
    >>> df["PC1"]
    0    5.59017
    1   -5.59017
    Name: PC1, dtype: float64
    >>> df.shape
    (2, 2)
    """

    if seed is not None:
        np.random.seed(seed)

    if not isinstance(array, np.ndarray) or len(array.shape) != 2:
        raise ValueError("Input must be a 2D numpy array.")

    if array.size == 0 or array.shape[1] == 0:
        return pd.DataFrame(columns=["PC1", "PC2"])

    shuffled_array = np.copy(array)
    np.random.shuffle(np.transpose(shuffled_array))

    n_components = min(2, shuffled_array.shape[1])
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(shuffled_array)

    column_labels = ["PC1", "PC2"][:n_components]
    df = pd.DataFrame(data=principal_components, columns=column_labels)

    return df


class TestTaskFunc(unittest.TestCase):

    def test_valid_input(self):
        array = np.array([[1, 2, 3], [4, 5, 6]])
        result = task_func(array)
        self.assertEqual(result.shape[1], 2)
        self.assertIn("PC1", result.columns)
        self.assertIn("PC2", result.columns)

    def test_empty_array(self):
        array = np.array([]).reshape(0, 0)  # No rows and columns
        result = task_func(array)
        self.assertTrue(result.empty)
        self.assertEqual(result.shape[1], 2)
        self.assertListEqual(result.columns.tolist(), ["PC1", "PC2"])

    def test_one_feature(self):
        array = np.array([[1], [2], [3]])
        result = task_func(array)
        self.assertEqual(result.shape[1], 1)
        self.assertIn("PC1", result.columns)
        self.assertNotIn("PC2", result.columns)

    def test_invalid_input_type(self):
        array = [[1, 2], [3, 4]]  # List instead of ndarray
        with self.assertRaises(ValueError) as context:
            task_func(array)
        self.assertEqual(str(context.exception), "Input must be a 2D numpy array.")

    def test_input_with_zero_columns(self):
        array = np.array([[], []])  # 2D with zero columns
        result = task_func(array)
        self.assertTrue(result.empty)
        self.assertEqual(result.shape[1], 2)
        self.assertListEqual(result.columns.tolist(), ["PC1", "PC2"])


if __name__ == '__main__':
    unittest.main()