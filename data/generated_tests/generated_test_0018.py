import unittest
import os
import csv

class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        self.test_csv_path = "test_file.csv"
        with open(self.test_csv_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows([
                ["header1", "header2"],
                ["data1", "data2"],
                ["data3", "data4"],
                ["data5", "data6"],
                ["data7", "data8"],
                ["data9", "data10"]
            ])

    def tearDown(self):
        # Clean up created test files
        for split_file in os.listdir('.'):
            if split_file.startswith('split_'):
                os.remove(split_file)
        if os.path.exists(self.test_csv_path):
            os.remove(self.test_csv_path)

    def test_nonexistent_file(self):
        result = task_func("nonexistent_file.csv")
        self.assertEqual(result, [], "Expected empty list for nonexistent file.")

    def test_non_csv_file(self):
        with open("non_csv_file.txt", 'w') as f:
            f.write("This is not a CSV file.")
        result = task_func("non_csv_file.txt")
        self.assertEqual(result, [], "Expected empty list for non-CSV file.")
        os.remove("non_csv_file.txt")

    def test_valid_csv_split(self):
        result = task_func(self.test_csv_path)
        self.assertTrue(len(result) > 0, "Expected non-empty list for valid CSV file.")
        for split_file in result:
            self.assertTrue(os.path.exists(split_file), f"Expected file {split_file} to exist.")

    def test_correct_number_of_splits(self):
        result = task_func(self.test_csv_path)
        self.assertEqual(len(result), 3, "Expected 3 split files for a 6-row CSV (5 rows each).")

    def test_file_content_shuffle(self):
        result = task_func(self.test_csv_path)
        with open(result[0], 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
            self.assertNotEqual(rows[0], ["header1", "header2"], "Expected rows to be shuffled and not in original order.")

if __name__ == '__main__':
    unittest.main()