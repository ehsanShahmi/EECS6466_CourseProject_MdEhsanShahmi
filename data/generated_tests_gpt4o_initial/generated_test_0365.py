from collections import Counter
import json
import random
import unittest
import os

# Constants
WORDS = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

def task_func(n, file_name, seed=77):
    """
    Create a json file with a number of n randomly selected words from a constant list named WORDS.
    
    Parameters:
    n (int): The number of words to select from the list.
    file_name (str): The name of the json file to be generated.
    seed (int, Optional): The seed for the random number generator. Defaults to 77.
    
    Returns:
    str: The name of the json file generated.

    Requirements:
    - collections
    - json
    - random
    """

    random.seed(seed)
    if n < 1 or n > len(WORDS):
        raise ValueError('n must be greater than 0')
    random.shuffle(WORDS)
    selected_words = WORDS[:n]
    counts = Counter(selected_words)

    with open(file_name, 'w') as f:
        json.dump(dict(counts), f)

    return file_name


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up a temporary file for testing."""
        self.test_file_name = 'test_word_counts.json'

    def tearDown(self):
        """Remove the test file after tests."""
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)

    def test_task_func_valid_input(self):
        """Test the task_func with a valid input."""
        result = task_func(5, self.test_file_name)
        self.assertTrue(result.endswith('word_counts.json'))

    def test_task_func_output_file_exists(self):
        """Test that the output file is created."""
        task_func(3, self.test_file_name)
        self.assertTrue(os.path.isfile(self.test_file_name))

    def test_task_func_json_content(self):
        """Test the content of the generated JSON file."""
        task_func(4, self.test_file_name)
        with open(self.test_file_name) as f:
            content = json.load(f)
            self.assertEqual(len(content), 4)  # Should contain exactly 4 entries

    def test_task_func_invalid_input_zero(self):
        """Test the task_func with n=0, which should raise ValueError."""
        with self.assertRaises(ValueError):
            task_func(0, self.test_file_name)

    def test_task_func_invalid_input_greater_than_words(self):
        """Test the task_func with n greater than available words."""
        with self.assertRaises(ValueError):
            task_func(9, self.test_file_name)


if __name__ == '__main__':
    unittest.main()