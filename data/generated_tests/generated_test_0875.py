import pandas as pd
import unittest

# Here is your prompt:
import pandas as pd
import random

def task_func(data, columns=['Name', 'Age', 'Occupation'], fill_missing=False, num_range=(0, 100), seed=None):
    """
    Create a Pandas DataFrame from a list of tuples, each representing a row.
    Tuples of unequal lengths are allowed, and missing elements are filled with None.
    Optionally, missing numeric values can be filled with random data.

    Parameters:
    data (list of tuples): Each tuple contains the data for each row.
                           Elements in tuples represent values corresponding to the columns parameter.
    columns (list of str): List of column names for the DataFrame.
                           Defaults to ['Name', 'Age', 'Occupation'].
    fill_missing (bool): If True, fill missing numeric values with random data.
                         Defaults to False.
    num_range (tuple): Range (min, max) of random numbers for filling missing values.
                       Defaults to (0, 100).
    seed (int): Optional seed for random number generator for reproducibility.
                Defaults to None.

    Returns:
    DataFrame: A pandas DataFrame with specified columns.
               Missing elements are represented as None or filled with random data.

    Requirements:
    - pandas
    - random

    Example:
    >>> data = [('John', 25, 'Engineer'), ('Alice', ), ('Bob', )]
    >>> df = task_func(data, fill_missing=True, num_range=(0, 10), seed=42)
    >>> print(df)
        Name   Age Occupation
    0   John  25.0   Engineer
    1  Alice  10.0       None
    2    Bob   1.0       None

    >>> data = [('Mango', 20), ('Apple', ), ('Banana', )]
    >>> df = task_func(data, columns=['Fruit', 'Quantity'], fill_missing=False, seed=42)
    >>> print(df)
        Fruit  Quantity
    0   Mango      20.0
    1   Apple       NaN
    2  Banana       NaN
    """

    if seed is not None:
        random.seed(seed)

    df = pd.DataFrame(data, columns=columns)

    if fill_missing:
        for col in df.columns:
            if df[col].dtype in ['float64', 'int64']:
                df[col] = df[col].apply(lambda x: random.randint(*num_range) if pd.isnull(x) else x)

    return df

class TestTaskFunc(unittest.TestCase):

    def test_data_with_complete_rows(self):
        data = [('John', 25, 'Engineer'), ('Alice', 30, 'Doctor'), ('Bob', 22, 'Artist')]
        result = task_func(data)
        expected_df = pd.DataFrame(data, columns=['Name', 'Age', 'Occupation'])
        pd.testing.assert_frame_equal(result, expected_df)

    def test_data_with_missing_values(self):
        data = [('Mango', 20), ('Apple',), ('Banana',)]
        result = task_func(data, columns=['Fruit', 'Quantity'])
        expected_df = pd.DataFrame(data, columns=['Fruit', 'Quantity'])
        pd.testing.assert_frame_equal(result, expected_df)

    def test_fill_missing_with_random(self):
        data = [('John', None, 'Engineer'), ('Alice', None, None), ('Bob', 22, None)]
        result = task_func(data, fill_missing=True, num_range=(0, 10), seed=42)
        self.assertEqual(result.iloc[0]['Age'], 1.0)
        self.assertEqual(result.iloc[1]['Age'], 10.0)
        self.assertEqual(result.iloc[2]['Occupation'], None)

    def test_empty_data(self):
        data = []
        result = task_func(data)
        expected_df = pd.DataFrame(columns=['Name', 'Age', 'Occupation'])
        pd.testing.assert_frame_equal(result, expected_df)

    def test_specific_columns_with_filled_missing(self):
        data = [(None, 5), ('Orange', None)]
        result = task_func(data, columns=['Fruit', 'Quantity'], fill_missing=True, num_range=(1, 10), seed=42)
        self.assertEqual(result.iloc[0]['Fruit'], None)
        self.assertTrue(result.iloc[0]['Quantity'] >= 1 and result.iloc[0]['Quantity'] <= 10)
        self.assertEqual(result.iloc[1]['Fruit'], 'Orange')
        self.assertTrue(result.iloc[1]['Quantity'] >= 1 and result.iloc[1]['Quantity'] <= 10)

if __name__ == '__main__':
    unittest.main()