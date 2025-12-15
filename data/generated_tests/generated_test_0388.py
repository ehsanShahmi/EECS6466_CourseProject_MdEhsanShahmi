import collections
import pandas as pd
import unittest
from unittest.mock import MagicMock

def task_func(my_tuple, path_csv_files):
    """
    Count the occurrences of each value in the specified columns in multiple CSV files.

    Parameters:
    my_tuple (tuple): The tuple of column names.
    path_csv_files (list of string): The list of csv files to read.

    Returns:
    dict: A dictionary where keys are column names and values are dictionaries 
        with unique values in the column as keys and their counts as values.

    Requirements:
    - collections
    - pandas

    Example:
    >>> from unittest.mock import MagicMock
    >>> import pandas as pd
    >>> df1 = pd.DataFrame({'Country': ['USA', 'Canada', 'USA'], 'Gender': ['Male', 'Female', 'Male']})
    >>> df2 = pd.DataFrame({'Country': ['UK', 'USA', 'Germany'], 'Gender': ['Male', 'Male', 'Female']})
    >>> pd.read_csv = MagicMock(side_effect=[df1, df2])
    >>> result = task_func(('Country', 'Gender'), ['file1.csv', 'file2.csv'])
    >>> print(result['Country'])
    Counter({'USA': 3, 'Canada': 1, 'UK': 1, 'Germany': 1})
    """

    counter = {column: collections.Counter() for column in my_tuple}

    for csv_file in path_csv_files:
        df = pd.read_csv(csv_file)

        for column in my_tuple:
            if column in df:
                counter[column].update(df[column])

    return counter

class TestTaskFunction(unittest.TestCase):
    
    def setUp(self):
        # Create mock DataFrames
        self.df1 = pd.DataFrame({'Country': ['USA', 'Canada', 'USA'], 'Gender': ['Male', 'Female', 'Male']})
        self.df2 = pd.DataFrame({'Country': ['UK', 'USA', 'Germany'], 'Gender': ['Male', 'Male', 'Female']})

    def test_count_countries(self):
        pd.read_csv = MagicMock(side_effect=[self.df1, self.df2])
        result = task_func(('Country',), ['file1.csv', 'file2.csv'])
        expected = collections.Counter({'USA': 3, 'Canada': 1, 'UK': 1, 'Germany': 1})
        self.assertEqual(result['Country'], expected)

    def test_count_genders(self):
        pd.read_csv = MagicMock(side_effect=[self.df1, self.df2])
        result = task_func(('Gender',), ['file1.csv', 'file2.csv'])
        expected = collections.Counter({'Male': 4, 'Female': 2})
        self.assertEqual(result['Gender'], expected)

    def test_count_multiple_columns(self):
        pd.read_csv = MagicMock(side_effect=[self.df1, self.df2])
        result = task_func(('Country', 'Gender'), ['file1.csv', 'file2.csv'])
        expected_country = collections.Counter({'USA': 3, 'Canada': 1, 'UK': 1, 'Germany': 1})
        expected_gender = collections.Counter({'Male': 4, 'Female': 2})
        self.assertEqual(result['Country'], expected_country)
        self.assertEqual(result['Gender'], expected_gender)

    def test_empty_csv_file(self):
        empty_df = pd.DataFrame(columns=['Country', 'Gender'])
        pd.read_csv = MagicMock(side_effect=[self.df1, empty_df])
        result = task_func(('Country', 'Gender'), ['file1.csv', 'file2.csv'])
        expected_country = collections.Counter({'USA': 2, 'Canada': 1})
        expected_gender = collections.Counter({'Male': 2, 'Female': 1})
        self.assertEqual(result['Country'], expected_country)
        self.assertEqual(result['Gender'], expected_gender)

    def test_non_existent_columns(self):
        pd.read_csv = MagicMock(side_effect=[self.df1])
        result = task_func(('Age', 'Country'), ['file1.csv'])
        expected = collections.Counter()
        self.assertEqual(result['Age'], expected)  # 'Age' does not exist
        expected_country = collections.Counter({'USA': 2, 'Canada': 1})
        self.assertEqual(result['Country'], expected_country)

if __name__ == '__main__':
    unittest.main()