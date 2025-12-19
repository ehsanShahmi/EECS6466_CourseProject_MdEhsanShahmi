import csv
import os
import unittest

# Here is your prompt:
import csv
import random
from faker import Faker


def task_func(file_path, num_rows, random_seed=None):
    """
    Generate a CSV file on a specific file path with fake personal data.
    The personal data consists of the following columns:
    - Name: random names generated with faker
    - Age: random age values: 20<=age<=60
    - Address: random adresses generated with faker
    - Email: random email adresses generated with faker

    Newlines '\n' in the generated addresses get replaced with ', '.
    The number of rows in the CSV file is determined by num_rows.

    Parameters:
    file_path (str): The file path where the CSV file should be created.
    num_rows (int): The number of rows of random data to generate.
    random_seed (int, optional): Seed used random generation. Same seed used for faker and random module.
                                 Defaults to None.
    
    Returns:
    str: The file path of the generated CSV file.

    Raises:
    ValueError: If num_rows is not an integer >= 0.

    Requirements:
    - csv
    - random
    - faker

    Example:
    >>> task_func('/tmp/people.csv', 100)
    '/tmp/people.csv'

    >>> path = task_func('test.csv', 5, random_seed=12)
    >>> with open(path, 'r') as file:
    >>>     reader = csv.reader(file)
    >>>     rows = list(reader)
    >>> print(rows)
    [
        ['Name', 'Age', 'Address', 'Email'], 
        ['Matthew Estrada', '50', '7479 Angela Shore, South Michael, MA 28059', 'johnstonjames@example.net'],
        ['Gabrielle Sullivan', '37', '83167 Donna Dale, Nicoleside, GA 91836', 'peterswilliam@example.org'],
        ['Jason Carlson', '53', '013 Kelly Lake Suite 414, West Michael, NY 75635', 'anthonycarson@example.com'],
        ['Alexander Lowe', '42', '183 Christian Harbor, South Joshuastad, PA 83984', 'palmermicheal@example.com'],
        ['John Benjamin', '29', '8523 Rhonda Avenue, Rosemouth, HI 32166', 'masonjohn@example.org']
    ]
    """

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test.csv'

    def tearDown(self):
        try:
            os.remove(self.test_file)
        except FileNotFoundError:
            pass

    def test_generate_csv_file(self):
        path = task_func(self.test_file, 5)
        self.assertTrue(os.path.isfile(path))

    def test_csv_content_header(self):
        task_func(self.test_file, 5)
        with open(self.test_file, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            self.assertEqual(header, ['Name', 'Age', 'Address', 'Email'])

    def test_csv_content_row_count(self):
        task_func(self.test_file, 10)
        with open(self.test_file, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertEqual(len(rows) - 1, 10)  # Excludes the header row

    def test_invalid_num_rows_negative(self):
        with self.assertRaises(ValueError):
            task_func(self.test_file, -1)

    def test_invalid_num_rows_non_integer(self):
        with self.assertRaises(ValueError):
            task_func(self.test_file, 'five')

if __name__ == '__main__':
    unittest.main()