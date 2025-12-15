import pandas as pd
import unittest
import matplotlib.pyplot as plt

# Here is your prompt:
import pandas as pd
import time


def task_func(df, target_value):
    '''
    Convert the input dic of list to DataFrame and searcher in this DataFrame for rows with cells equal to the
    provided target_value. It then plots the count of such rows per column.

    Parameters:
    - df (dic of list): The input dict. It should have a 'Name' key.
    - target_value (str): The target value to be searched in the DataFrame.

    Returns:
    tuple: A tuple containing:
        - A pandas Series with counts of the target value per column.
        - A matplotlib Axes object representing the plot (None if dataframe is empty).

    Requirements:
    - pandas
    - time

    Example:
    >>> df = {'Column1': ['0', 'a', '332', '33']}
    >>> series, ax = task_func(df, '332')
    '''

               start_time = time.time()
    # Convert dataframe to string type for uniform comparison
    dataframe = pd.DataFrame(df)
    dataframe = dataframe.astype(str)
    
    counts = dataframe.apply(lambda x: (x == target_value).sum())

    # Check if DataFrame is empty
    if not dataframe.empty:
        ax = counts.plot(kind='bar')
    else:
        ax = None
    end_time = time.time()  # End timing
    cost = f"Operation completed in {end_time - start_time} seconds."
    return counts, ax

class TestTaskFunc(unittest.TestCase):

    def test_normal_case(self):
        df = {'Column1': ['0', '332', 'a', '332'], 'Column2': ['332', '33', 'a', 'b']}
        target_value = '332'
        counts, ax = task_func(df, target_value)
        expected_counts = pd.Series([2, 1], index=['Column1', 'Column2'])
        pd.testing.assert_series_equal(counts, expected_counts)
        self.assertIsNotNone(ax)

    def test_empty_dataframe(self):
        df = {}
        target_value = '332'
        counts, ax = task_func(df, target_value)
        expected_counts = pd.Series([], dtype=int)
        pd.testing.assert_series_equal(counts, expected_counts)
        self.assertIsNone(ax)
    
    def test_no_occurrences(self):
        df = {'Column1': ['1', '2', '3'], 'Column2': ['4', '5', '6']}
        target_value = '332'
        counts, ax = task_func(df, target_value)
        expected_counts = pd.Series([0, 0], index=['Column1', 'Column2'])
        pd.testing.assert_series_equal(counts, expected_counts)
        self.assertIsNotNone(ax)  # Axes should still be created

    def test_single_column_multiple_occurrences(self):
        df = {'Column1': ['332', '332', '332']}
        target_value = '332'
        counts, ax = task_func(df, target_value)
        expected_counts = pd.Series([3], index=['Column1'])
        pd.testing.assert_series_equal(counts, expected_counts)
        self.assertIsNotNone(ax)

    def test_data_type_variations(self):
        df = {'Column1': [332, '332', 332.0, 'a', '332']}
        target_value = '332'
        counts, ax = task_func(df, target_value)
        expected_counts = pd.Series([3], index=['Column1'])
        pd.testing.assert_series_equal(counts, expected_counts)
        self.assertIsNotNone(ax)

if __name__ == '__main__':
    unittest.main()