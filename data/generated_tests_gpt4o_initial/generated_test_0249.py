import pandas as pd
import random
from sklearn.model_selection import train_test_split
import unittest

# Here is your prompt:
# (The function task_func is not defined here as per your request)

class TestTaskFunc(unittest.TestCase):

    def test_default_values(self):
        random.seed(0)
        train_data, test_data = task_func()
        self.assertEqual(train_data.shape[0], 8000)
        self.assertEqual(test_data.shape[0], 2000)

    def test_specific_values(self):
        random.seed(0)
        train_data, test_data = task_func(n_data_points=500, min_value=1.0, max_value=1.0, test_size=0.3)
        self.assertEqual(train_data.shape[0], 350)
        self.assertEqual(test_data.shape[0], 150)
        self.assertEqual(test_data.iloc[0]['Value'], 1.0)

    def test_data_range(self):
        random.seed(0)
        train_data, test_data = task_func(n_data_points=1000, min_value=0.0, max_value=10.0)
        self.assertTrue((train_data['Value'] >= 0.0).all() and (train_data['Value'] <= 10.0).all())
        self.assertTrue((test_data['Value'] >= 0.0).all() and (test_data['Value'] <= 10.0).all())

    def test_train_test_split_size(self):
        random.seed(0)
        train_data, test_data = task_func(n_data_points=10000, test_size=0.25)
        self.assertEqual(train_data.shape[0], 7500)
        self.assertEqual(test_data.shape[0], 2500)

    def test_truncation_of_values(self):
        random.seed(0)
        train_data, test_data = task_func()
        self.assertTrue(all(train_data['Value'].apply(lambda x: len(str(x).split('.')[1]) <= 3)))
        self.assertTrue(all(test_data['Value'].apply(lambda x: len(str(x).split('.')[1]) <= 3)))

if __name__ == '__main__':
    unittest.main()