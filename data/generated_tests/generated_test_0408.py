import sqlite3
import pandas as pd
import unittest

# Here is your prompt:
def task_func(db_file: str, query: str) -> pd.DataFrame:
    """Query an SQLite database and return the results.

    This function connects to a given SQLite database, executes a given SQL query,
    and returns the results as a pandas DataFrame.

    Parameters:
    - db_file (str): Path to the SQLite database file.
    - query (str): SQL query to execute.

    Returns:
    - pd.DataFrame: A DataFrame containing the results of the executed query.

    Requirements:
    - sqlite3
    - pandas

    Example:
    >>> db_file = 'sample_database.db'
    >>> df = task_func(db_file, "SELECT * FROM users WHERE name = 'John Doe'")
    pd.DataFrame:
    id        name  age
    --  ----------  ---
    ..  John Doe   ..
    >>> df = task_func(db_file, "SELECT age, COUNT(*) AS count FROM users GROUP BY age")
    pd.DataFrame:
    age  count
    ---  -----
    25   3
    """

    with sqlite3.connect(db_file) as conn:
        return pd.read_sql_query(query, conn)

# Test Suite
class TestTaskFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db_file = 'test_database.db'
        cls.conn = sqlite3.connect(cls.db_file)
        cls.create_test_data()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
        import os
        os.remove(cls.db_file)

    @classmethod
    def create_test_data(cls):
        cursor = cls.conn.cursor()
        cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('John Doe', 30)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Jane Doe', 25)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Alice Smith', 25)")
        cursor.execute("INSERT INTO users (name, age) VALUES ('Bob Brown', 40)")
        cls.conn.commit()

    def test_query_all_users(self):
        df = task_func(self.db_file, "SELECT * FROM users")
        expected_data = {
            'id': [1, 2, 3, 4],
            'name': ['John Doe', 'Jane Doe', 'Alice Smith', 'Bob Brown'],
            'age': [30, 25, 25, 40]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(df.reset_index(drop=True), expected_df.reset_index(drop=True)

    def test_query_user_by_name(self):
        df = task_func(self.db_file, "SELECT * FROM users WHERE name = 'John Doe'")
        expected_data = {
            'id': [1],
            'name': ['John Doe'],
            'age': [30]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(df.reset_index(drop=True), expected_df.reset_index(drop=True)

    def test_query_age_group_count(self):
        df = task_func(self.db_file, "SELECT age, COUNT(*) AS count FROM users GROUP BY age")
        expected_data = {
            'age': [25, 30, 40],
            'count': [2, 1, 1]
        }
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(df.sort_values(by='age').reset_index(drop=True), expected_df.sort_values(by='age').reset_index(drop=True)

    def test_empty_query(self):
        df = task_func(self.db_file, "SELECT * FROM users WHERE age = 999")
        expected_df = pd.DataFrame(columns=['id', 'name', 'age'])
        pd.testing.assert_frame_equal(df.reset_index(drop=True), expected_df)

    def test_query_with_invalid_sql(self):
        with self.assertRaises(pd.io.sql.DatabaseError):
            task_func(self.db_file, "SELECT * FORM users")  # Intentionally incorrect SQL query

if __name__ == '__main__':
    unittest.main()