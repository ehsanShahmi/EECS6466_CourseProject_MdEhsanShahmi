import os
import shutil
import string
import unittest

# Constants
INVALID_CHARACTERS = string.punctuation + string.whitespace

def create_test_directory_structure():
    os.makedirs('test_dir/txt', exist_ok=True)
    os.makedirs('test_dir/jpg', exist_ok=True)
    os.makedirs('test_dir/Invalid', exist_ok=True)
    with open('test_dir/file1.txt', 'w') as f:
        f.write('Hello World')
    with open('test_dir/file2.jpg', 'w') as f:
        f.write('Hello World')
    with open('test_dir/invalid file.txt', 'w') as f:
        f.write('Invalid Filename')
    with open('test_dir/file3.txt', 'w') as f:
        f.write('Another valid file')
    with open('test_dir/another_invalid!.jpg', 'w') as f:
        f.write('Another Invalid Filename')

class TestTaskFunc(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create test directory structure before all tests
        create_test_directory_structure()

    @classmethod
    def tearDownClass(cls):
        # Clean up test directory after all tests
        shutil.rmtree('test_dir')

    def test_organize_files_valid(self):
        summary = task_func('test_dir')
        self.assertEqual(summary['txt'], 3)
        self.assertEqual(summary['jpg'], 1)
        self.assertIn('Invalid', summary)
        self.assertEqual(summary['Invalid'], 2)

    def test_invalid_directory_created(self):
        summary = task_func('test_dir')
        self.assertTrue(os.path.exists(os.path.join('test_dir', 'Invalid')))

    def test_extension_directories_created(self):
        summary = task_func('test_dir')
        self.assertTrue(os.path.exists(os.path.join('test_dir', 'txt')))
        self.assertTrue(os.path.exists(os.path.join('test_dir', 'jpg')))

    def test_files_moved_correctly(self):
        task_func('test_dir')
        self.assertFalse(os.path.exists(os.path.join('test_dir', 'invalid file.txt')))
        self.assertFalse(os.path.exists(os.path.join('test_dir', 'another_invalid!.jpg')))
        self.assertTrue(os.path.exists(os.path.join('test_dir', 'Invalid', 'invalid file.txt')))
        self.assertTrue(os.path.exists(os.path.join('test_dir', 'Invalid', 'another_invalid!.jpg')))

    def test_summary_content(self):
        summary = task_func('test_dir')
        self.assertEqual(summary, {'txt': 3, 'jpg': 1, 'Invalid': 2})

# This will allow the test suite to run
if __name__ == '__main__':
    unittest.main()