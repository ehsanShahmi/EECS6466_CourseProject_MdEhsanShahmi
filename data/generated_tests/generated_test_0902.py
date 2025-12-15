import unittest
from collections import Counter

# Here is your prompt:
import pandas as pd
from collections import Counter

def task_func(d):
    """
    Count the occurrence of values with the keys "x," "y" and "z" from a list of dictionaries "d."

    Parameters:
    d (list): A list of dictionaries.

    Returns:
    dict: A dictionary with keys as 'x', 'y', and 'z' and values as Counter objects.

    Requirements:
    - pandas
    - collections.Counter

    Example:
    >>> data = [{'x': 1, 'y': 10, 'z': 5}, {'x': 3, 'y': 15, 'z': 5}, {'x': 2, 'y': 1, 'z': 7}]
    >>> print(task_func(data))
    {'x': Counter({1: 1, 3: 1, 2: 1}), 'y': Counter({10: 1, 15: 1, 1: 1}), 'z': Counter({5: 2, 7: 1})}
    >>> data = [{'x': 2, 'y': 10}, {'y': 15, 'z': 5}, {'x': 2, 'z': 7}]
    >>> print(task_func(data))
    {'x': Counter({2.0: 2}), 'y': Counter({10.0: 1, 15.0: 1}), 'z': Counter({5.0: 1, 7.0: 1})}
    """

    df = pd.DataFrame(d)
    counts = {}

    for key in ['x', 'y', 'z']:
        if key in df.columns:
            counts[key] = Counter(df[key].dropna().tolist())
        else:
            counts[key] = Counter()

    return counts

class TestTaskFunc(unittest.TestCase):

    def test_basic_input(self):
        data = [{'x': 1, 'y': 10, 'z': 5}, 
                {'x': 3, 'y': 15, 'z': 5}, 
                {'x': 2, 'y': 1, 'z': 7}]
        expected_output = {'x': Counter({1: 1, 3: 1, 2: 1}), 
                           'y': Counter({10: 1, 15: 1, 1: 1}), 
                           'z': Counter({5: 2, 7: 1})}
        self.assertEqual(task_func(data), expected_output)

    def test_partial_keys_input(self):
        data = [{'x': 2, 'y': 10}, 
                {'y': 15, 'z': 5}, 
                {'x': 2, 'z': 7}]
        expected_output = {'x': Counter({2: 2}), 
                           'y': Counter({10: 1, 15: 1}), 
                           'z': Counter({5: 1, 7: 1})}
        self.assertEqual(task_func(data), expected_output)

    def test_missing_keys_input(self):
        data = [{'a': 1, 'b': 10}, 
                {'c': 3, 'd': 15}]
        expected_output = {'x': Counter(), 
                           'y': Counter(), 
                           'z': Counter()}
        self.assertEqual(task_func(data), expected_output)

    def test_empty_input(self):
        data = []
        expected_output = {'x': Counter(), 
                           'y': Counter(), 
                           'z': Counter()}
        self.assertEqual(task_func(data), expected_output)

    def test_large_numbers_input(self):
        data = [{'x': 1000000000, 'y': 5000000000, 'z': 1}, 
                {'x': 1000000000, 'y': 5000000000, 'z': 1}]
        expected_output = {'x': Counter({1000000000: 2}), 
                           'y': Counter({5000000000: 2}), 
                           'z': Counter({1: 2})}
        self.assertEqual(task_func(data), expected_output)

if __name__ == '__main__':
    unittest.main()