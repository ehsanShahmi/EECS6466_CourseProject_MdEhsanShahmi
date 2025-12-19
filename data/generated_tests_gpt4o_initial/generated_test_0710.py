import pandas as pd
import unittest
from io import StringIO
from sklearn.preprocessing import MinMaxScaler

# Here is your prompt:
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(data_path):
    """
    Normalizes a dataset from a .csv file.
    
    Parameters:
    - data_path (str): The path to the csv data file.

    Returns:
    - df (DataFrame): The normalized dataset.

    Requirements:
    - pandas
    - sklearn
    
    Example:
    >>> df = task_func('path_to_data_file.csv')
    """

    df = pd.read_csv(data_path)
    data = df.to_numpy()
    
    scaler = MinMaxScaler()
    data = scaler.fit_transform(data)

    df = pd.DataFrame(data, columns=df.columns)

    return df

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a sample CSV data in-memory for testing
        self.csv_data = StringIO("""A,B,C
        1,2,3
        4,5,6
        7,8,9
        """)
        
        # Save the CSV to a file
        self.data_path = 'test_data.csv'
        pd.read_csv(self.csv_data).to_csv(self.data_path, index=False)

    def test_correct_normalization(self):
        df = task_func(self.data_path)
        expected_data = [[0.0, 0.0, 0.0],
                          [0.5, 0.5, 0.5],
                          [1.0, 1.0, 1.0]]
        pd.testing.assert_frame_equal(df.values, expected_data)

    def test_columns_names(self):
        df = task_func(self.data_path)
        expected_columns = ['A', 'B', 'C']
        self.assertListEqual(list(df.columns), expected_columns)

    def test_empty_dataset(self):
        empty_csv = StringIO("""A,B,C
        """)
        empty_data_path = 'empty_test_data.csv'
        pd.read_csv(empty_csv).to_csv(empty_data_path, index=False)
        
        df = task_func(empty_data_path)
        self.assertTrue(df.empty)

    def test_inaccessible_file(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_file.csv')

    def test_non_numeric_data(self):
        non_numeric_csv = StringIO("""A,B,C
        1,2,3
        4,five,6
        7,8,9
        """)
        non_numeric_data_path = 'non_numeric_test_data.csv'
        pd.read_csv(non_numeric_csv).to_csv(non_numeric_data_path, index=False)

        with self.assertRaises(ValueError):
            task_func(non_numeric_data_path)

if __name__ == '__main__':
    unittest.main()