import unittest
import os
import csv

class TestTaskFunc(unittest.TestCase):

    def test_empty_csv(self):
        """Test creating a CSV with 0 rows, should only contain headers."""
        file_path = 'test_empty.csv'
        result = task_func(file_path, 0)
        self.assertEqual(result, file_path)
        
        with open(file_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            rows = list(reader)
            self.assertEqual(len(rows), 1)  # Only header
            self.assertEqual(rows[0], ['Name', 'Age', 'Gender', 'Country'])
        
        os.remove(file_path)

    def test_one_row_csv(self):
        """Test creating a CSV with 1 random row."""
        file_path = 'test_one_row.csv'
        result = task_func(file_path, 1)
        self.assertEqual(result, file_path)
        
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
            self.assertEqual(len(rows), 1)  # One data row
        
        os.remove(file_path)

    def test_multiple_rows_csv(self):
        """Test creating a CSV with multiple random rows."""
        file_path = 'test_multiple_rows.csv'
        result = task_func(file_path, 5)
        self.assertEqual(result, file_path)
        
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
            self.assertEqual(len(rows), 5)  # Five data rows
        
        os.remove(file_path)

    def test_gender_and_country_options(self):
        """Test creating a CSV with custom gender and country options."""
        file_path = 'test_custom_options.csv'
        genders = ['CustomGender1', 'CustomGender2']
        countries = ['CustomCountry1', 'CustomCountry2']
        result = task_func(file_path, 3, gender=genders, countries=countries)
        self.assertEqual(result, file_path)
        
        with open(file_path, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)
            self.assertTrue(all(row['Gender'] in genders for row in rows))
            self.assertTrue(all(row['Country'] in countries for row in rows))
        
        os.remove(file_path)

    def test_seed_repeatability(self):
        """Test that using the same seed generates the same CSV content."""
        file_path_1 = 'test_seed_1.csv'
        file_path_2 = 'test_seed_2.csv'
        result_1 = task_func(file_path_1, 3, seed=42)
        result_2 = task_func(file_path_2, 3, seed=42)
        self.assertEqual(result_1, file_path_1)
        self.assertEqual(result_2, file_path_2)

        with open(file_path_1, 'r') as csv_file_1, open(file_path_2, 'r') as csv_file_2:
            reader_1 = list(csv.DictReader(csv_file_1))
            reader_2 = list(csv.DictReader(csv_file_2))
            self.assertEqual(reader_1, reader_2)  # Should be the same

        os.remove(file_path_1)
        os.remove(file_path_2)

if __name__ == '__main__':
    unittest.main()