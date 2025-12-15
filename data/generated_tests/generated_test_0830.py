import json
import os
import unittest

# The provided prompt and task_func is not modified
def task_func(filename, data):
    """
    Write a dictionary to a file as a JSON object and return the written content for verification.

    This function performs a write operation to store the dictionary data in JSON format
    and then reads it back to verify the content. Additionally, checks if the file exists using the os library.

    Parameters:
    - filename (str): The name of the file to be written to.
    - data (dict): The dictionary containing data to be written as JSON to the file.

    Returns:
    - tuple: A tuple containing a boolean indicating the success of the operation and the content that was written.
        - bool: indicating the success of the operation.
        - written_data (json): the content that was written.
    
    Requirements:
    - json
    - os
    """
    try:
        # Write the dictionary to the file as JSON
        with open(filename, 'w') as f:
            json.dump(data, f)
        
        # Verify the file exists after writing, using os.path.exists
        file_exists = os.path.exists(filename)
        if not file_exists:
            return False, None

        # Read the file back to verify content
        with open(filename, 'r') as f:
            written_data = json.load(f)
            if written_data != data:
                return False, None

        return True, written_data
    except Exception as e:
        return False, None

class TestTaskFunc(unittest.TestCase):
    def test_write_valid_data(self):
        filename = 'test_data_1.json'
        data = {'key': 'value'}
        result, written_data = task_func(filename, data)
        self.assertTrue(result)
        self.assertEqual(written_data, data)
        os.remove(filename)  # Clean up

    def test_write_empty_dict(self):
        filename = 'test_data_2.json'
        data = {}
        result, written_data = task_func(filename, data)
        self.assertTrue(result)
        self.assertEqual(written_data, data)
        os.remove(filename)  # Clean up

    def test_file_not_found_after_write(self):
        filename = 'test_data_3.json'
        data = {'key': 'value'}
        os.remove(filename) if os.path.exists(filename) else None  # Ensure the file does not exist
        result, written_data = task_func(filename, data)
        self.assertTrue(result)
        self.assertEqual(written_data, data)
        self.assertTrue(os.path.exists(filename))  # Check that file now exists
        os.remove(filename)  # Clean up

    def test_write_invalid_data(self):
        filename = 'test_data_4.json'
        data = None  # This is not a valid dictionary
        result, written_data = task_func(filename, data)
        self.assertFalse(result)
        self.assertIsNone(written_data)
        self.assertFalse(os.path.exists(filename))  # Ensure the file was not created

    def test_handle_exception_during_write(self):
        filename = '/invalid/path/test_data_5.json'  # Intentionally invalid path
        data = {'key': 'value'}
        result, written_data = task_func(filename, data)
        self.assertFalse(result)
        self.assertIsNone(written_data)

if __name__ == '__main__':
    unittest.main()