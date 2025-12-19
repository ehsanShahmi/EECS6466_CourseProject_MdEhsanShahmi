import unittest
import os
import pandas as pd
from texttable import Texttable
import glob


# Here is your prompt:
def task_func(data_dir='./data/'):
    """
    Generates a summary table of all ascendingly sorted CSV files in a specified directory using Texttable. 
    If an empty CSV file is encountered, a pandas.errors.EmptyDataError is raised.

    Parameters:
    - data_dir (str): The directory to search for CSV files. Default is './data/'.

    Returns:
    - str: A string representation of the table summarizing the CSV files. Each row contains the file name, number of rows, and number of columns.

    Raises:
    - FileNotFoundError: If the specified directory does not exist.
    - ValueError: If there are no CSV files in the specified directory.
    - pandas.errors.EmptyDataError: If an empty CSV file is encountered.

    Requirements:
    - pandas
    - texttable
    - os
    - glob

    Example:
    >>> data_dir = './test_data/'
    >>> dummy_files = create_dummy_files(data_dir)
    >>> print(task_func(data_dir))
    +-----------+------+---------+
    |   File    | Rows | Columns |
    +===========+======+=========+
    | test2.csv | 10   | 4       |
    +-----------+------+---------+
    | test2.csv | 10   | 4       |
    +-----------+------+---------+
    | test1.csv | 5    | 2       |
    +-----------+------+---------+
    | test1.csv | 5    | 2       |
    +-----------+------+---------+
    >>> tear_down_dummy_files(data_dir, dummy_files)
    """

    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"The directory '{data_dir}' does not exist.")

    data_files = sorted(glob.glob(os.path.join(data_dir, '*.csv')))
    if not data_files:
        raise ValueError(f"No CSV files found in the directory '{data_dir}'.")

    summary_data = []
    for file in data_files:
        try:
            data = pd.read_csv(file)
            summary_data.append([os.path.basename(file), data.shape[0], data.shape[1]])
        except pd.errors.EmptyDataError:
            # Handle empty CSV file
            raise pd.errors.EmptyDataError(f"Error when reading file '{file}'.")
        data = pd.read_csv(file)
        summary_data.append([os.path.basename(file), data.shape[0], data.shape[1]])

    table = Texttable()
    table.add_rows([['File', 'Rows', 'Columns']] + summary_data)

    return table.draw()

# Test Suite
class TestTaskFunction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = './test_data/'
        os.makedirs(cls.test_dir, exist_ok=True)

        # Creating test CSV files
        cls.csv_file_1 = os.path.join(cls.test_dir, 'test1.csv')
        cls.csv_file_2 = os.path.join(cls.test_dir, 'test2.csv')

        # Write some test data to CSV files
        pd.DataFrame({'A': [1, 2], 'B': [3, 4]}).to_csv(cls.csv_file_1, index=False)
        pd.DataFrame({'A': [5, 6, 7, 8, 9, 10], 'B': [11, 12, 13, 14, 15, 16], 'C': [17, 18, 19, 20, 21, 22], 'D': [23, 24, 25, 26, 27, 28]}).to_csv(cls.csv_file_2, index=False)

    @classmethod
    def tearDownClass(cls):
        for f in os.listdir(cls.test_dir):
            os.remove(os.path.join(cls.test_dir, f))
        os.rmdir(cls.test_dir)

    def test_valid_directory_with_csv_files(self):
        expected_output = "+-----------+------+---------+\n" \
                          "|   File    | Rows | Columns |\n" \
                          "+===========+======+=========+\n" \
                          "| test1.csv | 2    | 2       |\n" \
                          "+-----------+------+---------+\n" \
                          "| test2.csv | 6    | 4       |\n" \
                          "+-----------+------+---------+"
        actual_output = task_func(self.test_dir)
        self.assertEqual(expected_output, actual_output.strip())

    def test_empty_directory(self):
        empty_dir = './empty_test_data/'
        os.makedirs(empty_dir, exist_ok=True)
        with self.assertRaises(ValueError):
            task_func(empty_dir)
        os.rmdir(empty_dir)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func('./non_existent_directory/')

    def test_empty_csv_file(self):
        empty_csv_file = os.path.join(self.test_dir, 'empty.csv')
        pd.DataFrame().to_csv(empty_csv_file, index=False)
        with self.assertRaises(pd.errors.EmptyDataError):
            task_func(self.test_dir)

    def test_multiple_csv_files(self):
        additional_csv_file = os.path.join(self.test_dir, 'test3.csv')
        pd.DataFrame({'X': [1, 2, 3], 'Y': [4, 5, 6]}).to_csv(additional_csv_file, index=False)
        
        expected_output = "+-----------+------+---------+\n" \
                          "|   File    | Rows | Columns |\n" \
                          "+===========+======+=========+\n" \
                          "| test1.csv | 2    | 2       |\n" \
                          "+-----------+------+---------+\n" \
                          "| test2.csv | 6    | 4       |\n" \
                          "+-----------+------+---------+\n" \
                          "| test3.csv | 3    | 2       |\n" \
                          "+-----------+------+---------+"
        actual_output = task_func(self.test_dir)
        self.assertEqual(expected_output, actual_output.strip())        
        

if __name__ == '__main__':
    unittest.main()