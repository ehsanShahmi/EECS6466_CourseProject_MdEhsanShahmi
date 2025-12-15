import pandas as pd
import numpy as np
import unittest

# Here is your prompt:
def task_func(rows=100, columns=3):
    """
    Create a Pandas DataFrame with random alphabets in each cell.
    The DataFrame will have a specified number of rows and columns.
    Each column is named with a string from the list ['a', 'b', 'c', ...]
    depending on the number of columns specified.

    Parameters:
    - rows (int, optional): Number of rows in the DataFrame. Defaults to 100.
    - columns (int, optional): Number of columns in the DataFrame. Defaults to 3.

    Returns:
    DataFrame: A pandas DataFrame with random alphabets.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> np.random.seed(0)
    >>> df = task_func(5, 3)
    >>> print(df)
       a  b  c
    0  m  p  v
    1  a  d  d
    2  h  j  t
    3  v  s  e
    4  x  g  y
    >>> df['a'].value_counts()
    a
    m    1
    a    1
    h    1
    v    1
    x    1
    Name: count, dtype: int64
    """
    column_names = [
        chr(97 + i) for i in range(columns)
    ]  # generate column names based on the number of columns
    values = list("abcdefghijklmnopqrstuvwxyz")
    data = np.random.choice(values, size=(rows, columns))
    df = pd.DataFrame(data, columns=column_names)
    return df

class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        df = task_func()
        self.assertEqual(df.shape, (100, 3))  # Default should be 100 rows and 3 columns
        self.assertListEqual(list(df.columns), ['a', 'b', 'c'])  # Check column names

    def test_custom_parameters(self):
        df = task_func(10, 5)
        self.assertEqual(df.shape, (10, 5))  # Custom should create 10 rows and 5 columns
        self.assertListEqual(list(df.columns), ['a', 'b', 'c', 'd', 'e'])  # Check column names

    def test_random_values(self):
        df = task_func(5, 3)
        unique_values = set(df.values.flatten())
        self.assertTrue(unique_values.issubset(set("abcdefghijklmnopqrstuvwxyz")))  # Check if all values are alphabets

    def test_empty_dataframe(self):
        df = task_func(0, 0)
        self.assertEqual(df.shape, (0, 0))  # An empty DataFrame with 0 rows and 0 columns

    def test_column_count(self):
        df = task_func(20, 10)
        self.assertEqual(len(df.columns), 10)  # Ensure 10 columns are created

if __name__ == '__main__':
    unittest.main()