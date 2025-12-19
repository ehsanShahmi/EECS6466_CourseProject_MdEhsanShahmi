import unittest
import pandas as pd
import numpy as np

# Here is your prompt:
# (Provided code remains unchanged and intact, as per instructions)

def task_func(array: list, random_seed: int = 42) -> (pd.DataFrame, np.ndarray):
    """
    Converts a 2D list into a pandas DataFrame and applies PCA for dimensionality reduction.

    This function creates a DataFrame from the provided 2D list and then applies PCA to reduce the dataset
    to its two main components. The function uses a fixed random seed to ensure reproducibility.

    Parameters:
    - array (list of list of int): A 2D list representing data rows and columns.
    - random_seed (int, optional): The seed for the random number generator. Default is 42.

    Returns:
    - pd.DataFrame: The original data in DataFrame format.
    - np.ndarray: The data after PCA transformation.

    Requirements:
    - pandas
    - numpy
    - sklearn.decomposition.PCA

    Examples:
    >>> data = [[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]]
    >>> df, transformed = task_func(data)
    >>> print(df)
        0   1   2   3   4
    0   1   2   3   4   5
    1   6   7   8   9  10
    2  11  12  13  14  15
    >>> print(transformed[:, 0])
    [ 11.18033989  -0.         -11.18033989]
    """

    df = pd.DataFrame(array)

    pca = PCA(n_components=2, random_state=random_seed)
    transformed_data = pca.fit_transform(df)

    return df, transformed_data


class TestTaskFunc(unittest.TestCase):

    def test_basic_case(self):
        data = [[1, 2, 3, 4, 5], 
                [6, 7, 8, 9, 10], 
                [11, 12, 13, 14, 15]]
        df, transformed = task_func(data)
        expected_df = pd.DataFrame(data)
        expected_shape = (3, 2)  # Expecting two components from PCA
        
        pd.testing.assert_frame_equal(df, expected_df)
        self.assertEqual(transformed.shape, expected_shape)

    def test_empty_case(self):
        data = []
        df, transformed = task_func(data)
        expected_df = pd.DataFrame(data)
        expected_shape = (0, 2)
        
        pd.testing.assert_frame_equal(df, expected_df)
        self.assertEqual(transformed.shape, expected_shape)

    def test_single_row(self):
        data = [[1, 2, 3, 4, 5]]
        df, transformed = task_func(data)
        expected_df = pd.DataFrame(data)
        expected_shape = (1, 2)  # PCA should still output components even for a single row
        
        pd.testing.assert_frame_equal(df, expected_df)
        self.assertEqual(transformed.shape, expected_shape)

    def test_identical_rows(self):
        data = [[1, 1, 1, 1, 1], 
                [1, 1, 1, 1, 1], 
                [1, 1, 1, 1, 1]]
        df, transformed = task_func(data)
        expected_df = pd.DataFrame(data)
        expected_shape = (3, 2)  # PCA on identical rows will show 0 variance
        
        pd.testing.assert_frame_equal(df, expected_df)
        self.assertEqual(transformed.shape, expected_shape)
        np.testing.assert_array_equal(transformed, np.zeros((3, 2)))

    def test_large_numbers(self):
        data = [[1e10, 2e10, 3e10, 4e10, 5e10], 
                [6e10, 7e10, 8e10, 9e10, 10e10], 
                [11e10, 12e10, 13e10, 14e10, 15e10]]
        df, transformed = task_func(data)
        expected_df = pd.DataFrame(data)
        expected_shape = (3, 2)
        
        pd.testing.assert_frame_equal(df, expected_df)
        self.assertEqual(transformed.shape, expected_shape)


if __name__ == "__main__":
    unittest.main()