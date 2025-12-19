import os
import csv
import random
import unittest
from statistics import mean

# Constants
COLUMNS = ['Name', 'Age', 'Height', 'Weight']
PEOPLE_COUNT = 100

# Here is your prompt:
# (The provided task_func function is not modified or included in this test suite)

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.filename = 'people_report.csv'

    def tearDown(self):
        try:
            os.remove(self.filename)
        except OSError:
            pass

    def test_file_creation(self):
        """Test if the CSV file is created successfully."""
        path = task_func(self.filename)
        self.assertTrue(os.path.exists(path))

    def test_correct_number_of_rows(self):
        """Test if the CSV file contains the correct number of rows."""
        path = task_func(self.filename)
        with open(path, newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(len(rows), PEOPLE_COUNT + 2)  # +2 for header and averages row

    def test_average_calculation(self):
        """Test if the average values in the CSV file are calculated correctly."""
        path = task_func(self.filename)
        with open(path, newline='') as file:
            reader = csv.reader(file)
            rows = list(reader)
            data = rows[1:-1]  # Skip header and averages row
            
            ages = [int(row[1]) for row in data]
            heights = [int(row[2]) for row in data]
            weights = [int(row[3]) for row in data]

            expected_averages = [
                'Average',
                mean(ages),
                mean(heights),
                mean(weights)
            ]
            self.assertEqual(rows[-1], expected_averages)

    def test_column_names(self):
        """Test if the CSV file contains the correct column names."""
        path = task_func(self.filename)
        with open(path, newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            self.assertEqual(header, COLUMNS)

    def test_unique_names(self):
        """Test if the names in the CSV file are unique."""
        path = task_func(self.filename)
        with open(path, newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            names = [row[0] for row in reader]
            self.assertEqual(len(names), len(set(names)))  # Check for uniqueness

if __name__ == '__main__':
    unittest.main()