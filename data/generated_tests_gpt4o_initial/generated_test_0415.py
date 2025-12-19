import pandas as pd
import unittest
import codecs

def task_func(dataframe: pd.DataFrame) -> pd.DataFrame:
    """
    Decodes all Unicode escape strings in a particular column ("UnicodeString") in a given Pandas DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The pandas DataFrame which must contain the column "UnicodeString".

    Returns:
    pd.DataFrame: The DataFrame with decoded strings in the "UnicodeString" column.

    Raises:
    KeyError: If the column "UnicodeString" does not exist in the DataFrame.
    TypeError: If the input is not a Pandas DataFrame.
    """
    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError("The input must be a pandas DataFrame.")

    if 'UnicodeString' not in dataframe.columns:
        raise KeyError("'UnicodeString' column not found in the DataFrame.")

    dataframe['UnicodeString'] = dataframe['UnicodeString'].apply(lambda x: codecs.decode(x, 'unicode_escape'))

    return dataframe

class TestTaskFunc(unittest.TestCase):

    def test_valid_unicode_decoding(self):
        df = pd.DataFrame({
            'Name': ['John', 'Anna', 'Peter'],
            'Age': [27, 23, 29],
            'Salary': [50000, 60000, 70000],
            'UnicodeString': ['\u004A\u006F\u0068\u006E', '\u0041\u006E\u006E\u0061', '\u0050\u0065\u0074\u0065\u0072']
        })
        result = task_func(df)
        expected = pd.DataFrame({
            'Name': ['John', 'Anna', 'Peter'],
            'Age': [27, 23, 29],
            'Salary': [50000, 60000, 70000],
            'UnicodeString': ['John', 'Anna', 'Peter']
        })
        pd.testing.assert_frame_equal(result, expected)

    def test_empty_dataframe(self):
        df = pd.DataFrame(columns=['Name', 'Age', 'Salary', 'UnicodeString'])
        result = task_func(df)
        expected = pd.DataFrame(columns=['Name', 'Age', 'Salary', 'UnicodeString'])
        pd.testing.assert_frame_equal(result, expected)

    def test_non_dataframe_input(self):
        with self.assertRaises(TypeError):
            task_func("Not a DataFrame")

    def test_missing_unicode_column(self):
        df = pd.DataFrame({
            'Name': ['John', 'Anna', 'Peter'],
            'Age': [27, 23, 29],
            'Salary': [50000, 60000, 70000]
        })
        with self.assertRaises(KeyError):
            task_func(df)

    def test_unicode_escape_character(self):
        df = pd.DataFrame({
            'Name': ['Test'],
            'Age': [30],
            'Salary': [60000],
            'UnicodeString': ['\u0074\u0065\u0073\u0074']
        })
        result = task_func(df)
        expected = pd.DataFrame({
            'Name': ['Test'],
            'Age': [30],
            'Salary': [60000],
            'UnicodeString': ['test']
        })
        pd.testing.assert_frame_equal(result, expected)

if __name__ == '__main__':
    unittest.main()