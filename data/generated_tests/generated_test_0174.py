import unittest
import pandas as pd
import numpy as np

class TestTaskFunc(unittest.TestCase):
    
    def test_valid_dataframe(self):
        np.random.seed(0)
        data = pd.DataFrame({'key1': ['value1', 'value2', 'value3'], 'key2': [1, 2, 3]})
        updated_data = task_func(data, 'new_key', 0, 10)
        self.assertTrue('new_key' in updated_data.columns)
        self.assertEqual(len(updated_data), 3)

    def test_random_values_within_range(self):
        np.random.seed(0)
        data = pd.DataFrame({'key1': ['value1', 'value2', 'value3'], 'key2': [1, 2, 3]})
        min_value, max_value = 0, 10
        updated_data = task_func(data, 'new_key', min_value, max_value)
        self.assertTrue((updated_data['new_key'] >= min_value).all())
        self.assertTrue((updated_data['new_key'] <= max_value).all())
    
    def test_invalid_dataframe_type(self):
        with self.assertRaises(ValueError) as context:
            task_func("Not a dataframe", 'new_key', 0, 10)
        self.assertEqual(str(context.exception), "Input 'data' must be a pandas DataFrame.")

    def test_empty_dataframe(self):
        data = pd.DataFrame(columns=['key1', 'key2'])
        updated_data = task_func(data, 'new_key', 0, 10)
        self.assertTrue('new_key' in updated_data.columns)
        self.assertEqual(len(updated_data), 0)

    def test_large_range_of_random_values(self):
        np.random.seed(0)
        data = pd.DataFrame({'key1': ['value1', 'value2', 'value3'], 'key2': [1, 2, 3]})
        min_value, max_value = 1, 1000
        updated_data = task_func(data, 'new_key', min_value, max_value)
        self.assertTrue((updated_data['new_key'] >= min_value).all())
        self.assertTrue((updated_data['new_key'] <= max_value).all())

if __name__ == '__main__':
    unittest.main()