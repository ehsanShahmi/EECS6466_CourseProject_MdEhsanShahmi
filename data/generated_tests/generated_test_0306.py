import os
import logging
import unittest

# Here is your prompt:
import os
import logging

def task_func(directory):
    """
    Removes all jQuery files (JavaScript files containing 'jquery' in their name) from a specified directory.

    Parameters:
    directory (str): The directory path.

    Returns:
    tuple: A tuple containing two elements:
        - int: The number of files removed.
        - list: The names of the removed files.

    Raises:
    - If the specified directory does not exist the code would raise FileNotFoundError.
    
    Note:
    - Removed files are logged in 'jquery_removal.log' file.

    Requirements:
    - os
    - logging


    Example:
    >>> task_func("/path/to/directory")
    (3, ['jquery-1.js', 'jquery-2.js', 'jquery-ui.js'])  # Assuming 3 jQuery files were removed
    """

    # Configure logging
    logging.basicConfig(filename='jquery_removal.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Check if directory exists
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")

    # Get all files in the directory
    files = os.listdir(directory)

    # Remove jQuery files
    removed_files = 0
    removed_file_names = []
    for file in files:
        if 'jquery' in file and file.endswith('.js'):
            try:
                os.remove(os.path.join(directory, file))
                removed_files += 1
                removed_file_names.append(file)
                logging.info(f"Removed jQuery file: {file}")
            except Exception as e:
                logging.error(f"Error while removing file {file}: {e}")

    return removed_files, removed_file_names

class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        self.test_dir = 'test_directory'
        os.makedirs(self.test_dir, exist_ok=True)
        # Create sample jQuery files for testing
        self.files_to_create = [
            'jquery-1.js',
            'jquery-2.js',
            'otherfile.txt',
            'jquery-ui.js',
            'nonjqueryfile.js'
        ]
        for file in self.files_to_create:
            with open(os.path.join(self.test_dir, file), 'w') as f:
                f.write("dummy content")

    def tearDown(self):
        # Clean up test directory after each test
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)

    def test_remove_jquery_files(self):
        removed_count, removed_files = task_func(self.test_dir)
        self.assertEqual(removed_count, 3)
        self.assertEqual(set(removed_files), {'jquery-1.js', 'jquery-2.js', 'jquery-ui.js'})

    def test_no_jquery_files(self):
        # Add non-jQuery files and test the removal
        with open(os.path.join(self.test_dir, 'somefile.txt'), 'w') as f:
            f.write("dummy content")
        removed_count, removed_files = task_func(self.test_dir)
        self.assertEqual(removed_count, 0)
        self.assertEqual(removed_files, [])

    def test_empty_directory(self):
        # Test the function on an empty directory
        empty_dir = 'empty_test_directory'
        os.makedirs(empty_dir, exist_ok=True)
        removed_count, removed_files = task_func(empty_dir)
        self.assertEqual(removed_count, 0)
        self.assertEqual(removed_files, [])
        os.rmdir(empty_dir)

    def test_directory_not_exist(self):
        # Test when the directory does not exist
        with self.assertRaises(FileNotFoundError):
            task_func('non_existing_directory')

if __name__ == '__main__':
    unittest.main()