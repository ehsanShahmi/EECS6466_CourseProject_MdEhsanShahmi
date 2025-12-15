import unittest
import pandas as pd
from scipy import stats
import random

# Here is your prompt:
# (the prompt provided is included as is without modification)

def task_func(n_data_points=5000, min_value=0.0, max_value=10.0):
    """
    Generate a random dataset of floating-point numbers within a specified range, 
    truncate each value to 3 decimal places, and calculate statistical measures (mean, median, mode) of the data.
    
    Parameters:
    n_data_points (int): Number of data points to generate. Default is 5000.
    min_value (float): Minimum value range for data points. Default is 0.0.
    max_value (float): Maximum value range for data points. Default is 10.0.

    Returns:
    dict: A dictionary with keys 'mean', 'median', 'mode' and their corresponding calculated values.
    
    Requirements:
    - pandas
    - random
    - scipy.stats

    Example:
    >>> random.seed(0)
    >>> stats = task_func(1000, 5.0, 5.0)
    >>> print(stats)
    {'mean': 5.0, 'median': 5.0, 'mode': 5.0}
    """

    data = [round(random.uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=['Value'])

    mean = data_df['Value'].mean()
    median = data_df['Value'].median()
    mode = stats.mode(data_df['Value'].values)[0][0]

    return {'mean': mean, 'median': median, 'mode': mode}

class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        stats_result = task_func()
        self.assertEqual(len(stats_result), 3)
        self.assertIsInstance(stats_result['mean'], float)
        self.assertIsInstance(stats_result['median'], float)
        self.assertIsInstance(stats_result['mode'], float)

    def test_zero_data_points(self):
        stats_result = task_func(0)
        self.assertEqual(stats_result['mean'], 0)
        self.assertEqual(stats_result['median'], 0)
        self.assertEqual(stats_result['mode'], 0)

    def test_single_value_range(self):
        random.seed(0)  # For reproducibility 
        stats_result = task_func(1000, 5.0, 5.0)
        self.assertAlmostEqual(stats_result['mean'], 5.0)
        self.assertAlmostEqual(stats_result['median'], 5.0)
        self.assertEqual(stats_result['mode'], 5.0)

    def test_large_data_points(self):
        stats_result = task_func(n_data_points=100000)
        self.assertTrue(0.0 <= stats_result['mean'] <= 10.0)
        self.assertTrue(0.0 <= stats_result['median'] <= 10.0)
        self.assertTrue(0.0 <= stats_result['mode'] <= 10.0)

    def test_edge_values(self):
        stats_result = task_func(min_value=-10.0, max_value=10.0)
        self.assertTrue(-10.0 <= stats_result['mean'] <= 10.0)
        self.assertTrue(-10.0 <= stats_result['median'] <= 10.0)
        self.assertTrue(-10.0 <= stats_result['mode'] <= 10.0)

if __name__ == '__main__':
    unittest.main()