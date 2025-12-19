import ast
import os
import glob
import unittest

# Constants
DIRECTORY = 'data'

def task_func(directory):
    """
    Convert all Unicode string representations of dictionaries in all text files 
    in the specified directory to Python dictionaries.

    Parameters:
    directory (str): The path to the directory containing the text files.

    Returns:
    list: A list of dictionaries extracted from the text files.

    Requirements:
    - ast
    - os
    - glob

    Example:
    >>> task_func("sample_directory/")
    [{'key1': 'value1'}, {'key2': 'value2'}]

    Note:
    Ensure that the text files in the directory contain valid Unicode string representations of dictionaries.

    Raises:
    - The function would raise a ValueError if there are text file(s) that have invalid dictionary representation
    """

    path = os.path.join(directory, '*.txt')
    files = glob.glob(path)

    results = []
    for file in files:
        with open(file, 'r') as f:
            for line in f:
                results.append(ast.literal_eval(line.strip()))

    return results

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up a temporary directory with sample text files for testing."""
        os.makedirs(DIRECTORY, exist_ok=True)
        with open(os.path.join(DIRECTORY, 'test1.txt'), 'w') as f:
            f.write("{'key1': 'value1'}\n")
            f.write("{'key2': 'value2'}\n")
        with open(os.path.join(DIRECTORY, 'test2.txt'), 'w') as f:
            f.write("{'key3': 'value3'}\n")

    def tearDown(self):
        """Clean up the temporary directory after tests."""
        for file in glob.glob(os.path.join(DIRECTORY, '*')):
            os.remove(file)
        os.rmdir(DIRECTORY)

    def test_multiple_files(self):
        """Test that dictionaries from multiple files are combined correctly."""
        expected = [{'key1': 'value1'}, {'key2': 'value2'}, {'key3': 'value3'}]
        result = task_func(DIRECTORY)
        self.assertEqual(result, expected)

    def test_empty_file(self):
        """Test handling of an empty file."""
        with open(os.path.join(DIRECTORY, 'empty.txt'), 'w') as f:
            pass  # Create an empty file
        expected = [{'key1': 'value1'}, {'key2': 'value2'}, {'key3': 'value3'}]
        result = task_func(DIRECTORY)
        self.assertEqual(result, expected)

    def test_invalid_dictionary(self):
        """Test that a ValueError is raised for an invalid dictionary."""
        with open(os.path.join(DIRECTORY, 'invalid.txt'), 'w') as f:
            f.write("{'key1': 'value1'\n")  # Missing closing brace
        with self.assertRaises(ValueError):
            task_func(DIRECTORY)

    def test_no_text_files(self):
        """Test that it handles the case of no text files gracefully."""
        os.rmdir(DIRECTORY)  # Remove the directory to simulate no files
        os.makedirs(DIRECTORY)
        result = task_func(DIRECTORY)
        self.assertEqual(result, [])

    def test_single_valid_line(self):
        """Test that a single valid line returns the correct dictionary."""
        with open(os.path.join(DIRECTORY, 'single.txt'), 'w') as f:
            f.write("{'key5': 'value5'}\n")
        expected = [{'key5': 'value5'}]
        result = task_func(DIRECTORY)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()