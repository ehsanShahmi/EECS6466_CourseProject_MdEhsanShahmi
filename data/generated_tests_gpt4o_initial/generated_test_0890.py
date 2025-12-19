import os
import random
import pandas as pd
import unittest

# Here is your prompt
def task_func(data_dir,
              csv_files=['file1.csv', 'file2.csv', 'file3.csv'],
              seed=None):
    """
    Randomly select one of the provided csv_files and select a certain number 
    of records from the file at random.
    The selected records are returned in a DataFrame. 
    The name of the selected csv_file is also returned.

    If the csv_file is empty return an empty DataFrame.

    Parameters:
    data_dir (str): The directory where the CSV files are located.
    csv_files (list of str): The list of CSV files to choose from. Default is ['file1.csv', 'file2.csv', 'file3.csv'].
    seed (int, optional): Seed for random number generation and for sampling from the csv.
    
    Returns:
    tuple: A tuple containing two elements:
    - str: The name of the randomly selected file.
    - DataFrame: A pandas DataFrame with the selected rows.

    Requirements:
    - os
    - random
    - pandas

    Example:
    >>> file_name, df = task_func('test_data')
    >>> print(file_name)
    'file2.csv'
    >>> print(df)
           Animal     Weight
     0        Cat          1
    21      Mouse         12
    15   Elephant       1000
     2      Tiger        500
    """

    random.seed(seed)

    file = csv_files[random.randint(0, len(csv_files) - 1)]
    file_path = os.path.join(data_dir, file)

    try:
        df = pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        return file, pd.DataFrame()

    selected_rows = df.sample(n=random.randint(1, len(df)), random_state=seed)

    return file, selected_rows


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory and CSV files for testing
        os.makedirs('test_data', exist_ok=True)
        self.create_test_csv('test_data/file1.csv', [('Cat', 1), ('Mouse', 12), ('Elephant', 1000)])
        self.create_test_csv('test_data/file2.csv', [('Dog', 5), ('Tiger', 20), ('Lion', 250)])
        self.create_test_csv('test_data/file3.csv', [])
    
    def create_test_csv(self, filename, rows):
        df = pd.DataFrame(rows, columns=['Animal', 'Weight'])
        df.to_csv(filename, index=False)

    def tearDown(self):
        # Remove the temporary directory and CSV files after tests
        for file in os.listdir('test_data'):
            os.remove(os.path.join('test_data', file))
        os.rmdir('test_data')

    def test_random_file_selection(self):
        file_name, df = task_func('test_data')
        self.assertIn(file_name, ['file1.csv', 'file2.csv', 'file3.csv'])

    def test_non_empty_dataframe_return(self):
        file_name, df = task_func('test_data')
        if file_name != 'file3.csv':  # 'file3.csv' is empty
            self.assertGreater(len(df), 0)

    def test_empty_dataframe_return(self):
        file_name, df = task_func('test_data', csv_files=['file3.csv'])
        self.assertEqual(file_name, 'file3.csv')
        self.assertTrue(df.empty)

    def test_dataframe_column_names(self):
        file_name, df = task_func('test_data')
        if file_name == 'file1.csv':
            self.assertListEqual(df.columns.tolist(), ['Animal', 'Weight'])
        elif file_name == 'file2.csv':
            self.assertListEqual(df.columns.tolist(), ['Animal', 'Weight'])

    def test_seed_consistency(self):
        file_name_1, df_1 = task_func('test_data', seed=42)
        file_name_2, df_2 = task_func('test_data', seed=42)
        self.assertEqual(file_name_1, file_name_2)
        pd.testing.assert_frame_equal(df_1.reset_index(drop=True), df_2.reset_index(drop=True)


if __name__ == '__main__':
    unittest.main()