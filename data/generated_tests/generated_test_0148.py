import pandas as pd
from sklearn.preprocessing import LabelEncoder
import unittest

# Provided prompt
def task_func(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Encrypt the categorical data in a specific column of a DataFrame using LabelEncoder.

    Parameters:
    df (pd.DataFrame): The DataFrame that contains the data.
    column_name (str): The name of the column to encode.

    Returns:
    pd.DataFrame: The DataFrame with the encoded column.

    Requirements:
    - pandas
    - sklearn

    Example:
    >>> df = pd.DataFrame({'fruit': ['apple', 'banana', 'cherry', 'apple', 'banana']})
    >>> encoded_df = task_func(df, 'fruit')
    >>> encoded_df['fruit'].tolist()
    [0, 1, 2, 0, 1]
    """
    le = LabelEncoder()
    df[column_name] = le.fit_transform(df[column_name])
    return df

# Test suite
class TestTaskFunc(unittest.TestCase):

    def test_encode_single_column(self):
        df = pd.DataFrame({'fruit': ['apple', 'banana', 'cherry', 'apple', 'banana']})
        encoded_df = task_func(df, 'fruit')
        self.assertEqual(encoded_df['fruit'].tolist(), [0, 1, 2, 0, 1])

    def test_encode_with_missing_values(self):
        df = pd.DataFrame({'fruit': ['apple', 'banana', None, 'apple', 'banana']})
        encoded_df = task_func(df, 'fruit')
        self.assertEqual(encoded_df['fruit'].tolist(), [0, 1, 2, 0, 1])  # NaN will be treated as a separate class

    def test_encode_multiple_categories(self):
        df = pd.DataFrame({'fruit': ['grape', 'orange', 'lemon', 'grape', 'orange']})
        encoded_df = task_func(df, 'fruit')
        self.assertEqual(encoded_df['fruit'].tolist(), [0, 1, 2, 0, 1])

    def test_encode_all_values_same(self):
        df = pd.DataFrame({'fruit': ['banana', 'banana', 'banana']})
        encoded_df = task_func(df, 'fruit')
        self.assertEqual(encoded_df['fruit'].tolist(), [0, 0, 0])  # All identical should encode to a single value

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['fruit'])
        encoded_df = task_func(df, 'fruit')
        self.assertTrue(encoded_df.empty)  # Should return an empty DataFrame as well

if __name__ == '__main__':
    unittest.main()