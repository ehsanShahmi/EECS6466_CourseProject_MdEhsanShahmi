import subprocess
import time
import threading
import unittest

# The provided code (prompt) is left untouched as required

def task_func(file_list):
    """
    Run files from list of files as subprocesses at the same time.
    
    Parameters:
    - file_list (list of str): List of files name to run.

    Returns:
    list: The exit codes of the subprocesses.
    """
    exit_codes = []

    def execute_file(file):
        file_path = file
        process = subprocess.Popen(file_path)
        time.sleep(1)  # wait for the process to start
        exit_codes.append(process.poll())  # store the exit code

    # Start a thread for each file
    threads = [threading.Thread(target=execute_file, args=(file,)) for file in file_list]
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return exit_codes

class TestTaskFunc(unittest.TestCase):

    def test_empty_file_list(self):
        """Test with an empty file list."""
        result = task_func([])
        self.assertEqual(result, [])

    def test_single_file(self):
        """Test with a single valid file."""
        # Assuming testfile.bat exists and returns 0 exit code
        with open("testfile.bat", "w") as f:
            f.write("exit 0")
        result = task_func(["testfile.bat"])
        self.assertEqual(result, [0])

    def test_multiple_files(self):
        """Test with multiple valid files."""
        with open("testfile1.bat", "w") as f1, open("testfile2.bat", "w") as f2:
            f1.write("exit 0")
            f2.write("exit 0")
        result = task_func(["testfile1.bat", "testfile2.bat"])
        self.assertEqual(result, [0, 0])

    def test_invalid_file(self):
        """Test with an invalid file."""
        result = task_func(["non_existent_file.bat"])
        # Expecting a None return code since the file doesn't exist
        self.assertEqual(result, [None])

    def test_mixed_files(self):
        """Test with mixed valid and invalid files."""
        with open("validfile.bat", "w") as vf:
            vf.write("exit 0")
        result = task_func(["validfile.bat", "non_existent_file.bat"])
        # Expecting exit code 0 for the valid file and None for the invalid file
        self.assertEqual(result, [0, None])

if __name__ == '__main__':
    unittest.main()