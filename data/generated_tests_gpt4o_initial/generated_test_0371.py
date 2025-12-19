from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import unittest

def task_func(l):
    """
    Scale the input field to the range [0, 1] and display it as a DataFrame.

    Parameters:
    l (numpy array): The input array.

    Returns:
    DataFrame: A pandas DataFrame of the scaled array.

    Requirements:
    - numpy
    - sklearn.preprocessing
    - pandas

    Note:
    - The return DataFrame use 'Scaled Values' as the column name.

    Example:
    >>> import numpy as np
    >>> l = np.array([10, 20, 30, 40, 50])
    >>> df = task_func(l)
    >>> print(int(df.iloc[0]['Scaled Values']))
    0
    """

    scaler = MinMaxScaler()
    l_scaled = scaler.fit_transform(l.reshape(-1, 1))
    df = pd.DataFrame(l_scaled, columns=['Scaled Values'])
    return df

class TestTaskFunc(unittest.TestCase):
    
    def test_basic_functionality(self):
        l = np.array([10, 20, 30, 40, 50])
        df = task_func(l)
        expected_df = pd.DataFrame({'Scaled Values': [0, 0.25, 0.5, 0.75, 1]})
        pd.testing.assert_frame_equal(df, expected_df)

    def test_negative_values(self):
        l = np.array([-10, -20, -30])
        df = task_func(l)
        expected_df = pd.DataFrame({'Scaled Values': [1, 0.5, 0]})
        pd.testing.assert_frame_equal(df, expected_df)

    def test_zero_included(self):
        l = np.array([0, 5, 10])
        df = task_func(l)
        expected_df = pd.DataFrame({'Scaled Values': [0, 0.5, 1]})
        pd.testing.assert_frame_equal(df, expected_df)

    def test_floats(self):
        l = np.array([0.1, 0.2, 0.3, 0.4])
        df = task_func(l)
        expected_df = pd.DataFrame({'Scaled Values': [0, 0.33333333, 0.66666667, 1]})
        pd.testing.assert_frame_equal(df, expected_df, check_exact=False)

    def test_single_value(self):
        l = np.array([42])
        df = task_func(l)
        expected_df = pd.DataFrame({'Scaled Values': [0]})
        pd.testing.assert_frame_equal(df, expected_df)

if __name__ == '__main__':
    unittest.main()