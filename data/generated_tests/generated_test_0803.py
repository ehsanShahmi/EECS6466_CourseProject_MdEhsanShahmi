import pandas as pd
import unittest
from unittest.mock import patch, MagicMock
import os

# Here is your prompt:
def task_func(file_name: str) -> pd.DataFrame:
    """Normalize data in a csv file using MinMaxScaler from sklearn.
    Only numeric columns are normalized. Columns with other dtypes are left as
    they are.
    
    Parameters:
    file_name (str): The name of the csv file.
    
    Returns:
    DataFrame: A pandas DataFrame with normalized data.

    Raises:
    ValueError: If input does not have numeric columns.

    Requirements:
    - pandas
    - sklearn.preprocessing.MinMaxScaler
    
    Example:
    >>> normalized_data = task_func("sample.csv")
    >>> print(normalized_data.head())
    Name	Age	Salary
    0	Alex Anderson	0.304651	0.122298
    1	Mr. Leslie Casey	0.28140	0.598905
    2	Anthony George	0.996744	0.216552
    3	Brian Washington	0.126279	0.459948
    4	Elias Lawrence	0.337239	0.124185
    """

    df = pd.read_csv(file_name)
    if df.select_dtypes(include='number').empty:
        raise ValueError("Input must at least have one numeric column.")

    scaler = MinMaxScaler()
    numeric_columns = df.select_dtypes(include='number').columns
    df[numeric_columns] = scaler.fit_transform(df[numeric_columns])

    return df


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.csv_file_valid = 'test_valid.csv'
        self.csv_file_invalid = 'test_invalid.csv'
        self.csv_file_empty = 'test_empty.csv'

        # Create a valid CSV file for testing
        valid_data = "Name,Age,Salary\nAlex Anderson,30,50000\nMr. Leslie Casey,25,60000\nAnthony George,50,70000\nBrian Washington,40,80000\nElias Lawrence,35,90000"
        with open(self.csv_file_valid, 'w') as f:
            f.write(valid_data)

        # Create a CSV file with non-numeric data for testing invalid input
        invalid_data = "Name,Department\nAlex Anderson,HR\nMr. Leslie Casey,Finance\nAnthony George,IT\nBrian Washington,Marketing"
        with open(self.csv_file_invalid, 'w') as f:
            f.write(invalid_data)

        # Create an empty CSV file for testing
        with open(self.csv_file_empty, 'w') as f:
            f.write("")

    def tearDown(self):
        # Remove the files after tests
        os.remove(self.csv_file_valid)
        os.remove(self.csv_file_invalid)
        os.remove(self.csv_file_empty)

    def test_normalization_valid_data(self):
        df_result = task_func(self.csv_file_valid)
        self.assertTrue(df_result['Age'].min() >= 0 and df_result['Age'].max() <= 1)
        self.assertTrue(df_result['Salary'].min() >= 0 and df_result['Salary'].max() <= 1)

    def test_invalid_data_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.csv_file_invalid)
        self.assertEqual(str(context.exception), "Input must at least have one numeric column.")

    def test_empty_file_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.csv_file_empty)
        self.assertEqual(str(context.exception), "Input must at least have one numeric column.")

    def test_no_numeric_columns_raises_value_error(self):
        # Creating a csv file with only string data
        no_numeric_data = "Name,City\nAlex Anderson,New York\nMr. Leslie Casey,Los Angeles"
        with open('test_no_numeric.csv', 'w') as f:
            f.write(no_numeric_data)

        with self.assertRaises(ValueError) as context:
            task_func('test_no_numeric.csv')
        self.assertEqual(str(context.exception), "Input must at least have one numeric column.")

        # Clean up
        os.remove('test_no_numeric.csv')

    def test_dataframe_structure_after_norm(self):
        df_result = task_func(self.csv_file_valid)
        self.assertEqual(df_result.shape, (5, 3))  # Ensure data frame shape is correct
        self.assertIn('Name', df_result.columns)
        self.assertIn('Age', df_result.columns)
        self.assertIn('Salary', df_result.columns)


if __name__ == '__main__':
    unittest.main()