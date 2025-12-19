import numpy as np
import unittest

# Here is your prompt:
import numpy as np
import itertools

def task_func(dimension, seed=42):
    """
    Create a 2D numeric array (matrix) of a given dimension with random integers between 1 and 100, 
    and a flat list of all elements in the matrix.

    Parameters:
    - dimension (int): The dimension of the square matrix to be created. It must be a positive integer.

    Returns:
    tuple: A tuple containing:
        - A 2D numpy array of the given dimension with random integers between 1 and 100.
        - A flat list of all elements in the matrix.

    Requirements:
    - numpy
    - itertools

    Example:
    >>> matrix, flat_list = task_func(3)
    >>> print(matrix)
    [[52 93 15]
     [72 61 21]
     [83 87 75]]
    >>> print(flat_list)
    [52, 93, 15, 72, 61, 21, 83, 87, 75]
    """

    np.random.seed(seed)  # Ensure reproducible results
    
    if dimension <= 0:
        raise ValueError("The dimension must be a positive integer")
    
    matrix = np.random.randint(1, 101, size=(dimension, dimension))
    flat_list = matrix.flatten().tolist()
    
    combinations = list(itertools.combinations(flat_list, 2))
    
    return matrix, flat_list

class TestTaskFunction(unittest.TestCase):

    def test_matrix_dimensions(self):
        matrix, flat_list = task_func(3)
        self.assertEqual(matrix.shape, (3, 3), "Matrix should be 3x3 dimensions")

    def test_flat_list_length(self):
        dimension = 4
        matrix, flat_list = task_func(dimension)
        self.assertEqual(len(flat_list), dimension * dimension, "Flat list length should be equal to dimension squared")

    def test_positive_dimension_value(self):
        with self.assertRaises(ValueError):
            task_func(0)  # Should raise ValueError for zero dimension
        with self.assertRaises(ValueError):
            task_func(-1)  # Should raise ValueError for negative dimension

    def test_randomness_with_seed(self):
        matrix1, _ = task_func(2, seed=1)
        matrix2, _ = task_func(2, seed=1)
        np.testing.assert_array_equal(matrix1, matrix2, "Matrices should be equal when the same seed is used")

    def test_randomness_different_seeds(self):
        matrix1, _ = task_func(3, seed=1)
        matrix2, _ = task_func(3, seed=2)
        self.assertFalse(np.array_equal(matrix1, matrix2), "Matrices should not be equal with different seeds")

if __name__ == '__main__':
    unittest.main()