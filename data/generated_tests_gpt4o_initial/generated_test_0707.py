import json
import numpy as np
import pandas as pd
import unittest
import os


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create a temporary DataFrame for testing."""
        self.df = pd.DataFrame({'IntCol': [10, 100, 1000, 10000, 100000]})

    def tearDown(self):
        """Remove the generated JSON file if it exists."""
        if os.path.exists('IntCol.json'):
            os.remove('IntCol.json')

    def test_transform_values(self):
        """Test if the logarithm transformation is applied correctly."""
        transformed_df = task_func(self.df.copy())
        expected_values = [1.0, 2.0, 3.0, 4.0, 5.0]
        np.testing.assert_array_almost_equal(transformed_df['IntCol'].values, expected_values)

    def test_json_file_creation(self):
        """Test if the JSON file is created."""
        task_func(self.df.copy())
        self.assertTrue(os.path.exists('IntCol.json'))

    def test_json_file_content(self):
        """Test if the JSON file contains the correct transformed values."""
        task_func(self.df.copy())
        with open('IntCol.json', 'r') as json_file:
            content = json.load(json_file)
            expected_content = [1.0, 2.0, 3.0, 4.0, 5.0]
            self.assertEqual(content, expected_content)

    def test_returned_dataframe_structure(self):
        """Test if the returned DataFrame structure is correct."""
        transformed_df = task_func(self.df.copy())
        self.assertEqual(transformed_df.shape, (5, 1))
        self.assertIn('IntCol', transformed_df.columns)

    def test_function_with_empty_dataframe(self):
        """Test the function with an empty DataFrame."""
        empty_df = pd.DataFrame(columns=['IntCol'])
        transformed_df = task_func(empty_df.copy())
        self.assertTrue(transformed_df.empty)
        self.assertEqual(transformed_df.shape, (0, 1))  # Structurally it should have one column


if __name__ == '__main__':
    unittest.main()