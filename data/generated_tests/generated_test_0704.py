import pandas as pd
from itertools import combinations
import unittest

# Constants
MIN_PERCENTAGE = 0.75

def task_func(data, cols, percentage):
    """
    Find all combinations of columns from a given DataFrame so that the absolute correlation between them is greater than a certain threshold.

    Parameters:
    - data (list): List of lists with the data, where the length of the inner list equals the number of columns
    - cols (list): List of column names
    - percentage (float): The threshold for the absolute correlation.

    Returns:
    - corr_combinations (list): A list of tuples where each tuple contains two column names.
    """

    if not 0 <= percentage <= 1:
        raise ValueError('Percentage must be between 0 and 1')
    df = pd.DataFrame(data, columns=cols)
    corr_matrix = df.corr().abs()
    columns = corr_matrix.columns
    corr_combinations = []

    for col1, col2 in combinations(columns, 2):
        if corr_matrix.loc[col1, col2] > percentage:
            corr_combinations.append((col1, col2))

    return corr_combinations

class TestTaskFunc(unittest.TestCase):

    def test_valid_combinations(self):
        data = [[5.1, 5.0, 1.4], [4.9, 4.8, 1.4], [4.7, 4.6, 2.0]]
        cols = ['x', 'y', 'z']
        result = task_func(data, cols, 0.9)
        expected = [('x', 'y')]
        self.assertEqual(result, expected)

    def test_no_combinations_below_threshold(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        cols = ['a', 'b', 'c']
        result = task_func(data, cols, 1)
        expected = []
        self.assertEqual(result, expected)

    def test_empty_data(self):
        data = []
        cols = []
        result = task_func(data, cols, 0.5)
        expected = []
        self.assertEqual(result, expected)

    def test_invalid_percentage_low(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        cols = ['a', 'b', 'c']
        with self.assertRaises(ValueError):
            task_func(data, cols, -0.1)

    def test_invalid_percentage_high(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        cols = ['a', 'b', 'c']
        with self.assertRaises(ValueError):
            task_func(data, cols, 1.5)

if __name__ == '__main__':
    unittest.main()