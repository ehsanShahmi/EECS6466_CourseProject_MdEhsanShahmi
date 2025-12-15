import unittest
import csv
import os

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a sample CSV file for testing
        self.filename = 'test_sample.csv'
        self.csv_content = "Name,Age\nAlice,30\nBob,25\n"
        with open(self.filename, 'w', encoding='cp1251') as f:
            f.write(self.csv_content.encode('cp1251').decode('utf-8'))

    def tearDown(self):
        # Remove the sample CSV file after tests
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_encoding_conversion(self):
        data, converted_csv = task_func(self.filename, 'cp1251', 'utf8')
        self.assertEqual(data, [{'Name': 'Alice', 'Age': '30'}, {'Name': 'Bob', 'Age': '25'}])
        self.assertEqual(converted_csv, "Name,Age\nAlice,30\nBob,25\n")

    def test_default_parameters(self):
        data, converted_csv = task_func('sample.csv')  # using default filename
        self.assertIsInstance(data, list)
        self.assertIsInstance(converted_csv, str)

    def test_empty_file(self):
        empty_filename = 'empty_test.csv'
        with open(empty_filename, 'w', encoding='cp1251'):
            pass  # create an empty file
        
        data, converted_csv = task_func(empty_filename, 'cp1251', 'utf8')
        self.assertEqual(data, [])
        self.assertEqual(converted_csv, "Column\n")  # default column name

        os.remove(empty_filename)

    def test_invalid_encoding(self):
        with self.assertRaises(UnicodeDecodeError):
            task_func(self.filename, 'invalid_encoding', 'utf8')

    def test_custom_delimiter(self):
        custom_csv_content = "Name|Age\nAlice|30\nBob|25\n"
        with open(self.filename, 'w', encoding='cp1251') as f:
            f.write(custom_csv_content.encode('cp1251').decode('utf-8'))
        
        data, converted_csv = task_func(self.filename, 'cp1251', 'utf8', delimiter='|')
        self.assertEqual(data, [{'Name': 'Alice', 'Age': '30'}, {'Name': 'Bob', 'Age': '25'}])
        self.assertEqual(converted_csv, "Name|Age\nAlice|30\nBob|25\n")

if __name__ == '__main__':
    unittest.main()