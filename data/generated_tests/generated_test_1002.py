import unittest
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO
import numpy as np

# Here is your prompt:
def task_func(data, column_name="target_column"):
    """
    Converts a given JSON data into a Pandas DataFrame and plots a histogram of a specified column.
    The function handles non-numeric columns by converting them to categorical type and then to numeric codes. 
    It also checks if the specified column exists in the DataFrame.

    - The histogram's title is set to 'Histogram of <column_name>'.
    - The histogram's x-label are set to the name of the specified column.
    
    Parameters:
    - data (list of dict)
    - column_name (str, optional)

    Returns:
    - DataFrame: A pandas DataFrame created from the input JSON data.
    - Axes: A matplotlib Axes object showing the histogram plot of the specified column.

    Exceptions:
    - ValueError: Raised if the specified column name does not exist in the DataFrame.

    Requirements:
    - pandas
    - matplotlib

    Example:
    >>> sample_data = [{'userId': 1, 'value': 10}, {'userId': 2, 'value': 15}]
    >>> df, ax = task_func(sample_data, 'userId')
    >>> print(df)
       userId  value
    0       1     10
    1       2     15
    """

    df = pd.DataFrame(data)

    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the DataFrame.")

    if not pd.api.types.is_numeric_dtype(df[column_name]):
        df[column_name] = df[column_name].astype("category").cat.codes

    _, ax = plt.subplots()
    df[column_name].hist(ax=ax)
    ax.set_title(f"Histogram of {column_name}")
    ax.set_xlabel(column_name)
    return df, ax

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        sample_data = [{'userId': 1, 'value': 10}, {'userId': 2, 'value': 15}]
        df, ax = task_func(sample_data, 'userId')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn('userId', df.columns)
        self.assertEqual(len(df), 2)

    def test_histogram_plot(self):
        sample_data = [{'userId': 1, 'value': 10}, {'userId': 2, 'value': 15}]
        df, ax = task_func(sample_data, 'value')
        self.assertEqual(ax.get_title(), "Histogram of value")

    def test_column_not_found(self):
        sample_data = [{'userId': 1, 'value': 10}, {'userId': 2, 'value': 15}]
        with self.assertRaises(ValueError):
            task_func(sample_data, 'nonexistent_column')

    def test_non_numeric_column(self):
        sample_data = [{'userId': 'a', 'value': 10}, {'userId': 'b', 'value': 15}]
        df, ax = task_func(sample_data, 'userId')
        self.assertTrue(pd.api.types.is_numeric_dtype(df['userId']))

    def test_empty_data(self):
        sample_data = []
        df, ax = task_func(sample_data, 'userId')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(len(df), 0)

if __name__ == "__main__":
    unittest.main()