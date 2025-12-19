import unittest
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Provided Prompt
def task_func(df):
    """
    Use a linear regression model to predict the "value" of "feature" in the given dataframe and return the coefficients and intercept.

    Parameters:
    - df (pd.DataFrame): pandas DataFrame that contains columns named 'feature' and 'value'.

    Returns:
    - result (dict): A dictionary with the coefficients and the intercept of the fitted linear regression model.

    Requirements:
    - numpy
    - sklearn

    Example:
    >>> import pandas as pd
    >>> np.random.seed(42)
    >>> df = pd.DataFrame({'feature': np.random.rand(100), 'value': np.random.rand(100)})
    >>> coefficients = task_func(df)
    >>> print(coefficients)
    {'coefficients': [[-0.03353164387961974]], 'intercept': [0.5135976564010359]}
    """

    X = np.array(df['feature']).reshape(-1, 1)  # Explicitly converting to numpy array and reshaping
    y = np.array(df['value']).reshape(-1, 1)    # Explicitly converting to numpy array and reshaping

    model = LinearRegression().fit(X, y)

    return {'coefficients': model.coef_.tolist(), 'intercept': model.intercept_.tolist()}

class TestTaskFunc(unittest.TestCase):
    
    def test_linear_regression_coefficients(self):
        """ Test that the coefficients are of the correct shape and type """
        df = pd.DataFrame({'feature': [1, 2, 3], 'value': [2, 3, 4]})
        result = task_func(df)
        self.assertEqual(len(result['coefficients']), 1, "Should return one coefficient.")
        self.assertEqual(len(result['coefficients'][0]), 1, "Coefficient should be a scalar.")
        self.assertIsInstance(result['coefficients'][0][0], float, "Coefficient should be a float.")

    def test_linear_regression_intercept(self):
        """ Test that the intercept is of the correct type """
        df = pd.DataFrame({'feature': [1, 2, 3], 'value': [3, 4, 5]})
        result = task_func(df)
        self.assertEqual(len(result['intercept']), 1, "Intercept should be a scalar in list form.")
        self.assertIsInstance(result['intercept'][0], float, "Intercept should be a float.")

    def test_empty_dataframe(self):
        """ Test behavior with an empty DataFrame """
        df = pd.DataFrame({'feature': [], 'value': []})
        with self.assertRaises(ValueError):
            task_func(df)

    def test_dataframe_with_na_values(self):
        """ Test behavior with NaN values in DataFrame """
        df = pd.DataFrame({'feature': [1, 2, np.nan], 'value': [3, np.nan, 5]})
        with self.assertRaises(ValueError):
            task_func(df)

    def test_random_data_return_shape(self):
        """ Test that coefficients and intercept are returned in expected format with random data """
        np.random.seed(42)
        df = pd.DataFrame({'feature': np.random.rand(100), 'value': np.random.rand(100)})
        result = task_func(df)
        self.assertIn('coefficients', result, "Result should contain 'coefficients'.")
        self.assertIn('intercept', result, "Result should contain 'intercept'.")
        self.assertIsInstance(result['coefficients'], list, "Coefficients should be a list.")
        self.assertIsInstance(result['intercept'], list, "Intercept should be a list.")

if __name__ == '__main__':
    unittest.main()