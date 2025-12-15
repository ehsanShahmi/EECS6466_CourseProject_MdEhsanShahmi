import os
import csv
import unittest
from collections import Counter

# Constants
FILE_DIR = './yourdictfiles/'

def task_func(output_file, test_directory):
    """
    Count the number of words in multiple dictionary files (.txt) in a specific directory,
    export the counts to a CSV file, and then return the total number of words.

    Parameters:
    filename (str): The name of the output CSV file.
    test_directory (str): The directory containing the dictionary files (.txt).

    Returns:
    int: total number of words in .txt files

    Note:
    - Header for the csv output file is "Word", "Count"
    - Return 0 if the input invalid or error raised

    Requirements:
    - collections.Counter
    - os
    - csv

    Example:
    >>> task_func('word_counts.csv')
    10
    """
    total_words = 0
    try:
        word_counts = Counter()
        for file_name in os.listdir(test_directory):
            if not file_name.endswith('.txt'):
                continue
            with open(os.path.join(test_directory, file_name), 'r') as file:
                words = file.read().split()
                word_counts.update(words)

        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Word', 'Count'])
            writer.writerows(word_counts.items())
        
        for word in word_counts:
            total_words += word_counts[word]
    except Exception as e:
        print(e)
    return total_words

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        # Setup: Create a mock directory with .txt files for testing.
        self.test_directory = './test_dir/'
        os.makedirs(self.test_directory, exist_ok=True)
        
        # Create sample text files
        with open(os.path.join(self.test_directory, 'file1.txt'), 'w') as f:
            f.write("apple banana apple")
        with open(os.path.join(self.test_directory, 'file2.txt'), 'w') as f:
            f.write("banana orange")
        with open(os.path.join(self.test_directory, 'file3.txt'), 'w') as f:
            f.write("apple")
        with open(os.path.join(self.test_directory, 'file_invalid.txt'), 'w') as f:
            f.write("invalid file")

    def tearDown(self):
        # Cleanup: Remove test directory and files after tests
        for filename in os.listdir(self.test_directory):
            file_path = os.path.join(self.test_directory, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        os.rmdir(self.test_directory)

    def test_word_count(self):
        output_file = 'word_counts.csv'
        result = task_func(output_file, self.test_directory)
        self.assertEqual(result, 5)  # Testing total word count

    def test_csv_output(self):
        output_file = 'word_counts.csv'
        task_func(output_file, self.test_directory)
        expected_csv_content = [
            ['Word', 'Count'],
            ['apple', 3],
            ['banana', 2],
            ['orange', 1]
        ]
        with open(output_file, 'r') as f:
            reader = csv.reader(f)
            content = list(reader)
            self.assertEqual(content, expected_csv_content)

    def test_invalid_directory(self):
        output_file = 'word_counts.csv'
        result = task_func(output_file, './invalid_dir/')
        self.assertEqual(result, 0)  # Testing for invalid directory

    def test_no_txt_files(self):
        output_file = 'word_counts.csv'
        os.makedirs('./empty_dir/', exist_ok=True)  # Create an empty directory
        result = task_func(output_file, './empty_dir/')
        self.assertEqual(result, 0)  # No .txt files should return 0

    def test_empty_files(self):
        # Create an empty .txt file and test
        with open(os.path.join(self.test_directory, 'empty_file.txt'), 'w') as f:
            f.write("")
        output_file = 'word_counts.csv'
        result = task_func(output_file, self.test_directory)
        self.assertEqual(result, 5)  # Total should still count non-empty files

if __name__ == '__main__':
    unittest.main()