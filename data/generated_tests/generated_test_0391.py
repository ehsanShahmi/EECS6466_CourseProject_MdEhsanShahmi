import os
import glob
import shutil
import unittest
import tempfile

# Here is your prompt:
# import os
# import glob
# import shutil

def task_func(directory, archive_dir='archive'):
    """
    Archive all JSON files in a given directory by moving them to a specified archive directory.

    Parameters:
    directory (str): The directory where the JSON files are located.
    archive_dir (str): The directory to which the JSON files will be archived. Defaults to 'archive'.

    Returns:
    tuple: A tuple containing a boolean value and a list of error messages.
           The boolean is True if all files are successfully moved, and False otherwise.
           The list contains error messages for each file that failed to move.

    Requirements:
    - os
    - glob
    - shutil

    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.mkdtemp()
    >>> files = ['file1.json', 'file2.json', 'file3.json']
    >>> for file in files:
    ...     with open(os.path.join(temp_dir, file), 'w') as f:
    ...         _ = f.write("Dummy content for testing.")
    >>> backup_dir = tempfile.mkdtemp()
    >>> task_func(temp_dir, backup_dir)
    (True, [])
    """

    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)

    json_files = glob.glob(os.path.join(directory, '*.json'))
    error_messages = []

    for json_file in json_files:
        try:
            shutil.move(json_file, archive_dir)
        except Exception as e:
            error_message = f'Unable to move {json_file} due to {str(e)}'
            error_messages.append(error_message)

    return (len(error_messages) == 0, error_messages)

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up a temporary directory for testing."""
        self.test_dir = tempfile.mkdtemp()
        self.archive_dir = os.path.join(tempfile.mkdtemp(), 'archive')

    def tearDown(self):
        """Clean up temporary directories after testing."""
        shutil.rmtree(self.test_dir)
        shutil.rmtree(os.path.dirname(self.archive_dir))

    def test_no_json_files(self):
        """Test with no JSON files in the directory."""
        success, errors = task_func(self.test_dir, self.archive_dir)
        self.assertTrue(success)
        self.assertEqual(errors, [])

    def test_move_single_json_file(self):
        """Test moving a single JSON file."""
        with open(os.path.join(self.test_dir, 'single.json'), 'w') as f:
            f.write('{"key": "value"}')
        success, errors = task_func(self.test_dir, self.archive_dir)
        self.assertTrue(success)
        self.assertEqual(errors, [])
        self.assertTrue(os.path.exists(os.path.join(self.archive_dir, 'single.json')))

    def test_move_multiple_json_files(self):
        """Test moving multiple JSON files."""
        for i in range(3):
            with open(os.path.join(self.test_dir, f'file{i}.json'), 'w') as f:
                f.write('{"key": "value"}')
        success, errors = task_func(self.test_dir, self.archive_dir)
        self.assertTrue(success)
        self.assertEqual(errors, [])
        self.assertEqual(len(os.listdir(self.archive_dir)), 3)

    def test_move_with_error(self):
        """Test with a filename that causes an error moving (read-only file)."""
        error_file_path = os.path.join(self.test_dir, 'error.json')
        with open(error_file_path, 'w') as f:
            f.write('{"key": "value"}')
        os.chmod(error_file_path, 0o444)  # Make it read-only

        success, errors = task_func(self.test_dir, self.archive_dir)
        self.assertFalse(success)
        self.assertGreater(len(errors), 0)  # Expect an error message
        self.assertIn('Unable to move', errors[0])  # Check for the error message

if __name__ == '__main__':
    unittest.main()