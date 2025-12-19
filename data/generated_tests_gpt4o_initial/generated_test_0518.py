import unittest
import pandas as pd
from scipy.spatial.distance import pdist, squareform

# Here is your prompt:
# 
# import pandas as pd
# from scipy.spatial.distance import pdist, squareform
#
# def task_func(array):
#     """
#     Generate a Pandas DataFrame from a 2D list and calculate a distance matrix.
#
#     This function converts a 2D list into a DataFrame, with columns named alphabetically starting from 'A'.
#     It uses the `chr()` function, which converts an integer to its corresponding Unicode character,
#     to dynamically assign alphabetical labels to each column based on their index. The function then
#     computes the Euclidean distance matrix between rows.
#
#     Parameters:
#     array (list of list of int): The 2D list representing the data.
#                                  Each sublist must contain only integers or floats. If the input does not
#                                  conform to this structure, a TypeError is raised.
#
#     Returns:
#     - df (pd.DataFrame): data converted from 2D list.
#     - distance_matrix (pd.DataFrame): output distance matrix.
#
#     Requirements:
#     - pandas
#     - scipy.spatial.distance.pdist
#     - scipy.spatial.distance.squareform
#
#     Example:
#     >>> df, distance_matrix = task_func([[1,2,3,4,5], [6,7,8,9,10]])
#     >>> print(df)
#        A  B  C  D   E
#     0  1  2  3  4   5
#     1  6  7  8  9  10
#     >>> print(distance_matrix)
#               0         1
#     0   0.00000  11.18034
#     1  11.18034   0.00000
#     """
#
#               if not isinstance(array, list):
#         raise TypeError("Input must be a list.")
#
#     if not all(isinstance(sublist, list) for sublist in array):
#         raise TypeError("Input must be a list of lists.")
#
#     for sublist in array:
#         if not all(isinstance(item, (int, float)) for item in sublist):
#             raise TypeError("All elements in the sublists must be int or float.")
#
#     columns = [chr(65 + i) for i in range(len(array[0]))]
#     df = pd.DataFrame(array, columns=columns)
#
#     distances = pdist(df.values, metric="euclidean")
#     distance_matrix = pd.DataFrame(
#         squareform(distances), index=df.index, columns=df.index
#     )
#
#     return df, distance_matrix


class TestTaskFunction(unittest.TestCase):
    
    def test_valid_input(self):
        df, distance_matrix = task_func([[1, 2, 3], [4, 5, 6]])
        expected_df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['A', 'B', 'C'])
        expected_distance_matrix = pd.DataFrame(
            [[0.0, 5.196152422706632], [5.196152422706632, 0.0]], index=[0, 1], columns=[0, 1]
        )
        pd.testing.assert_frame_equal(df, expected_df)
        pd.testing.assert_frame_equal(distance_matrix, expected_distance_matrix)

    def test_invalid_input_not_list(self):
        with self.assertRaises(TypeError):
            task_func("not_a_list")

    def test_invalid_input_list_of_lists(self):
        with self.assertRaises(TypeError):
            task_func([[1, 2, 3], "not_a_list"])

    def test_invalid_input_non_numeric(self):
        with self.assertRaises(TypeError):
            task_func([[1, 2, 3], [4, 'not_a_number', 6]])

    def test_empty_input(self):
        df, distance_matrix = task_func([])
        expected_df = pd.DataFrame(columns=[])
        expected_distance_matrix = pd.DataFrame(columns=[], index=[])
        pd.testing.assert_frame_equal(df, expected_df)
        pd.testing.assert_frame_equal(distance_matrix, expected_distance_matrix)


if __name__ == '__main__':
    unittest.main()