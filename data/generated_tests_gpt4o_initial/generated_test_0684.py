import pandas as pd
import numpy as np
import unittest

class TestTaskFunc(unittest.TestCase):

    def test_remove_column(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        result_df = task_func(df, 'C')
        self.assertNotIn('C', result_df.columns)
        
    def test_is_even_index_column(self):
        df = pd.DataFrame({'A': [1, 2, 3]})
        result_df = task_func(df, 'A')
        expected_index_values = [True, False]
        self.assertTrue((result_df['IsEvenIndex'].values == expected_index_values).all())
        
    def test_dataframe_shape(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
        result_df = task_func(df, 'B')
        self.assertEqual(result_df.shape, (3, 2))  # 3 rows, 2 columns after removal
        
    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['A', 'B', 'C'])
        result_df = task_func(df, 'B')
        self.assertTrue(result_df.empty)  # Confirm the result is still an empty DataFrame
    
    def test_non_existent_column(self):
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        with self.assertRaises(KeyError):
            task_func(df, 'C')  # Assuming it raises KeyError for nonexistent column

if __name__ == '__main__':
    unittest.main()