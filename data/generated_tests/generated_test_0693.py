import unittest
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Below is the provided prompt without modifications
def task_func(tuples_list, columns):
    """
    Convert a list of tuples into a Pandas DataFrame, perform a default scaling in each column, and return the transformed DataFrame.
    
    Parameters:
    - tuples_list (list): The list of tuples.
    - columns (list): The list of column names.
    
    Returns:
    - df_scaled (DataFrame): A pandas DataFrame containing the scaled versions of the original data.

    Requirements:
    - pandas
    - sklearn
    
    Example:
    >>> df = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], ['A', 'B', 'C', 'D'])
    >>> print(df)
              A         B         C         D
    0 -1.224745 -1.224745 -1.224745 -1.224745
    1  0.000000  0.000000  0.000000  0.000000
    2  1.224745  1.224745  1.224745  1.224745
    """

    df = pd.DataFrame(tuples_list, columns=columns)
    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

    return df_scaled

class TestTaskFunc(unittest.TestCase):

    def test_basic_scaling(self):
        result = task_func([(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)], ['A', 'B', 'C', 'D'])
        expected = pd.DataFrame({
            'A': [-1.224745, 0.0, 1.224745],
            'B': [-1.224745, 0.0, 1.224745],
            'C': [-1.224745, 0.0, 1.224745],
            'D': [-1.224745, 0.0, 1.224745]
        })
        pd.testing.assert_frame_equal(result, expected, check_dtype=False)

    def test_empty_input(self):
        result = task_func([], ['A', 'B', 'C'])
        expected = pd.DataFrame(columns=['A', 'B', 'C'])
        pd.testing.assert_frame_equal(result, expected)

    def test_single_element_input(self):
        result = task_func([(1, 2, 3)], ['A', 'B', 'C'])
        expected = pd.DataFrame({
            'A': [0.0],
            'B': [0.0],
            'C': [0.0]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_identical_rows(self):
        result = task_func([(1, 1, 1), (1, 1, 1), (1, 1, 1)], ['A', 'B', 'C'])
        expected = pd.DataFrame({
            'A': [0.0, 0.0, 0.0],
            'B': [0.0, 0.0, 0.0],
            'C': [0.0, 0.0, 0.0]
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_non_numeric_input(self):
        with self.assertRaises(ValueError):
            task_func([(1, 'a', 3)], ['A', 'B', 'C'])

if __name__ == '__main__':
    unittest.main()