import unittest
import json
import os
from collections import defaultdict
import itertools
import random

# Here is your prompt:
def task_func(LETTERS, n):
    """
    Generates all possible combinations of a given set of letters of length 'n'.
    Counts the occurrences of each letter in these combinations and saves the results
    in a JSON file. The name of the file is prefix_<random-number-here>.json. The value of
    <random-number-here> is between 0 and 100. 

    Parameters:
        LETTERS (list): The list of letters to generate combinations from.
        n (int): The length of the combinations.

    Returns:
        str: The name of the generated JSON file containing letter counts.

    Requirements:
    - collections.defaultdict
    - itertools
    - json
    - random

    Examples:
    >>> isinstance(task_func(['a', 'b', 'c', 'd', 'e'], 3), str)
    True
    >>> 'letter_combinations_' in task_func(['a', 'b', 'c', 'd', 'e'], 2)
    True
    """
    
    combinations = list(itertools.combinations(LETTERS, n))
    letter_counts = defaultdict(int)

    for combination in combinations:
        for letter in combination:
            letter_counts[letter] += 1

    filename = f'letter_combinations_{random.randint(1, 100)}.json'
    with open(filename, 'w') as f:
        json.dump(letter_counts, f)

    return filename

class TestTaskFunc(unittest.TestCase):

    def test_valid_filename_format(self):
        """Test if the generated filename has the correct format."""
        letters = ['a', 'b', 'c']
        n = 2
        filename = task_func(letters, n)
        self.assertTrue(filename.startswith("letter_combinations_") and filename.endswith(".json"))

    def test_json_file_creation(self):
        """Test if a JSON file is created after the function is called."""
        letters = ['x', 'y', 'z']
        n = 1
        filename = task_func(letters, n)
        self.assertTrue(os.path.isfile(filename))
        os.remove(filename)  # Clean up after test

    def test_letter_counts(self):
        """Test if the letter counts in the JSON file are correct."""
        letters = ['a', 'b', 'c']
        n = 2
        filename = task_func(letters, n)
        
        with open(filename, 'r') as f:
            letter_counts = json.load(f)
        
        expected_counts = defaultdict(int)
        combinations = list(itertools.combinations(letters, n))
        for combination in combinations:
            for letter in combination:
                expected_counts[letter] += 1

        # Verify that the actual counts match the expected counts
        for letter in letters:
            self.assertEqual(letter_counts.get(letter, 0), expected_counts[letter])
        
        os.remove(filename)  # Clean up after test

    def test_empty_letters(self):
        """Test if calling the function with an empty list raises an error."""
        with self.assertRaises(ValueError):
            task_func([], 1)

    def test_invalid_combination_length(self):
        """Test if calling the function with a combination length larger than the letters raises an error."""
        letters = ['a', 'b']
        n = 3
        with self.assertRaises(ValueError):
            task_func(letters, n)

if __name__ == '__main__':
    unittest.main()