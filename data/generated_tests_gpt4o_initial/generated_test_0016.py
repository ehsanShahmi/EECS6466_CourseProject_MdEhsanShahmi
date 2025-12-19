import os
import glob
import subprocess
import unittest

# Here is your prompt:
def task_func(directory, backup_dir='/path/to/backup'):
    """
    Backup all '.log' files in a specified directory to a tar.gz file and delete the original files after backup.
    The backup file is named 'logs_backup.tar.gz' and placed in the specified backup directory.
    
    Parameters:
    - directory (str): The directory that contains the log files to be backed up.
    - backup_dir (str, optional): The directory where the backup file will be saved.
                                  Default is '/path/to/backup'.
    
    Returns:
    - str: The path to the backup file if logs are found, otherwise returns a message 'No logs found to backup'.
    
    Raises:
    - FileNotFoundError: If the specified directory does not exist.
    
    Requirements:
    - subprocess
    - glob
    - os
    
    Example:
    >>> task_func('/path/to/logs')
    '/path/to/backup/logs_backup.tar.gz'
    >>> task_func('/path/to/logs', '/alternative/backup/dir')
    '/alternative/backup/dir/logs_backup.tar.gz'
    """

    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' not found.")

    log_files = glob.glob(os.path.join(directory, '*.log'))
    if not log_files:
        return "No logs found to backup."

    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    backup_file = os.path.join(backup_dir, 'logs_backup.tar.gz')
    subprocess.call(['tar', '-czvf', backup_file] + log_files)

    for file in log_files:
        os.remove(file)

    return backup_file

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = 'test_logs'
        self.backup_dir = 'test_backup'
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        # Clean up by removing the test directories after each test
        if os.path.exists(self.test_dir):
            for file in glob.glob(os.path.join(self.test_dir, '*.log')):
                os.remove(file)
            os.rmdir(self.test_dir)
        if os.path.exists(self.backup_dir):
            os.remove(os.path.join(self.backup_dir, 'logs_backup.tar.gz'))
            os.rmdir(self.backup_dir)

    def test_no_log_files(self):
        """Test case when there are no log files to back up."""
        result = task_func(self.test_dir, self.backup_dir)
        self.assertEqual(result, "No logs found to backup.")

    def test_backup_log_files(self):
        """Test case to back up log files and ensure they are removed."""
        with open(os.path.join(self.test_dir, 'test.log'), 'w') as f:
            f.write('This is a test log file.')

        task_func(self.test_dir, self.backup_dir)
        self.assertTrue(os.path.exists(os.path.join(self.backup_dir, 'logs_backup.tar.gz')))
        self.assertFalse(os.path.exists(os.path.join(self.test_dir, 'test.log')))

    def test_backup_directory_creation(self):
        """Test case to ensure that the backup directory is created if it doesn't exist."""
        with open(os.path.join(self.test_dir, 'test.log'), 'w') as f:
            f.write('This is a test log file.')

        task_func(self.test_dir, 'new_backup_dir')
        self.assertTrue(os.path.exists('new_backup_dir/logs_backup.tar.gz'))
        self.assertFalse(os.path.exists(os.path.join(self.test_dir, 'test.log')))
        os.rmdir('new_backup_dir')  # Clean up

    def test_invalid_directory(self):
        """Test case for raising FileNotFoundError when provided directory does not exist."""
        with self.assertRaises(FileNotFoundError):
            task_func('invalid_directory', self.backup_dir)

if __name__ == '__main__':
    unittest.main()