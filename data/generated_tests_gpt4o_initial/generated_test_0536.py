import unittest
import os
import sqlite3
import pandas as pd

# Here is your prompt:
import sqlite3
import pandas as pd
import os


def task_func(db_name, table_name, csv_path="data.csv"):
    """
    Read SQLite3 table via pandas and export to a CSV file.

    Parameters:
    - db_name (str): The path to the SQLite3 database.
    - table_name (str): The name of the table to export.
    - csv_path (str, optional): The path where the CSV file will be saved. Defaults to 'data.csv'.

    Requirements:
    - sqlite3
    - pandas
    - os

    Returns:
    str: The absolute path of the exported CSV file.

    Example:
    >>> task_func('test.db', 'People')
    'data.csv'
    >>> task_func('/absolute/path/to/test.db', 'Orders', 'orders.csv')
    '/absolute/path/to/orders.csv'
    """

    try:
        conn = sqlite3.connect(db_name)
        df = pd.read_sql_query(f"SELECT * from {table_name}", conn)
        df.to_csv(csv_path, index=False)
        return os.path.abspath(csv_path)
    finally:
        conn.close()


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up a temporary SQLite database for testing."""
        self.db_name = 'test.db'
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE People (id INTEGER PRIMARY KEY, name TEXT)')
        self.cursor.execute('INSERT INTO People (name) VALUES (?)', ('Alice',))
        self.cursor.execute('INSERT INTO People (name) VALUES (?)', ('Bob',))
        self.connection.commit()

    def tearDown(self):
        """Clean up the database and temporary files after tests."""
        self.cursor.close()
        self.connection.close()
        os.remove(self.db_name)
        if os.path.exists('data.csv'):
            os.remove('data.csv')

    def test_export_csv_default_path(self):
        """Test exporting to default CSV file path."""
        result = task_func(self.db_name, 'People')
        self.assertEqual(result, os.path.abspath('data.csv'))
        self.assertTrue(os.path.exists('data.csv'))

    def test_export_csv_custom_path(self):
        """Test exporting to a custom CSV file path."""
        custom_path = 'custom_people.csv'
        result = task_func(self.db_name, 'People', custom_path)
        self.assertEqual(result, os.path.abspath(custom_path))
        self.assertTrue(os.path.exists(custom_path))

    def test_export_empty_table(self):
        """Test exporting an empty table."""
        self.cursor.execute('DROP TABLE People')
        self.cursor.execute('CREATE TABLE People (id INTEGER PRIMARY KEY, name TEXT)')
        self.connection.commit()
        result = task_func(self.db_name, 'People')
        self.assertEqual(result, os.path.abspath('data.csv'))
        self.assertTrue(os.path.exists('data.csv'))
        df = pd.read_csv('data.csv')
        self.assertTrue(df.empty)

    def test_export_non_existing_table(self):
        """Test exporting a non-existing table raises an error."""
        with self.assertRaises(pd.io.sql.DatabaseError):
            task_func(self.db_name, 'NonExistingTable')

if __name__ == '__main__':
    unittest.main()