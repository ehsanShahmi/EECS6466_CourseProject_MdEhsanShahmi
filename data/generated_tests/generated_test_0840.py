import pandas as pd
import numpy as np
import unittest
import os

# Here is your prompt:
def task_func(file_path, num_rows, data_dimensions=5, random_seed=None):
    """
    Creates a CSV file on a given file path with random numeric data. 
    The number of rows in the CSV file is determined by the 'num_rows' parameter, 
    and the number of columns (features) is determined by the 'data_dimensions' parameter.
    Columns are named following the convention: 'Feature_x', where x is the number of the 
    feature column starting at 1.

    Parameters:
    file_path (str): The file path where the CSV file should be created.
    num_rows (int): The number of rows of random data to generate.
    data_dimensions (int, optional): The number of columns (features) in the CSV file. Defaults to 5.
    random_seed (int, optional): Seed used in rng. Defaults to None.
    
    Returns:
    str: The file path of the generated CSV file.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> task_func('/tmp/data.csv', 100)
    '/tmp/data.csv'
    """

    np.random.seed(random_seed)
    df = pd.DataFrame(np.random.rand(num_rows, data_dimensions),
                      columns=[f'Feature_{i + 1}' for i in range(data_dimensions)])

    df.to_csv(file_path, index=False)

    return file_path

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.test_file_path = './test_data.csv'
    
    def tearDown(self):
        # Remove the file after the test
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_file_creation(self):
        result = task_func(self.test_file_path, 10)
        self.assertEqual(result, self.test_file_path)
        self.assertTrue(os.path.exists(self.test_file_path))

    def test_correct_number_of_rows(self):
        task_func(self.test_file_path, 15)
        df = pd.read_csv(self.test_file_path)
        self.assertEqual(len(df), 15)

    def test_correct_number_of_columns(self):
        task_func(self.test_file_path, 10, data_dimensions=3)
        df = pd.read_csv(self.test_file_path)
        self.assertEqual(len(df.columns), 3)

    def test_feature_column_names(self):
        task_func(self.test_file_path, 5)
        df = pd.read_csv(self.test_file_path)
        expected_columns = [f'Feature_{i + 1}' for i in range(5)]
        self.assertListEqual(list(df.columns), expected_columns)

    def test_different_random_seed(self):
        task_func(self.test_file_path, 10, random_seed=42)
        df1 = pd.read_csv(self.test_file_path)
        
        task_func(self.test_file_path, 10, random_seed=42)
        df2 = pd.read_csv(self.test_file_path)
        
        # Random data with the same seed should produce the same output
        pd.testing.assert_frame_equal(df1, df2)

if __name__ == '__main__':
    unittest.main()