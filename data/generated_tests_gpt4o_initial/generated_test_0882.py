import unittest
import pandas as pd
import sqlite3
import os

# Here is your prompt:
def task_func(db_file, table_name, column_name, pattern='\d+[xX]'):
    """
    Find all matches with a regex pattern in a list of strings in an SQL database.
    
    The function loads an sql database and selects all entries from the specified
    table. Matches are returned in a DataFrame.

    Parameters:
    db_file (str): The SQLite database file.
    table_name (str): The name of the table to search.
    column_name (str): The name of the column to search.
    pattern (str, optional): The regex pattern to search for. Defaults to '\d+[xX]'.

    Returns:
    DataFrame: A pandas DataFrame with the matches.
        
    Raises:
    ValueError: If db_file does not exist.

    Requirements:
    - sqlite3
    - pandas
    - os
        
    Example:
    >>> result = task_func('task_func_data/sample.db', 'test_table', 'test_column')
    >>> print(result.head(10))
        id              test_column
    0    1                  4x4 car
    1    2           New 3x3 puzzle
    3    4  Product with 5X feature
    55  56                   1xsafe
    56  57                 3xmother
    57  58                  5xenjoy
    58  59                   2xhome
    59  60                 3xanswer
    60  61                   5xgirl
    61  62                   5xkind
    """

class TestTaskFunc(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.db_file = 'test.db'
        cls.connection = sqlite3.connect(cls.db_file)
        cls.cursor = cls.connection.cursor()
        cls.cursor.execute("CREATE TABLE test_table (id INTEGER, test_column TEXT)")
        cls.cursor.execute("INSERT INTO test_table VALUES (1, '4x4 car')")
        cls.cursor.execute("INSERT INTO test_table VALUES (2, 'New 3x3 puzzle')")
        cls.cursor.execute("INSERT INTO test_table VALUES (3, 'Some feature')")
        cls.cursor.execute("INSERT INTO test_table VALUES (4, 'Product with 5X feature')")
        cls.cursor.execute("INSERT INTO test_table VALUES (5, '1xsafe')")
        cls.connection.commit()
        
    @classmethod
    def tearDownClass(cls):
        cls.connection.close()
        os.remove(cls.db_file)

    def test_valid_matches(self):
        result = task_func(self.db_file, 'test_table', 'test_column')
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertGreater(len(result), 0)
        self.assertTrue(all(result['test_column'].str.contains(r'\d+[xX]')))

    def test_no_matches(self):
        result = task_func(self.db_file, 'test_table', 'test_column', pattern='no_match')
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertEqual(len(result), 0)

    def test_invalid_db_file(self):
        with self.assertRaises(ValueError):
            task_func('invalid_file.db', 'test_table', 'test_column')

    def test_empty_column(self):
        self.cursor.execute("CREATE TABLE empty_table (id INTEGER, test_column TEXT)")
        self.connection.commit()
        result = task_func(self.db_file, 'empty_table', 'test_column')
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertEqual(len(result), 0)

    def test_non_string_column(self):
        self.cursor.execute("CREATE TABLE number_table (id INTEGER, value INTEGER)")
        self.cursor.execute("INSERT INTO number_table VALUES (1, 10)")
        self.connection.commit()
        result = task_func(self.db_file, 'number_table', 'value')
        self.assertTrue(isinstance(result, pd.DataFrame))
        self.assertEqual(len(result), 0)

if __name__ == '__main__':
    unittest.main()