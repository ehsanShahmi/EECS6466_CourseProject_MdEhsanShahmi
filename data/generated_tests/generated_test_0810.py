import unittest
import os
import tempfile
import subprocess

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory to hold dummy executable files
        self.test_dir = tempfile.mkdtemp()

        # Create some dummy executable files for testing
        self.exe_files = [
            'test1.exe',   # This one should match the regex
            'test2.executable',  # This one should not match
            'test3.exe',   # This one should match the regex
            'Distillr.exe',    # This one should not match due to negative lookbehind
        ]

        for exe in self.exe_files:
            with open(os.path.join(self.test_dir, exe), 'w') as f:
                f.write('#!/bin/sh\necho Hello World')  # Dummy shell script
            # Set the file as executable
            os.chmod(os.path.join(self.test_dir, exe), 0o755)

    def tearDown(self):
        # Clean up the temporary directory and files created
        for exe in self.exe_files:
            os.remove(os.path.join(self.test_dir, exe))
        os.rmdir(self.test_dir)

    def test_execute_files(self):
        """ Test executing the found files and returning their outputs. """
        result = task_func(self.test_dir, r'test\d\.exe')
        self.assertEqual(result, ['Hello World\n', 'Hello World\n'], "Should return correct outputs from executables.")

    def test_return_paths(self):
        """ Test returning paths of the found files without execution. """
        result = task_func(self.test_dir, r'test\d\.exe', execute_files=False)
        expected_paths = [os.path.join(self.test_dir, 'test1.exe'), os.path.join(self.test_dir, 'test3.exe')]
        self.assertEqual(result, expected_paths, "Should return correct paths of found executables.")

    def test_negative_lookbehind(self):
        """ Test that the function respects the negative lookbehind in regex. """
        result = task_func(self.test_dir, r'(?<!Distillr)test\d\.exe', execute_files=False)
        expected_paths = [os.path.join(self.test_dir, 'test1.exe'), os.path.join(self.test_dir, 'test3.exe')]
        self.assertEqual(result, expected_paths, "Should not match Distillr.exe.")

    def test_no_matches(self):
        """ Test the scenario where no files match the regex pattern. """
        result = task_func(self.test_dir, r'nonexistent\.exe')
        self.assertEqual(result, [], "Should return an empty list when no matches are found.")

    def test_invalid_directory(self):
        """ Test handling of an invalid directory path. """
        with self.assertRaises(FileNotFoundError):
            task_func('/invalid/path', r'test\.exe')

if __name__ == '__main__':
    unittest.main()