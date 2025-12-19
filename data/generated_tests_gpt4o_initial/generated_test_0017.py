import unittest
import subprocess
import psutil
import time

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up test environment - This runs before each test."""
        self.process_name = "notepad.exe"  # Example process; adjust for your environment

    def test_process_not_found_starting(self):
        """Test case for when the process is not running and needs to be started."""
        # Ensure the process is not running
        self.assertFalse(self.check_process_running(self.process_name))
        
        # Call the task_func (you would call the actual function in practice)
        result = task_func(self.process_name)
        
        # Check the result
        self.assertEqual(result, f"Process not found. Starting {self.process_name}.")
        
    def test_process_found_restarting(self):
        """Test case for when the process is already running and needs to be restarted."""
        # Start the process manually for the test
        subprocess.Popen(self.process_name)
        time.sleep(2)  # Wait for a moment to ensure the process is running

        # Ensure the process is running
        self.assertTrue(self.check_process_running(self.process_name))
        
        # Call the task_func (you would call the actual function in practice)
        result = task_func(self.process_name)

        # Check the result
        self.assertEqual(result, f"Process found. Restarting {self.process_name}.")
    
    def test_multiple_instances(self):
        """Test case for handling multiple instances of the process."""
        # Start multiple instances of the process
        subprocess.Popen(self.process_name)
        subprocess.Popen(self.process_name)
        time.sleep(2)  # Allow time for launches

        # Ensure that at least two instances are running
        self.assertGreaterEqual(len(psutil.process_iter([self.process_name])), 2)

        # Call the task_func (you would call the actual function in practice)
        result = task_func(self.process_name)

        # Check the result - we expect that it restarted since there were running instances
        self.assertEqual(result, f"Process found. Restarting {self.process_name}.")

    def test_invalid_process(self):
        """Test case for an invalid process name."""
        invalid_process = "invalid_process_name.exe"
        
        # Call the task_func with invalid process name
        result = task_func(invalid_process)

        # Check that the appropriate response is returned
        self.assertEqual(result, f"Process not found. Starting {invalid_process}.")

    def check_process_running(self, process_name):
        """Helper function to check if a process is running."""
        for proc in psutil.process_iter():
            if proc.name() == process_name:
                return True
        return False

    def tearDown(self):
        """Clean up after tests - This runs after each test."""
        # Attempt to kill the process if it is running
        for proc in psutil.process_iter():
            if proc.name() == self.process_name:
                proc.terminate()

if __name__ == '__main__':
    unittest.main()