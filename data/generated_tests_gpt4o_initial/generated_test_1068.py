import unittest
import warnings
import pandas as pd
import sqlite3
import os

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Setup a temporary SQLite database for testing
        self.db_path = 'test_database.db'
        self.create_test_db()

    def tearDown(self):
        # Remove the test database file after tests
        os.remove(self.db_path)

    def create_test_db(self):
        # Create a test SQLite database with a sample table
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE test_table (column1 INTEGER, column2 INTEGER)')
        # Insert sample data into the table
        for i in range(100):
            cursor.execute('INSERT INTO test_table (column1, column2) VALUES (?, ?)', (i, i * 2))
        conn.commit()
        conn.close()

    def test_fetch_data(self):
        query = 'SELECT * FROM test_table'
        data = task_func(self.db_path, query)
        self.assertEqual(len(data), 100)
        self.assertEqual(list(data.columns), ['column1', 'column2'])

    def test_warn_large_dataset(self):
        query = 'SELECT * FROM test_table'
        with self.assertRaises(Warning) as context:
            with warnings.catch_warnings(record=True) as w:
                task_func(self.db_path, query, warn_large_dataset=True)
                self.assertGreater(len(w), 0)
                self.assertEqual(str(context.warning[0].message), "The data contains more than 10000 rows.")

    def test_fetch_empty_data(self):
        # Create a new table with no data
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE empty_table (column1 INTEGER, column2 INTEGER)')
        conn.commit()
        conn.close()
        
        query = 'SELECT * FROM empty_table'
        data = task_func(self.db_path, query)
        self.assertEqual(len(data), 0)

    def test_fetch_non_existent_table(self):
        query = 'SELECT * FROM non_existent_table'
        with self.assertRaises(Exception) as context:
            task_func(self.db_path, query)
            self.assertTrue("Error fetching data from the database:" in str(context.exception))

    def test_invalid_query(self):
        # Test with an invalid SQL query
        invalid_query = 'SELECT * FROM'  # incomplete SQL statement
        with self.assertRaises(Exception) as context:
            task_func(self.db_path, invalid_query)
            self.assertTrue("Error fetching data from the database:" in str(context.exception))

if __name__ == '__main__':
    unittest.main()