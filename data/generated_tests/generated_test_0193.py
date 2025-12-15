import pandas as pd
import numpy as np
from random import choice
import unittest

# Constants
DATA_TYPES = [str, int, float, list, tuple, dict, set]

# Provided prompt code (without modification)
def task_func(rows, columns):
    """
    Generates a DataFrame with a specified number of rows and columns, populated with randomly generated data.
    Each column's data type is randomly selected from a set of Python data types,
    including primitive and complex structures.
    """

    data = {}
    for col in range(columns):
        data_type = choice(DATA_TYPES)
        if data_type == str:
            data['col' + str(col)] = [''.join(np.random.choice(list('abcdefghijklmnopqrstuvwxyz'), size=5)) for _ in
                                      range(rows)]
        elif data_type in [int, float]:
            data['col' + str(col)] = np.random.choice([data_type(i) for i in range(10)], size=rows)
        elif data_type == list:
            data['col' + str(col)] = [list(np.random.choice(range(10), size=np.random.randint(1, 6))) for _ in
                                      range(rows)]
        elif data_type == tuple:
            data['col' + str(col)] = [tuple(np.random.choice(range(10), size=np.random.randint(1, 6))) for _ in
                                      range(rows)]
        elif data_type == dict:
            data['col' + str(col)] = [dict(zip(np.random.choice(range(10), size=np.random.randint(1, 6)),
                                               np.random.choice(range(10), size=np.random.randint(1, 6)))) for _ in
                                      range(rows)]
        elif data_type == set:
            data['col' + str(col)] = [set(np.random.choice(range(10), size=np.random.randint(1, 6))) for _ in
                                      range(rows)]

    df = pd.DataFrame(data)
    return df

class TestTaskFunc(unittest.TestCase):

    def test_dataframe_shape(self):
        """Test if the generated DataFrame has the correct shape."""
        df = task_func(5, 3)
        self.assertEqual(df.shape, (5, 3))

    def test_dataframe_column_types(self):
        """Test if all columns in the DataFrame are of the expected generated types."""
        df = task_func(5, 3)
        for col in df.columns:
            data_type = type(df[col][0])
            self.assertTrue(data_type in DATA_TYPES)

    def test_dataframe_row_count(self):
        """Test if the DataFrame contains the expected number of rows."""
        rows = 10
        df = task_func(rows, 5)
        self.assertEqual(len(df), rows)

    def test_dataframe_column_count(self):
        """Test if the DataFrame contains the expected number of columns."""
        columns = 4
        df = task_func(3, columns)
        self.assertEqual(df.shape[1], columns)

    def test_random_data_distribution(self):
        """Test if the generated data is from the correct types and ranges."""
        df = task_func(5, 2)
        for col in df.columns:
            unique_values = df[col].apply(type).unique()
            if str in unique_values:
                self.assertTrue(all(isinstance(x, str) for x in df[col]))
            elif int in unique_values:
                self.assertTrue(all(isinstance(x, int) for x in df[col]) and all(0 <= x < 10 for x in df[col]))
            elif float in unique_values:
                self.assertTrue(all(isinstance(x, float) for x in df[col]) and all(0.0 <= x < 10.0 for x in df[col]))
            elif list in unique_values:
                self.assertTrue(all(isinstance(x, list) and all(0 <= item < 10 for item in x) for x in df[col]))
            elif tuple in unique_values:
                self.assertTrue(all(isinstance(x, tuple) and all(0 <= item < 10 for item in x) for x in df[col]))
            elif dict in unique_values:
                self.assertTrue(all(isinstance(x, dict) and all(0 <= k < 10 and 0 <= v < 10 for k, v in x.items()) for x in df[col]))
            elif set in unique_values:
                self.assertTrue(all(isinstance(x, set) and all(0 <= item < 10 for item in x) for x in df[col]))

if __name__ == '__main__':
    unittest.main()