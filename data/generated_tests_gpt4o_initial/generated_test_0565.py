import unittest
import os

class TestTaskFunction(unittest.TestCase):

    def setUp(self):
        # Create a temporary DLL file for testing
        self.test_dll_path = 'test_dll.dll'
        with open(self.test_dll_path, 'wb') as f:
            f.write(b'\x00')  # Writing a single byte to create a valid file

    def tearDown(self):
        # Remove the temporary DLL file after tests
        if os.path.exists(self.test_dll_path):
            os.remove(self.test_dll_path)

    def test_load_dll(self):
        """Test if the DLL can be loaded correctly."""
        result = task_func(self.test_dll_path)
        self.assertEqual(result, '_name')  # placeholder for the expected DLL name

    def test_md5_hash(self):
        """Test if the MD5 hash generated is correct."""
        # Capture the output
        with self.assertLogs(level='INFO') as log:
            task_func(self.test_dll_path)
        self.assertIn('MD5 Hash: d41d8cd98f00b204e9800998ecf8427e', log.output)

    def test_sha256_hash(self):
        """Test if the SHA256 hash generated is correct."""
        # Capture the output
        with self.assertLogs(level='INFO') as log:
            task_func(self.test_dll_path)
        self.assertIn('SHA256 Hash: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', log.output)

    def test_invalid_filepath(self):
        """Test if the function handles invalid file paths correctly."""
        with self.assertRaises(OSError):
            task_func('invalid_path.dll')

    def test_empty_file(self):
        """Test if the function handles an empty file correctly."""
        empty_dll_path = 'empty_dll.dll'
        with open(empty_dll_path, 'wb') as f:
            pass  # Create an empty file

        result = task_func(empty_dll_path)
        self.assertEqual(result, '_name')  # placeholder for the expected DLL name
        os.remove(empty_dll_path)

if __name__ == '__main__':
    unittest.main()