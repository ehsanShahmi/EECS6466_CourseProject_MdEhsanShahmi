import unittest
import os
import rsa

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up test environment."""
        self.test_file = 'test_file.txt'
        with open(self.test_file, 'w') as f:
            f.write('This is a test file for encryption.')

    def tearDown(self):
        """Clean up test environment."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_file + '.encrypted'):
            os.remove(self.test_file + '.encrypted')
        if os.path.exists('aes_key.encrypted'):
            os.remove('aes_key.encrypted')

    def test_return_types(self):
        """Test return types of the function."""
        pub_key, encrypted_file, encrypted_key_file = task_func(self.test_file)
        self.assertIsInstance(pub_key, rsa.PublicKey)
        self.assertIsInstance(encrypted_file, str)
        self.assertIsInstance(encrypted_key_file, str)

    def test_encrypted_file_exists(self):
        """Test if the encrypted file is created."""
        _, encrypted_file, _ = task_func(self.test_file)
        self.assertTrue(os.path.exists(encrypted_file))

    def test_encrypted_key_file_exists(self):
        """Test if the encrypted AES key file is created."""
        _, _, encrypted_key_file = task_func(self.test_file)
        self.assertTrue(os.path.exists(encrypted_key_file))

    def test_encrypted_file_extension(self):
        """Test if encrypted file has the correct extension."""
        _, encrypted_file, _ = task_func(self.test_file)
        self.assertTrue(encrypted_file.endswith('.encrypted'))

    def test_encrypted_key_file_extension(self):
        """Test if encrypted AES key file has the correct extension."""
        _, _, encrypted_key_file = task_func(self.test_file)
        self.assertTrue(encrypted_key_file.endswith('.encrypted'))

if __name__ == '__main__':
    unittest.main()