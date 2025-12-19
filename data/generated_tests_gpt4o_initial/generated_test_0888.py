import pandas as pd
import os
import unittest

class TestTaskFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = 'test_data'
        os.makedirs(cls.test_dir, exist_ok=True)
        cls.test_file_1 = os.path.join(cls.test_dir, 'file1.csv')
        cls.test_file_2 = os.path.join(cls.test_dir, 'file2.csv')
        
        # Create test CSV files
        df1 = pd.DataFrame({
            'Name': ['Simon', 'Bobby'],
            'Age': [5, 32],
            'Gender': ['Male', 'Male']
        })
        df1.to_csv(cls.test_file_1, index=False)

        df2 = pd.DataFrame({
            'Name': ['Elena', 'Tom'],
            'Age': [13, 23],
            'Gender': ['Female', 'Male']
        })
        df2.to_csv(cls.test_file_2, index=False)

    @classmethod
    def tearDownClass(cls):
        # Remove the test directory and files after tests
        for file in [cls.test_file_1, cls.test_file_2]:
            if os.path.exists(file):
                os.remove(file)
        if os.path.exists(cls.test_dir):
            os.rmdir(cls.test_dir)

    def test_merge_two_csv_files(self):
        expected_data = {
            'Name': ['Simon', 'Bobby', 'Elena', 'Tom'],
            'Age': [5, 32, 13, 23],
            'Gender': ['Male', 'Male', 'Female', 'Male']
        }
        expected_df = pd.DataFrame(expected_data)
        result_df = task_func(self.test_dir, ['file1.csv', 'file2.csv'])
        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True)

    def test_merge_empty_file_list(self):
        result_df = task_func(self.test_dir, [])
        expected_df = pd.DataFrame()
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_merge_nonexistent_file(self):
        result_df = task_func(self.test_dir, ['file1.csv', 'nonexistent_file.csv'])
        expected_data = {
            'Name': ['Simon', 'Bobby'],
            'Age': [5, 32],
            'Gender': ['Male', 'Male']
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True)

    def test_merge_files_with_different_columns(self):
        df3 = pd.DataFrame({
            'Name': ['Alice', 'Bob'],
            'City': ['New York', 'Los Angeles']
        })
        df3.to_csv(os.path.join(self.test_dir, 'file3.csv'), index=False)

        result_df = task_func(self.test_dir, ['file1.csv', 'file3.csv'])
        expected_data = {
            'Name': ['Simon', 'Bobby', 'Alice', 'Bob'],
            'Age': [5, 32, None, None],
            'Gender': ['Male', 'Male', None, None],
            'City': [None, None, 'New York', 'Los Angeles']
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True)

    def test_path_with_trailing_slash(self):
        result_df = task_func(self.test_dir + '/', ['file1.csv', 'file2.csv'])
        expected_data = {
            'Name': ['Simon', 'Bobby', 'Elena', 'Tom'],
            'Age': [5, 32, 13, 23],
            'Gender': ['Male', 'Male', 'Female', 'Male']
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result_df.reset_index(drop=True), expected_df.reset_index(drop=True)

if __name__ == '__main__':
    unittest.main()