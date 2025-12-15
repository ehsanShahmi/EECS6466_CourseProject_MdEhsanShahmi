import unittest
import os
import glob
import subprocess

# Constants
ARCHIVE_DIR = '/tmp/archive'

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        if not os.path.exists(ARCHIVE_DIR):
            os.makedirs(ARCHIVE_DIR)

    def tearDown(self):
        # Clean up the ARCHIVE_DIR and any created files
        for file in glob.glob(os.path.join(ARCHIVE_DIR, '*')):
            os.remove(file)
        os.rmdir(ARCHIVE_DIR)

    def test_task_func_no_files(self):
        """Test when no files match the pattern."""
        result = task_func('*.txt')
        self.assertEqual(result, "No files found matching the pattern.")

    def test_task_func_single_file(self):
        """Test archiving a single file."""
        test_file = '/tmp/test_file.txt'
        with open(test_file, 'w') as f:
            f.write("This is a test file.")
        
        result = task_func('/tmp/test_file.txt')
        self.assertTrue(os.path.exists(result))
        self.assertFalse(os.path.exists(test_file))

    def test_task_func_multiple_files(self):
        """Test archiving multiple files."""
        test_files = ['/tmp/test_file1.txt', '/tmp/test_file2.txt']
        for file in test_files:
            with open(file, 'w') as f:
                f.write("This is a test file.")

        result = task_func('/tmp/test_file*.txt')
        self.assertTrue(os.path.exists(result))
        for file in test_files:
            self.assertFalse(os.path.exists(file))

    def test_task_func_archive_name(self):
        """Test that multiple calls create unique archive names."""
        test_file = '/tmp/test_file.txt'
        with open(test_file, 'w') as f:
            f.write("This is a test file.")
        
        archive_name1 = task_func('/tmp/test_file.txt')
        self.assertTrue(os.path.exists(archive_name1))
        
        # Call again with no files to ensure same name doesn't overwrite
        archive_name2 = task_func('/tmp/test_file.txt')
        self.assertEqual(archive_name2, "No files found matching the pattern.")
        
        # Check that the archive file name is unique
        self.assertNotEqual(archive_name1, archive_name2)

    def test_task_func_archive_directory_creation(self):
        """Test that the archive directory is created if it doesn't exist."""
        os.rmdir(ARCHIVE_DIR)  # Remove directory for the test
        self.assertFalse(os.path.exists(ARCHIVE_DIR))
        
        result = task_func('*.txt')
        self.assertTrue(os.path.exists(ARCHIVE_DIR))
        self.assertEqual(result, "No files found matching the pattern.")

if __name__ == '__main__':
    unittest.main()