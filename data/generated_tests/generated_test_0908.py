import os
import pandas as pd
import re
import matplotlib.pyplot as plt
import unittest
from unittest.mock import patch, mock_open

class TestTaskFunction(unittest.TestCase):

    @patch('os.listdir')
    @patch('pandas.read_csv')
    @patch('matplotlib.pyplot.show')
    def test_task_func_matches_csv_files(self, mock_show, mock_read_csv, mock_listdir):
        mock_listdir.return_value = ['sales_data_2021.csv', 'sales_data_2022.csv', 'some_other_file.txt']
        mock_read_csv.side_effect = [
            pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar'], 'Sales': [100, 150, 200]}),
            pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar'], 'Sales': [200, 250, 300]})
        ]

        from task_module import task_func  # Assuming the function is in task_module
        axes = task_func('/path/to/data/', r'^sales_data_\d{4}.csv')
        
        self.assertEqual(len(axes), 2)
        self.assertEqual(axes[0].get_title(), 'sales_data_2021.csv')
        self.assertEqual(axes[1].get_title(), 'sales_data_2022.csv')

    @patch('os.listdir')
    @patch('pandas.read_csv')
    @patch('matplotlib.pyplot.show')
    def test_task_func_no_matching_files(self, mock_show, mock_read_csv, mock_listdir):
        mock_listdir.return_value = ['some_other_file.txt', 'not_matching_file.doc']
        
        from task_module import task_func
        axes = task_func('/path/to/data/', r'^sales_data_\d{4}.csv')
        
        self.assertEqual(len(axes), 0)

    @patch('os.listdir')
    @patch('pandas.read_csv')
    @patch('matplotlib.pyplot.show')
    def test_task_func_single_csv_file(self, mock_show, mock_read_csv, mock_listdir):
        mock_listdir.return_value = ['sales_data_2023.csv']
        mock_read_csv.return_value = pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar'], 'Sales': [300, 400, 500]})

        from task_module import task_func
        axes = task_func('/path/to/data/', r'^sales_data_\d{4}.csv')
        
        self.assertEqual(len(axes), 1)
        self.assertEqual(axes[0].get_title(), 'sales_data_2023.csv')

    @patch('os.listdir')
    @patch('pandas.read_csv')
    @patch('matplotlib.pyplot.show')
    def test_task_func_with_different_pattern(self, mock_show, mock_read_csv, mock_listdir):
        mock_listdir.return_value = ['sales_data_2021.csv', 'sales_data_2022.csv']
        mock_read_csv.side_effect = [
            pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar'], 'Sales': [100, 150, 200]}),
            pd.DataFrame({'Month': ['Jan', 'Feb', 'Mar'], 'Sales': [200, 300, 400]})
        ]

        from task_module import task_func
        axes = task_func('/path/to/data/', r'^sales_data_.+\.csv')
        
        self.assertEqual(len(axes), 2)

    @patch('os.listdir')
    @patch('pandas.read_csv')
    @patch('matplotlib.pyplot.show')
    def test_task_func_incorrect_csv_format(self, mock_show, mock_read_csv, mock_listdir):
        mock_listdir.return_value = ['sales_data_2021.csv']
        mock_read_csv.return_value = pd.DataFrame({'Sales': [100, 150, 200]})  # Missing 'Month' column

        from task_module import task_func
        with self.assertRaises(KeyError):
            task_func('/path/to/data/', r'^sales_data_\d{4}.csv')

if __name__ == '__main__':
    unittest.main()