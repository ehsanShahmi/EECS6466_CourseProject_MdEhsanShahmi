import unittest
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(data):
    """
    Transforms categorical data into a numerical format suitable for machine learning algorithms using sklearn's
    LabelEncoder. This function generates a DataFrame that pairs original categorical values with their numerical
    encodings.

    Parameters:
    data (list): List of categorical data to be encoded.

    Returns:
    DataFrame: A DataFrame with columns 'Category' and 'Encoded', where 'Category' is the original data and 'Encoded'
    is the numerical representation.

    Requirements:
    - pandas
    - sklearn

    Example:
    >>> df = task_func(['A', 'B', 'C', 'A', 'D', 'E', 'B', 'C'])
    >>> print(df.to_string(index=False))
    Category  Encoded
           A        0
           B        1
           C        2
           A        0
           D        3
           E        4
           B        1
           C        2
    """

    le = LabelEncoder()
    encoded = le.fit_transform(data)
    df = pd.DataFrame({'Category': data, 'Encoded': encoded})

    return df

class TestTaskFunc(unittest.TestCase):

    def test_basic_encoding(self):
        data = ['A', 'B', 'C', 'A', 'D', 'E', 'B', 'C']
        expected = pd.DataFrame({
            'Category': ['A', 'B', 'C', 'A', 'D', 'E', 'B', 'C'],
            'Encoded': [0, 1, 2, 0, 3, 4, 1, 2]
        })
        result = task_func(data)
        pd.testing.assert_frame_equal(result, expected)

    def test_empty_input(self):
        data = []
        expected = pd.DataFrame({
            'Category': [],
            'Encoded': []
        })
        result = task_func(data)
        pd.testing.assert_frame_equal(result, expected)

    def test_single_unique_category(self):
        data = ['A', 'A', 'A']
        expected = pd.DataFrame({
            'Category': ['A', 'A', 'A'],
            'Encoded': [0, 0, 0]
        })
        result = task_func(data)
        pd.testing.assert_frame_equal(result, expected)

    def test_numeric_strings(self):
        data = ['1', '2', '1', '3']
        expected = pd.DataFrame({
            'Category': ['1', '2', '1', '3'],
            'Encoded': [0, 1, 0, 2]
        })
        result = task_func(data)
        pd.testing.assert_frame_equal(result, expected)

    def test_non_string_categories(self):
        data = [10, 20, 10, 30]
        expected = pd.DataFrame({
            'Category': [10, 20, 10, 30],
            'Encoded': [0, 1, 0, 2]
        })
        result = task_func(data)
        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()