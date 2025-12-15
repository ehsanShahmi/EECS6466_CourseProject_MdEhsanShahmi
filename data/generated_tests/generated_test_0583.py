import unittest
import os
import rsa
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode

def task_func():
    (pub_key, priv_key) = rsa.newkeys(512)
    password = get_random_bytes(16)

    cipher = AES.new(password, AES.MODE_EAX)
    nonce = cipher.nonce
    priv_key_encrypted, tag = cipher.encrypt_and_digest(priv_key.save_pkcs1())

    priv_key_encrypted = b64encode(priv_key_encrypted).decode('utf-8')

    filename = f'private_key_{os.urandom(8).hex()}.txt'
    with open(filename, 'w') as f:
        f.write(priv_key_encrypted)

    return pub_key, filename, password, nonce

class TestTaskFunc(unittest.TestCase):
    
    def test_return_type(self):
        pub_key, filename, password, nonce = task_func()
        self.assertIsInstance(pub_key, rsa.PublicKey)
        self.assertIsInstance(filename, str)
        self.assertIsInstance(password, bytes)
        self.assertIsInstance(nonce, bytes)

    def test_file_creation(self):
        pub_key, filename, password, nonce = task_func()
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)  # Clean up after test

    def test_correct_file_content(self):
        pub_key, filename, password, nonce = task_func()
        with open(filename, 'r') as f:
            content = f.read()
            self.assertIsInstance(content, str)
            self.assertTrue(len(content) > 0)  # Ensure file is not empty
        os.remove(filename)  # Clean up after test

    def test_password_bytes_length(self):
        pub_key, filename, password, nonce = task_func()
        self.assertEqual(len(password), 16)  # Ensure password is 16 bytes long

    def test_nonce_bytes_length(self):
        pub_key, filename, password, nonce = task_func()
        self.assertEqual(len(nonce), 16)  # Ensure nonce is 16 bytes long

if __name__ == '__main__':
    unittest.main()