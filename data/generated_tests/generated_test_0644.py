import unittest
import os
import hashlib
import base64

# Here is your prompt:
def task_func(filename, data, password):
    """
    Encrypt a string with a password, then write the encrypted string to a file. 
    If the file or directory does not exist, create it.

    Parameters:
    filename (str): The name of the file to write to.
    data (str): The string to encrypt and write to the file.
    password (str): The password to use for encryption.

    Returns:
    str: The encrypted string.

    Requirements:
    - hashlib
    - base64

    Example:
    >>> task_func('test.txt', 'Hello, World!', 'password')
    'Fu0k9LUEJCY+ookLrA=='
    """

               # Ensure the file exists
    directory = os.path.dirname(filename)
    os.makedirs(directory, exist_ok=True)
    if not os.path.exists(filename):
        open(filename, 'a').close()

    # Encrypt the data using simple XOR operation with password hash as key
    key = hashlib.sha256(password.encode()).digest()
    encrypted_bytes = [byte ^ key[i % len(key)] for i, byte in enumerate(data.encode())]
    encrypted = base64.b64encode(bytes(encrypted_bytes)).decode()

    # Write to the file
    with open(filename, 'w') as f:
        f.write(encrypted)

    return encrypted


class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.test_filename = 'test_dir/test.txt'
        self.test_data = 'Hello, World!'
        self.test_password = 'password'
    
    def tearDown(self):
        # Remove the test file and directory after each test
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
        if os.path.exists('test_dir'):
            os.rmdir('test_dir')
    
    def test_file_creation(self):
        """Test if the function creates the file when it does not exist."""
        result = task_func(self.test_filename, self.test_data, self.test_password)
        self.assertTrue(os.path.exists(self.test_filename))
        self.assertEqual(result, 'Fu0k9LUEJCY+ookLrA==')
    
    def test_encrypted_output(self):
        """Test if the function returns the correct encrypted output."""
        result = task_func(self.test_filename, self.test_data, self.test_password)
        expected = 'Fu0k9LUEJCY+ookLrA=='
        self.assertEqual(result, expected)

    def test_file_content(self):
        """Test if the content of the file is as expected after writing."""
        task_func(self.test_filename, self.test_data, self.test_password)
        with open(self.test_filename, 'r') as f:
            content = f.read()
        self.assertEqual(content, 'Fu0k9LUEJCY+ookLrA==')

    def test_multiple_calls(self):
        """Test if multiple calls result in the same output for the same input."""
        result1 = task_func(self.test_filename, self.test_data, self.test_password)
        result2 = task_func(self.test_filename, self.test_data, self.test_password)
        self.assertEqual(result1, result2)

    def test_different_passwords(self):
        """Test if different passwords produce different outputs."""
        result1 = task_func(self.test_filename, self.test_data, self.test_password)
        result2 = task_func(self.test_filename, self.test_data, 'different_password')
        self.assertNotEqual(result1, result2)

if __name__ == '__main__':
    unittest.main()