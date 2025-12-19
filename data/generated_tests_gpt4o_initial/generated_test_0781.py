import os
import unittest
from datetime import datetime

# Here is your prompt:
import os
from datetime import datetime

def task_func(filepath: str) -> dict:
    """
    Determine the size and date of the last modification of a file.

    Parameters:
    - filepath (str): The path to the file.

    Returns:
    - dict: A dictionary containing the size (in bytes) and last modification 
          date of the file in the format '%Y-%m-%d %H:%M:%S'.

    Requirements:
    - os
    - datetime

    Example:
    >>> task_func('/path/to/file.txt')
    {'size': '1024 bytes', 'last_modified': '2022-01-01 12:30:45'}
    """

    try:
        size = os.path.getsize(filepath)
        mtime = os.path.getmtime(filepath)
        mtime = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
    except OSError as e:
        raise Exception(f"Error: {e}")

    return {'size': f"{size} bytes", 'last_modified': mtime}

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary file for testing
        self.test_file = 'test_file.txt'
        with open(self.test_file, 'w') as f:
            f.write('This is a test file.')

    def tearDown(self):
        # Remove the test file after tests are done
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_file_size(self):
        result = task_func(self.test_file)
        self.assertEqual(result['size'], '27 bytes')  # Size of the test file content

    def test_last_modified_format(self):
        result = task_func(self.test_file)
        # Check if the last modified time is correctly formatted
        self.assertIsNotNone(datetime.strptime(result['last_modified'], '%Y-%m-%d %H:%M:%S'))

    def test_non_existent_file(self):
        with self.assertRaises(Exception):
            task_func('non_existent_file.txt')

    def test_empty_file(self):
        empty_file = 'empty_file.txt'
        with open(empty_file, 'w'):
            pass  # Create an empty file
        result = task_func(empty_file)
        self.assertEqual(result['size'], '0 bytes')  # Size of an empty file
        os.remove(empty_file)

    def test_file_modification_time(self):
        temp_file = 'temp_file.txt'
        with open(temp_file, 'w') as f:
            f.write('Temporary file.')
        result = task_func(temp_file)
        # Here, we check that the modification time is close to the current time
        current_time = datetime.now()
        last_modified_time = datetime.strptime(result['last_modified'], '%Y-%m-%d %H:%M:%S')
        self.assertLessEqual((current_time - last_modified_time).total_seconds(), 1)
        os.remove(temp_file)

if __name__ == '__main__':
    unittest.main()