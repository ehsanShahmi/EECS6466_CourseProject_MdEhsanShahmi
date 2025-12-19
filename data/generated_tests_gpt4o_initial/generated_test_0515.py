import unittest
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Here is your prompt:
# import pandas as pd
# import seaborn as sns
#
#
# def task_func(array):
#     """Generates a DataFrame and heatmap from a 2D list.
#
#     This function takes a 2D list and returns a pandas DataFrame and a seaborn heatmap
#     representing the correlation matrix of the DataFrame. Assumes sublists of length 5.
#     Also assumes DataFrame columns: 'A', 'B', 'C', 'D', 'E'.
#
#     Parameters:
#     - array (list of list of int): 2D list with sublists of length 5. Must not be empty.
#
#     Returns:
#     - DataFrame: Constructed from the input 2D list.
#     - heatmap: Seaborn heatmap of the DataFrame's correlation matrix.
#
#     Requirements:
#     - pandas
#     - seaborn
#
#     Raises:
#     - ValueError: If the input array is empty or contains sublists of varying lengths.
#     
#     Example:
#     >>> df, ax = task_func([[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]])
#     >>> df
#        A  B  C  D  E
#     0  1  2  3  4  5
#     1  5  4  3  2  1
#     >>> ax
#     <Axes: >
#     """
# 
#                COLUMNS = ["A", "B", "C", "D", "E"]
#
#     if not array or any(len(sublist) != 5 for sublist in array):
#         raise ValueError("array must be non-empty and all sublists must have a length of 5.")
#
#     df = pd.DataFrame(array, columns=COLUMNS)
#     heatmap = sns.heatmap(df.corr(), annot=True)
#     return df, heatmap

class TestTaskFunc(unittest.TestCase):

    def test_valid_input(self):
        array = [[1, 2, 3, 4, 5], [5, 4, 3, 2, 1]]
        df, ax = task_func(array)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (2, 5))
        self.assertListEqual(list(df.columns), ['A', 'B', 'C', 'D', 'E'])

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            task_func([])

    def test_invalid_sublists_length(self):
        array = [[1, 2, 3], [4, 5, 6, 7, 8]]
        with self.assertRaises(ValueError):
            task_func(array)

    def test_all_zeroes_input(self):
        array = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        df, ax = task_func(array)
        expected_correlation = np.zeros((5, 5))
        pd.testing.assert_frame_equal(df.corr().values, expected_correlation)

    def test_large_numbers_input(self):
        array = [[10**6, 10**6, 10**6, 10**6, 10**6], [10**6, 10**6, 10**6, 10**6, 10**6]]
        df, ax = task_func(array)
        expected_correlation = np.zeros((5, 5))
        pd.testing.assert_frame_equal(df.corr().values, expected_correlation)

if __name__ == '__main__':
    unittest.main()