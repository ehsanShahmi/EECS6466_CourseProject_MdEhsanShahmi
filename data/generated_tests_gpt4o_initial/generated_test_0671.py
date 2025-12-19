import os
import random
import json
import unittest

# Here is your prompt:
def task_func(directory, n):
    """
    Create n random files in a directory with json content with the key 'number' and a random integer value between 1 and 100, and then reset the cursor to the beginning of each file.

    Parameters:
    - directory (str): The directory in which to generate the files.
    - n (int): The number of files to generate.

    Returns:
    - directory (str): The directory in which the files were generated.

    Requirements:
    - os
    - random
    - json

    Example:
    >>> task_func('/path/to/directory', 1)
    '/path/to/directory'
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(n):
        filename = str(i) + ".json"
        filepath = os.path.join(directory, filename)

        with open(filepath, 'w') as file:
            json.dump({'number': random.randint(1, 100)}, file)
            file.seek(0)

    return directory

class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        self.test_directory = 'test_dir'
        self.n = 5

    def tearDown(self):
        for i in range(self.n):
            os.remove(os.path.join(self.test_directory, f"{i}.json"))
        os.rmdir(self.test_directory)

    def test_directory_creation(self):
        result = task_func(self.test_directory, self.n)
        self.assertTrue(os.path.exists(self.test_directory))
        self.assertEqual(result, self.test_directory)

    def test_file_creation(self):
        task_func(self.test_directory, self.n)
        for i in range(self.n):
            self.assertTrue(os.path.exists(os.path.join(self.test_directory, f"{i}.json")))

    def test_json_content(self):
        task_func(self.test_directory, self.n)
        for i in range(self.n):
            with open(os.path.join(self.test_directory, f"{i}.json"), 'r') as file:
                content = json.load(file)
                self.assertIn('number', content)
                self.assertIsInstance(content['number'], int)
                self.assertGreaterEqual(content['number'], 1)
                self.assertLessEqual(content['number'], 100)

    def test_correct_number_of_files(self):
        task_func(self.test_directory, self.n)
        files = os.listdir(self.test_directory)
        self.assertEqual(len(files), self.n)

    def test_empty_directory(self):
        result = task_func(self.test_directory, 0)
        self.assertTrue(os.path.exists(self.test_directory))
        self.assertEqual(result, self.test_directory)
        self.assertEqual(len(os.listdir(self.test_directory)), 0)

if __name__ == '__main__':
    unittest.main()