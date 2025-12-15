import unittest
import os
import sqlite3

# Here is your prompt:
import sqlite3
import numpy as np
from random import choice, seed


def task_func(db_path, table_name, num_entries, random_seed=None):
    """
    Insert random data into an SQLite3 table that contains random names, ages, and heights.
    If the table does not exist, it will be created.
    This function uses the following constants:
    - NAMES: List of possible names ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia'].
    - AGES: Range of possible ages from 18 to 64.
    - HEIGHTS: Range of possible heights from 150cm to 199cm.

    Parameters:
    db_path (str): The path to the SQLite3 database file.
    table_name (str): The name of the table to insert data into.
    num_entries (int): The number of entries to insert. Must not be negative.
    random_seed (int, optional): Seed for random number generation. Defaults to None (no fixed seed).

    Returns:
    int: The number of rows inserted.

    Raises:
    ValueError: If num_entries is negative.
    
    Requirements:
    - sqlite3
    - numpy
    - random.choice
    - random.seed

    Example:
    >>> task_func('path_to_test.db', 'People', 100, random_seed=42)
    100
    """ 
    # The implementation code remains unchanged and is not provided here.

class TestTaskFunction(unittest.TestCase):
    
    def setUp(self):
        # Set up a temporary SQLite database and a test table
        self.db_path = 'test_database.db'
        self.table_name = 'People'
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        
    def tearDown(self):
        # Clean up the database after each test
        self.conn.close()
        os.remove(self.db_path)

    def test_insert_positive_entries(self):
        result = task_func(self.db_path, self.table_name, 100)
        self.assertEqual(result, 100)
        
        self.cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 100)

    def test_insert_zero_entries(self):
        result = task_func(self.db_path, self.table_name, 0)
        self.assertEqual(result, 0)

        self.cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 0)

    def test_insert_negative_entries(self):
        with self.assertRaises(ValueError):
            task_func(self.db_path, self.table_name, -10)

    def test_insert_with_random_seed(self):
        result = task_func(self.db_path, self.table_name, 50, random_seed=10)
        self.assertEqual(result, 50)

        self.cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        count = self.cursor.fetchone()[0]
        self.assertEqual(count, 50)

    def test_table_creation_if_not_exists(self):
        task_func(self.db_path, self.table_name, 10)
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (self.table_name,))
        table_exists = self.cursor.fetchone() is not None
        self.assertTrue(table_exists)

if __name__ == '__main__':
    unittest.main()