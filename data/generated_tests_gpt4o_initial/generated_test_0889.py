import os
import pandas as pd
import numpy as np
import unittest

class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory and some CSV files for testing
        self.test_dir = "test_data"
        os.makedirs(self.test_dir, exist_ok=True)

        # Create a CSV file with data
        self.csv_file_with_data = os.path.join(self.test_dir, "data.csv")
        with open(self.csv_file_with_data, 'w') as f:
            f.write("Fruit,Taste,Cost\n")
            f.write("Apple,Good,1\n")
            f.write("Orange,,2\n")
            f.write("Avocado,Bad,2.5\n")
            f.write("Coconut,Tasty,\n")
        
        # Create an empty CSV file
        self.empty_csv_file = os.path.join(self.test_dir, "empty.csv")
        with open(self.empty_csv_file, 'w') as f:
            f.write("")
        
        # Non-existent file path
        self.non_existent_file = os.path.join(self.test_dir, "non_existent.csv")

    def test_load_data_with_nan(self):
        # Test loading data and replacing NaN values
        df = task_func(self.test_dir, "data.csv")
        expected_cost_mean = (1 + 2.5) / 2  # Mean of the Cost column excluding NaN
        expected_df = pd.DataFrame({
            'Fruit': ['Apple', 'Orange', 'Avocado', 'Coconut'],
            'Taste': ['Good', None, 'Bad', 'Tasty'],
            'Cost': [1.0, expected_cost_mean, 2.5, expected_cost_mean]
        })
        pd.testing.assert_frame_equal(df, expected_df)

    def test_load_empty_csv(self):
        # Test loading an empty CSV file
        df = task_func(self.test_dir, "empty.csv")
        pd.testing.assert_frame_equal(df, pd.DataFrame())

    def test_file_not_found(self):
        # Test for FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            task_func(self.test_dir, "non_existent.csv")

    def test_no_numeric_columns(self):
        # Test handling of a CSV file with no numeric columns
        no_numeric_file = os.path.join(self.test_dir, "no_numeric.csv")
        with open(no_numeric_file, 'w') as f:
            f.write("Fruit,Taste\n")
            f.write("Apple,Good\n")
            f.write("Orange,Great\n")
        
        df = task_func(self.test_dir, "no_numeric.csv")
        expected_df = pd.DataFrame({
            'Fruit': ['Apple', 'Orange'],
            'Taste': ['Good', 'Great']
        })
        pd.testing.assert_frame_equal(df, expected_df)

    def tearDown(self):
        # Remove the test directory and files after tests
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

if __name__ == '__main__':
    unittest.main()