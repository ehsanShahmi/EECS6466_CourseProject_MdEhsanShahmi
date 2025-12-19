import os
import re
import unittest

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up a temporary log directory for testing."""
        self.test_log_dir = '/tmp/test_logs'
        os.makedirs(self.test_log_dir, exist_ok=True)

    def tearDown(self):
        """Remove the temporary log directory after tests."""
        for file in os.listdir(self.test_log_dir):
            os.remove(os.path.join(self.test_log_dir, file))
        os.rmdir(self.test_log_dir)

    def test_no_log_files(self):
        """Test that None is returned when there are no matching log files."""
        result = task_func(r'^access.log.[0-9]+$', self.test_log_dir)
        self.assertIsNone(result)

    def test_single_matching_log_file(self):
        """Test that the function returns the correct log file when one matches."""
        with open(os.path.join(self.test_log_dir, 'access.log.1'), 'w') as f:
            f.write('Test log entry.')
        result = task_func(r'^access.log.[0-9]+$', self.test_log_dir)
        self.assertEqual(result, os.path.join(self.test_log_dir, 'access.log.1'))

    def test_multiple_matching_log_files(self):
        """Test that the function returns the most recent log file among multiple matches."""
        with open(os.path.join(self.test_log_dir, 'access.log.1'), 'w') as f:
            f.write('Test log entry 1.')
        with open(os.path.join(self.test_log_dir, 'access.log.2'), 'w') as f:
            f.write('Test log entry 2.')
        os.utime(os.path.join(self.test_log_dir, 'access.log.1'), (1, 1))  # Older timestamp
        os.utime(os.path.join(self.test_log_dir, 'access.log.2'), (2, 2))  # Newer timestamp
        result = task_func(r'^access.log.[0-9]+$', self.test_log_dir)
        self.assertEqual(result, os.path.join(self.test_log_dir, 'access.log.2'))

    def test_no_matching_files_with_other_files(self):
        """Test that None is returned when there are no matching files but some other files exist."""
        with open(os.path.join(self.test_log_dir, 'error.log.1'), 'w') as f:
            f.write('Error log entry.')
        result = task_func(r'^access.log.[0-9]+$', self.test_log_dir)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()