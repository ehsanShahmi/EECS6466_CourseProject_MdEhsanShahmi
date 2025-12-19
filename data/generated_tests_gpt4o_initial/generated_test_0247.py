import pandas as pd
import random
from sklearn.preprocessing import StandardScaler
import unittest

# Constants
N_DATA_POINTS = 5000
MIN_VALUE = 0.0
MAX_VALUE = 10.0

def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    """
    Generate a random dataset of floating point numbers, truncate each value to 3 decimal places and normalize the data using standard scaling (mean = 0, std = 1).
    
    Parameters:
    n_data_points (int): Number of data points to generate. Default is 5000.
    min_value (float): Minimum value range for data points. Default is 0.0.
    max_value (float): Maximum value range for data points. Default is 10.0.
    
    Returns:
    DataFrame: A pandas DataFrame with the normalized data.
    
    Raises:
    If max_value is less than min_value, a ValueError is raised.
    
    Note:
    - The function use "Normalized Value" for the column name in the DataFrame that being returned.

    Requirements:
    - pandas
    - random
    - sklearn.preprocessing.StandardScaler

    Example:
    >>> random.seed(0)
    >>> normalized_data = task_func(5000, 5, 5)
    >>> print(normalized_data['Normalized Value'][0])
    0.0
    """

    if max_value < min_value:
        raise ValueError()

    data = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=['Value'])

    scaler = StandardScaler()
    normalized_data = scaler.fit_transform(data_df[['Value']])

    return pd.DataFrame(normalized_data, columns=['Normalized Value'])

class TestTaskFunc(unittest.TestCase):

    def test_default_case(self):
        """Test the default parameters return a DataFrame with correct shape."""
        result = task_func()
        self.assertEqual(result.shape, (N_DATA_POINTS, 1))

    def test_col_name(self):
        """Test the column name is 'Normalized Value'."""
        result = task_func()
        self.assertIn('Normalized Value', result.columns)

    def test_value_range(self):
        """Test that normalized values have mean approximately 0 and std approximately 1."""
        result = task_func()
        self.assertAlmostEqual(result['Normalized Value'].mean(), 0, delta=0.1)
        self.assertAlmostEqual(result['Normalized Value'].std(), 1, delta=0.1)

    def test_min_max_value(self):
        """Test if ValueError is raised when max_value is less than min_value."""
        with self.assertRaises(ValueError):
            task_func(n_data_points=5000, min_value=5, max_value=3)

    def test_empty_data(self):
        """Test the case when number of data points is 0 returns an empty DataFrame."""
        result = task_func(n_data_points=0)
        self.assertEqual(result.shape, (0, 1))

if __name__ == '__main__':
    unittest.main()