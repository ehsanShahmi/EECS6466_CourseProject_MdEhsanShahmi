import json
import hashlib
import blake3
import unittest

def task_func(req_data):
    """
    Hashes the specified request data with BLAKE3 and then converts it into a hexadecimal representation.
    Additionally, generates an MD5 hash of the BLAKE3 hash for demonstration purposes (not for security).
    BLAKE3 is a cryptographic hash function that is much faster than MD5 and SHA-1, while providing
    high security.

    Parameters:
        req_data (dict): The request data to be hashed. It should be a dictionary.

    Returns:
        tuple: 
            - str: The hexadecimal representation of the BLAKE3 hash of the request data.
            - str: An MD5 hash of the hexadecimal BLAKE3 representation, for demonstration.

    Examples:
    >>> blake3_hash, md5_hash = task_func({'key': 'value'})
    >>> isinstance(blake3_hash, str) and len(blake3_hash) == 64
    True
    >>> isinstance(md5_hash, str) and len(md5_hash) == 32
    True
    >>> task_func({'empty': ''})[0] != task_func({'another': 'data'})[0]
    True
    """

    # Convert request data to json string
    json_req_data = json.dumps(req_data)
    # Hash the request data using BLAKE3 and get hexadecimal representation directly
    blake3_hex = blake3.blake3(json_req_data.encode('utf-8')).hexdigest()
    # Use hashlib for generating an MD5 hash of the BLAKE3 hex representation (for demonstration)
    md5_hash = hashlib.md5(blake3_hex.encode('utf-8')).hexdigest()

    return blake3_hex, md5_hash

class TestTaskFunction(unittest.TestCase):

    def test_hash_length(self):
        """Test that the BLAKE3 hash is 64 characters long and MD5 hash is 32 characters long."""
        blake3_hash, md5_hash = task_func({'key': 'value'})
        self.assertEqual(len(blake3_hash), 64)
        self.assertEqual(len(md5_hash), 32)

    def test_different_inputs(self):
        """Test that different inputs result in different BLAKE3 hashes."""
        hash1 = task_func({'input': 'first'})[0]
        hash2 = task_func({'input': 'second'})[0]
        self.assertNotEqual(hash1, hash2)

    def test_empty_input(self):
        """Test the function with an empty dictionary."""
        blake3_hash, md5_hash = task_func({})
        self.assertEqual(len(blake3_hash), 64)
        self.assertEqual(len(md5_hash), 32)

    def test_identical_inputs(self):
        """Test that identical inputs give the same BLAKE3 hash."""
        hash1 = task_func({'key': 'value'})[0]
        hash2 = task_func({'key': 'value'})[0]
        self.assertEqual(hash1, hash2)

    def test_non_string_data(self):
        """Test that the function can handle non-string data types in dictionary."""
        blake3_hash, md5_hash = task_func({'int': 123, 'list': [1, 2, 3]})
        self.assertEqual(len(blake3_hash), 64)
        self.assertEqual(len(md5_hash), 32)


if __name__ == '__main__':
    unittest.main()