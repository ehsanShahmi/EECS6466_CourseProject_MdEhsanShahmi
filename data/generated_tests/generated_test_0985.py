import unittest
import pandas as pd
import os
import json

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.output_dir = "./test_output"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def tearDown(self):
        # Clean up any generated files after each test
        for file in os.listdir(self.output_dir):
            file_path = os.path.join(self.output_dir, file)
            os.remove(file_path)
        os.rmdir(self.output_dir)

    def test_valid_json_data(self):
        json_data = '{"Countries": {"Country A": 331002651, "Country B": 67886011}}'
        csv_file_path, df = task_func(json_data, self.output_dir)
        
        self.assertTrue(os.path.exists(csv_file_path))
        self.assertEqual(df.shape, (2, 2))
        self.assertEqual(list(df.columns), ["Country", "Population"])
        self.assertEqual(df["Country"].tolist(), ["Country A", "Country B"])
        self.assertEqual(df["Population"].tolist(), [331002651, 67886011])

    def test_json_data_with_float_population(self):
        json_data = '{"Countries": {"Country A": 331002651.0, "Country B": 67886011.5}}'
        csv_file_path, df = task_func(json_data, self.output_dir)
        
        self.assertTrue(os.path.exists(csv_file_path))
        self.assertEqual(df["Population"].tolist(), [331002651, 67886011])  # Check rounding down

    def test_json_data_with_negative_population(self):
        json_data = '{"Countries": {"Country A": -331002651, "Country B": 67886011}}'
        
        with self.assertRaises(ValueError) as context:
            task_func(json_data, self.output_dir)
        self.assertEqual(str(context.exception), "Population cannot be negative.")

    def test_malformed_json_data(self):
        json_data = '{"Countries": {"Country A": "not_a_number", "Country B": 67886011}}'
        
        with self.assertRaises(ValueError) as context:
            task_func(json_data, self.output_dir)
        self.assertTrue("Population must be an integer." in str(context.exception))

    def test_empty_json_data(self):
        json_data = '{"Countries": {}}'
        
        with self.assertRaises(ValueError) as context:
            task_func(json_data, self.output_dir)
        self.assertEqual(str(context.exception), "No valid country population data found in JSON.")

if __name__ == '__main__':
    unittest.main()