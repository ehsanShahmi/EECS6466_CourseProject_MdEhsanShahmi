import pandas as pd
import unittest
from sklearn.linear_model import LinearRegression
import heapq

# Here is your prompt:
def task_func(df, feature, target, n=10):
    """
    Fit a simple linear regression model to two columns of a DataFrame 
    specified by feature and target. 
    return the indices of the n largest residuals as well as the linear 
    regression model.
    
    Parameters:
    df (pandas.DataFrame): A DataFrame with at least two numerical columns named 'col1' and 'col2'.
    feature (str): The DataFrame column used as feature.
    target (str): The DataFrame column used as target.
    n (int, optional): Number of largest residuals to return. Default is 10.
    
    Returns:
    list[int]: Indices of the n largest residuals.
    LinearRegression: The LinearRegression model.
    
    Raises:
    ValueError: If specified columns are not in the provided DataFrame.

    Requirements:
    - heapq
    - sklearn.linear_model
    
    Example:
    >>> df = pd.DataFrame({
    ...     'col1': [99, 86, 90, 70, 86, 95, 56, 98, 80, 81],
    ...     'col2': [21, 11, 21, 1, 26, 40, 4, 50, 34, 37]
    ... })
    >>> indices, model = task_func(df, 'col1', 'col2', n=5)
    >>> print(indices)
    [0, 1, 9, 7, 8]
    >>> print(model)
    LinearRegression()

    >>> df = pd.DataFrame({
    ...     'a': [1, 2, 3, 4, 5],
    ...     'b': [1, 2, 3, 4, 5]
    ... })
    >>> indices, model = task_func(df, 'a', 'b', n=3)
    >>> print(indices)
    [0, 1, 2]
    >>> print(model)
    LinearRegression()
    """

    # Ensure provided columns exist in the dataframe
    if feature not in df.columns or target not in df.columns:
        raise ValueError(f"Columns {feature} or {target} not found in the DataFrame.")

    X = df[feature].values.reshape(-1, 1)
    y = df[target].values
    model = LinearRegression()
    model.fit(X, y)
    residuals = y - model.predict(X)
    largest_residual_indices = heapq.nlargest(n, range(len(residuals)), key=lambda i: abs(residuals[i]))
    return largest_residual_indices, model

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        df = pd.DataFrame({
            'col1': [99, 86, 90, 70, 86, 95, 56, 98, 80, 81],
            'col2': [21, 11, 21, 1, 26, 40, 4, 50, 34, 37]
        })
        indices, model = task_func(df, 'col1', 'col2', n=5)
        self.assertEqual(indices, [0, 1, 9, 7, 8])
        self.assertIsInstance(model, LinearRegression)

    def test_different_columns(self):
        df = pd.DataFrame({
            'a': [1, 2, 3, 4, 5],
            'b': [1, 2, 3, 4, 5]
        })
        indices, model = task_func(df, 'a', 'b', n=3)
        self.assertEqual(indices, [0, 1, 2])
        self.assertIsInstance(model, LinearRegression)

    def test_invalid_feature_column(self):
        df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': [4, 5, 6]
        })
        with self.assertRaises(ValueError):
            task_func(df, 'non_existent_feature', 'col2')

    def test_invalid_target_column(self):
        df = pd.DataFrame({
            'col1': [1, 2, 3],
            'col2': [4, 5, 6]
        })
        with self.assertRaises(ValueError):
            task_func(df, 'col1', 'non_existent_target')

    def test_no_residuals(self):
        df = pd.DataFrame({
            'col1': [1, 1, 1],
            'col2': [1, 1, 1]
        })
        indices, model = task_func(df, 'col1', 'col2', n=2)
        self.assertEqual(indices, [0, 1])  # All residuals are zero, return first two indices
        self.assertIsInstance(model, LinearRegression)

if __name__ == '__main__':
    unittest.main()