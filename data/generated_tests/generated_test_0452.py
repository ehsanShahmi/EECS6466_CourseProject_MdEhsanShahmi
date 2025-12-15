import unittest
import numpy as np
from sklearn.linear_model import LinearRegression

# Here is your prompt:
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


def task_func(n_samples=100, n_features=10, random_seed=None):
    """
    Generate synthetic data using a simple regression model, fit a linear regression model to the data,
    and return the predicted values along with the coefficients and intercept of the model.

    Parameters:
    - n_samples (int): The number of samples for the synthetic data. Default is 100.
    - n_features (int): The number of features for the synthetic data. Default is 10.
    - random_seed (int, optional): The seed for reproducibility. Default is None.

    Returns:
    - tuple: A tuple containing:
        - predictions (numpy.ndarray): The predicted values of the test set.
        - coefficients (numpy.ndarray): Coefficients of the linear regression model.
        - intercept (float): Intercept of the linear regression model.
        - mse (float): Mean squared error of the model predictions.

    Requirements:
    - numpy
    - sklearn.datasets.make_regression
    - sklearn.model_selection.train_test_split
    - sklearn.linear_model.LinearRegression
    
    Example:
    >>> predictions, coefficients, intercept, mse = task_func(100, 5, random_seed=42)
    >>> predictions[:3]
    array([ 180.79207843, -295.0210232 ,  118.23799221])
    >>> round(mse, 4)
    0.0113
    """

    # Generate synthetic data
    X, y = datasets.make_regression(
        n_samples=n_samples, n_features=n_features, noise=0.1, random_state=random_seed
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=random_seed
    )

    # Fit a linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test set
    predictions = model.predict(X_test)
    coefficients = model.coef_
    intercept = model.intercept_

    mse = np.mean((predictions - y_test) ** 2)
    return predictions, coefficients, intercept, mse


class TestTaskFunc(unittest.TestCase):

    def test_output_shape(self):
        predictions, coefficients, intercept, mse = task_func(100, 10, random_seed=42)
        self.assertEqual(predictions.shape[0], 20)  # 20 is 20% of 100
        self.assertEqual(coefficients.shape[0], 10)  # Should match the number of features

    def test_mse_non_negativity(self):
        predictions, coefficients, intercept, mse = task_func(100, 10, random_seed=42)
        self.assertGreaterEqual(mse, 0.0)  # Mean Squared Error should be non-negative

    def test_coefficients_length(self):
        predictions, coefficients, intercept, mse = task_func(100, 5, random_seed=42)
        self.assertEqual(len(coefficients), 5)  # Coefficients length should equal n_features

    def test_intercept_type(self):
        predictions, coefficients, intercept, mse = task_func(150, 8, random_seed=123)
        self.assertIsInstance(intercept, float)  # Intercept should be of type float

    def test_predictions_values(self):
        predictions, coefficients, intercept, mse = task_func(100, 10, random_seed=42)
        self.assertTrue(isinstance(predictions, np.ndarray))  # Predictions should be numpy array
        self.assertTrue(np.all(np.isfinite(predictions)))  # Predictions should be finite numbers


if __name__ == '__main__':
    unittest.main()