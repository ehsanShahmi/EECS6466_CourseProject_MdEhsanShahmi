import os
import re
import unittest

def task_func(directory):
    """
    Finds all files in the specified directory whose names contain any type of 
    bracket (round, curly, or square).

    Uses an internal constant BRACKET_PATTERN = '[(){}\\[\\]]', which specifies
    the brackets that are looked for.

    
    Parameters:
    directory (str): The directory path to search in.
    
    Returns:
    list[str]: A list of file paths that contain brackets in their names.
    
    Requirements:
    - re
    - os
    
    Example:
    >>> task_func('./some_directory/')
    ['./some_directory/file(1).txt', './some_directory/folder/file[2].jpg']
    
    >>> task_func('./another_directory/')
    ['./another_directory/file{3}.png']
    """

    BRACKET_PATTERN = '[(){}\\[\\]]'  # Corrected pattern to match any type of bracket
    
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if re.search(BRACKET_PATTERN, file):
                file_list.append(os.path.join(root, file))
    return file_list

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Set up a temporary directory structure for testing
        self.test_dir = './test_directory'
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Create test files
        with open(os.path.join(self.test_dir, 'file(1).txt'), 'w') as f:
            f.write("Sample text.")
        with open(os.path.join(self.test_dir, 'file[2].jpg'), 'w') as f:
            f.write("Sample image.")
        with open(os.path.join(self.test_dir, 'file{3}.png'), 'w') as f:
            f.write("Sample image.")
        with open(os.path.join(self.test_dir, 'file.txt'), 'w') as f:
            f.write("Sample text without brackets.")

    def tearDown(self):
        # Remove the temporary test directory after each test
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        os.rmdir(self.test_dir)

    def test_find_files_with_round_brackets(self):
        expected = [os.path.join(self.test_dir, 'file(1).txt')]
        result = task_func(self.test_dir)
        self.assertIn(expected[0], result)

    def test_find_files_with_square_brackets(self):
        expected = [os.path.join(self.test_dir, 'file[2].jpg')]
        result = task_func(self.test_dir)
        self.assertIn(expected[0], result)

    def test_find_files_with_curly_brackets(self):
        expected = [os.path.join(self.test_dir, 'file{3}.png')]
        result = task_func(self.test_dir)
        self.assertIn(expected[0], result)

    def test_no_files_found_no_brackets(self):
        # Create an empty file
        with open(os.path.join(self.test_dir, 'file.txt'), 'w') as f:
            f.write("Sample text without brackets.")
        result = task_func(self.test_dir)
        self.assertNotIn(os.path.join(self.test_dir, 'file.txt'), result)

    def test_multiple_file_types(self):
        # Check that all files with brackets are found in a mixed environment
        expected_files = [
            os.path.join(self.test_dir, 'file(1).txt'),
            os.path.join(self.test_dir, 'file[2].jpg'),
            os.path.join(self.test_dir, 'file{3}.png')
        ]
        result = task_func(self.test_dir)
        for expected in expected_files:
            self.assertIn(expected, result)

if __name__ == "__main__":
    unittest.main()