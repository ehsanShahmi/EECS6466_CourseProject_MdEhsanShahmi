import pandas as pd
import os
import numpy as np
import ast
import unittest
from unittest.mock import patch, mock_open

class TestTaskFunc(unittest.TestCase):

    @patch("builtins.open", new_callable=mock_open, read_data='email,list\nexample@example.com,"[1, 2, 3, 4]"\n')
    @patch("os.listdir", return_value=['file1.csv'])
    def test_single_csv_file(self, mock_listdir, mock_open):
        result_df, result_hist = task_func("dummy_directory")
        expected_df = pd.DataFrame({
            'email': ['example@example.com'],
            'list': [[1, 2, 3, 4]],
            'sum': [10],
            'mean': [2.5],
            'median': [2.5]
        })
        pd.testing.assert_frame_equal(result_df, expected_df)
        self.assertIsNotNone(result_hist)

    @patch("os.listdir", return_value=['file1.csv', 'file2.csv'])
    @patch("builtins.open", new_callable=mock_open, read_data='email,list\nexample@example.com,"[1, 2, 3, 4]"\n')
    def test_multiple_csv_files_choose_longest(self, mock_open, mock_listdir):
        result_df, result_hist = task_func("dummy_directory")
        expected_df = pd.DataFrame({
            'email': ['example@example.com'],
            'list': [[1, 2, 3, 4]],
            'sum': [10],
            'mean': [2.5],
            'median': [2.5]
        })
        pd.testing.assert_frame_equal(result_df, expected_df)
        self.assertIsNotNone(result_hist)

    @patch("os.listdir", return_value=['short.csv', 'longer_file.csv'])
    @patch("builtins.open", new_callable=mock_open, read_data='email,list\nexample@example.com,"[1, 2, 3, 4, 5]"\n')
    def test_longest_filename_selection(self, mock_open, mock_listdir):
        result_df, result_hist = task_func("dummy_directory")
        expected_df = pd.DataFrame({
            'email': ['example@example.com'],
            'list': [[1, 2, 3, 4, 5]],
            'sum': [15],
            'mean': [3.0],
            'median': [3.0]
        })
        pd.testing.assert_frame_equal(result_df, expected_df)
        self.assertIsNotNone(result_hist)

    @patch("os.listdir", return_value=[])
    def test_no_csv_files(self, mock_listdir):
        result_df, result_hist = task_func("dummy_directory")
        expected_df = pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median'])
        pd.testing.assert_frame_equal(result_df, expected_df)
        self.assertIsNone(result_hist)

    @patch("os.listdir", return_value=['file.csv'])
    @patch("builtins.open", new_callable=mock_open, read_data='email,list\nexample@example.com,"[1, 2, 3]"\n')
    def test_csv_with_string_converted_to_list(self, mock_open, mock_listdir):
        result_df, result_hist = task_func("dummy_directory")
        expected_df = pd.DataFrame({
            'email': ['example@example.com'],
            'list': [[1, 2, 3]],
            'sum': [6],
            'mean': [2.0],
            'median': [2.0]
        })
        pd.testing.assert_frame_equal(result_df, expected_df)
        self.assertIsNotNone(result_hist)

if __name__ == '__main__':
    unittest.main()