import pandas as pd
import unittest
import os

# Here is your prompt:
import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def task_func(sheet_name, excel_file_location="test.xlsx", csv_file_location="test.csv"):
    """
    Reads data from an Excel spreadsheet, converts it to a CSV file, then calculates the sum of each column in the CSV file.

    Parameters:
    - sheet_name (str): The name of the sheet to load data from.
    - excel_file_location (str): The path to the Excel file. Default is 'test.xlsx'.
    - csv_file_location (str): The path where the CSV file will be saved. Default is 'test.csv'.

    Returns:
    - dict: A dictionary with the sum of each column.

    Raises:
    - FileNotFoundError: If the Excel file does not exist at the specified path.
    - ValueError: If the specified sheet name is not found in the Excel file.

    Requirements:
    - pandas
    - logging

    Example:
    >>> test_excel_file = 'dummy_test.xlsx'
    >>> test_csv_file = 'dummy_test.csv'
    >>> test_sheet_name = 'TestSheet'
    >>> data = {'A': [10, 20, 30], 'B': [40, 50, 60]}
    >>> df = pd.DataFrame(data)
    >>> df.to_excel(test_excel_file, sheet_name=test_sheet_name, index=False)
    >>> task_func(sheet_name='TestSheet', excel_file_location=test_excel_file, csv_file_location=test_csv_file) # {'Column1': sum_value1, 'Column2': sum_value2, ...}
    {'A': 60, 'B': 150}
    >>> os.remove(test_excel_file)
    >>> os.remove(test_csv_file)
    
    Note:
    - Ensure the Excel file contains only numerical data for accurate sum calculations.
    """


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a test Excel file before each test
        self.test_excel_file = 'dummy_test.xlsx'
        self.test_csv_file = 'dummy_test.csv'
        self.test_sheet_name = 'TestSheet'
        data = {'A': [10, 20, 30], 'B': [40, 50, 60]}
        self.df = pd.DataFrame(data)
        self.df.to_excel(self.test_excel_file, sheet_name=self.test_sheet_name, index=False)

    def tearDown(self):
        # Remove the test files created
        if os.path.exists(self.test_excel_file):
            os.remove(self.test_excel_file)
        if os.path.exists(self.test_csv_file):
            os.remove(self.test_csv_file)

    def test_sum_of_columns(self):
        expected_sum = {'A': 60, 'B': 150}
        result = task_func(sheet_name=self.test_sheet_name, excel_file_location=self.test_excel_file)
        self.assertEqual(result, expected_sum)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func(sheet_name=self.test_sheet_name, excel_file_location='non_existing_file.xlsx')

    def test_value_error_sheet_not_found(self):
        with self.assertRaises(ValueError):
            task_func(sheet_name='NonExistingSheet', excel_file_location=self.test_excel_file)

    def test_csv_creation(self):
        task_func(sheet_name=self.test_sheet_name, excel_file_location=self.test_excel_file, csv_file_location=self.test_csv_file)
        self.assertTrue(os.path.exists(self.test_csv_file))

    def test_empty_excel_file(self):
        # Create an empty Excel file
        empty_test_excel_file = 'empty_test.xlsx'
        pd.DataFrame().to_excel(empty_test_excel_file, sheet_name=self.test_sheet_name, index=False)
        with self.assertRaises(ValueError):
            task_func(sheet_name=self.test_sheet_name, excel_file_location=empty_test_excel_file)
        os.remove(empty_test_excel_file)

# This will allow the test suite to run
if __name__ == '__main__':
    unittest.main()