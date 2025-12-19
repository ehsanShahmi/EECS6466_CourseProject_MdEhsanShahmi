import pandas as pd
import os
import unittest

OUTPUT_DIR = './output'

def task_func(df, filename, output_dir=OUTPUT_DIR):
    """
    Save a Pandas DataFrame to a JSON file in a specified directory.
    
    Parameters:
    - df (DataFrame): A Pandas DataFrame to be saved.
    - filename (str): The filename of the JSON file where the DataFrame will be saved.
    - output_dir (str, optional): the output directory.
    
    Returns:
    str: The full file path where the DataFrame is saved.
    
    Requirements:
    - os
    - pandas
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    file_path = os.path.join(output_dir, filename)
    df_clean = df.where(pd.notnull(df), None)
    with open(file_path, 'w') as f:
        df_clean.to_json(f, orient='records')
    return file_path

class TestTaskFunction(unittest.TestCase):

    def setUp(self):
        """Set up the testing environment."""
        self.df_valid = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        self.df_nan = pd.DataFrame({'A': [1, None, 3], 'B': [4, 5, None]})
        self.output_dir = './test_output'
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def tearDown(self):
        """Clean up after tests."""
        for filename in os.listdir(self.output_dir):
            file_path = os.path.join(self.output_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        os.rmdir(self.output_dir)

    def test_valid_dataframe(self):
        """Test saving a valid DataFrame to JSON."""
        file_path = task_func(self.df_valid, 'valid_data.json', self.output_dir)
        self.assertTrue(os.path.exists(file_path))
        self.assertTrue(file_path.endswith('valid_data.json'))

    def test_dataframe_with_nan(self):
        """Test saving a DataFrame that contains NaN values."""
        file_path = task_func(self.df_nan, 'nan_data.json', self.output_dir)
        self.assertTrue(os.path.exists(file_path))
        self.assertTrue(file_path.endswith('nan_data.json'))

    def test_output_directory_creation(self):
        """Test if the output directory is created if it doesn't exist."""
        test_subdir = './nonexistent_dir'
        try:
            file_path = task_func(self.df_valid, 'test.json', test_subdir)
            self.assertTrue(os.path.exists(test_subdir))
            self.assertTrue(os.path.exists(file_path))
        finally:
            if os.path.exists(test_subdir):
                for filename in os.listdir(test_subdir):
                    file_path = os.path.join(test_subdir, filename)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                os.rmdir(test_subdir)

    def test_empty_dataframe(self):
        """Test saving an empty DataFrame."""
        empty_df = pd.DataFrame()
        file_path = task_func(empty_df, 'empty.json', self.output_dir)
        self.assertTrue(os.path.exists(file_path))
        self.assertTrue(file_path.endswith('empty.json'))

if __name__ == '__main__':
    unittest.main()