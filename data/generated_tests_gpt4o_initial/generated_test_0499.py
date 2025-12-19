import unittest
import os

class TestTaskFunc(unittest.TestCase):

    def test_simple_csv_conversion(self):
        csv_content = 'ID,Name,Age\n1,John Doe,30\n2,Jane Doe,28'
        filename = 'test_data.xls'
        result = task_func(csv_content, filename)
        self.assertTrue(os.path.isfile(result))
        os.remove(result)

    def test_single_cell_csv_conversion(self):
        csv_content = 'Hello'
        filename = 'single_cell.xls'
        result = task_func(csv_content, filename)
        self.assertTrue(os.path.isfile(result))
        os.remove(result)

    def test_empty_csv_conversion(self):
        csv_content = ''
        filename = 'empty_data.xls'
        result = task_func(csv_content, filename)
        self.assertTrue(os.path.isfile(result))
        os.remove(result)

    def test_multiple_rows_csv_conversion(self):
        csv_content = 'ID,Name\n1,Alice\n2,Bob\n3,Charlie'
        filename = 'multiple_rows.xls'
        result = task_func(csv_content, filename)
        self.assertTrue(os.path.isfile(result))
        os.remove(result)

    def test_csv_with_special_characters(self):
        csv_content = 'ID,Description\n1,"A, B & C"\n2,"X/Y: Z"'
        filename = 'special_chars.xls'
        result = task_func(csv_content, filename)
        self.assertTrue(os.path.isfile(result))
        os.remove(result)


if __name__ == '__main__':
    unittest.main()