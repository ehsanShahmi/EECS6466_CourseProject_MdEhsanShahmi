import unittest
import hashlib
import codecs
import random
import string

def task_func(password_length=10, salt="salty"):
    password_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(password_chars) for i in range(password_length))
    password = codecs.encode(password, 'latin-1').decode('utf-8')
    salted_password = (password + salt).encode('utf-8')
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    
    return hashed_password

class TestTaskFunc(unittest.TestCase):
    
    def test_default_password_length(self):
        # Test if the default password length is 10
        hashed_password = task_func()
        self.assertEqual(len(codecs.decode(hashed_password, 'hex')), 64)  # SHA256 returns 64 hex characters

    def test_custom_password_length(self):
        # Test a custom password length of 12
        hashed_password = task_func(12)
        self.assertEqual(len(codecs.decode(hashed_password, 'hex')), 64)

    def test_hash_with_different_salts(self):
        # Test that different salts yield different hashes
        hash1 = task_func(10, "salt1")
        hash2 = task_func(10, "salt2")
        self.assertNotEqual(hash1, hash2)

    def test_hash_same_password_length_and_salt(self):
        # Test that the same password length and salt yields the same hash
        random.seed(0)  # Set seed for reproducibility
        hash1 = task_func(12, "my_salt")
        random.seed(0)  # Reset seed
        hash2 = task_func(12, "my_salt")
        self.assertEqual(hash1, hash2)

    def test_hash_contains_valid_length(self):
        # Test that the hashed output is a valid SHA256 hash
        hashed_password = task_func(15, "test_salt")
        self.assertRegex(hashed_password, r'^[a-f0-9]{64}$')  # Check if it's a valid hex string of length 64

if __name__ == '__main__':
    unittest.main()