import os
import unittest
import random
import shutil

# Here is your prompt:
# 
# import os
# import random
# 
# def task_func(directory, n_files):
#     """
#     Create n random text files in a specific directory, write a random string to each file, and then reset the cursor to the beginning of each file.
# 
#     Parameters:
#     - directory (str): The directory in which to generate the files.
#     - n_files (int): The number of files to generate.
# 
#     Returns:
#     - directory (str): The directory in which the files were generated.
# 
#     Requirements:
#     - os
#     - random
# 
#     Example:
#     >>> task_func('/path/to/directory', 5)
#     '/path/to/directory'
#     """
# 
#                if not os.path.exists(directory):
#         os.makedirs(directory)
# 
#     for i in range(n_files):
#         filename = os.path.join(directory, f"file_{i+1}.txt")
# 
#         with open(filename, 'w') as file:
#             file.write(str(random.randint(1, 100)))
#             file.seek(0)
# 
#     return directory

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create a temporary directory for testing."""
        self.test_dir = 'test_directory'
        if not os.path.exists(self.test_dir):
            os.makedirs(self.test_dir)

    def tearDown(self):
        """Remove the temporary directory after testing."""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_create_zero_files(self):
        """Test that no files are created when n_files is 0."""
        result = task_func(self.test_dir, 0)
        self.assertEqual(result, self.test_dir)
        self.assertEqual(len(os.listdir(self.test_dir)), 0)

    def test_create_single_file(self):
        """Test that one file is created and written to."""
        result = task_func(self.test_dir, 1)
        self.assertEqual(result, self.test_dir)
        self.assertEqual(len(os.listdir(self.test_dir)), 1)

        with open(os.path.join(self.test_dir, 'file_1.txt')) as f:
            content = f.read()
            self.assertTrue(content.isdigit())  # Check if it's a number

    def test_create_multiple_files(self):
        """Test that multiple files are created."""
        n_files = 5
        result = task_func(self.test_dir, n_files)
        self.assertEqual(result, self.test_dir)
        self.assertEqual(len(os.listdir(self.test_dir)), n_files)

        for i in range(1, n_files + 1):
            with open(os.path.join(self.test_dir, f'file_{i}.txt')) as f:
                content = f.read()
                self.assertTrue(content.isdigit())  # Check if it's a number

    def test_directory_creation(self):
        """Test that the specified directory is created if it does not exist."""
        new_dir = 'new_test_directory'
        task_func(new_dir, 3)
        self.assertTrue(os.path.exists(new_dir))
        shutil.rmtree(new_dir)  # Clean up

    def test_non_existent_directory(self):
        """Test specifying a non-existent directory."""
        non_existent_dir = 'non_existent_directory/test'
        task_func(non_existent_dir, 2)
        self.assertTrue(os.path.exists(non_existent_dir))
        self.assertEqual(len(os.listdir(non_existent_dir)), 2)
        shutil.rmtree(non_existent_dir)  # Clean up


if __name__ == '__main__':
    unittest.main()