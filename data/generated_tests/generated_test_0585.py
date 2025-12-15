import unittest
import os
import rsa
import zipfile
from base64 import b64encode

# Here is your prompt:
def task_func(directory):
    """
    Generates RSA public and private keys, encrypts all files in the specified directory using the public key,
    and saves the encrypted files into a zip file. It returns the public key and the name of the zip file.

    Note: This method directly encrypts file data with RSA, which is not recommended for large files or
    production use. Typically, RSA is used to encrypt a symmetric key (like AES), which is then used to
    encrypt the actual data.

    Parameters:
    directory (str): The directory containing the files to be encrypted.

    Returns:
    rsa.PublicKey: The RSA public key.
    str: The filename of the zip file containing the encrypted files.

    Requirements:
    - rsa
    - os
    - zipfile
    - base64.b64encode

    Examples:
    >>> pub_key, zipfile_name = task_func('./')
    >>> isinstance(pub_key, rsa.PublicKey)
    'True'
    >>> isinstance(zipfile_name, str)
    'True'
    """

    (pub_key, priv_key) = rsa.newkeys(512)
    zipfile_name = 'encrypted_files.zip'

    with zipfile.ZipFile(zipfile_name, 'w') as zipf:
        for filename in os.listdir(directory):
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                with open(filepath, 'rb') as f:
                    data = f.read()
                    encrypted_data = rsa.encrypt(data, pub_key)
                    zipf.writestr(filename, b64encode(encrypted_data).decode('utf-8'))

    return pub_key, zipfile_name

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create a temporary directory and some files for testing."""
        self.test_dir = 'test_directory'
        os.makedirs(self.test_dir, exist_ok=True)
        # Create sample files to encrypt
        with open(os.path.join(self.test_dir, 'file1.txt'), 'w') as f:
            f.write('This is a test file 1.')
        with open(os.path.join(self.test_dir, 'file2.txt'), 'w') as f:
            f.write('This is a test file 2.')

    def tearDown(self):
        """Clean up the temporary directory after tests."""
        for filename in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, filename)
            os.remove(file_path)
        os.rmdir(self.test_dir)

    def test_task_function_returns_keys_and_zip(self):
        """Test if the function returns a public key and a zip file name."""
        pub_key, zipfile_name = task_func(self.test_dir)
        self.assertIsInstance(pub_key, rsa.PublicKey)
        self.assertIsInstance(zipfile_name, str)
        self.assertEqual(zipfile_name, 'encrypted_files.zip')

    def test_zip_file_creation(self):
        """Test if the zip file is created after running task_func."""
        task_func(self.test_dir)
        self.assertTrue(os.path.exists('encrypted_files.zip'))

    def test_encrypted_file_count(self):
        """Test if the number of files in the zip matches the number of original files."""
        task_func(self.test_dir)
        with zipfile.ZipFile('encrypted_files.zip', 'r') as zipf:
            zip_contents = zipf.namelist()
        self.assertEqual(len(zip_contents), 2)

    def test_encrypted_file_integrity(self):
        """Test if the elastic encrypted files can be decrypted successfully."""
        pub_key, _ = task_func(self.test_dir)
        # The private key is not returned in this implementation,
        # so we'll simply check that the encryption does not raise an error
        try:
            for filename in os.listdir(self.test_dir):
                with open(os.path.join(self.test_dir, filename), 'rb') as f:
                    data = f.read()
                    encrypted_data = rsa.encrypt(data, pub_key)
                    self.assertIsNotNone(encrypted_data)
        except Exception as e:
            self.fail(f"Encryption failed with error: {e}")

if __name__ == '__main__':
    unittest.main()