import csv
from collections import Counter
import operator
import unittest

def task_func(csv_file, csv_delimiter):
    """
    Reads a CSV file and counts the most common words in the file.

    This function opens the specified CSV file using the provided delimiter, reads its contents,
    and counts the frequency of each word. It returns a list of tuples, each containing a word 
    and its frequency, sorted by frequency in descending order.

    Note: The function assumes that each cell in the CSV contains a single word.

    Parameters:
        csv_file (str): The path to the CSV file to be read.
        csv_delimiter (str): The delimiter used in the CSV file.

    Requirements:
    - csv
    - collections.Counter
    - operator

    Returns:
        list of tuple: A list of tuples where each tuple contains a word and its count,
                       sorted by count in descending order.
    """
    words = []

    with open(csv_file, 'r') as f:
        reader = csv.reader(f, delimiter=csv_delimiter)
        for row in reader:
            words.extend(row)

    word_counter = Counter(words)
    most_common_words = sorted(word_counter.items(), key=operator.itemgetter(1), reverse=True)

    return most_common_words

class TestTaskFunction(unittest.TestCase):
    
    def setUp(self):
        """Create temp CSV files for testing."""
        self.test_file1 = 'test_data1.csv'
        self.test_file2 = 'test_data2.csv'
        with open(self.test_file1, 'w') as f:
            f.write("apple,banana,apple\nbanana,orange,banana")
        with open(self.test_file2, 'w') as f:
            f.write("dog,cat,cat,dog,dog\nfish")

    def tearDown(self):
        """Remove the temp CSV files after tests."""
        import os
        os.remove(self.test_file1)
        os.remove(self.test_file2)

    def test_word_count_from_file1(self):
        """Test the word count from the first CSV file."""
        expected_result = [('banana', 3), ('apple', 2), ('orange', 1)]
        result = task_func(self.test_file1, ',')
        self.assertEqual(result, expected_result)

    def test_word_count_from_file2(self):
        """Test the word count from the second CSV file."""
        expected_result = [('dog', 3), ('cat', 2), ('fish', 1)]
        result = task_func(self.test_file2, ',')
        self.assertEqual(result, expected_result)

    def test_empty_file(self):
        """Test the function with an empty CSV file."""
        empty_file = 'empty.csv'
        with open(empty_file, 'w') as f:
            f.write("")
        expected_result = []
        result = task_func(empty_file, ',')
        self.assertEqual(result, expected_result)

    def test_single_word_file(self):
        """Test the function with a CSV file that contains a single word."""
        single_word_file = 'single_word.csv'
        with open(single_word_file, 'w') as f:
            f.write("hello")
        expected_result = [('hello', 1)]
        result = task_func(single_word_file, ',')
        self.assertEqual(result, expected_result)

    def test_different_delimiter(self):
        """Test the function with a different CSV delimiter."""
        test_file3 = 'test_data3.csv'
        with open(test_file3, 'w') as f:
            f.write("red;blue;green\nblue;green;green")
        expected_result = [('green', 3), ('blue', 2), ('red', 1)]
        result = task_func(test_file3, ';')
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()