import unittest
import os
import base64
import rsa

# Here is your prompt:
import hashlib


def task_func(file_path):
    """
    Generates a signed hash of a file's contents using RSA encryption. The file's contents are hashed using SHA-256,
    and then the hash is signed with a private RSA key stored in 'private.pem'. The signed hash is encoded in base64.

    Parameters:
    file_path (str): The path to the file whose contents are to be signed.

    Returns:
    str: The base64 encoded signed hash of the file.

    Requirements:
    - hashlib
    - rsa
    - base64

    Examples:
    Assuming 'example.txt' contains some text and a valid 'private.pem' is present,
    >>> len(task_func('example.txt')) > 0
    True

    Assuming 'empty.txt' is an empty file and a valid 'private.pem' is present,
    >>> len(task_func('empty.txt')) > 0
    True
    """
    with open(file_path, 'rb') as f:
        content = f.read()

    hash_output = hashlib.sha256(content).digest()

    with open('private.pem', 'rb') as key_file:
        private_key = rsa.PrivateKey.load_pkcs1(key_file.read())
    signature = rsa.sign(hash_output, private_key, 'SHA-256')

    return base64.b64encode(signature).decode('utf-8')

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a temporary file for testing
        self.test_file_path = 'test_file.txt'
        self.empty_file_path = 'empty_file.txt'
        
        with open(self.test_file_path, 'w') as f:
            f.write('This is a test file for RSA signing.')
        
        # Create an empty file
        open(self.empty_file_path, 'w').close()

        # Initialize RSA keys for the tests
        self.public_key, self.private_key = rsa.newkeys(512)
        with open('private.pem', 'wb') as pem_file:
            pem_file.write(self.private_key.save_pkcs1(format='PEM'))

    def tearDown(self):
        # Remove the test files after tests
        os.remove(self.test_file_path)
        os.remove(self.empty_file_path)
        os.remove('private.pem')

    def test_task_func_non_empty_file(self):
        """Test signing a non-empty file"""
        result = task_func(self.test_file_path)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_task_func_empty_file(self):
        """Test signing an empty file"""
        result = task_func(self.empty_file_path)
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_task_func_with_invalid_path(self):
        """Test signing with an invalid file path"""
        with self.assertRaises(FileNotFoundError):
            task_func('non_existing_file.txt')

    def test_task_func_signature_format(self):
        """Test the format of the signed hash"""
        result = task_func(self.test_file_path)
        decoded_result = base64.b64decode(result)
        self.assertTrue(isinstance(decoded_result, bytes))
        self.assertTrue(len(decoded_result) > 0)

    def test_task_func_multiple_calls(self):
        """Test multiple calls return different results for the same file"""
        result1 = task_func(self.test_file_path)
        result2 = task_func(self.test_file_path)
        self.assertNotEqual(result1, result2)

if __name__ == '__main__':
    unittest.main()