import pandas as pd
import unittest
from statsmodels.tsa.stattools import adfuller

# Here is your prompt:
def task_func(df: pd.DataFrame, column_a: str, column_b: str, column_c: str) -> bool:
    """
    Determines if a specific subset of data is stationary by filtering rows where column_b bigger than 50 and column_c equal to 900. 
    Data is considered to be stationary if the p_value returned by the Augmented Dickey-Fuller test is smaller than 0.05.

    If column_a is empty after filtering or if its values are constant, True
    is returned.
    
    Parameters:
        df (pd.DataFrame): A DataFrame containing the data.
        column_a (str): The name of the column to test for stationarity.
        column_b (str): The name of the column used for filtering based on its value being greater than 50.
        column_c (str): The name of the column used for filtering based on its value being equal to 900.
    
    Returns:
        bool: True if the data in column_a (after filtering based on column_b and column_c) is stationary, False otherwise.
    
    Requirements:
        pandas
        statsmodels: for using the adfuller test

    Example:
    >>> df = pd.DataFrame({
    ...      'A': [1, 2, 3, 4, 5, 6],
    ...      'B': [60, 70, 80, 90, 100, 110],
    ...      'C': [900, 900, 900, 900, 900, 900]
    ... })
    >>> task_func(df, 'A', 'B', 'C')
    False
    """

class TestTaskFunc(unittest.TestCase):
    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['A', 'B', 'C'])
        self.assertTrue(task_func(df, 'A', 'B', 'C'))

    def test_constant_values_in_column_a(self):
        df = pd.DataFrame({
            'A': [5, 5, 5],
            'B': [60, 70, 80],
            'C': [900, 900, 900]
        })
        self.assertTrue(task_func(df, 'A', 'B', 'C'))

    def test_stationary_data(self):
        df = pd.DataFrame({
            'A': [1, 2, 3, 4],
            'B': [60, 70, 80, 90],
            'C': [900, 900, 900, 900]
        })
        self.assertFalse(task_func(df, 'A', 'B', 'C'))

    def test_non_stationary_data(self):
        df = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [60, 70, 80, 90, 100],
            'C': [900, 900, 900, 900, 900]
        })
        self.assertFalse(task_func(df, 'A', 'B', 'C'))

    def test_no_rows_after_filtering(self):
        df = pd.DataFrame({
            'A': [1, 2, 3],
            'B': [10, 20, 30],  # All values less than or equal to 50
            'C': [800, 800, 800]  # Not equal to 900
        })
        self.assertTrue(task_func(df, 'A', 'B', 'C'))

if __name__ == '__main__':
    unittest.main()