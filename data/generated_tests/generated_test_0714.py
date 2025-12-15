import sys
import os
from pathlib import Path
import unittest

# Constants
PATH_TO_APPEND = '/path/to/whatever'

def task_func(path_to_append=PATH_TO_APPEND):
    """
    Add a specific path to sys.path and create a directory in that path if it does not exist.

    Note:
    - The function uses a constant PATH_TO_APPEND which defaults to '/path/to/whatever'.

    Parameters:
    - path_to_append (str): The path to append to sys.path and to create a directory. Default is '/path/to/whatever'.

    Returns:
    - path_to_append (str): The path that was appended and where the directory was created.

    Requirements:
    - sys
    - pathlib

    Examples:
    >>> task_func("/new/path/to/append")
    "/new/path/to/append"

    >>> task_func()
    "/path/to/whatever"
    """

    # Creating the directory if it does not exist
    Path(path_to_append).mkdir(parents=True, exist_ok=True)
    
    # Adding the directory to sys.path
    sys.path.append(path_to_append)
    
    return path_to_append

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.default_path = PATH_TO_APPEND
        self.custom_path = '/new/path/to/append'
        self.nonexistent_path = '/non/existent/path'

    def test_default_path(self):
        """Test the default path functionality."""
        result = task_func()
        self.assertEqual(result, self.default_path)
        self.assertTrue(Path(self.default_path).exists())
        self.assertIn(self.default_path, sys.path)

    def test_custom_path(self):
        """Test the custom path functionality."""
        result = task_func(self.custom_path)
        self.assertEqual(result, self.custom_path)
        self.assertTrue(Path(self.custom_path).exists())
        self.assertIn(self.custom_path, sys.path)

    def test_nonexistent_path(self):
        """Test the creation of a non-existent path."""
        result = task_func(self.nonexistent_path)
        self.assertEqual(result, self.nonexistent_path)
        self.assertTrue(Path(self.nonexistent_path).exists())
        self.assertIn(self.nonexistent_path, sys.path)

    def test_path_does_not_exist_initially(self):
        """Check that a directory is created when it didn't exist before."""
        temp_path = '/temp/test/path'
        if Path(temp_path).exists():
            os.rmdir(temp_path)  # Clean up if the path already exists

        self.assertFalse(Path(temp_path).exists())
        task_func(temp_path)
        self.assertTrue(Path(temp_path).exists())

    def test_duplicate_append(self):
        """Test appending the same path multiple times does not create duplicates."""
        task_func(self.custom_path)
        initial_sys_path_length = len(sys.path)
        task_func(self.custom_path)
        self.assertEqual(initial_sys_path_length, len(sys.path))

# Run the test suite
if __name__ == '__main__':
    unittest.main()