import unittest
import os
import json
import time

LOGFILE_PATH = "logfile.log"

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create a clean environment before each test."""
        if os.path.exists(LOGFILE_PATH):
            os.remove(LOGFILE_PATH)

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(LOGFILE_PATH):
            os.remove(LOGFILE_PATH)

    def test_valid_input(self):
        """Test with valid interval and duration."""
        path = task_func(1, 5)
        self.assertEqual(path, LOGFILE_PATH)
        self.assertTrue(os.path.exists(LOGFILE_PATH), "Log file should exist after execution.")
        
        with open(LOGFILE_PATH, "r") as logfile:
            data = logfile.readlines()
            self.assertGreater(len(data), 0, "Log file should contain data.")
            for line in data:
                log_entry = json.loads(line.strip())
                self.assertIn("timestamp", log_entry)
                self.assertIn("cpu_usage", log_entry)

    def test_zero_interval(self):
        """Test with zero as interval."""
        with self.assertRaises(ValueError):
            task_func(0, 5)

    def test_negative_duration(self):
        """Test with negative duration."""
        with self.assertRaises(ValueError):
            task_func(2, -5)

    def test_zero_duration(self):
        """Test with zero as duration."""
        with self.assertRaises(ValueError):
            task_func(5, 0)

    def test_file_creation_on_io_error(self):
        """Simulate an IOError when writing to the log file."""
        # Temporarily change LOGFILE_PATH to an invalid location
        global LOGFILE_PATH
        LOGFILE_PATH = "/invalid_path/logfile.log"  # This path likely won't exist

        result = task_func(1, 5)
        self.assertIsNone(result, "Function should return None on IOError due to file write error.")
        
        # Restore the original log file path
        LOGFILE_PATH = "logfile.log"

if __name__ == "__main__":
    unittest.main()