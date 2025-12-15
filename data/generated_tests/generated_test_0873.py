import csv
import os
import unittest

def task_func(data, file_path, headers):
    """
    Writes a list of tuples to a CSV file.

    Each tuple in the 'data' list represents a row in the CSV file, with each 
    element of the tuple corresponding to a cell in the row. If a tuple contains
    fewer elements than there are headers, the missing elements are filled with None.

    Parameters:
        data (list of tuples): A list of tuples with each tuple representing a row of data.
        file_path (str): The complete file path where the CSV file will be saved. If the file already exists, it will be overwritten.
        headers (list of str): A list of strings representing the headers (column names) in the CSV file.

    Returns:
        str: The absolute path of the saved CSV file.

    Raises:
        ValueError: If 'file_path' is None.

    Requirements:
    - csv
    - os
    """

    if file_path is None:
        raise ValueError("The file path is invalid.")

    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for row in data:
            if len(row) < len(headers):
                row += (None,) * (len(headers) - len(row))
            writer.writerow(row)
    return os.path.abspath(file_path)

class TestCSVWriter(unittest.TestCase):

    def setUp(self):
        self.test_file_path = 'test_output.csv'
        self.test_file_path2 = 'test_output2.csv'
        self.headers = ['a', 'b', 'c']
        self.data = [(1, 'a', 2), ('a', 3, 5), ('c', 1, -2)]
        self.data_incomplete = [(1, 'a'), (3,), ('c', -2)]
    
    def tearDown(self):
        """Cleanup CSV files after tests"""
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
        if os.path.exists(self.test_file_path2):
            os.remove(self.test_file_path2)

    def test_csv_creation(self):
        full_path = task_func(self.data, self.test_file_path, self.headers)
        self.assertTrue(os.path.isfile(full_path))

    def test_incomplete_data(self):
        task_func(self.data_incomplete, self.test_file_path, self.headers)
        with open(self.test_file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertEqual(rows[1], ['1', 'a', '2'])
            self.assertEqual(rows[2], ['a', '3', '5'])
            self.assertEqual(rows[3], ['c', '1', '-2'])

    def test_write_empty_data(self):
        task_func([], self.test_file_path, self.headers)
        with open(self.test_file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertEqual(rows, [['a', 'b', 'c']])

    def test_value_error_on_none_file_path(self):
        with self.assertRaises(ValueError):
            task_func(self.data, None, self.headers)

    def test_overwrite_file(self):
        task_func(self.data, self.test_file_path, self.headers)
        task_func(self.data_incomplete, self.test_file_path, self.headers)
        with open(self.test_file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertEqual(rows[1], ['1', 'a', 'None'])
            self.assertEqual(rows[2], ['None', 'None', 'None']) # The last row is expected to be three Nones

if __name__ == '__main__':
    unittest.main()