import os
import json
import unittest

# Here is your prompt:
import os
import json

def task_func(config_path: str) -> dict:
    """
    Load a JSON configuration file and return the configuration dictionary.
    
    Parameters:
    - config_path (str): Path to the configuration file.
    
    Returns:
    - config (dict): Configuration dictionary loaded from the file.
    
    Requirements:
    - os
    - json
    
    Raises:
    - FileNotFoundError: If the provided configuration file does not exist.
    
    Example:
    >>> task_func("config.json")
    {'key': 'value', 'setting': True}
    """

    if not os.path.isfile(config_path):
        raise FileNotFoundError(f"The configuration file {config_path} does not exist.")

    with open(config_path) as f:
        config = json.load(f)
    
    return config

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        """Create a temporary file for testing."""
        self.test_file = 'test_config.json'
        with open(self.test_file, 'w') as f:
            json.dump({'key': 'value', 'setting': True}, f)
    
    def tearDown(self):
        """Remove the temporary file after each test."""
        if os.path.isfile(self.test_file):
            os.remove(self.test_file)

    def test_load_valid_config(self):
        """Test loading a valid JSON configuration file."""
        expected = {'key': 'value', 'setting': True}
        result = task_func(self.test_file)
        self.assertEqual(result, expected)

    def test_file_not_found(self):
        """Test that FileNotFoundError is raised for a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_file.json')

    def test_load_empty_json(self):
        """Test loading an empty JSON file."""
        empty_file = 'empty_config.json'
        with open(empty_file, 'w') as f:
            f.write('{}')
        
        expected = {}
        result = task_func(empty_file)
        self.assertEqual(result, expected)
        
        os.remove(empty_file)

    def test_load_invalid_json(self):
        """Test that JSONDecodeError is raised for an invalid JSON file."""
        invalid_file = 'invalid_config.json'
        with open(invalid_file, 'w') as f:
            f.write('{key: value}')  # Invalid JSON format
        
        with self.assertRaises(json.JSONDecodeError):
            task_func(invalid_file)
        
        os.remove(invalid_file)

    def test_load_config_with_additional_keys(self):
        """Test loading a configuration file with additional keys."""
        extra_file = 'extra_config.json'
        with open(extra_file, 'w') as f:
            json.dump({'key': 'value', 'setting': True, 'extra_key': 'extra_value'}, f)
        
        expected = {'key': 'value', 'setting': True, 'extra_key': 'extra_value'}
        result = task_func(extra_file)
        self.assertEqual(result, expected)
        
        os.remove(extra_file)

if __name__ == '__main__':
    unittest.main()