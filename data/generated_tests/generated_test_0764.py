import csv
import random
import unittest
import os

def task_func(csv_file='names.csv', 
          latin_names=['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'],
          names=['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'],
          encoding='latin-1', rng_seed=None):
    """
    Create a CSV file with 100 lines. Each line contains a name and an age (randomly generated between 20 and 50).
    Half of the names are randomly selected from a list of Latin names (default: ['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz']), 
    the other half from a list of English names (default: ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones']).
    All names are encoded using the specified encoding.
    If empty name arrays are passed, a csv with headers but no entries is generated.

    Args:
    - csv_file (str, optional): Name of the CSV file to be created. Defaults to 'names.csv'.
    - latin_names (list, optional): List of Latin names. Defaults to ['Sopetón', 'Méndez', 'Gómez', 'Pérez', 'Muñoz'].
    - names (list, optional): List of English names. Defaults to ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'].
    - encoding (str, optional): The encoding used for writing the names. Defaults to 'latin-1'
    - rng_seed (int, optional): The seed for the rng. Defaults to None.

    Returns:
    - str: The CSV file name.

    Raises:
    - TypeError: If csv_file is not a string.
    - TypeError: If latin_names is not an array.
    - TypeError: If names is not an array.

    Requirements:
    - csv
    - random

    Example:
    >>> file_name = task_func()
    >>> print(file_name)
    names.csv

    >>> file_name = task_func(csv_file='test.csv', names=['simon', 'alex'], rng_seed=1)
    >>> with open(file_name, 'r', newline='', encoding='latin-1') as csvfile:
    ...     reader = csv.reader(csvfile)
    ...     rows = list(reader)
    ...     print(rows)
    [['Name', 'Age'], ['Méndez', '38'], ['simon', '28'], ['Sopetón', '35'], ['alex', '35'], ['Pérez', '45'], ...]
    """

class TestTaskFunction(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_names.csv'

    def tearDown(self):
        try:
            os.remove(self.test_file)
        except OSError:
            pass

    def test_default_file_creation(self):
        file_name = task_func(csv_file=self.test_file)
        self.assertEqual(file_name, self.test_file)
        with open(file_name, 'r', encoding='latin-1') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), 101)  # 100 names + header

    def test_empty_name_lists(self):
        file_name = task_func(csv_file=self.test_file, latin_names=[], names=[])
        self.assertEqual(file_name, self.test_file)
        with open(file_name, 'r', encoding='latin-1') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            self.assertEqual(len(rows), 1)  # Only header

    def test_invalid_csv_file_type(self):
        with self.assertRaises(TypeError):
            task_func(csv_file=123)

    def test_invalid_latin_names_type(self):
        with self.assertRaises(TypeError):
            task_func(latin_names="not a list")

    def test_invalid_names_type(self):
        with self.assertRaises(TypeError):
            task_func(names=10)

if __name__ == '__main__':
    unittest.main()