import os
import shutil
import unittest

# Constants
BACKUP_DIR = '/tmp/backup'

def get_unique_backup_dir():
    return "/fake/backup/path"

def task_func(directory):
    """
    Create a backup of a directory and clean the directory afterwards.
    
    Parameters:
    - directory (str): The directory path to be backed up and cleaned.
    
    Returns:
    tuple: A tuple containing:
        - str: The backup directory path.
        - list: A list of any errors encountered during the operation (empty list if no errors).
    """
    errors = []
    if not os.path.exists(directory):
        errors.append(f"Directory does not exist: {directory}")
        return None, errors

    try:
        if not os.path.exists(BACKUP_DIR):
            os.makedirs(BACKUP_DIR)

        backup_dir = get_unique_backup_dir()
        os.makedirs(backup_dir)
        shutil.copytree(directory, os.path.join(backup_dir, os.path.basename(directory)))
        shutil.rmtree(directory)  # Deleting contents after backup
        os.makedirs(directory)  # Recreating the original directory
    except Exception as e:
        errors.append(str(e))

    return backup_dir, errors

class TestBackupFunctionality(unittest.TestCase):

    def setUp(self):
        self.test_dir = '/tmp/test_dir'
        os.makedirs(self.test_dir, exist_ok=True)
        with open(os.path.join(self.test_dir, 'test_file.txt'), 'w') as f:
            f.write('This is a test file.')

    def tearDown(self):
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)
        if os.path.exists(BACKUP_DIR):
            shutil.rmtree(BACKUP_DIR)

    def test_successful_backup(self):
        backup_path, errors = task_func(self.test_dir)
        self.assertEqual(errors, [])
        self.assertTrue(os.path.exists(backup_path))

    def test_non_existent_directory(self):
        backup_path, errors = task_func('/tmp/non_existent_dir')
        self.assertIsNone(backup_path)
        self.assertIn("Directory does not exist: /tmp/non_existent_dir", errors)

    def test_backup_creates_backup_dir(self):
        task_func(self.test_dir)
        self.assertTrue(os.path.exists(BACKUP_DIR))
        self.assertTrue(len(os.listdir(BACKUP_DIR)) > 0)

    def test_cleanup_on_permission_error(self):
        # Simulate a permission error by marking the directory as read-only
        os.chmod(self.test_dir, 0o400)
        backup_path, errors = task_func(self.test_dir)
        self.assertIn("Permission denied:", errors)
        self.assertFalse(os.path.exists(backup_path))  # Backup should not succeed

    def test_returned_backup_path(self):
        backup_path, errors = task_func(self.test_dir)
        self.assertEqual(backup_path, "/fake/backup/path")


if __name__ == '__main__':
    unittest.main()