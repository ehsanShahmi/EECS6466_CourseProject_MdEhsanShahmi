import numpy as np
from sklearn.preprocessing import MinMaxScaler
import unittest

def task_func(rows=3, columns=2, seed=42):
    """
    Generate a matrix of random values with specified dimensions and scale it between 0 and 1.
    
    Parameters:
    rows (int): The number of rows for the matrix. Default is 3.
    columns (int): The number of columns for the matrix. Default is 2.
    
    Returns:
    ndarray: A numpy ndarray with scaled values between 0 and 1.
    
    Requirements:
    - numpy
    - sklearn.preprocessing.MinMaxScaler
    
    Example:
    >>> task_func(3, 2)
    array([[0.37939383, 1.        ],
           [1.        , 0.55700635],
           [0.        , 0.        ]])
    
    >>> task_func(2, 2)
    array([[0., 1.],
           [1., 0.]])
    """
    np.random.seed(seed)  # Ensure reproducibility for consistent outputs across different runs
    matrix = np.random.rand(rows, columns)
    scaler = MinMaxScaler()
    scaled_matrix = scaler.fit_transform(matrix)

    return scaled_matrix

class TestTaskFunc(unittest.TestCase):
    def test_default_output_shape(self):
        result = task_func()
        self.assertEqual(result.shape, (3, 2), "Default output shape should be (3, 2)")

    def test_custom_output_shape(self):
        result = task_func(2, 3)
        self.assertEqual(result.shape, (2, 3), "Output shape should match the input dimensions (2, 3)")

    def test_output_values_range(self):
        result = task_func(5, 5)
        self.assertTrue(np.all(result >= 0) and np.all(result <= 1), "All output values should be in the range [0, 1]")

    def test_reproducibility(self):
        result1 = task_func(3, 2, seed=42)
        result2 = task_func(3, 2, seed=42)
        np.testing.assert_array_equal(result1, result2, "Outputs should be the same for the same seed")

    def test_non_negative_values(self):
        result = task_func(4, 4)
        self.assertTrue(np.all(result >= 0), "All values in the output should be non-negative")

if __name__ == '__main__':
    unittest.main()