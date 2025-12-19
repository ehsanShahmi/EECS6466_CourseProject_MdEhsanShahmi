import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import unittest

def task_func(df, target_column, target_values=None):
    """
    Replace all elements in DataFrame columns that are not present in the target_values array with zeros, and then perform a linear regression using the target column.

    Parameters:
        df (DataFrame): The input pandas DataFrame.
        target_column (str): The target column for the linear regression.
        target_values (array-like, optional): An array of target values to keep in the DataFrame. 
        All other values will be replaced with zeros. Defaults to None.

    Returns:
        LinearRegression: The trained Linear Regression model.

    Raises:
        ValueError: If df is not a DataFrame or if target_column is not a string or if target_values is not an array-like object
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df should be a DataFrame.")
    
    if df.empty:
        raise ValueError("df should contain at least one row")
    
    if target_column not in df.columns:
        raise ValueError("target_column should be in DataFrame")
    
    if not all(np.issubdtype(dtype, np.number) for dtype in df.dtypes):
        raise ValueError("df values should be numeric only")

    if target_values is not None:
        df = df.applymap(lambda x: x if x in target_values else 0)

    X = df.drop(target_column, axis=1)
    y = df[target_column]

    model = LinearRegression().fit(X, y)

    return model

class TestTaskFunc(unittest.TestCase):

    def test_valid_input(self):
        rng = np.random.default_rng(seed=0)
        df = pd.DataFrame(rng.integers(0, 100, size=(100, 2)), columns=['A', 'predict'])
        model = task_func(df, 'predict')
        self.assertIsInstance(model, LinearRegression)
    
    def test_invalid_dataframe(self):
        with self.assertRaises(ValueError) as context:
            task_func(None, 'predict')
        self.assertEqual(str(context.exception), "df should be a DataFrame.")
    
    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['A', 'predict'])
        with self.assertRaises(ValueError) as context:
            task_func(df, 'predict')
        self.assertEqual(str(context.exception), "df should contain at least one row")
    
    def test_non_existent_target_column(self):
        df = pd.DataFrame({'A': [1, 2, 3]})
        with self.assertRaises(ValueError) as context:
            task_func(df, 'nonexistent')
        self.assertEqual(str(context.exception), "target_column should be in DataFrame")

    def test_non_numeric_dataframe(self):
        df = pd.DataFrame({'A': ['a', 'b', 'c'], 'predict': [1, 2, 3]})
        with self.assertRaises(ValueError) as context:
            task_func(df, 'predict')
        self.assertEqual(str(context.exception), "df values should be numeric only")

if __name__ == '__main__':
    unittest.main()