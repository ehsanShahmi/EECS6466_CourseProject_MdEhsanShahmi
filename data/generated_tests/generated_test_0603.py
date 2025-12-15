import numpy as np
import pandas as pd
import unittest

def task_func(matrix1, matrix2):
    """
    Connects two 2D numeric arrays (matrices) along the second axis (columns),
    converts them into a Pandas DataFrame, and returns a string representation of the DataFrame.

    Parameters:
    - matrix1 (np.ndarray): The first 2D numpy array.
    - matrix2 (np.ndarray): The second 2D numpy array.

    Returns:
    - str: The string representation of the DataFrame without the index and header.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
    >>> matrix2 = np.array([[7, 8, 9], [10, 11, 12]])
    >>> result = task_func(matrix1, matrix2)
    >>> all(x in result.replace(' ', '') for x in ['123789', '456101112'])
    True
    """
    combined_matrix = np.concatenate((matrix1, matrix2), axis=1)
    df = pd.DataFrame(combined_matrix)
    return df.to_string(index=False, header=False)

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        matrix1 = np.array([[1, 2, 3], [4, 5, 6]])
        matrix2 = np.array([[7, 8, 9], [10, 11, 12]])
        result = task_func(matrix1, matrix2)
        expected = "  1  2  3  7  8  9\n  4  5  6 10 11 12"
        self.assertEqual(result.replace(' ', ''), expected.replace(' ', ''))

    def test_different_shapes(self):
        matrix1 = np.array([[1, 2], [3, 4]])
        matrix2 = np.array([[5, 6]])
        result = task_func(matrix1, matrix2)
        expected = "  1  2  5  6\n  3  4"
        self.assertEqual(result.replace(' ', ''), expected.replace(' ', ''))

    def test_single_row_matrices(self):
        matrix1 = np.array([[1, 2, 3]])
        matrix2 = np.array([[4, 5, 6]])
        result = task_func(matrix1, matrix2)
        expected = "  1  2  3  4  5  6"
        self.assertEqual(result.replace(' ', ''), expected.replace(' ', ''))

    def test_empty_matrices(self):
        matrix1 = np.empty((0, 0))
        matrix2 = np.empty((0, 0))
        result = task_func(matrix1, matrix2)
        expected = ""
        self.assertEqual(result, expected)

    def test_large_matrices(self):
        matrix1 = np.random.randint(0, 10, size=(100, 100))
        matrix2 = np.random.randint(10, 20, size=(100, 100))
        result = task_func(matrix1, matrix2)
        combined_matrix = np.concatenate((matrix1, matrix2), axis=1)
        expected_df = pd.DataFrame(combined_matrix)
        expected_result = expected_df.to_string(index=False, header=False)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()