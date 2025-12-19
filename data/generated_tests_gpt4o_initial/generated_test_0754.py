import numpy as np
import pandas as pd
import unittest
from datetime import datetime

# Constants
DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

# Provided Prompt
def task_func(result):
    """
    Calculate the mean, median, min, max, and standard deviation of the "from_user" values in "result" 
    and add the current date and time in the format YYYY-mm-dd HHL:MM:SS to the summary.
    The global constant DATE_FORMAT is used to transform the currnet date and time into this format.

    Parameters:
    result (list of dict): A list of dictionaries containing the key "from_user" whose numeric values are to be analyzed.

    Returns:
    Series: A pandas Series with the statistical summary, including 'mean', 'median', 'min', 'max', 'std', and 'current_time'.
            If the input contains no "from_user" values all statistical values are set to np.nan

    Data Structures:
    - Uses numpy arrays for efficient statistical computations.

    Raises:
    - ValueError: If the "from_user" values are not numeric.

    Requirements:
    - numpy
    - pandas
    - datetime

    Example:
    >>> result = [{"hi": 7, "bye": 4, "from_user": 0}, {"from_user": 0}, {"from_user": 1}]
    >>> stats = task_func(result)
    >>> print(stats['mean'], stats['median'], stats['min'], stats['max'], stats['std'])
    0.3333333333333333 0.0 0 1 0.4714045207910317
    >>> result = [{"test": 7, "hallo": 4, "from_user": 1.3},
    ...           {"from_user": 2},
    ...           {"from_user": 4.6},
    ...           {"from_user": -2.3, "b": 1},
    ...           {"a": "test", "from_user": 12.12},
    ...          ]
    >>> summary = task_func(result)
    """
    from_user_values = np.array([d['from_user'] for d in result if 'from_user' in d])
    # Handle edge case of empty array
    if len(from_user_values) == 0:
        summary = {
            'mean': np.nan,
            'median': np.nan,
            'min': np.nan,
            'max': np.nan,
            'std': np.nan,
            'current_time': datetime.now().strftime(DATE_FORMAT)
        }
    
    elif not np.issubdtype(from_user_values.dtype, np.number):
         raise ValueError("from_user values should be numeric only.")
    
    else:
        summary = {
            'mean': np.mean(from_user_values),
            'median': np.median(from_user_values),
            'min': np.min(from_user_values),
            'max': np.max(from_user_values),
            'std': np.std(from_user_values),
            'current_time': datetime.now().strftime(DATE_FORMAT)
        }

    summary_series = pd.Series(summary)
    return summary_series

# Test Suite
class TestTaskFunction(unittest.TestCase):

    def test_basic_statistics(self):
        result = [{"from_user": 0}, {"from_user": 0}, {"from_user": 1}]
        stats = task_func(result)
        self.assertAlmostEqual(stats['mean'], 0.3333333333)
        self.assertEqual(stats['min'], 0)
        self.assertEqual(stats['max'], 1)
        self.assertAlmostEqual(stats['std'], 0.47140452079)

    def test_varied_numeric_values(self):
        result = [{"from_user": 1.3}, {"from_user": 2}, {"from_user": 4.6}, 
                  {"from_user": -2.3}, {"from_user": 12.12}]
        stats = task_func(result)
        self.assertAlmostEqual(stats['mean'], 3.828)
        self.assertEqual(stats['min'], -2.3)
        self.assertEqual(stats['max'], 12.12)
        self.assertAlmostEqual(stats['std'], 5.575073468)

    def test_no_user_values(self):
        result = [{"unknown": 7}, {"not_from_user": 4}]
        stats = task_func(result)
        self.assertTrue(np.isnan(stats['mean']))
        self.assertTrue(np.isnan(stats['std']))

    def test_invalid_not_numeric(self):
        result = [{"from_user": "string"}, {"from_user": [1, 2, 3]}]
        with self.assertRaises(ValueError) as context:
            task_func(result)
        self.assertEqual(str(context.exception), "from_user values should be numeric only.")

    def test_mixed_content(self):
        result = [{"from_user": -1}, {"from_user": 0}, {"not_from_user": 10}, 
                  {"from_user": 1.5}, {"from_user": "text"}]
        stats = task_func(result)
        self.assertAlmostEqual(stats['mean'], 0.16666666667)
        self.assertEqual(stats['min'], -1)
        self.assertEqual(stats['max'], 1.5)
        self.assertAlmostEqual(stats['std'], 0.86602540378)

if __name__ == '__main__':
    unittest.main()