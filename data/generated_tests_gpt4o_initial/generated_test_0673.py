import os
import unittest

# Here is your prompt:
import os
import random

def task_func(directory, n_files):
    """
    Create n random txt files in a specific directory, write only a single digit random integer into each file, and then reset the cursor to the beginning of each file.
    The file names start from 'file_1.txt' and increment by 1 for each file.
    
    Parameters:
    - directory (str): The directory in which to generate the files.
    - n_files (int): The number of files to generate.

    Returns:
    - n_files (int): The number of files generated.

    Requirements:
    - os
    - random

    Example:
    >>> random.seed(2)
    >>> task_func('/path/to/directory', 5)
    5
    """

    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(n_files):
        filename = os.path.join(directory, f"file_{i+1}.txt")

        with open(filename, 'w') as file:
            file.write(str(random.randint(0, 9)))
            file.seek(0)

    return n_files

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.test_directory = "test_dir"
        if not os.path.exists(self.test_directory):
            os.makedirs(self.test_directory)

    def tearDown(self):
        for filename in os.listdir(self.test_directory):
            file_path = os.path.join(self.test_directory, filename)
            os.remove(file_path)
        os.rmdir(self.test_directory)

    def test_create_zero_files(self):
        result = task_func(self.test_directory, 0)
        self.assertEqual(result, 0)
        self.assertEqual(len(os.listdir(self.test_directory)), 0)

    def test_create_five_files(self):
        result = task_func(self.test_directory, 5)
        self.assertEqual(result, 5)
        self.assertEqual(len(os.listdir(self.test_directory)), 5)

    def test_file_contents(self):
        task_func(self.test_directory, 3)
        for i in range(3):
            with open(os.path.join(self.test_directory, f"file_{i+1}.txt")) as f:
                content = f.read()
                self.assertTrue(content.isdigit())
                self.assertGreaterEqual(int(content), 0)
                self.assertLessEqual(int(content), 9)

    def test_file_naming(self):
        task_func(self.test_directory, 2)
        expected_files = {f"file_{i+1}.txt" for i in range(2)}
        actual_files = set(os.listdir(self.test_directory))
        self.assertEqual(expected_files, actual_files)

    def test_directory_creation(self):
        task_func("new_test_dir", 3)
        self.assertTrue(os.path.exists("new_test_dir"))
        
        # Cleanup the created directory
        for filename in os.listdir("new_test_dir"):
            os.remove(os.path.join("new_test_dir", filename))
        os.rmdir("new_test_dir")

if __name__ == '__main__':
    unittest.main()