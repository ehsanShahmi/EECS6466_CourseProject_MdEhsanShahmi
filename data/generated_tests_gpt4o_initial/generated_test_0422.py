import pandas as pd
from sklearn.model_selection import train_test_split
import unittest

def task_func(df, target_column, column_to_remove="c", test_size=0.2):
    df = pd.DataFrame(df)
    
    if column_to_remove in df.columns:
        df = df.drop(columns=column_to_remove)

    X_train, X_test, y_train, y_test = train_test_split(
        df.drop(columns=target_column), df[target_column], test_size=test_size
    )

    return X_train, X_test, y_train, y_test

class TestTaskFunc(unittest.TestCase):

    def test_simple_case(self):
        data = {
            'a': [1, 2, 3, 4],
            'b': [5, 6, 7, 8],
            'c': [9, 10, 11, 12],
            'target': [0, 1, 0, 1]
        }
        X_train, _, _, _ = task_func(data, 'target')
        self.assertEqual(type(X_train), pd.DataFrame)
        self.assertEqual(X_train.shape[1], 2)  # 'c' column should be removed

    def test_removing_non_existent_column(self):
        data = {
            'x1': [10, 20, 30, 40],
            'x2': [50, 60, 70, 80],
            'target': [1, 2, 3, 4]
        }
        X_train, _, _, y_test = task_func(data, 'target', 'non_existent_column')
        self.assertEqual(type(y_test), pd.Series)
        self.assertEqual(y_test.shape[0], 1)  # Test size will still be honored

    def test_custom_test_size(self):
        data = {
            'p': [2, 4, 6, 8],
            'q': [10, 20, 30, 40],
            'r': [3, 1, 4, 2],
            'label': [1, 0, 1, 0]
        }
        _, _, _, y_test = task_func(data, 'label', test_size=0.25)
        self.assertEqual(y_test.shape[0], 1)  # 1 row should be in the test set

    def test_no_target_column(self):
        data = {
            'm': [7, 8, 9],
            'n': [14, 15, 16]
        }
        with self.assertRaises(KeyError):
            task_func(data, 'missing_target')

    def test_multiple_columns(self):
        data = {
            'f1': [0, 1, 2, 3],
            'f2': [4, 5, 6, 7],
            'f3': [8, 9, 10, 11],
            'target': [1, 0, 1, 0]
        }
        X_train, X_test, y_train, y_test = task_func(data, 'target', column_to_remove='f2')
        self.assertNotIn('f2', X_train.columns)
        self.assertEqual(X_train.shape[1], 2)  # One column dropped

if __name__ == '__main__':
    unittest.main()