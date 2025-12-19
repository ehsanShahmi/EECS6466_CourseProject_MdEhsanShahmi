import unittest
import os
import pandas as pd
import matplotlib.pyplot as plt

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create a temporary CSV file for testing."""
        self.test_file_valid = 'test_data.csv'
        self.test_file_invalid = 'test_data.txt'
        self.test_data = """name,age,city
Alice,25,New York
Bob,30,London
Alice,25,New York
Bob,30,London
Alice,25,New York
Charlie,35,Paris
"""
        with open(self.test_file_valid, 'w') as f:
            f.write(self.test_data)

    def tearDown(self):
        """Remove the temporary files created for testing."""
        if os.path.exists(self.test_file_valid):
            os.remove(self.test_file_valid)
        if os.path.exists(self.test_file_invalid):
            os.remove(self.test_file_invalid)

    def test_valid_csv_input(self):
        """Test with a valid CSV file containing duplicates."""
        from task_module import task_func  # Assuming the function is defined in task_module
        duplicates, ax = task_func(self.test_file_valid)
        self.assertIsInstance(duplicates, dict)
        self.assertIn(('Alice', '25', 'New York'), duplicates)
        self.assertIn(('Bob', '30', 'London'), duplicates)
        self.assertEqual(duplicates[('Alice', '25', 'New York')], 3)
        self.assertEqual(duplicates[('Bob', '30', 'London')], 2)

    def test_invalid_file_format(self):
        """Test with an invalid file format."""
        from task_module import task_func  # Assuming the function is defined in task_module
        with self.assertRaises(ValueError) as context:
            task_func(self.test_file_invalid)
        self.assertEqual(str(context.exception), "Invalid file format. Only .csv files are accepted.")

    def test_empty_csv(self):
        """Test with an empty CSV file."""
        empty_file = 'empty_data.csv'
        with open(empty_file, 'w') as f:
            pass  # Create an empty file

        from task_module import task_func  # Assuming the function is defined in task_module
        duplicates, ax = task_func(empty_file)
        self.assertEqual(duplicates, {})
        plt.close(ax.figure)  # Close the plot created during the test

        os.remove(empty_file)

    def test_no_duplicates_in_csv(self):
        """Test with a CSV file that has no duplicates."""
        unique_data = """name,age,city
Alice,25,New York
Bob,30,London
Charlie,35,Paris
"""
        unique_file = 'unique_data.csv'
        with open(unique_file, 'w') as f:
            f.write(unique_data)

        from task_module import task_func  # Assuming the function is defined in task_module
        duplicates, ax = task_func(unique_file)
        self.assertEqual(duplicates, {})
        plt.close(ax.figure)  # Close the plot created during the test

        os.remove(unique_file)

if __name__ == '__main__':
    unittest.main()