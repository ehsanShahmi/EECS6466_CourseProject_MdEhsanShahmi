import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import unittest

def task_func(df):
    """
    Divide the given DataFrame into a training set and a test set (70%: 30% split), separate the "target" column and return the four resulting DataFrames.

    Parameters:
    - df (pd.DataFrame): pandas DataFrame that contains a column named 'target'.

    Returns:
    - tuple: A tuple containing four DataFrames: X_train, X_test, y_train, y_test.
    """
    X = pd.DataFrame.drop(df, 'target', axis=1)
    y = pd.DataFrame(df['target'])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    return X_train, X_test, y_train, y_test

class TestTaskFunction(unittest.TestCase):

    def test_shape_of_outputs(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 5)), columns=list('ABCDE'))
        df['target'] = np.random.randint(0, 2, size=100)
        X_train, X_test, y_train, y_test = task_func(df)
        self.assertEqual(X_train.shape[0], 70)
        self.assertEqual(X_test.shape[0], 30)
        self.assertEqual(y_train.shape[0], 70)
        self.assertEqual(y_test.shape[0], 30)

    def test_target_column_existence(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 5)), columns=list('ABCDE'))
        df['target'] = np.random.randint(0, 2, size=100)
        X_train, X_test, y_train, y_test = task_func(df)
        self.assertIn('target', df.columns)

    def test_feature_columns_in_train_set(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 5)), columns=list('ABCDE'))
        df['target'] = np.random.randint(0, 2, size=100)
        X_train, X_test, y_train, y_test = task_func(df)
        self.assertTrue(set(df.columns[:-1]).issubset(X_train.columns))

    def test_output_data_types(self):
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 5)), columns=list('ABCDE'))
        df['target'] = np.random.randint(0, 2, size=100)
        X_train, X_test, y_train, y_test = task_func(df)
        self.assertIsInstance(X_train, pd.DataFrame)
        self.assertIsInstance(X_test, pd.DataFrame)
        self.assertIsInstance(y_train, pd.DataFrame)
        self.assertIsInstance(y_test, pd.DataFrame)

    def test_random_state_reproducibility(self):
        # Test for reproducibility of the split
        df = pd.DataFrame(np.random.randint(0, 100, size=(100, 5)), columns=list('ABCDE'))
        df['target'] = np.random.randint(0, 2, size=100)
        X_train1, X_test1, y_train1, y_test1 = task_func(df)
        X_train2, X_test2, y_train2, y_test2 = task_func(df)
        self.assertTrue(np.array_equal(X_train1, X_train2))
        self.assertTrue(np.array_equal(X_test1, X_test2))
        self.assertTrue(np.array_equal(y_train1, y_train2))
        self.assertTrue(np.array_equal(y_test1, y_test2))

if __name__ == '__main__':
    unittest.main()