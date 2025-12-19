import unittest
import os
import sys
from configparser import ConfigParser

# Provided Prompt
import sys
from configparser import ConfigParser

# Constants
PATH_TO_APPEND = '/path/to/whatever'
CONFIG_FILE = '/path/to/config.ini'

def task_func(path_to_append=PATH_TO_APPEND, config_file=CONFIG_FILE):
    """
    Add a specific path to sys.path and update a configuration file with this path.

    Parameters:
    - path_to_append (str): The path to append to sys.path. Default is '/path/to/whatever'.
    - config_file (str): The path to the config file to update. Default is '/path/to/config.ini'.

    Returns:
    - config (object): The object contains the updated configuration.
    - config_file (str): The path to the configuration file that was just modified.

    Requirements:
    - sys
    - configparser.ConfigParser

    Example:
    >>> config = task_func('/path/to/new_directory', '/path/to/new_config.ini')
    >>> 'path_to_append' in config['DEFAULT']
    True
    """

    if isinstance(path_to_append, list):
        for path in path_to_append:
            sys.path.append(path)
    else:
        sys.path.append(path_to_append)

    config = ConfigParser()

    # Create the file if it doesn't exist
    if not os.path.exists(config_file):
        open(config_file, 'a').close()

    config.read(config_file)
    path_str = ','.join(path_to_append) if isinstance(path_to_append, list) else path_to_append
    config.set('DEFAULT', 'path_to_append', path_str)

    with open(config_file, 'w') as file:
        config.write(file)

    return config, config_file

# Test Suite
class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.config_file = 'test_config.ini'
        self.path_to_append = '/path/to/test_directory'
    
    def tearDown(self):
        if os.path.exists(self.config_file):
            os.remove(self.config_file)
        if self.path_to_append in sys.path:
            sys.path.remove(self.path_to_append)

    def test_single_path_append(self):
        config, config_file = task_func(self.path_to_append, self.config_file)
        self.assertIn(self.path_to_append, sys.path)
        self.assertTrue(os.path.exists(config_file))
        self.assertEqual(config.get('DEFAULT', 'path_to_append'), self.path_to_append)

    def test_multiple_path_append(self):
        paths_to_append = ['/path/to/one', '/path/to/two']
        config, config_file = task_func(paths_to_append, self.config_file)
        for path in paths_to_append:
            self.assertIn(path, sys.path)
        self.assertTrue(os.path.exists(config_file))
        self.assertEqual(config.get('DEFAULT', 'path_to_append'), ','.join(paths_to_append))

    def test_non_existent_config_file(self):
        config, config_file = task_func(self.path_to_append, self.config_file)
        self.assertTrue(os.path.exists(config_file))
        self.assertEqual(config.get('DEFAULT', 'path_to_append'), self.path_to_append)

    def test_no_append_on_empty_string(self):
        config, config_file = task_func('', self.config_file)
        self.assertNotIn('', sys.path)
        self.assertTrue(os.path.exists(config_file))
        self.assertEqual(config.get('DEFAULT', 'path_to_append'), '')

    def test_path_not_in_sys_path_after_tear_down(self):
        task_func(self.path_to_append, self.config_file)
        self.assertIn(self.path_to_append, sys.path)
        self.tearDown()
        self.assertNotIn(self.path_to_append, sys.path)

# Execute the test suite
if __name__ == '__main__':
    unittest.main()