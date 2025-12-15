import unittest
import os
from collections import OrderedDict

# Constants
FIELDS = ['ID', 'Name', 'Age']

# Here is the provided prompt
def task_func(values, filename):
    """
    Writes a list of OrderedDicts to an Excel file. Each OrderedDict in the list represents a row in the Excel sheet,
    and each key in the OrderedDict corresponds to a column defined in the FIELDS constant comprising column names 
    'ID', 'Name', and 'Age'.

    Parameters:
    values (list of OrderedDict): A list where each element is an OrderedDict with keys matching the FIELDS constant.
    filename (str): The filename for the Excel file to be created. It should include the '.xls' extension.

    Returns:
    str: The absolute path of the created Excel file.

    Requirements:
    - xlwt
    - os

    Examples:
    Create an Excel file with data from a list of OrderedDicts.
    >>> data = [OrderedDict([('ID', 1), ('Name', 'John Doe'), ('Age', 30)]),
    ...         OrderedDict([('ID', 2), ('Name', 'Jane Doe'), ('Age', 28)])]
    >>> path = task_func(data, 'test_data.xls')
    >>> os.path.exists(path) and 'test_data.xls' in path
    True

    Create an Excel file with no data.
    >>> empty_data = []
    >>> path = task_func(empty_data, 'empty_data.xls')
    >>> os.path.exists(path) and 'empty_data.xls' in path
    True
    """

    book = xlwt.Workbook()
    sheet1 = book.add_sheet("persons")

    # Write header
    for col_index, col in enumerate(FIELDS):
        sheet1.write(0, col_index, col)

    # Write data rows
    for row_index, row_values in enumerate(values, 1):
        for col_index, col in enumerate(FIELDS):
            value = row_values.get(col, "")
            sheet1.write(row_index, col_index, value)

    book.save(filename)

    return os.path.abspath(filename)

class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        self.test_file_path = 'test_data.xls'
        self.empty_file_path = 'empty_data.xls'

    def tearDown(self):
        # Remove the files after tests
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
        if os.path.exists(self.empty_file_path):
            os.remove(self.empty_file_path)

    def test_create_excel_with_data(self):
        data = [OrderedDict([('ID', 1), ('Name', 'John Doe'), ('Age', 30)]),
                OrderedDict([('ID', 2), ('Name', 'Jane Doe'), ('Age', 28)])]
        path = task_func(data, self.test_file_path)
        self.assertTrue(os.path.exists(path))
        self.assertIn(self.test_file_path, path)

    def test_create_excel_with_empty_data(self):
        empty_data = []
        path = task_func(empty_data, self.empty_file_path)
        self.assertTrue(os.path.exists(path))
        self.assertIn(self.empty_file_path, path)

    def test_column_headers_written(self):
        data = [OrderedDict([('ID', 1), ('Name', 'John Doe'), ('Age', 30)])]
        task_func(data, self.test_file_path)
        expected_headers = FIELDS
        
        # Validate header in the created Excel file
        book = xlrd.open_workbook(self.test_file_path)
        sheet = book.sheet_by_index(0)

        for col_index, expected_header in enumerate(expected_headers):
            self.assertEqual(sheet.cell_value(0, col_index), expected_header)

    def test_excel_file_contains_data(self):
        data = [OrderedDict([('ID', 1), ('Name', 'John Doe'), ('Age', 30)])]
        task_func(data, self.test_file_path)

        book = xlrd.open_workbook(self.test_file_path)
        sheet = book.sheet_by_index(0)

        for row_index, row in enumerate(data):
            for col_index, col in enumerate(FIELDS):
                self.assertEqual(sheet.cell_value(row_index + 1, col_index), row[col])

    def test_file_creation_error_on_empty_filename(self):
        with self.assertRaises(TypeError):
            task_func([], '')

if __name__ == '__main__':
    unittest.main()