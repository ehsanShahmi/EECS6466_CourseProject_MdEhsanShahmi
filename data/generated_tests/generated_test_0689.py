import unittest
import pandas as pd
import numpy as np
from scipy import stats

# Here is your prompt:
def task_func(df):
    """
    Given a Pandas DataFrame with random numeric values test if the data in each column is normally distributed using the Shapiro-Wilk test.

    Parameters:
    - df (DataFrame): A Pandas DataFrame with random numeric values.
    
    Returns:
    - dict: A dictionary with p-values from the Shapiro-Wilk test for each column.

    Requirements:
    - numpy
    - scipy

    Example:
    >>> np.random.seed(42)
    >>> df = pd.DataFrame(np.random.normal(size=(100, 5)))
    >>> p_values = task_func(df)
    >>> print(p_values)
    {0: 0.3595593273639679, 1: 0.23594242334365845, 2: 0.7625704407691956, 3: 0.481273353099823, 4: 0.13771861791610718}
    """

    p_values = {}

    for col in df.columns:
        column_data = np.array(df[col])
        
        test_stat, p_value = stats.shapiro(column_data)
        
        p_values[col] = p_value

    return p_values

class TestTaskFunc(unittest.TestCase):
    
    def test_normal_distribution(self):
        """Test with normal distributed data"""
        np.random.seed(42)
        df = pd.DataFrame(np.random.normal(size=(100, 5)))
        p_values = task_func(df)
        self.assertTrue(all(p > 0.05 for p in p_values.values()), "Not all columns should pass normality test")

    def test_uniform_distribution(self):
        """Test with uniform distributed data"""
        df = pd.DataFrame(np.random.uniform(low=0, high=1, size=(100, 5)))
        p_values = task_func(df)
        self.assertTrue(all(p < 0.05 for p in p_values.values()), "All columns should fail normality test")

    def test_single_column(self):
        """Test with a single column of normal distributed data"""
        df = pd.DataFrame(np.random.normal(size=(100, 1)))
        p_values = task_func(df)
        self.assertTrue(p_values[0] > 0.05, "Single column with normal data should pass")

    def test_empty_dataframe(self):
        """Test with an empty DataFrame"""
        df = pd.DataFrame()
        p_values = task_func(df)
        self.assertEqual(p_values, {}, "Empty DataFrame should return an empty dictionary")

    def test_non_numeric_data(self):
        """Test with non-numeric data"""
        df = pd.DataFrame({'A': ['a', 'b', 'c'], 'B': [1, 2, 3]})
        with self.assertRaises(ValueError):
            task_func(df)

if __name__ == '__main__':
    unittest.main()