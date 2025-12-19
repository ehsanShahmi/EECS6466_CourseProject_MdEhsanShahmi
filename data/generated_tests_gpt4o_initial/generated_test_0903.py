import pandas as pd
from sklearn.linear_model import LinearRegression
import unittest

def task_func(d, target='z'):
    df = pd.DataFrame(d)
    predictors = [k for k in df.columns if k != target]
    
    X = df[predictors]
    y = df[target]
    
    model = LinearRegression().fit(X, y)
    
    return model

class TestTaskFunc(unittest.TestCase):

    def test_model_type(self):
        data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
        model = task_func(data)
        self.assertIsInstance(model, LinearRegression)

    def test_predictors_excluded(self):
        data = [{'x': 4, 'y': 20, 'z': 10}, {'x': 5, 'y': 25, 'z': 15}, {'x': 6, 'y': 5, 'z': 20}]
        model = task_func(data, target='y')
        self.assertEqual(model.coef_.shape[0], 1)  # Expecting 1 predictor 'x' only

    def test_multiple_predictors(self):
        data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 4, 'y': 5, 'z': 6}, {'x': 7, 'y': 8, 'z': 9}]
        model = task_func(data)
        self.assertEqual(len(model.coef_), 2)  # Expecting 2 predictors 'x' and 'y'

    def test_target_variable(self):
        data = [{'x': 1, 'y': 2, 'z': 3}, {'x': 2, 'y': 4, 'z': 6}, {'x': 3, 'y': 6, 'z': 9}]
        model = task_func(data, target='z')
        self.assertAlmostEqual(model.predict([[1, 2]])[0], 3)  # Check prediction matches

    def test_empty_data(self):
        data = []
        with self.assertRaises(ValueError):  # Expecting ValueError for fitting on empty data
            task_func(data)

if __name__ == '__main__':
    unittest.main()