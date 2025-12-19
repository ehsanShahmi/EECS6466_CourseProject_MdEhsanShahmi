import unittest
import os
import json

class TestTaskFunc(unittest.TestCase):
    
    def test_valid_json_conversion(self):
        json_str = '[{"Name": "John", "Age": 30}, {"Name": "Jane", "Age": 28}]'
        filename = 'test_data.xls'
        result = task_func(json_str, filename)
        self.assertTrue(result.endswith(filename))
        self.assertTrue(os.path.exists(filename))
        
    def test_empty_json_array(self):
        json_str = '[]'
        filename = 'empty_data.xls'
        result = task_func(json_str, filename)
        self.assertTrue(result.endswith(filename))
        self.assertTrue(os.path.exists(filename))
        
    def test_invalid_json(self):
        json_str = '[{"Name": "John", "Age": 30], {"Name": "Jane", "Age": 28}]'  # Invalid JSON
        with self.assertRaises(ValueError):
            task_func(json_str, 'invalid_data.xls')

    def test_non_string_json_input(self):
        json_str = 12345  # Invalid type
        with self.assertRaises(TypeError):
            task_func(json_str, 'non_string_data.xls')
    
    def test_default_sheet_name(self):
        json_str = '[{"Name": "John", "Age": 30}]'
        filename = 'default_sheet_data.xls'
        result = task_func(json_str, filename)
        self.assertTrue(result.endswith(filename))
        # Checking if the default sheet name is correctly set
        book = xlrd.open_workbook(result)
        self.assertEqual(book.sheet_names()[0], 'sheet1')

if __name__ == '__main__':
    unittest.main()