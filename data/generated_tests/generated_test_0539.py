import sqlite3
from random import choice, seed
import os
import unittest

# Here is your prompt:
def task_func(db_name, table_name, num_entries, random_seed=None):
    """
    Create an SQLite3 table and fill it with random data using the provided database and table names.

    The function populates the table with columns 'name', 'age', 'height' using random data from the
    following constants:
    - NAMES: List of names ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
    - AGES: Range of ages from 18 to 65.
    - HEIGHTS: Range of heights from 150cm to 200cm.

    Parameters:
    db_name (str): The name of the SQLite3 database.
    table_name (str): The name of the table to create and populate.
    num_entries (int): The number of entries to insert. Must not be negative.
    random_seed (int, optional): The seed for generating random values. Default is None.

    Returns:
    str: The absolute path of the SQLite3 database file.

    Raises:
    ValueError: If num_entries is negative.
    
    Requirements:
    - sqlite3
    - random.choice
    - random.seed
    - os

    Example:
    >>> db_path = task_func('test.db', 'People', 100, random_seed=42)
    >>> print(db_path)
    '/absolute/path/to/test.db'
    """

    NAMES = ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
    AGES = range(18, 65)
    HEIGHTS = range(150, 200)

    if random_seed:
        seed(random_seed)

    if num_entries < 0:
        raise ValueError("num_entries must not be negative")

    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute(f"CREATE TABLE {table_name} (name TEXT, age INTEGER, height INTEGER)")

    for _ in range(num_entries):
        name = choice(NAMES)
        age = choice(AGES)
        height = choice(HEIGHTS)
        cur.execute(f"INSERT INTO {table_name} VALUES (?, ?, ?)", (name, age, height))

    conn.commit()
    return os.path.abspath(db_name)


class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.db_name = 'test.db'
        self.table_name = 'People'
    
    def tearDown(self):
        """Remove the test database after each test."""
        if os.path.exists(self.db_name):
            os.remove(self.db_name)

    def test_create_database(self):
        """Test that the database is created successfully."""
        db_path = task_func(self.db_name, self.table_name, 10)
        self.assertTrue(os.path.exists(db_path))
    
    def test_create_table_and_insert_data(self):
        """Test that the table is created and populated with data."""
        task_func(self.db_name, self.table_name, 10)
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        count = cur.fetchone()[0]
        self.assertEqual(count, 10)
    
    def test_negative_entries(self):
        """Test that a ValueError is raised for negative entries."""
        with self.assertRaises(ValueError) as context:
            task_func(self.db_name, self.table_name, -1)
        self.assertEqual(str(context.exception), "num_entries must not be negative")
    
    def test_random_seed_behavior(self):
        """Test that using a fixed random_seed generates the same data."""
        task_func(self.db_name, self.table_name, 10, random_seed=42)
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {self.table_name}")
        data1 = cur.fetchall()

        # Create a new database with the same seed
        task_func(self.db_name, self.table_name, 10, random_seed=42)
        cur.execute(f"SELECT * FROM {self.table_name}")
        data2 = cur.fetchall()

        self.assertEqual(data1, data2)

    def test_database_structure(self):
        """Test that the table has the correct structure."""
        task_func(self.db_name, self.table_name, 10)
        conn = sqlite3.connect(self.db_name)
        cur = conn.cursor()
        cur.execute(f"PRAGMA table_info({self.table_name})")
        columns = cur.fetchall()
        expected_columns = [('0', 'name', 'TEXT', 0, None, 0),
                            ('1', 'age', 'INTEGER', 0, None, 0),
                            ('2', 'height', 'INTEGER', 0, None, 0)]
        self.assertEqual(columns, expected_columns)


if __name__ == "__main__":
    unittest.main()