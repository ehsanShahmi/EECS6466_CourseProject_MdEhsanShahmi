import numpy as np
import unittest
from scipy.linalg import svd

# Provided prompt code
def task_func(rows=3, columns=2, seed=0):
    """
    Generate a matrix of random values with specified dimensions and perform Singular Value Decomposition (SVD) on it.

    Requirements:
    - numpy
    - scipy.linalg.svd

    Parameters:
    - rows (int): Number of rows for the random matrix. Default is 3.
    - columns (int): Number of columns for the random matrix. Default is 2.
    - seed (int, optional): Seed for the random number generator to ensure reproducibility. Default is None.

    Returns:
    tuple: A tuple containing three elements:
        - U (ndarray): The unitary matrix U.
        - s (ndarray): The singular values, sorted in descending order.
        - Vh (ndarray): The conjugate transpose of the unitary matrix V.

    Example:
    >>> U, s, Vh = task_func(3, 2, seed=42)
    >>> print('U shape:', U.shape)
    U shape: (3, 3)
    >>> print('s shape:', s.shape)
    s shape: (2,)
    >>> print('Vh shape:', Vh.shape)
    Vh shape: (2, 2)
    """

    np.random.seed(seed)
    matrix = np.random.rand(rows, columns)
    U, s, Vh = svd(matrix)

    return U, s, Vh

class TestTaskFunc(unittest.TestCase):
    
    def test_default_shape(self):
        U, s, Vh = task_func()
        self.assertEqual(U.shape, (3, 3))
        self.assertEqual(s.shape, (2,))
        self.assertEqual(Vh.shape, (2, 2))

    def test_custom_shape(self):
        U, s, Vh = task_func(rows=4, columns=3)
        self.assertEqual(U.shape, (4, 4))
        self.assertEqual(s.shape, (3,))
        self.assertEqual(Vh.shape, (3, 3))

    def test_seed_reproducibility(self):
        U1, s1, Vh1 = task_func(seed=42)
        U2, s2, Vh2 = task_func(seed=42)
        np.testing.assert_array_equal(U1, U2)
        np.testing.assert_array_equal(s1, s2)
        np.testing.assert_array_equal(Vh1, Vh2)

    def test_different_seed(self):
        U1, s1, Vh1 = task_func(seed=42)
        U2, s2, Vh2 = task_func(seed=100)
        self.assertFalse(np.array_equal(U1, U2))
        self.assertFalse(np.array_equal(s1, s2))
        self.assertFalse(np.array_equal(Vh1, Vh2))

    def test_negative_dimensions(self):
        with self.assertRaises(ValueError):
            task_func(rows=-3, columns=2)

if __name__ == '__main__':
    unittest.main()