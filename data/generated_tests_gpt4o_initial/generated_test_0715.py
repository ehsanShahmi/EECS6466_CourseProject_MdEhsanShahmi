import sys
import subprocess
import unittest

# Constants
PYTHON_VERSION = '3.8'
PATH_TO_APPEND = '/path/to/whatever'

def task_func(python_version=PYTHON_VERSION, path_to_append=PATH_TO_APPEND):
    """
    Switch to a specific version of Python and add a specific path to sys.path.
    
    Note: This function changes the global Python version and should be used carefully.
    
    Parameters:
    - python_version (str): The Python version to switch to. Default is '3.8'.
    - path_to_append (str): The path to append to sys.path. Default is '/path/to/whatever'.

    Returns:
    - python_version (str): The Python version that was switched to.

    Requirements:
    - sys
    - subprocess

    Example:
    >>> task_func('3.7', '/path/to/new_directory')
    '3.7'
    """

    subprocess.run(['pyenv', 'global', python_version], check=True)
    sys.path.append(path_to_append)

    return python_version

class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        """Test the function with default parameters."""
        result = task_func()
        self.assertEqual(result, PYTHON_VERSION)
        self.assertIn(PATH_TO_APPEND, sys.path)

    def test_custom_python_version(self):
        """Test the function with custom Python version."""
        custom_version = '3.7'
        result = task_func(python_version=custom_version)
        self.assertEqual(result, custom_version)

    def test_custom_path(self):
        """Test the function with custom path appended to sys.path."""
        custom_path = '/custom/path'
        task_func(path_to_append=custom_path)
        self.assertIn(custom_path, sys.path)

    def test_multiple_calls(self):
        """Test the function behavior across multiple calls."""
        task_func('3.6', '/path/one')
        self.assertEqual(task_func('3.7', '/path/two'), '3.7')
        self.assertIn('/path/one', sys.path)
        self.assertIn('/path/two', sys.path)

    def test_invalid_python_version(self):
        """Test the function with an invalid Python version."""
        with self.assertRaises(subprocess.CalledProcessError):
            task_func('invalid_version')

if __name__ == '__main__':
    unittest.main()