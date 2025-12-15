import unittest
import os
import rsa
from cryptography.fernet import Fernet

# Here is your prompt:
import rsa
from cryptography.fernet import Fernet
from base64 import b64encode

def task_func(file_path):
    """
    Generates RSA public and private keys and uses Fernet symmetric encryption to encrypt the contents
    of a specified file. The Fernet key is then encrypted with the public RSA key. The encrypted file
    contents and the encrypted Fernet key are saved in separate files.

    This method demonstrates a hybrid encryption approach where symmetric encryption is used for the file
    contents and asymmetric encryption for the encryption key.

    Parameters:
    file_path (str): The path to the file to be encrypted.

    Returns:
    PublicKey: The RSA public key.
    str: The filename of the encrypted file.
    str: The filename of the file containing the encrypted Fernet key.

    Requirements:
    - rsa
    - cryptography.fernet.Fernet
    - base64.b64encode

    Examples:
    >>> pub_key, encrypted_file, encrypted_key_file = task_func('my_file.txt')
    >>> len(pub_key.save_pkcs1()) > 100
    True
    >>> encrypted_file.endswith('.encrypted')
    True
    >>> encrypted_key_file.endswith('.encrypted')
    True
    """

    (pub_key, priv_key) = rsa.newkeys(512)
    fernet_key = Fernet.generate_key()
    fernet = Fernet(fernet_key)

    with open(file_path, 'rb') as f:
        data = f.read()
        encrypted_data = fernet.encrypt(data)

    encrypted_file = file_path + '.encrypted'
    with open(encrypted_file, 'wb') as f:
        f.write(encrypted_data)

    encrypted_fernet_key = rsa.encrypt(fernet_key, pub_key)
    encrypted_key_file = 'fernet_key.encrypted'
    with open(encrypted_key_file, 'wb') as f:
        f.write(b64encode(encrypted_fernet_key))

    return pub_key, encrypted_file, encrypted_key_file

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.test_file = 'test_file.txt'
        with open(self.test_file, 'wb') as f:
            f.write(b'This is a test file for encryption.')

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        if os.path.exists(self.test_file + '.encrypted'):
            os.remove(self.test_file + '.encrypted')
        if os.path.exists('fernet_key.encrypted'):
            os.remove('fernet_key.encrypted')

    def test_generate_rsa_keys(self):
        pub_key, encrypted_file, encrypted_key_file = task_func(self.test_file)
        self.assertIsInstance(pub_key, rsa.PublicKey)

    def test_encrypted_file_exists(self):
        pub_key, encrypted_file, encrypted_key_file = task_func(self.test_file)
        self.assertTrue(os.path.exists(encrypted_file))

    def test_encrypted_key_file_exists(self):
        pub_key, encrypted_file, encrypted_key_file = task_func(self.test_file)
        self.assertTrue(os.path.exists(encrypted_key_file))

    def test_encrypted_file_extension(self):
        pub_key, encrypted_file, encrypted_key_file = task_func(self.test_file)
        self.assertTrue(encrypted_file.endswith('.encrypted'))

    def test_encrypted_key_file_extension(self):
        pub_key, encrypted_file, encrypted_key_file = task_func(self.test_file)
        self.assertTrue(encrypted_key_file.endswith('.encrypted'))

if __name__ == '__main__':
    unittest.main()