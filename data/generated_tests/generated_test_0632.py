import os
import json
import pandas as pd
import unittest

OUTPUT_DIR = './output'


class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        """Set up a temporary file for testing."""
        if not os.path.exists(OUTPUT_DIR):
            os.makedirs(OUTPUT_DIR)

    def tearDown(self):
        """Clean up the output directory after tests."""
        for filename in os.listdir(OUTPUT_DIR):
            file_path = os.path.join(OUTPUT_DIR, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

    def test_empty_dataframe(self):
        """Test with an empty DataFrame."""
        df = pd.DataFrame()
        filename = 'empty.jsonl'
        result = task_func(df, filename)
        self.assertTrue(os.path.isfile(result))
        with open(result, 'r') as file:
            content = file.read()
        self.assertEqual(content, '')  # Check if file is empty

    def test_dataframe_with_single_row(self):
        """Test with a DataFrame containing a single row."""
        df = pd.DataFrame({'A': [1], 'B': [4]})
        filename = 'single_row.jsonl'
        result = task_func(df, filename)
        self.assertTrue(os.path.isfile(result))
        with open(result, 'r') as file:
            content = file.readlines()
        expected_content = '{"A": 1, "B": 4}\n'
        self.assertEqual(content, [expected_content])  # Check the file content

    def test_dataframe_with_multiple_rows(self):
        """Test with a DataFrame containing multiple rows."""
        df = pd.DataFrame({'A': [1, 2], 'B': [4, 5]})
        filename = 'multiple_rows.jsonl'
        result = task_func(df, filename)
        self.assertTrue(os.path.isfile(result))
        with open(result, 'r') as file:
            content = file.readlines()
        expected_content = [
            '{"A": 1, "B": 4}\n',
            '{"A": 2, "B": 5}\n'
        ]
        self.assertEqual(content, expected_content)  # Check the file content

    def test_filename_uniqueness(self):
        """Test to ensure that two different DataFrames save safely to different files."""
        df1 = pd.DataFrame({'A': [1], 'B': [4]})
        df2 = pd.DataFrame({'A': [2], 'B': [5]})
        filename1 = 'test1.jsonl'
        filename2 = 'test2.jsonl'
        result1 = task_func(df1, filename1)
        result2 = task_func(df2, filename2)
        self.assertNotEqual(result1, result2)  # Check that they are different files
        self.assertTrue(os.path.isfile(result1))  # Ensure first file exists
        self.assertTrue(os.path.isfile(result2))  # Ensure second file exists

if __name__ == '__main__':
    unittest.main()