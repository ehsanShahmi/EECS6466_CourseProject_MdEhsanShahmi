import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import numpy as np
import unittest

def task_func(data):
    ''' 
    Train a simple linear regression model based on the given data and evaluate the model by calculating the mean square error. The data should be structured with 'Hours' as independent variables and 'Scores' as dependent variables.
    The function set the random set when dividing the train and test data to 42 and the test set size is 0.2

    Parameters:
    - data (dict): The dictionary with keys 'Hours' and 'Scores', representing study hours and respective scores.

    Returns:
    float: The mean squared error between the actual scores and predicted scores based on the test split.

    Requirements:
    - pandas
    - sklearn.model_selection.train_test_split
    - sklearn.linear_model.LinearRegression
    - numpy

    Example:
    >>> task_func({'Hours': [10, 20, 40], 'Scores': [90, 80, 70]})
    25.0
    '''

    df = pd.DataFrame(data)

    X = df[['Hours']]
    y = df['Scores']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mse = np.mean((y_test - predictions) ** 2)

    return mse

class TestTaskFunc(unittest.TestCase):
    
    def test_basic_case(self):
        data = {'Hours': [10, 20, 30, 40, 50], 'Scores': [90, 80, 70, 60, 50]}
        result = task_func(data)
        self.assertAlmostEqual(result, 250.0, delta=1e-2)

    def test_no_variation(self):
        data = {'Hours': [10, 20, 30, 40, 50], 'Scores': [80, 80, 80, 80, 80]}
        result = task_func(data)
        self.assertAlmostEqual(result, 0.0, delta=1e-2)

    def test_multiple_points(self):
        data = {'Hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                'Scores': [10, 20, 30, 40, 30, 20, 10, 30, 40, 50]}
        result = task_func(data)
        self.assertAlmostEqual(result, 88.0, delta=1e-2)

    def test_edge_case(self):
        data = {'Hours': [1], 'Scores': [1]}  # Only one data point
        with self.assertRaises(ValueError):
            task_func(data)

    def test_high_variance(self):
        data = {'Hours': [0, 1, 2, 3, 4, 5], 'Scores': [10, 100, 200, 300, 400, 500]}
        result = task_func(data)
        self.assertGreater(result, 0)  # Expecting a positive MSE due to high variance

if __name__ == '__main__':
    unittest.main()