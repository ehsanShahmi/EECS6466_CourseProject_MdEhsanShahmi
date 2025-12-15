import pandas as pd
import unittest
import os

class TestTaskFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a temporary CSV file for testing
        cls.test_csv = 'test_data.csv'
        data = {
            'data': [
                '123x is a number', 
                'there are no numbers here', 
                '456X is another number',
                'no match in this one',
                '789x and 101x are also numbers'
            ]
        }
        df = pd.DataFrame(data)
        df.to_csv(cls.test_csv, index=False)

    @classmethod
    def tearDownClass(cls):
        # Remove the temporary CSV file after tests
        os.remove(cls.test_csv)

    def test_return_all_matches(self):
        # Testing to return all matches
        result = task_func(self.test_csv, column_name='data', pattern='\d+[xX]')
        expected_data = [
            '123x is a number', 
            '456X is another number', 
            '789x and 101x are also numbers'
        ]
        matches = result['data'].tolist()
        self.assertEqual(matches, expected_data)

    def test_return_sample_size(self):
        # Testing to return a sample with a specified sample size
        result = task_func(self.test_csv, column_name='data', pattern='\d+[xX]', sample_size=2, seed=42)
        self.assertEqual(len(result), 2)  # Check if we got 2 results

    def test_sample_size_exceeding_matches(self):
        # Testing sample size exceeding number of matches
        result = task_func(self.test_csv, column_name='data', pattern='\d+[xX]', sample_size=10, seed=42)
        expected_data = [
            '123x is a number', 
            '456X is another number', 
            '789x and 101x are also numbers'
        ]
        matches = result['data'].tolist()
        self.assertEqual(sorted(matches), sorted(expected_data))  # Ensure all matches are included

    def test_no_matches(self):
        # Testing with a pattern that matches nothing
        result = task_func(self.test_csv, column_name='data', pattern='no match')
        self.assertTrue(result.empty)  # Result should be an empty DataFrame

    def test_invalid_column_name(self):
        # Testing with an invalid column name
        with self.assertRaises(KeyError):
            task_func(self.test_csv, column_name='invalid_column', pattern='\d+[xX]')

if __name__ == '__main__':
    unittest.main()