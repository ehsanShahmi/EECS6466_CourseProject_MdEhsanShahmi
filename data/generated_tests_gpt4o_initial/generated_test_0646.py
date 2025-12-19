import os
import pandas as pd
import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
from dateutil.parser import parse

OUTPUT_DIR = './output'

def task_func(csv_path=os.path.join(OUTPUT_DIR, 'data.csv'), date_column='date'):
    """
    Read a CSV file, convert a column of date strings into datetime objects,
    and draw a histogram of the year distribution of these dates.

    Parameters:
    - csv_path (str): The path to the CSV file. Default is the 'data.csv' in the script's directory.
    - date_column (str): The column in the CSV file with the date strings. Default is 'date'.

    Returns:
    - matplotlib.axes._axes.Axes: A histogram plot object showing the distribution of years.

    Requirements:
    - pandas
    - dateutil.parser
    - os

    Example:
    >>> import os
    >>> from unittest.mock import patch
    >>> with patch('os.path.exists', return_value=False):
    ...     task_func('nonexistent.csv')
    Traceback (most recent call last):
        ...
    FileNotFoundError: nonexistent.csv does not exist
    """

           
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"{csv_path} does not exist")

    df = pd.read_csv(csv_path)
    df[date_column] = df[date_column].apply(lambda x: parse(x))

    return df[date_column].dt.year.hist()

# Test Suite
class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a sample CSV file for testing
        self.test_csv_path = os.path.join(OUTPUT_DIR, 'test_data.csv')
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        self.test_data = pd.DataFrame({
            'date': ['2021-01-01', '2021-06-15', '2022-03-20', '2020-08-05']
        })
        self.test_data.to_csv(self.test_csv_path, index=False)

    def tearDown(self):
        # Cleanup the test CSV file
        if os.path.isfile(self.test_csv_path):
            os.remove(self.test_csv_path)
        if os.path.isdir(OUTPUT_DIR) and not os.listdir(OUTPUT_DIR):
            os.rmdir(OUTPUT_DIR)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func('nonexistent.csv')

    def test_date_parsing(self):
        result = task_func(self.test_csv_path)
        self.assertIsNotNone(result)
        self.assertEqual(result.get_children()[0].get_xdata().tolist(), [2020, 2021, 2022])
    
    def test_default_date_column(self):
        result = task_func(self.test_csv_path)
        self.assertIsNotNone(result)

    def test_custom_date_column(self):
        # Test with a different column name
        self.test_data['custom_date'] = ['2021-01-01', '2021-06-15', '2022-03-20', '2020-08-05']
        self.test_data.to_csv(self.test_csv_path, index=False)
        result = task_func(self.test_csv_path, date_column='custom_date')
        self.assertIsNotNone(result)

    def test_empty_csv(self):
        empty_csv_path = os.path.join(OUTPUT_DIR, 'empty_data.csv')
        pd.DataFrame().to_csv(empty_csv_path, index=False)
        with self.assertRaises(ValueError):
            task_func(empty_csv_path)

if __name__ == '__main__':
    unittest.main()