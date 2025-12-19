import unittest
import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import ast
import os

# Here is your prompt:
def task_func(db_file):
    """
    Load e-mail data from an SQLite database and convert it into a Pandas DataFrame. 
    Calculate the sum, mean, and variance of the list associated with each e-mail and then record these values.

    - The function expects the SQLite database to have a table named "EmailData" with columns 'email' and 'list'.
    - The column 'list' contains a string representation of the list. It should be converted before usage.
    - The function will return a DataFrame with additional columns 'sum', 'mean', and 'var' representing the calculated sum, mean, and variance respectively for each e-mail.

    Parameters:
    - db_file (str): The path to the SQLite database file.

    Returns:
    - tuple: A tuple containing:
      - DataFrame: A pandas DataFrame with email data including the calculated sum, mean, and variance.
      - Axes: A matplotlib Axes object representing the plotted bar chart of sum, mean, and variance.

    Requirements:
    - pandas
    - sqlite3
    - numpy
    - matplotlib.pyplot
    - ast

    Example:
    >>> df, ax = task_func('data/task_func/db_1.db')
    >>> print(df)
    """

    conn = sqlite3.connect(db_file)
    df = pd.read_sql_query("SELECT * FROM EmailData", conn)
    df["list"] = df["list"].map(ast.literal_eval)
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)
    df['var'] = df['list'].apply(np.var)

    ax = df[['sum', 'mean', 'var']].plot(kind='bar')
    plt.show()

    return df, ax

class TestTaskFunc(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Set up a temporary SQLite database for testing
        cls.db_file = 'test_db.db'
        cls.conn = sqlite3.connect(cls.db_file)
        cls.create_test_table()

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
        os.remove(cls.db_file)

    @classmethod
    def create_test_table(cls):
        # Create the EmailData table with test data
        cls.conn.execute('''
            CREATE TABLE EmailData (email TEXT, list TEXT)
        ''')
        test_data = [
            ('test1@example.com', '[1, 2, 3]'),
            ('test2@example.com', '[4, 5, 6]'),
            ('test3@example.com', '[7, 8, 9]'),
            ('test4@example.com', '[]'),  # empty list
            ('test5@example.com', '[10, 20, 30]'),
        ]
        cls.conn.executemany('INSERT INTO EmailData (email, list) VALUES (?, ?)', test_data)
        cls.conn.commit()

    def test_output_structure(self):
        df, ax = task_func(self.db_file)
        self.assertIsInstance(df, pd.DataFrame, "The result should be a pandas DataFrame.")
        self.assertEqual(set(df.columns), {'email', 'list', 'sum', 'mean', 'var'}, "DataFrame should contain 'email', 'list', 'sum', 'mean', and 'var' columns.")

    def test_calculations(self):
        df, _ = task_func(self.db_file)
        self.assertEqual(df.loc[0, 'sum'], 6, "Sum for test1@example.com should be 6.")
        self.assertEqual(df.loc[1, 'mean'], 5, "Mean for test2@example.com should be 5.")
        self.assertAlmostEqual(df.loc[2, 'var'], 1, places=2, msg="Variance for test3@example.com should be 1.")

    def test_empty_list(self):
        df, _ = task_func(self.db_file)
        self.assertEqual(df.loc[3, 'sum'], 0, "Sum for test4@example.com (empty list) should be 0.")
        self.assertEqual(df.loc[3, 'mean'], 0, "Mean for test4@example.com (empty list) should be 0.")
        self.assertEqual(df.loc[3, 'var'], 0, "Variance for test4@example.com (empty list) should be 0.")

    def test_plotting(self):
        _, ax = task_func(self.db_file)
        self.assertIsInstance(ax, plt.Axes, "The second return value should be a matplotlib Axes object.")

if __name__ == '__main__':
    unittest.main()