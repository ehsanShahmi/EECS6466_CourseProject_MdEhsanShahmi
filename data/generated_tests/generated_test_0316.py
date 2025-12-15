import pandas as pd
import random
import unittest

# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def task_func(value_range=(0, 100)):
    """
    Generate a category distribution within a specified range and return as a DataFrame.

    Parameters:
    value_range (tuple): A tuple specifying the range (min, max) for generating random values for categories.
    
    Returns:
    DataFrame: A pandas DataFrame that has two columns: 'Category' (category names) and 'Count' (count of each category). 

    Requirements:
    - pandas
    - random

    Example:
    >>> random.seed(0)
    >>> df = task_func()
    >>> df['Count'][0] >= 0
    True
    """

    distribution = {category: random.randint(*value_range) for category in CATEGORIES}
    df = pd.DataFrame(list(distribution.items()), columns=['Category', 'Count'])

    return df

class TestTaskFunc(unittest.TestCase):

    def test_output_type(self):
        df = task_func()
        self.assertIsInstance(df, pd.DataFrame)

    def test_output_columns(self):
        df = task_func()
        self.assertTrue(set(['Category', 'Count']).issubset(df.columns))

    def test_category_count(self):
        df = task_func()
        self.assertEqual(len(df), len(CATEGORIES))

    def test_value_range(self):
        df = task_func(value_range=(10, 20))
        self.assertTrue(all((df['Count'] >= 10) & (df['Count'] <= 20)))

    def test_randomness(self):
        random.seed(0)  # Setting seed for reproducibility
        df1 = task_func()
        random.seed(0)  # Reset seed
        df2 = task_func()
        pd.testing.assert_frame_equal(df1, df2)

if __name__ == '__main__':
    unittest.main()