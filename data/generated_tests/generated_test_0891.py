import unittest
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import os

# Here is your prompt:
def task_func(csv_file_path, attribute, test_size=0.2, random_state=42):
    """
    Train a linear regression model on a dataset and predict the value of a particular attribute.
    This function reads a CSV file to create a pandas DataFrame, separates the data into 
    training and testing sets, and performs linear regression. It returns the predicted 
    values for the testing set as well as the trained model.

    Parameters:
    csv_file_path (str): The path to the CSV file containing the data set.
    attribute (str): The attribute to predict.
    test_size (float, optional): Proportion of the dataset to include in the test split. Default is 0.2.
    random_state (int, optional): Seed used by the random number generator. Default is 42.

    Returns:
    tuple: A tuple containing:
        - model (LinearRegression): The trained linear regression model.
        - predictions (ndarray): An array of predicted values for the test set.

    Requirements:
    - pandas
    - sklearn.linear_model
    - sklearn.model_selection

    Note: The function assumes that the CSV file is correctly formatted and that the specified attribute exists.

    Example:
    >>> model, predictions = task_func("/path/to/data.csv", "target")
    >>> print(predictions)
    [123.45, ..., 126.78]
    """

    df = pd.read_csv(csv_file_path)
    X = df.drop(columns=[attribute])
    y = df[attribute]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    return model, predictions

class TestTaskFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up a temporary CSV file for testing."""
        cls.test_csv = 'test_data.csv'
        data = {
            'feature1': [1, 2, 3, 4, 5],
            'feature2': [5, 4, 3, 2, 1],
            'target': [2, 3, 5, 7, 11]
        }
        df = pd.DataFrame(data)
        df.to_csv(cls.test_csv, index=False)

    @classmethod
    def tearDownClass(cls):
        """Remove the temporary CSV file after tests."""
        os.remove(cls.test_csv)

    def test_return_type(self):
        """Test if the return type is correct."""
        model, predictions = task_func(self.test_csv, 'target')
        self.assertIsInstance(model, LinearRegression)
        self.assertIsInstance(predictions, np.ndarray)

    def test_predictions_size(self):
        """Test if the size of predictions is correct."""
        model, predictions = task_func(self.test_csv, 'target', test_size=0.4)
        self.assertEqual(predictions.size, 3)  # 3 predictions expected with 40% test size

    def test_linear_regression_model(self):
        """Test if the model is trained correctly by checking the coefficients."""
        model, _ = task_func(self.test_csv, 'target')
        self.assertGreater(len(model.coef_), 0)  # Ensure model has been fitted and coefficients exist

    def test_invalid_attribute(self):
        """Test if an error is raised for an invalid attribute."""
        with self.assertRaises(KeyError):
            task_func(self.test_csv, 'invalid_target')

    def test_model_persistence(self):
        """Test if the model can predict after being trained (consistency check)."""
        model1, predictions1 = task_func(self.test_csv, 'target')
        model2, predictions2 = task_func(self.test_csv, 'target')
        # Check that predictions are of the same length and similar (not equal due to randomness)
        self.assertEqual(predictions1.size, predictions2.size)
        self.assertTrue(np.allclose(predictions1, predictions2, rtol=1e-2))

if __name__ == '__main__':
    unittest.main()