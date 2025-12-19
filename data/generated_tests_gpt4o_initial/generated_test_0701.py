import pandas as pd
from sklearn.linear_model import LinearRegression
import unittest

# Here is your prompt:
def task_func(df, target):
    """
    Perform a linear regression analysis on a given DataFrame.
    
    Parameters:
    - df (pd.DataFrame): The pandas DataFrame.
    - target (str): The target variable.
    
    Returns:
    - score (float): The R-squared score of the model.

    Requirements:
    - pandas
    - sklearn

    Example:
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> df = pd.DataFrame({'feature': np.random.rand(100), 'target': np.random.rand(100)})  # Explicitly using pd
    >>> r_squared = task_func(df, 'target')
    >>> print(r_squared)
    0.0011582111228732872
    """

    X = pd.DataFrame.drop(df, target, axis=1)  
    y = pd.Series(df[target])  
    
    model = LinearRegression()
    model.fit(X, y)

    return model.score(X, y)

class TestTaskFunc(unittest.TestCase):
    
    def test_basic_functionality(self):
        # Test with a simple DataFrame with a clear linear relationship
        df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'target': [2, 4, 6, 8, 10]})
        result = task_func(df, 'target')
        self.assertAlmostEqual(result, 1.0, places=6)

    def test_no_correlation(self):
        # Test with a DataFrame that has no correlation
        df = pd.DataFrame({'feature': [1, 2, 3, 4, 5], 'target': [5, 3, 8, 2, 9]})
        result = task_func(df, 'target')
        self.assertLess(result, 0.0)

    def test_multiple_features(self):
        # Test with multiple features
        df = pd.DataFrame({'feature1': [1, 2, 3, 4, 5],
                           'feature2': [5, 4, 3, 2, 1],
                           'target': [2, 4, 6, 8, 10]})
        result = task_func(df, 'target')
        self.assertAlmostEqual(result, 1.0, places=6)
        
    def test_target_not_in_dataframe(self):
        # Test with a target variable not present in the DataFrame
        df = pd.DataFrame({'feature': [1, 2, 3, 4, 5]})
        with self.assertRaises(KeyError):
            task_func(df, 'non_existent_target')

    def test_empty_dataframe(self):
        # Test with an empty DataFrame
        df = pd.DataFrame(columns=['feature', 'target'])
        with self.assertRaises(ValueError):
            task_func(df, 'target')

if __name__ == '__main__':
    unittest.main()