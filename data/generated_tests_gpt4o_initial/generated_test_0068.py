import pandas as pd
import seaborn as sns
import unittest
from unittest.mock import patch, MagicMock

# Here is your prompt:
def task_func(data='/path/to/data.csv', emp_prefix='EMP'):
    """
    Load a CSV file into a DataFrame, filter the lines in which the employee ID begins with a prefix, and draw a histogram of its age.

    Parameters:
    - data (str): The path to the data file. Default is '/path/to/data.csv'.
    - emp_prefix (str): The prefix of the employee IDs. Default is 'EMP$$'.

    Returns:
    - DataFrame: A pandas DataFrame with the filtered data, containing the columns 'Employee ID' and 'Age'.
    - Axes: A histogram plot of the 'Age' column of the filtered data.

    Requirements:
    - pandas
    - seaborn

    Example:
    >>> df, ax = task_func()
    >>> print(df)
    """

    # Load data and filter
    df = pd.read_csv(data)
    df = df[df['Employee ID'].str.startswith(emp_prefix)]

    # Plot histogram
    ax = sns.histplot(data=df, x='Age', kde=True)

    return df, ax

class TestTaskFunc(unittest.TestCase):
    
    @patch('pandas.read_csv')
    def test_load_data(self, mock_read_csv):
        # Mock data
        mock_read_csv.return_value = pd.DataFrame({
            'Employee ID': ['EMP001', 'EMP002', 'EMP003'],
            'Age': [25, 30, 22]
        })
        
        df, _ = task_func(data='dummy_path.csv', emp_prefix='EMP')
        
        # Check if data is loaded and filtered correctly
        self.assertEqual(df.shape[0], 3)
        self.assertTrue(all(df['Employee ID'].str.startswith('EMP')))
    
    @patch('pandas.read_csv')
    def test_empty_dataframe(self, mock_read_csv):
        # Mocking an empty CSV
        mock_read_csv.return_value = pd.DataFrame(columns=['Employee ID', 'Age'])
        
        df, ax = task_func(data='dummy_path.csv', emp_prefix='EMP')
        
        # Verify that the returned DataFrame is empty
        self.assertEqual(df.shape[0], 0)
    
    @patch('pandas.read_csv')
    def test_no_matching_prefix(self, mock_read_csv):
        # Mock data with employee IDs that do not match the prefix
        mock_read_csv.return_value = pd.DataFrame({
            'Employee ID': ['EMP004', 'EMP005'],
            'Age': [35, 28]
        })
        
        df, _ = task_func(data='dummy_path.csv', emp_prefix='EMP001')
        
        # Verify that the returned DataFrame is empty
        self.assertEqual(df.shape[0], 0)
    
    @patch('pandas.read_csv')
    def test_histogram_called(self, mock_read_csv):
        # Mock data
        mock_read_csv.return_value = pd.DataFrame({
            'Employee ID': ['EMP001', 'EMP002'],
            'Age': [25, 30]
        })
        
        _, ax = task_func(data='dummy_path.csv', emp_prefix='EMP')
        
        # Check if the plot was created
        self.assertIsNotNone(ax)
    
    @patch('pandas.read_csv')
    def test_age_column_is_numeric(self, mock_read_csv):
        # Mock data
        mock_read_csv.return_value = pd.DataFrame({
            'Employee ID': ['EMP001', 'EMP002'],
            'Age': [30, 40]
        })
        
        df, _ = task_func(data='dummy_path.csv', emp_prefix='EMP')
        
        # Check if the Age column contains only numeric values
        self.assertTrue(pd.api.types.is_numeric_dtype(df['Age']))

if __name__ == '__main__':
    unittest.main()