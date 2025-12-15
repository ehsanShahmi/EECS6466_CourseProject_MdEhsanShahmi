import unittest
import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class TestTaskFunction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up a test database and table for the test cases."""
        cls.conn = sqlite3.connect("test.db")
        cls.create_table()

    @classmethod
    def tearDownClass(cls):
        """Clean up the test database after all tests."""
        cls.conn.close()
        import os
        os.remove("test.db")

    @classmethod
    def create_table(cls):
        """Create a test table with sample data."""
        cls.conn.execute("CREATE TABLE People (age INTEGER)")
        sample_data = [(25,), (30,), (35,), (40,), (20,)]
        cls.conn.executemany("INSERT INTO People (age) VALUES (?)", sample_data)
        cls.conn.commit()

    def test_valid_age_distribution(self):
        """Test if the task_func returns a valid Axes object for valid ages."""
        ax = task_func("test.db", "People")
        self.assertIsInstance(ax, plt.Axes)

    def test_default_database_and_table(self):
        """Test the default parameters for the task_func."""
        ax = task_func()
        self.assertIsInstance(ax, plt.Axes)

    def test_negative_age_value(self):
        """Insert negative age into the database and assert ValueError is raised."""
        self.conn.execute("INSERT INTO People (age) VALUES (-5)")
        self.conn.commit()
        with self.assertRaises(ValueError):
            task_func("test.db", "People")

    def test_empty_table(self):
        """Test if the function handles empty tables properly."""
        self.conn.execute("DELETE FROM People")
        self.conn.commit()
        with self.assertRaises(ValueError):
            task_func("test.db", "People")

    def test_plot_properties(self):
        """Test if the plotted histogram has correct x-axis label."""
        ax = task_func("test.db", "People")
        self.assertEqual(ax.get_xlabel(), "age")

if __name__ == '__main__':
    unittest.main()