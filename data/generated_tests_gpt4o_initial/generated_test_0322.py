import unittest
import os
import shutil
import subprocess
import sys

# Constants
DIRECTORY = 'c:\\Program Files\\VMware\\VMware Server'
BACKUP_DIRECTORY = 'c:\\Program Files\\VMware\\VMware Server\\Backup'

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        # Create directories for testing purposes
        os.makedirs(DIRECTORY, exist_ok=True)
        os.makedirs(BACKUP_DIRECTORY, exist_ok=True)
        # Create a sample file to back up
        self.test_filename = 'vmware-cmd.bat'
        self.test_file_path = os.path.join(DIRECTORY, self.test_filename)
        with open(self.test_file_path, 'w') as f:
            f.write('echo Hello World')

    def tearDown(self):
        # Clean up created directories and files
        try:
            os.remove(self.test_file_path)
        except FileNotFoundError:
            pass
        try:
            backup_file_path = os.path.join(BACKUP_DIRECTORY, self.test_filename)
            os.remove(backup_file_path)
        except FileNotFoundError:
            pass
        shutil.rmtree(BACKUP_DIRECTORY, ignore_errors=True)
        shutil.rmtree(DIRECTORY, ignore_errors=True)

    def test_backup_and_execute_success(self):
        # Test backing up and executing an existing file
        result = task_func(self.test_filename)
        backup_exists = os.path.exists(os.path.join(BACKUP_DIRECTORY, self.test_filename))
        self.assertEqual(result, 0)  # Assuming the subprocess returns 0 on success
        self.assertTrue(backup_exists)

    def test_backup_failure(self):
        # Test handling of a non-existing file
        result = task_func('nonexistent.bat')
        self.assertEqual(result, -1)  # Expect -1 for backup failure

    def test_backup_directory_creation(self):
        # Ensure the backup directory is created on backup
        task_func(self.test_filename)
        self.assertTrue(os.path.exists(BACKUP_DIRECTORY))

    def test_execute_file_failure(self):
        # Test the execution failure case
        # Remove access to the test file to simulate a failure
        os.chmod(self.test_file_path, 0o000)
        result = task_func(self.test_filename)
        self.assertEqual(result, -1)  # Expect -1 for execution failure
        os.chmod(self.test_file_path, 0o644)  # Restore access

if __name__ == '__main__':
    unittest.main()