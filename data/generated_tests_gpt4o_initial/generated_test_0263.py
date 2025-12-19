import os
import glob
import shutil
import time
import unittest

# Constants for the test suite
TEST_DIRECTORY = 'test_directory'
ARCHIVE_DIRECTORY = os.path.join(TEST_DIRECTORY, 'archive')

class TestTaskFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Create a test directory and some test files
        os.makedirs(TEST_DIRECTORY, exist_ok=True)
        cls.file_names = [
            'old_file.txt', 
            'new_file.txt', 
            'old_file.csv', 
            'old_file.docx', 
            'recent_file.xlsx'
        ]
        cls.old_time = time.time() - (31 * 86400)  # 31 days old
        cls.new_time = time.time()  # current time

        # Create old test files
        for file_name in cls.file_names[:3]: # First three files as old
            with open(os.path.join(TEST_DIRECTORY, file_name), 'w') as f:
                f.write('This is a test file.')
            os.utime(os.path.join(TEST_DIRECTORY, file_name), (cls.old_time, cls.old_time))

        # Create new test files
        for file_name in cls.file_names[3:]:  # Last two files as new
            with open(os.path.join(TEST_DIRECTORY, file_name), 'w') as f:
                f.write('This is a test file.')
            os.utime(os.path.join(TEST_DIRECTORY, file_name), (cls.new_time, cls.new_time))

    @classmethod
    def tearDownClass(cls):
        # Cleanup the created files and directories
        shutil.rmtree(TEST_DIRECTORY, ignore_errors=True)

    def test_function_archives_old_files(self):
        from task_func import task_func  # Assuming task_func is in the same directory
        
        archive_path = task_func(TEST_DIRECTORY, 30)
        self.assertEqual(archive_path, ARCHIVE_DIRECTORY)
        archived_files = os.listdir(ARCHIVE_DIRECTORY)
        self.assertIn('old_file.txt', archived_files)
        self.assertIn('old_file.csv', archived_files)
        self.assertIn('old_file.docx', archived_files)
        self.assertNotIn('new_file.txt', archived_files)
        self.assertNotIn('recent_file.xlsx', archived_files)

    def test_function_does_not_move_recent_files(self):
        from task_func import task_func  # Assuming task_func is in the same directory
        
        task_func(TEST_DIRECTORY, 30)
        self.assertTrue(os.path.isfile(os.path.join(TEST_DIRECTORY, 'new_file.txt')))
        self.assertTrue(os.path.isfile(os.path.join(TEST_DIRECTORY, 'recent_file.xlsx')))

    def test_function_creates_archive_directory(self):
        from task_func import task_func  # Assuming task_func is in the same directory
        
        task_func(TEST_DIRECTORY, 30)
        self.assertTrue(os.path.exists(ARCHIVE_DIRECTORY))
        self.assertTrue(os.path.isdir(ARCHIVE_DIRECTORY))

    def test_function_returns_correct_path(self):
        from task_func import task_func  # Assuming task_func is in the same directory
        
        returned_path = task_func(TEST_DIRECTORY, 30)
        self.assertEqual(returned_path, ARCHIVE_DIRECTORY)

    def test_function_with_no_old_files(self):
        from task_func import task_func  # Assuming task_func is in the same directory
        
        # Modify the files to be all recent
        os.utime(os.path.join(TEST_DIRECTORY, 'old_file.txt'), (time.time(), time.time()))
        os.utime(os.path.join(TEST_DIRECTORY, 'old_file.csv'), (time.time(), time.time()))
        os.utime(os.path.join(TEST_DIRECTORY, 'old_file.docx'), (time.time(), time.time()))

        task_func(TEST_DIRECTORY, 30)
        archived_files = os.listdir(ARCHIVE_DIRECTORY)
        self.assertEqual(len(archived_files), 0)

if __name__ == '__main__':
    unittest.main()