import unittest
import pandas as pd
import numpy as np

# Constants
COLUMNS = ['Column1', 'Column2', 'Column3', 'Column4', 'Column5']

# Here is your prompt:
# Import the functions from the module or define them in place.
def task_func(length):
    """
    Generate a Pandas DataFrame with specified length and random data and then record the data.

    Parameters:
    length (int): The length of the DataFrame to be generated.

    Returns:
    DataFrame: A pandas DataFrame with random data.

    Requirements:
    - pandas
    - numpy

    Example:
    >>> np.random.seed(0)
    >>> df = task_func(5)
    >>> df.shape
    (5, 5)
    """

    data = np.random.randint(0, 100, size=(length, len(COLUMNS)))
    df = pd.DataFrame(data, columns=COLUMNS)

    return df

# Test Suite
class TestTaskFunction(unittest.TestCase):

    def test_dataframe_shape(self):
        np.random.seed(0)
        df = task_func(10)
        self.assertEqual(df.shape, (10, 5), "The shape of the DataFrame should be (10, 5)")

    def test_column_names(self):
        np.random.seed(0)
        df = task_func(10)
        self.assertListEqual(list(df.columns), COLUMNS, "The DataFrame should have correct column names")

    def test_random_data_range(self):
        np.random.seed(0)
        df = task_func(10)
        self.assertTrue((df >= 0).all().all() and (df < 100).all().all(), "All data should be in the range [0, 100)")

    def test_empty_dataframe(self):
        np.random.seed(0)
        df = task_func(0)
        self.assertEqual(df.shape, (0, 5), "The shape of the DataFrame should be (0, 5) for zero length")

    def test_dataframe_integrity(self):
        np.random.seed(0)
        df = task_func(10)
        self.assertIsInstance(df, pd.DataFrame, "The output should be a pandas DataFrame")
        self.assertEqual(len(df), 10, "The DataFrame should have 10 rows")

if __name__ == '__main__':
    unittest.main()