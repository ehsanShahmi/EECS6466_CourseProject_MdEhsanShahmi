import subprocess
import os
import random
import unittest

def task_func(directory, file_list):
    """
    Select a random file from a given list of files in a specified directory and run it as a subprocess.
    
    Parameters:
    directory (str): The directory path where the files are located.
    file_list (list of str): A list of file names to choose from.

    Returns:
    int: The exit code of the subprocess, or None if the process is still running or if the file list is empty.

    Requirements:
    - subprocess
    - os
    - random

    Example:
    >>> random.seed(0)
    >>> task_func("c:\Program Files\VMware\VMware Server", ["file1.bat", "file2.bat"]) #valid directory and file list
    0 
    """
    if not file_list:
        return None

    file = random.choice(file_list)
    file_path = os.path.join(directory, file)
    try:
        process = subprocess.Popen(file_path)
        process.wait()  # wait for the process to complete
        return process.returncode  # return the exit code
    except Exception as e:
        return None

class TestTaskFunc(unittest.TestCase):

    def test_empty_file_list(self):
        """Test when the file list is empty."""
        result = task_func("some_directory", [])
        self.assertIsNone(result)

    def test_valid_file_list(self):
        """Test valid directory and file list."""
        # Here we would mock subprocess to simulate execution since we cannot
        # actually run files in a test context.
        directory = "some_directory"
        file_list = ["valid_script.bat", "another_script.bat"]
        with unittest.mock.patch('subprocess.Popen') as mock_popen:
            mock_process = unittest.mock.Mock()
            mock_process.returncode = 0
            mock_popen.return_value = mock_process
            
            result = task_func(directory, file_list)
            self.assertEqual(result, 0)
            mock_popen.assert_called_once()

    def test_invalid_directory(self):
        """Test when the directory does not exist."""
        result = task_func("non_existent_directory", ["file1.bat"])
        # Here we would expect a mocked response, potentially raising an exception
        self.assertIsNone(result)

    def test_process_exception(self):
        """Test when an exception occurs in subprocess."""
        directory = "some_directory"
        file_list = ["script_that_raises_exception.bat"]
        with unittest.mock.patch('subprocess.Popen', side_effect=Exception("Process failed")):
            result = task_func(directory, file_list)
            self.assertIsNone(result)

    def test_multiple_files(self):
        """Test with multiple files, ensuring random selection and execution."""
        directory = "some_directory"
        file_list = ["file1.bat", "file2.bat", "file3.bat"]
        with unittest.mock.patch('subprocess.Popen') as mock_popen:
            mock_process = unittest.mock.Mock()
            mock_process.returncode = 0
            mock_popen.return_value = mock_process
            
            result = task_func(directory, file_list)
            self.assertEqual(result, 0)  # Expecting a successful execution
            self.assertIn(mock_popen.call_args[0][0], [os.path.join(directory, f) for f in file_list])

if __name__ == '__main__':
    unittest.main()