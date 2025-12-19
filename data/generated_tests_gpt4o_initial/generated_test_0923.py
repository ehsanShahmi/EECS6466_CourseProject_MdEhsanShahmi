import pandas as pd
import random
import re
import unittest

# The provided prompt has not been modified, and the 'task_func' function is not altered or implemented here.
# Assuming task_func is defined as per the provided prompt.

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        random.seed(0)
        result = task_func(['John Doe', 'Jane Smith'], ['gmail.com', 'yahoo.com'], 2)
        expected_data = {
            'Name': ['Jane Smith', 'John Doe'],
            'Email': ['jane[at]gmail.com', 'john[at]yahoo.com']
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result, expected_df)

    def test_single_name_and_domain(self):
        result = task_func(['Alice'], ['outlook.com'], 1)
        expected_data = {
            'Name': ['Alice'],
            'Email': ['alice[at]outlook.com']
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(result, expected_df)

    def test_insufficient_names(self):
        with self.assertRaises(ValueError):
            task_func(['Alice'], ['gmail.com'], 2)

    def test_no_email_domains(self):
        with self.assertRaises(ValueError):
            task_func(['Alice', 'Bob'], [], 2)

    def test_generate_multiple_records(self):
        random.seed(0)
        result = task_func(['John Doe', 'Jane Smith', 'Alice', 'Bob'], ['gmail.com', 'yahoo.com'], 3)
        # You would have to define the expected output based on the randomness and your test case
        self.assertEqual(result.shape[0], 3)  # Check if 3 records are generated
        self.assertIn('Name', result.columns)  # Confirm 'Name' column exists
        self.assertIn('Email', result.columns)  # Confirm 'Email' column exists


if __name__ == '__main__':
    unittest.main()