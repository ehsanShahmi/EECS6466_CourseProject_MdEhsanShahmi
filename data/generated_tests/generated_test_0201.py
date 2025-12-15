import unittest
import pandas as pd
import numpy as np

# Here is your prompt:
import bisect
import statistics

def task_func(df, column, value):
    """
    Analyze a column of a pandas DataFrame, find the values that are larger than the average, and count the number of values that are larger than a given value.

    Parameters:
    df (DataFrame): The pandas DataFrame.
    column (str): The column to analyze.
    value (float): The value to compare with the data in the column.
    
    Returns:
    tuple: A tuple containing (numpy.ndarray, int, matplotlib.axes.Axes).
           The numpy array contains values greater than the average.
           The int is the number of values greater than the given value.
           The Axes object is for the generated histogram plot.

    Raises:
    ValueError: If the column does not exist in the DataFrame or value is not a number.

    Requirements:
    - bisect
    - statistics
    
    Example:
    >>> df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    >>> greater_avg, num_greater_value, ax = task_func(df, 'A', 5)
    """

               if column not in df.columns:
        raise ValueError(f"Column '{column}' does not exist in DataFrame")
    if not isinstance(value, (int, float)):
        raise ValueError("Value must be a number")

    data = df[column].values
    avg = statistics.mean(data)
    greater_avg = data[data > avg]
    
    data.sort()
    bpoint = bisect.bisect_right(data, value)
    num_greater_value = len(data) - bpoint
    
    ax = df.hist(column=column, bins=10)[0][0]
    # plt.show()
    
    return greater_avg, num_greater_value, ax

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.df_valid = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
        self.df_empty = pd.DataFrame(columns=['A'])
        self.df_invalid_col = pd.DataFrame({'B': [1, 2, 3]})

    def test_valid_case(self):
        greater_avg, num_greater_value, ax = task_func(self.df_valid, 'A', 5)
        self.assertTrue(np.array_equal(greater_avg, np.array([6, 7, 8, 9, 10])))
        self.assertEqual(num_greater_value, 5)

    def test_no_values_greater_than_avg(self):
        df = pd.DataFrame({'A': [1, 1, 1, 1]})
        greater_avg, num_greater_value, ax = task_func(df, 'A', 1)
        self.assertTrue(np.array_equal(greater_avg, np.array([])))
        self.assertEqual(num_greater_value, 0)

    def test_empty_dataframe(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.df_empty, 'A', 1)
        self.assertEqual(str(context.exception), "Column 'A' does not exist in DataFrame")

    def test_column_does_not_exist(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.df_invalid_col, 'A', 1)
        self.assertEqual(str(context.exception), "Column 'A' does not exist in DataFrame")

    def test_invalid_value_type(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.df_valid, 'A', 'string_value')
        self.assertEqual(str(context.exception), "Value must be a number")

if __name__ == '__main__':
    unittest.main()