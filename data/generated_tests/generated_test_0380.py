import os
import shutil
import tempfile
import unittest
import re

def task_func(directory):
    """
    Arrange files in a directory by their extensions. Create a new directory for each extension and move the 
    files to the corresponding directories.

    Parameters:
    directory (str): The path to the directory.

    Returns:
    None
    """
    for filename in os.listdir(directory):
        match = re.search(r'\.(.*?)$', filename)
        if match:
            ext_dir = os.path.join(directory, match.group(1))
            if not os.path.exists(ext_dir):
                os.mkdir(ext_dir)
            shutil.move(os.path.join(directory, filename), ext_dir)

class TestTaskFunction(unittest.TestCase):

    def setUp(self):
        """Create a temporary directory and some test files before each test."""
        self.test_dir = tempfile.mkdtemp()
        self.file_names = ['file1.txt', 'file2.txt', 'file3.jpg', 'file4.png']
        for file_name in self.file_names:
            with open(os.path.join(self.test_dir, file_name), 'w') as f:
                f.write('This is a test file.')

    def tearDown(self):
        """Remove the temporary directory after each test."""
        shutil.rmtree(self.test_dir)

    def test_file_extension_directories_created(self):
        """Test that the function creates directories for each file extension."""
        task_func(self.test_dir)
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'txt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'jpg')))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'png')))
    
    def test_files_are_moved(self):
        """Test that files are moved to the respective extension directories."""
        task_func(self.test_dir)
        for file_name in self.file_names:
            ext = file_name.split('.')[-1]
            self.assertNotIn(file_name, os.listdir(self.test_dir))
            self.assertIn(file_name, os.listdir(os.path.join(self.test_dir, ext)))

    def test_multiple_files_same_extension(self):
        """Test that multiple files with the same extension are handled correctly."""
        with open(os.path.join(self.test_dir, 'file5.txt'), 'w') as f:
            f.write('Another text file.')
        task_func(self.test_dir)
        self.assertEqual(len(os.listdir(os.path.join(self.test_dir, 'txt'))), 3)
    
    def test_no_files(self):
        """Test the behavior when the directory is empty."""
        empty_test_dir = tempfile.mkdtemp()
        task_func(empty_test_dir)
        self.assertEqual(os.listdir(empty_test_dir), [])  # No files should be present
        shutil.rmtree(empty_test_dir)

if __name__ == '__main__':
    unittest.main()