import pandas as pd
import unittest
from random import seed

# Here is your prompt:
import pandas as pd
from random import uniform


def task_func(n_data_points=1000, min_value=0.0, max_value=10.0, column_name='Value'):
    """
    Generate a random dataset of floating-point numbers, truncate each value to 3 decimal places, then return the generated DataFrame with
    the specified column name.

    Parameters:
    n_data_points (int, optional): The number of data points to generate. Default is 1000.
    min_value (float, optional): The minimum value for the generated data. Default is 0.0.
    max_value (float, optional): The maximum value for the generated data. Default is 10.0.
    column_name (str, optional): The column name in generated DataFrame. Default is 'Value'.


    Returns:
    DataFrame: A pandas DataFrame with the generated data.
    
    Requirements:
    - pandas
    - random.uniform

    Example:
    >>> random.seed(0)
    >>> data = task_func()
    >>> data.shape[0]
    1000
    """

           
    data = [round(uniform(min_value, max_value), 3) for _ in range(n_data_points)]
    data_df = pd.DataFrame(data, columns=[column_name])

    return data_df


class TestTaskFunc(unittest.TestCase):
    
    def test_default_data_points(self):
        result = task_func()
        self.assertEqual(result.shape[0], 1000)
        self.assertIn('Value', result.columns)

    def test_data_points_count(self):
        result = task_func(n_data_points=500)
        self.assertEqual(result.shape[0], 500)

    def test_value_range(self):
        result = task_func()
        self.assertTrue((result['Value'] >= 0.0).all() and (result['Value'] <= 10.0).all())

    def test_column_name(self):
        result = task_func(column_name='TestColumn')
        self.assertIn('TestColumn', result.columns)
        self.assertNotIn('Value', result.columns)

    def test_truncation(self):
        result = task_func(min_value=0.0, max_value=10.0)
        for value in result['Value']:
            self.assertEqual(value, round(value, 3))


if __name__ == '__main__':
    unittest.main()