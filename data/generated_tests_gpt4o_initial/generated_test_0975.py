import numpy as np
import pandas as pd
import unittest

# Here is your prompt:
def task_func(rows, columns=["A", "B", "C", "D", "E"], seed=0) -> pd.DataFrame:
    """
    Create a Pandas DataFrame with a specified number of rows filled with random
    values in [0, 1) and shuffled columns.
    
    Note:
    - The columns should be unique and sorted in the ascending order.

    Parameters:
    rows (int): The number of rows for the DataFrame. Must not be negative.
    columns (list of str): Column names for the DataFrame.
                           Defaults to ['A', 'B', 'C', 'D', 'E'].
                           If it contains repeated columns, the function deduplicates
                           it in a case and spacing sensitive way. If it is empty,
                           the function returns an empty DataFrame.
    seed (int): The random seed for reproducibility.
    
    Returns:
    pd.DataFrame: A pandas DataFrame with shuffled columns.

    Requirements:
    - numpy
    - pandas

    Example:
    >>> df = task_func(10)
    >>> df.head(2)
              D         E         A         C         B
    0  0.548814  0.715189  0.602763  0.544883  0.423655
    1  0.645894  0.437587  0.891773  0.963663  0.383442
    """

    np.random.seed(seed)
    columns = sorted(list(set(columns)))
    data = np.random.rand(rows, len(columns))
    np.random.shuffle(columns)
    df = pd.DataFrame(data, columns=columns)
    return df


class TestTaskFunc(unittest.TestCase):

    def test_empty_dataframe(self):
        """Test that the function returns an empty DataFrame when rows are 0."""
        df = task_func(0)
        self.assertEqual(df.shape, (0, 5))
        self.assertTrue(df.empty)

    def test_negative_rows(self):
        """Test that the function raises a ValueError when rows are negative."""
        with self.assertRaises(ValueError):
            task_func(-1)

    def test_default_columns(self):
        """Test that the function returns a DataFrame with default columns."""
        df = task_func(5)
        self.assertEqual(df.shape[0], 5)
        self.assertEqual(sorted(df.columns.tolist()), ['A', 'B', 'C', 'D', 'E'])

    def test_custom_columns(self):
        """Test that the function handles custom column names correctly."""
        custom_columns = ["X", "Y", "Z"]
        df = task_func(5, columns=custom_columns)
        self.assertEqual(df.shape[0], 5)
        self.assertEqual(sorted(df.columns.tolist()), ['X', 'Y', 'Z'])

    def test_duplicate_columns(self):
        """Test that the function handles duplicate columns correctly."""
        duplicate_columns = ["A", "A", "B", "C", "C"]
        df = task_func(5, columns=duplicate_columns)
        self.assertEqual(df.shape[0], 5)
        self.assertEqual(sorted(df.columns.tolist()), ['A', 'B', 'C'])

if __name__ == '__main__':
    unittest.main()