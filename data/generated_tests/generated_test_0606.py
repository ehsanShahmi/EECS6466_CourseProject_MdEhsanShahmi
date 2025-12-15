import pandas as pd
import numpy as np
import unittest
from scipy import stats

def task_func(matrix):
    """
    Normalizes a 2D numeric array (matrix) using the Z score.
    
    Parameters:
    matrix (array): The 2D numpy array.
    
    Returns:
    DataFrame: The normalized DataFrame.

    Requirements:
    - pandas
    - numpy
    - scipy
    """

    df = pd.DataFrame(matrix)
    normalized_df = df.apply(stats.zscore)
    # Handle NaN values by replacing them with 0.0
    normalized_df = normalized_df.fillna(0.0)
    return normalized_df

class TestTaskFunc(unittest.TestCase):

    def test_normalization_shape(self):
        matrix = np.array([[1, 2], [3, 4]])
        normalized_df = task_func(matrix)
        self.assertEqual(normalized_df.shape, (2, 2))

    def test_normalization_contents(self):
        matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        normalized_df = task_func(matrix)
        self.assertTrue(np.allclose(normalized_df.mean(axis=0), 0))
        self.assertTrue(np.allclose(normalized_df.std(ddof=0), 1))

    def test_empty_matrix(self):
        matrix = np.array([[]])
        normalized_df = task_func(matrix)
        self.assertEqual(normalized_df.shape, (1, 0))

    def test_nan_values(self):
        matrix = np.array([[1, 2, np.nan], [4, 5, 6], [np.nan, 8, 9]])
        normalized_df = task_func(matrix)
        self.assertTrue(np.all(np.isfinite(normalized_df.values)))

    def test_single_value_matrix(self):
        matrix = np.array([[42]])
        normalized_df = task_func(matrix)
        self.assertTrue(np.allclose(normalized_df.values, 0))

if __name__ == '__main__':
    unittest.main()