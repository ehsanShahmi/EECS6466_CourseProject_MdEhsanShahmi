import pandas as pd
import numpy as np
import unittest

def task_func(d):
    """
    Calculate mean, sum, max, min and standard deviation for the keys "x," "y" and "z" from a list of dictionaries "d."
    
    Parameters:
    d (list): A list of dictionaries.

    Returns:
    dict: A dictionary with keys as 'x', 'y', and 'z' and values as dictionaries of statistics.

    Raises:
    - ValueError: If input is not a list of dictionaries.

    Requirements:
    - pandas
    - numpy

    Examples:
    >>> data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
    >>> task_func(data)
    {'x': {'mean': 2.0, 'sum': 6, 'max': 3, 'min': 1, 'std': 0.816496580927726}, 'y': {'mean': 8.666666666666666, 'sum': 26, 'max': 15, 'min': 1, 'std': 5.792715732327589}, 'z': {'mean': 6.0, 'sum': 18, 'max': 7, 'min': 5, 'std': 0.816496580927726}}
    >>> task_func([])
    {'x': None, 'y': None, 'z': None}
    >>> task_func([{'a': 1}])
    {'x': None, 'y': None, 'z': None}
    """
    if not isinstance(d, list) or any(not isinstance(item, dict) for item in d):
        raise ValueError("Input must be a list of dictionaries.")
    
    if not d:
        return {key: None for key in ['x', 'y', 'z']}

    df = pd.DataFrame(d).fillna(0)  # Replace missing values with 0 to allow computations
    stats = {}

    for key in ['x', 'y', 'z']:
        if key in df.columns:
            stats[key] = {
                'mean': np.mean(df[key]),
                'sum': np.sum(df[key]),
                'max': np.max(df[key]),
                'min': np.min(df[key]),
                'std': np.std(df[key], ddof=0)  # Population standard deviation
            }
        else:
            stats[key] = None

    return stats

class TestTaskFunc(unittest.TestCase):

    def test_valid_input(self):
        data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 6}, {'x': 2, 'y': 1, 'z': 7}]
        expected_output = {
            'x': {'mean': 2.0, 'sum': 6, 'max': 3, 'min': 1, 'std': 0.816496580927726},
            'y': {'mean': 8.666666666666666, 'sum': 26, 'max': 15, 'min': 1, 'std': 5.792715732327589},
            'z': {'mean': 6.0, 'sum': 18, 'max': 7, 'min': 5, 'std': 0.816496580927726}
        }
        result = task_func(data)
        self.assertEqual(result, expected_output)

    def test_empty_input(self):
        result = task_func([])
        expected_output = {'x': None, 'y': None, 'z': None}
        self.assertEqual(result, expected_output)

    def test_input_with_missing_keys(self):
        data = [{'a': 1}, {'x': 2, 'y': 3}]
        result = task_func(data)
        expected_output = {'x': {'mean': 2.0, 'sum': 2, 'max': 2, 'min': 2, 'std': 0.0}, 'y': {'mean': 3.0, 'sum': 3, 'max': 3, 'min': 3, 'std': 0.0}, 'z': None}
        self.assertEqual(result, expected_output)

    def test_non_dict_input(self):
        with self.assertRaises(ValueError):
            task_func("invalid input")

    def test_input_with_mix_of_dicts_and_non_dicts(self):
        with self.assertRaises(ValueError):
            task_func([{'x': 5}, "invalid item", {'y': 2}])

if __name__ == '__main__':
    unittest.main()