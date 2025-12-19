import re
import os
import glob
import natsort
import pandas as pd
import unittest

def create_dummy_files(directory):
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, "file1.txt"), "w") as f:
        f.write("123 456")
    with open(os.path.join(directory, "file2.txt"), "w") as f:
        f.write("789")
    with open(os.path.join(directory, "mixed.txt"), "w") as f:
        f.write("123 cats 456 dogs")
    with open(os.path.join(directory, "empty.txt"), "w") as f:
        f.write("")
    with open(os.path.join(directory, "non_numeric.txt"), "w") as f:
        f.write("hello world")

def tear_down_files(directory):
    files = glob.glob(os.path.join(directory, '*'))
    for f in files:
        os.remove(f)
    os.rmdir(directory)

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.test_dir = './test_data/'
        create_dummy_files(self.test_dir)

    def tearDown(self):
        tear_down_files(self.test_dir)

    def test_valid_case(self):
        df = task_func(self.test_dir, '*.txt', r'([0-9]+)')
        expected_data = {
            'Filename': ['empty.txt', 'file1.txt', 'file2.txt', 'mixed.txt', 'non_numeric.txt'],
            'Numeric Data': [[], ['123', '456'], ['789'], ['123', '456'], []]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(df, expected_df)

    def test_directory_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func('./invalid_directory/', '*.txt', r'([0-9]+)')

    def test_no_matching_files(self):
        with self.assertRaises(ValueError):
            task_func(self.test_dir, '*.md', r'([0-9]+)')

    def test_regex_empty_result(self):
        df = task_func(self.test_dir, '*.txt', r'([a-zA-Z]+)')
        expected_data = {
            'Filename': ['empty.txt', 'file1.txt', 'file2.txt', 'mixed.txt', 'non_numeric.txt'],
            'Numeric Data': [[], [], [], [], []]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(df, expected_df)

    def test_regex_matching_varied_numbers(self):
        df = task_func(self.test_dir, '*.txt', r'([0-9]+)')
        self.assertTrue((df['Numeric Data'].apply(lambda x: len(x) > 0)).any())

if __name__ == '__main__':
    unittest.main()