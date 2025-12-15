import sys
import sqlite3
import unittest
import os

# Constants
PATH_TO_APPEND = "path/to/whatever"
DATABASE = "path/to/database.db"

# Here is your prompt:
def task_func(path_to_append=PATH_TO_APPEND, database=DATABASE):
    """
    This function appends a given path to sys.path and updates an SQLite database with the path, 
    creating the table if needed and avoiding duplicates.

    Parameters:
    - path_to_append (str): A file system path to be appended to sys.path and inserted
      into the SQLite database. Defaults to 'path/to/whatever' if not specified.
    - database (str): The file system path to the SQLite database file. Defaults to
      'path/to/database.db' if not provided. The function interacts with this database
      to store the path.

    Returns:
    - str: The path that was appended to sys.path and inserted into the database.

    Requirements:
    - sys
    - sqlite3


    Examples:
    >>> task_func('path/to/new_directory', 'path/to/new_database.db')
    'path/to/new_directory'
    >>> task_func()
    'path/to/whatever'
    """

    sys.path.append(path_to_append)

    conn = sqlite3.connect(database)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS paths (path TEXT UNIQUE)")
    cur.execute("INSERT OR IGNORE INTO paths (path) VALUES (?)", (path_to_append,))
    conn.commit()
    conn.close()

    return path_to_append


class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        # Set up a fresh database for each test
        self.test_db = "test_database.db"
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def tearDown(self):
        # Cleanup: Remove the test database if it exists
        if os.path.exists(self.test_db):
            os.remove(self.test_db)

    def test_default_parameters(self):
        result = task_func(database=self.test_db)
        self.assertEqual(result, PATH_TO_APPEND)

        # Check if the path was added to the database
        conn = sqlite3.connect(self.test_db)
        cur = conn.cursor()
        cur.execute("SELECT path FROM paths")
        paths = cur.fetchall()
        conn.close()
        self.assertIn((PATH_TO_APPEND,), paths)

    def test_custom_path(self):
        custom_path = 'path/to/custom_directory'
        result = task_func(path_to_append=custom_path, database=self.test_db)
        self.assertEqual(result, custom_path)

        # Check if the custom path was added to the database
        conn = sqlite3.connect(self.test_db)
        cur = conn.cursor()
        cur.execute("SELECT path FROM paths")
        paths = cur.fetchall()
        conn.close()
        self.assertIn((custom_path,), paths)

    def test_duplicate_insertion(self):
        custom_path = 'path/to/another_directory'
        task_func(path_to_append=custom_path, database=self.test_db)  # First insert
        result = task_func(path_to_append=custom_path, database=self.test_db)  # Duplicate insert
        self.assertEqual(result, custom_path)

        # Check if the path is still only inserted once
        conn = sqlite3.connect(self.test_db)
        cur = conn.cursor()
        cur.execute("SELECT path FROM paths")
        paths = cur.fetchall()
        conn.close()
        self.assertEqual(len(paths), 1)  # Ensure only one entry exists

    def test_check_sys_path_modification(self):
        test_path = 'path/to/test'
        task_func(path_to_append=test_path, database=self.test_db)
        self.assertIn(test_path, sys.path)  # Verify path was added to sys.path

if __name__ == '__main__':
    unittest.main()