import os
import pandas as pd
import numpy as np
import unittest

# Here is your prompt:
def task_func(excel_file_path, file_name, column_name):
    """
    Calculate the mean, median, and standard deviation of the data from a specific column in an Excel file.

    Parameters:
    - excel_file_path (str): The path to the directory containing the Excel file.
    - file_name (str): The name of the Excel file.
    - column_name (str): The name of the column to analyze.

    Returns:
    - dict: A dictionary with the mean, median, and standard deviation.

    Raises:
    - FileNotFoundError: If the Excel file does not exist at the specified path.
    - ValueError: If the specified column is not found in the Excel file.

    Requirements:
    - pandas
    - numpy
    - os 
    """

    excel_file = os.path.join(excel_file_path, file_name)
    if not os.path.exists(excel_file):
        raise FileNotFoundError(f"No file found at {excel_file}")

    df = pd.read_excel(excel_file)
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the Excel file.")

    mean = np.mean(df[column_name])
    median = np.median(df[column_name])
    std_dev = np.std(df[column_name])

    return {'mean': mean, 'median': median, 'std_dev': std_dev}

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        """Set up a sample Excel file for testing purposes."""
        self.test_dir = './test_data/'
        os.makedirs(self.test_dir, exist_ok=True)
        self.test_file = os.path.join(self.test_dir, 'test_file.xlsx')
        
        # Create a DataFrame and save it as an Excel file
        test_data = {'Sales': [100, 200, 300, 400, 500]}
        df = pd.DataFrame(test_data)
        df.to_excel(self.test_file, index=False)
    
    def tearDown(self):
        """Remove the test directory and file after tests."""
        os.remove(self.test_file)
        os.rmdir(self.test_dir)
    
    def test_valid_data(self):
        result = task_func(self.test_dir, 'test_file.xlsx', 'Sales')
        expected = {'mean': 300.0, 'median': 300.0, 'std_dev': 141.4213562373095}
        self.assertEqual(result, expected)
    
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func(self.test_dir, 'non_existent_file.xlsx', 'Sales')
    
    def test_column_not_found(self):
        with self.assertRaises(ValueError):
            task_func(self.test_dir, 'test_file.xlsx', 'NonExistentColumn')
    
    def test_empty_column(self):
        """Test the function with an Excel file containing an empty column."""
        empty_data = {'Sales': []}  # Empty column
        df = pd.DataFrame(empty_data)
        df.to_excel(self.test_file, index=False)

        with self.assertRaises(ValueError):
            task_func(self.test_dir, 'test_file.xlsx', 'Sales')
    
    def test_non_numeric_data(self):
        """Test the function with non-numeric data in the column."""
        non_numeric_data = {'Sales': ['a', 'b', 'c']}  # Non-numeric values
        df = pd.DataFrame(non_numeric_data)
        df.to_excel(self.test_file, index=False)

        with self.assertRaises(ValueError):
            task_func(self.test_dir, 'test_file.xlsx', 'Sales')

if __name__ == '__main__':
    unittest.main()