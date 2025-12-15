import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import unittest

class TestTaskFunc(unittest.TestCase):

    def test_basic_normalization(self):
        data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
        expected_result = pd.DataFrame({'a': [0.0, 0.5, 1.0], 'b': [0.0, 0.5, 1.0]})
        result = task_func(data, ['a', 'b'])
        pd.testing.assert_frame_equal(result, expected_result)

    def test_single_column_normalization(self):
        data = {'a': [10, 20, 30], 'b': [5, 15, 25]}
        expected_result = pd.DataFrame({'a': [0.0, 0.5, 1.0], 'b': [0.0, 0.5, 1.0]})
        result = task_func(data, ['a', 'b'])
        pd.testing.assert_frame_equal(result, expected_result)

    def test_no_columns_to_normalize(self):
        data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
        result = task_func(data, [])
        expected_result = pd.DataFrame(data)
        pd.testing.assert_frame_equal(result, expected_result)

    def test_empty_dataframe(self):
        data = {}
        expected_result = pd.DataFrame(columns=[])
        result = task_func(data, ['a'])
        pd.testing.assert_frame_equal(result, expected_result)

    def test_invalid_column_names(self):
        data = {'a': [1, 2, 3], 'b': [4, 5, 6]}
        with self.assertRaises(KeyError):
            task_func(data, ['c'])  # 'c' does not exist in data

if __name__ == '__main__':
    unittest.main()