import unittest
import os
import numpy as np
import pandas as pd

# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
OUTPUT_DIR = './output'

def task_func(file_path, output_dir=OUTPUT_DIR):
    """
    Create a CSV file containing a 2D matrix populated exclusively with random lowercase letters.
    
    Parameters:
    - file_path (str): The path of the CSV file to be created.
    - output_dir (str, optional): The dir of the CSV file to be created.
    
    Returns:
    None: Writes a CSV file to the specified path.
    
    Requirements:
    - pandas
    - numpy

    Example:
    >>> task_func(os.path.join(OUTPUT_DIR, 'random_matrix.csv'))
    """

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)
    matrix = pd.DataFrame(np.random.choice(LETTERS, (10, 10)))
    matrix.to_csv(file_path, sep='\t', header=False, index=False)

    return None

class TestTaskFunction(unittest.TestCase):

    def setUp(self):
        # Setup for the tests that includes creating an output directory
        self.test_output_dir = OUTPUT_DIR
        self.test_file_path = os.path.join(self.test_output_dir, 'random_matrix.csv')
        if not os.path.exists(self.test_output_dir):
            os.makedirs(self.test_output_dir)

    def tearDown(self):
        # Remove the created test file and directory after tests
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
        if os.path.exists(self.test_output_dir) and not os.listdir(self.test_output_dir):
            os.rmdir(self.test_output_dir)

    def test_create_csv_file(self):
        task_func(self.test_file_path)
        self.assertTrue(os.path.isfile(self.test_file_path), 
                        "The CSV file should be created.")

    def test_output_directory_creates(self):
        if os.path.exists(self.test_output_dir):
            os.rmdir(self.test_output_dir) # Remove to test creation
        task_func(self.test_file_path)
        self.assertTrue(os.path.exists(self.test_output_dir), 
                        "The output directory should be created.")

    def test_matrix_size(self):
        task_func(self.test_file_path)
        matrix = pd.read_csv(self.test_file_path, sep='\t', header=None)
        self.assertEqual(matrix.shape, (10, 10), 
                         "The matrix should be of size 10x10.")

    def test_matrix_contains_letters(self):
        task_func(self.test_file_path)
        matrix = pd.read_csv(self.test_file_path, sep='\t', header=None)
        # Check if all entries in the matrix are among the allowed letters
        self.assertTrue(matrix.applymap(lambda x: x in LETTERS).all().all(), 
                        "All elements of the matrix should be lowercase letters.")

if __name__ == '__main__':
    unittest.main()