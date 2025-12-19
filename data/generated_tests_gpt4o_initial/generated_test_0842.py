import sqlite3
import unittest
import os
import random

def task_func(db_path,
              num_entries,
              users=['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
              countries=['USA', 'UK', 'Canada', 'Australia', 'India'],
              random_seed=None):
    """
    Generate an SQLite database to a given file path with random user data.

    The user data consists of a table named 'users' with columns:
        - id (integer): Used as Primary Key. numbering of entries starting at 0.
        - name (string): name of the user. sampled from 'users'
        - age (int): age of the user, where 20 <= age <= 60.
        - country (string): sampled from 'countries'

    The number of entries in the database is determined by num_entries.

    Parameters:
    db_path (str): The file path where the SQLite database should be created.
    num_entries (int): The number of entries of random data to generate.
    users (list of str, optional): List of user names to choose from. Defaults to ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'].
    countries (list of str, optional): List of countries to choose from. Defaults to ['USA', 'UK', 'Canada', 'Australia', 'India'].
    random_seed (int, optional): Seed used in rng. Defaults to Nonee.
    
    Returns:
    str: The file path of the generated SQLite database.
    """
    random.seed(random_seed)

    conn = sqlite3.connect(db_path)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE users
        (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, country TEXT)
    ''')

    for _ in range(num_entries):
        user = random.choice(users)
        age = random.randint(20, 60)
        country = random.choice(countries)
        c.execute('INSERT INTO users (name, age, country) VALUES (?, ?, ?)', (user, age, country))

    conn.commit()
    conn.close()

    return db_path

class TestTaskFunction(unittest.TestCase):
    
    def setUp(self):
        self.db_path = 'test_users.db'
        
    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
    
    def test_create_database(self):
        result = task_func(self.db_path, 10)
        self.assertEqual(result, self.db_path)
        self.assertTrue(os.path.isfile(self.db_path))

    def test_number_of_entries(self):
        task_func(self.db_path, 5)
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM users")
        count = c.fetchone()[0]
        conn.close()
        self.assertEqual(count, 5)

    def test_user_data_structure(self):
        task_func(self.db_path, 3)
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("PRAGMA table_info(users)")
        columns = c.fetchall()
        conn.close()
        
        expected_columns = [(0, 'id', 'INTEGER', 0, None, 1),
                            (1, 'name', 'TEXT', 0, None, 0),
                            (2, 'age', 'INTEGER', 0, None, 0),
                            (3, 'country', 'TEXT', 0, None, 0)]
        self.assertEqual(columns, expected_columns)

    def test_random_seed_effect(self):
        task_func(self.db_path, 10, random_seed=1)
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        results1 = c.fetchall()
        conn.close()
        
        task_func(self.db_path, 10, random_seed=1)  # Re-generate with the same seed
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT * FROM users")
        results2 = c.fetchall()
        conn.close()
        
        self.assertEqual(results1, results2)

    def test_age_range(self):
        task_func(self.db_path, 100)
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT age FROM users")
        ages = c.fetchall()
        conn.close()
        
        for (age,) in ages:
            self.assertGreaterEqual(age, 20)
            self.assertLessEqual(age, 60)

if __name__ == '__main__':
    unittest.main()