import unittest
import os
import sqlite3
import pandas as pd
from matplotlib import pyplot as plt


class TestTaskFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Setting up a temporary SQLite database for testing
        cls.db_name = 'test.db'
        cls.table_name = 'People'
        cls.conn = sqlite3.connect(cls.db_name)
        cls.create_test_table()

    @classmethod
    def tearDownClass(cls):
        # Remove the test database file after tests
        cls.conn.close()
        os.remove(cls.db_name)

    @classmethod
    def create_test_table(cls):
        # Create a table with sample data for testing purposes
        cls.conn.execute(f'''
            CREATE TABLE {cls.table_name} (
                id INTEGER PRIMARY KEY,
                age INTEGER,
                salary FLOAT,
                name TEXT
            )
        ''')
        cls.conn.execute(f"INSERT INTO {cls.table_name} (age, salary, name) VALUES (25, 50000, 'Alice')")
        cls.conn.execute(f"INSERT INTO {cls.table_name} (age, salary, name) VALUES (30, 70000, 'Bob')")
        cls.conn.commit()

    def test_task_func_returns_axes(self):
        ax = task_func(self.db_name, self.table_name)
        self.assertIsInstance(ax, plt.Axes)

    def test_task_func_x_axis_label(self):
        ax = task_func(self.db_name, self.table_name)
        self.assertEqual(ax.get_xlabel(), 'age')

    def test_task_func_y_axis_label(self):
        ax = task_func(self.db_name, self.table_name)
        self.assertEqual(ax.get_ylabel(), 'salary')

    def test_task_func_raises_error_with_one_numerical_column(self):
        self.conn.execute('DROP TABLE People')
        self.conn.execute(f'''
            CREATE TABLE People (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        ''')
        self.conn.commit()

        with self.assertRaises(ValueError) as context:
            task_func(self.db_name, 'People')
        self.assertEqual(str(context.exception), "The table must have at least two numerical columns to plot.")

    def test_task_func_raises_error_with_no_numerical_columns(self):
        self.conn.execute('DROP TABLE People')
        self.conn.execute(f'''
            CREATE TABLE People (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        ''')
        self.conn.commit()

        with self.assertRaises(ValueError) as context:
            task_func(self.db_name, 'People')
        self.assertEqual(str(context.exception), "The table must have at least two numerical columns to plot.")


if __name__ == '__main__':
    unittest.main()