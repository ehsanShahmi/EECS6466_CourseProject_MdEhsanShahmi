import os
import pandas as pd
import unittest
from datetime import datetime

# Here is your prompt:
# (The prompt code remains intact and is not modified in any way)
import os
import pandas as pd
from datetime import datetime

def task_func(excel_directory: str, file_name: str, column_name: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Filters data in a specific date range from a column in an Excel file and returns a Pandas DataFrame of the filtered data.

    Parameters:
    excel_directory (str): The directory of the Excel file.
    file_name (str): The name of the Excel file.
    column_name (str): The name of the date column to filter.
    start_date (str): The start date in 'yyyy-mm-dd' format.
    end_date (str): The end date in 'yyyy-mm-dd' format.

    Returns:
    pd.DataFrame: A pandas DataFrame with the filtered data.

    Raises:
    FileNotFoundError: If the specified Excel file does not exist.
    ValueError: If start_date or end_date are in an incorrect format, or if column_name does not exist in the DataFrame.

    Example:
    >>> data_dir, file_name = './excel_files/', 'excel_file1.xls'
    >>> test_file = create_dummy_file(data_dir, file_name)
    >>> filtered_df = task_func(data_dir, file_name, 'Date', '2020-01-01', '2020-12-31')
    >>> os.remove(test_file)
    >>> os.rmdir(data_dir)
    >>> print(filtered_df.head())
       Unnamed: 0       Date     Value
    0           0 2020-01-01  0.823110
    1           1 2020-01-02  0.026118
    2           2 2020-01-03  0.210771
    3           3 2020-01-04  0.618422
    4           4 2020-01-05  0.098284
    
    Requirements:
    - os
    - pandas
    - datetime
    """

class TestTaskFunc(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Setup code to create dummy Excel files for testing
        cls.test_dir = './test_excel_files'
        os.makedirs(cls.test_dir, exist_ok=True)
        cls.file_name = 'test_data.xlsx'
        
        # Creating a sample dataframe and saving it as an Excel file
        data = {
            'Date': pd.date_range(start='2020-01-01', end='2020-12-31'),
            'Value': pd.np.random.rand(366)
        }
        df = pd.DataFrame(data)
        df.to_excel(os.path.join(cls.test_dir, cls.file_name), index=False)

    @classmethod
    def tearDownClass(cls):
        # Cleanup the test directory and files
        os.remove(os.path.join(cls.test_dir, cls.file_name))
        os.rmdir(cls.test_dir)

    def test_valid_date_range(self):
        """Test filtering within a valid date range."""
        result_df = task_func(self.test_dir, self.file_name, 'Date', '2020-01-01', '2020-01-31')
        self.assertEqual(len(result_df), 31)
        self.assertTrue((result_df['Date'] >= '2020-01-01').all() and (result_df['Date'] <= '2020-01-31').all())

    def test_non_existent_file(self):
        """Test handling a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            task_func(self.test_dir, 'non_existent_file.xlsx', 'Date', '2020-01-01', '2020-01-31')

    def test_invalid_column_name(self):
        """Test handling an invalid column name."""
        with self.assertRaises(ValueError):
            task_func(self.test_dir, self.file_name, 'InvalidColumn', '2020-01-01', '2020-01-31')

    def test_invalid_date_format(self):
        """Test handling an invalid date format."""
        with self.assertRaises(ValueError):
            task_func(self.test_dir, self.file_name, 'Date', '01-01-2020', '2020-01-31')

    def test_empty_result(self):
        """Test for an empty result when no dates match the criteria."""
        result_df = task_func(self.test_dir, self.file_name, 'Date', '2019-01-01', '2019-01-31')
        self.assertTrue(result_df.empty)

if __name__ == '__main__':
    unittest.main()