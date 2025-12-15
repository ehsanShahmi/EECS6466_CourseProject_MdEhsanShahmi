import os
import unittest
import csv
import collections

# Constants
FILE_NAME = 'file_sizes.csv'

def task_func(my_path):
    """
    Create a report on the file size in a directory and write it to a CSV file.

    Parameters:
    my_path (str): The directory path.

    Returns:
    str: The path of the CSV file.
    """
    file_sizes = collections.defaultdict(int)

    for dirpath, dirnames, filenames in os.walk(my_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            file_sizes[f] += os.path.getsize(fp)

    with open(os.path.join(my_path, FILE_NAME), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File Name', 'Size'])
        for row in file_sizes.items():
            writer.writerow(row)

    return os.path.join(my_path, FILE_NAME)

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create a temporary directory and files for testing."""
        self.test_dir = 'test_directory'
        os.makedirs(self.test_dir, exist_ok=True)
        self.file1 = os.path.join(self.test_dir, 'file1.txt')
        self.file2 = os.path.join(self.test_dir, 'file2.txt')
        
        with open(self.file1, 'w') as f:
            f.write('Hello, world!')
        with open(self.file2, 'w') as f:
            f.write('Another file content.')
    
    def tearDown(self):
        """Cleanup the test directory."""
        for filename in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, filename)
            os.remove(file_path)
        os.rmdir(self.test_dir)

    def test_csv_file_creation(self):
        """Test that the CSV file is created."""
        result = task_func(self.test_dir)
        self.assertTrue(os.path.isfile(result))

    def test_csv_file_content(self):
        """Test that the CSV file contains correct file sizes."""
        task_func(self.test_dir)
        with open(os.path.join(self.test_dir, FILE_NAME), mode='r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            self.assertEqual(header, ['File Name', 'Size'])
            data = list(reader)
            self.assertEqual(len(data), 2)
            self.assertIn(['file1.txt', str(os.path.getsize(self.file1))], data)
            self.assertIn(['file2.txt', str(os.path.getsize(self.file2))], data)

    def test_empty_directory(self):
        """Test behavior for an empty directory."""
        empty_dir = 'empty_directory'
        os.makedirs(empty_dir, exist_ok=True)
        result = task_func(empty_dir)
        with open(result, 'r') as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            self.assertEqual(header, ['File Name', 'Size'])
            data = list(reader)
            self.assertEqual(len(data), 0)
        os.rmdir(empty_dir)

    def test_non_existent_directory(self):
        """Test behavior when the provided directory does not exist."""
        non_existent_dir = 'non_existent_directory'
        with self.assertRaises(FileNotFoundError):
            task_func(non_existent_dir)

if __name__ == '__main__':
    unittest.main()