import re
import pandas as pd
import numpy as np
import unittest

# Constants
DATA_PATTERN = r'>\d+\.\d+<'

def task_func(dataframe, data_pattern=DATA_PATTERN):
    """
    Extract numeric data from a Pandas DataFrame based on a specific pattern. The function searches 
    each cell for occurrences of the regex pattern '>number<number>' (e.g., '>1.23<') and replaces 
    the cell content with the extracted numeric value. If no match is found, the cell is replaced with NaN.
    
    Parameters:
    - dataframe (pd.DataFrame): A pandas DataFrame containing data to be processed.
    - data_pattern (str, optional): data search pattern. Default value is '>\d+\.\d+<'.
    
    Returns:
    - pd.DataFrame: A modified DataFrame with cells containing the extracted numeric values or NaN.
    
    Requirements:
    - re
    - pandas
    - numpy
    
    Example:
    >>> import pandas as pd
    >>> df = pd.DataFrame({'A': ['>1.23<', '>4.56<'], 'B': ['>7.89<', '>0.12<']})
    >>> task_func(df)
          A     B
    0  1.23  7.89
    1  4.56  0.12
    """
    for col in dataframe.columns:
        dataframe[col] = dataframe[col].apply(lambda x: float(re.search(data_pattern, x).group(0)[1:-1])
                                              if pd.notnull(x) and re.search(data_pattern, x) else np.nan)
    return dataframe

class TestTaskFunc(unittest.TestCase):

    def test_basic_case(self):
        df = pd.DataFrame({'A': ['>1.23<', '>4.56<'], 'B': ['>7.89<', '>0.12<']})
        expected = pd.DataFrame({'A': [1.23, 4.56], 'B': [7.89, 0.12]})
        result = task_func(df)
        pd.testing.assert_frame_equal(result, expected)

    def test_no_matches(self):
        df = pd.DataFrame({'A': ['abc', 'def'], 'B': ['ghi', 'jkl']})
        expected = pd.DataFrame({'A': [np.nan, np.nan], 'B': [np.nan, np.nan]})
        result = task_func(df)
        pd.testing.assert_frame_equal(result, expected)

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['A', 'B'])
        expected = pd.DataFrame(columns=['A', 'B'])
        result = task_func(df)
        pd.testing.assert_frame_equal(result, expected)

    def test_mixed_data(self):
        df = pd.DataFrame({'A': ['>1.23<', 'nope', '>3.45<'], 'B': ['>6.78<', 'invalid', '>0.00<']})
        expected = pd.DataFrame({'A': [1.23, np.nan, 3.45], 'B': [6.78, np.nan, 0.00]})
        result = task_func(df)
        pd.testing.assert_frame_equal(result, expected)

    def test_nan_values(self):
        df = pd.DataFrame({'A': [np.nan, '>2.34<', '>5.67<'], 'B': ['>8.90<', np.nan, '>1.23<']})
        expected = pd.DataFrame({'A': [np.nan, 2.34, 5.67], 'B': [8.90, np.nan, 1.23]})
        result = task_func(df)
        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()