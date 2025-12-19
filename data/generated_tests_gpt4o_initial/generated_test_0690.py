import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import unittest

ROWS = 100
COLUMNS = ['X', 'Y']

def task_func(df):
    """
    Given a Pandas DataFrame with random numeric values and columns X & Y, use sklearn's linear regression to match the data to a linear model.

    Parameters:
    - df (DataFrame): The DataFrame to use.

    Returns:
    - model (LinearRegression): The fitted linear model.

    Requirements:
    - pandas
    - sklearn

    Example:
    >>> import numpy as np
    >>> np.random.seed(42)
    >>> df = pd.DataFrame(np.random.normal(size=(100, 2)), columns=['X', 'Y'])
    >>> model = task_func(df)
    >>> print(model)
    LinearRegression()
    """

    X = pd.DataFrame(df[['X']])  # Extracting column 'X' as a DataFrame
    y = pd.Series(df['Y'])       # Extracting column 'Y' as a Series
    
    # Fitting the linear regression model
    model = LinearRegression().fit(X, y)
    
    return model

class TestLinearRegressionModel(unittest.TestCase):

    def setUp(self):
        """Sets up a random DataFrame for testing."""
        np.random.seed(42)
        self.df = pd.DataFrame(np.random.normal(size=(ROWS, 2)), columns=['X', 'Y'])

    def test_model_fitting(self):
        """Test that the model can be created and fitted."""
        model = task_func(self.df)
        self.assertIsInstance(model, LinearRegression, "The model should be an instance of LinearRegression")

    def test_coefficients_shape(self):
        """Test the model coefficients shape after fitting."""
        model = task_func(self.df)
        self.assertEqual(model.coef_.shape, (1,), "The coefficients should have shape (1,) for one feature")

    def test_intercept(self):
        """Test that the model has an intercept after fitting."""
        model = task_func(self.df)
        self.assertIsNotNone(model.intercept_, "The model should have a non-null intercept")

    def test_predict_shape(self):
        """Test that predictions have the correct shape."""
        model = task_func(self.df)
        predictions = model.predict(self.df[['X']])
        self.assertEqual(predictions.shape, (ROWS,), "Predictions should have the same number of rows as the input data")

    def test_random_input(self):
        """Test the model with a randomly generated DataFrame."""
        random_df = pd.DataFrame(np.random.rand(ROWS, 2), columns=COLUMNS)
        model = task_func(random_df)
        self.assertIsInstance(model, LinearRegression, "Model should be an instance of LinearRegression for random input")

if __name__ == "__main__":
    unittest.main()