import unittest
import os
import random
import string
import pickle

# Here is your prompt:
def task_func(strings, filename=None):
    
    """
    Save the list of random strings "Strings" in a pickle file and then read it back for validation.
    If a filename is not provided, a unique filename is generated.

    Parameters:
    - strings (list): The list of random strings to be saved.
    - filename (str, optional): The filename for saving the pickle file. Defaults to a unique generated name.

    Returns:
    - loaded_strings (list): The loaded list of strings from the pickle file.

    Requirements:
    - pickle
    - os
    - random
    - string

    Example:
    >>> strings = [''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) for _ in range(10)]
    >>> loaded_strings = task_func(strings)
    >>> assert strings == loaded_strings
    """
  
    if filename is None:
        # Generate a unique filename using a random string
        filename = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) + ".pkl"

    with open(filename, 'wb') as file:
        pickle.dump(strings, file)
    
    with open(filename, 'rb') as file:
        loaded_strings = pickle.load(file)

    os.remove(filename)

    return loaded_strings

class TestTaskFunc(unittest.TestCase):

    def test_non_empty_strings(self):
        test_strings = ['HELLO', 'WORLD', 'TESTING']
        loaded_strings = task_func(test_strings)
        self.assertEqual(test_strings, loaded_strings)

    def test_empty_strings(self):
        test_strings = []
        loaded_strings = task_func(test_strings)
        self.assertEqual(test_strings, loaded_strings)

    def test_random_string_length(self):
        test_strings = [''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)) for _ in range(10)]
        loaded_strings = task_func(test_strings)
        self.assertEqual(len(test_strings), len(loaded_strings))

    def test_unique_filename_generation(self):
        test_strings = ['STRING1', 'STRING2']
        filename = 'unique_test.pkl'
        task_func(test_strings, filename)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

    def test_preservation_of_data_type(self):
        test_strings = ['STRING1', '123', 'A1B2C3']
        loaded_strings = task_func(test_strings)
        self.assertIsInstance(loaded_strings, list)

if __name__ == '__main__':
    unittest.main()