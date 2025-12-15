import unittest
import random
import string
import base64
import zlib

def task_func(string_length=100):
    """
    Create a random string of a specified length with uppercase letters and digits, compress it with zlib, 
    and then encode the compressed string in base64.

    Parameters:
    - string_length (int, optional): The length of the random string to be generated. Default is 100.

    Returns:
    str: The compressed string in base64.
    """
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=string_length))
    compressed_string = zlib.compress(random_string.encode('utf-8'))
    encoded_compressed_string = base64.b64encode(compressed_string)

    return encoded_compressed_string.decode('utf-8')

class TestTaskFunc(unittest.TestCase):
    
    def test_default_length(self):
        """Test the default length of 100 characters"""
        result = task_func()
        # Check if the result is a valid base64 string
        self.assertEqual(base64.b64encode(zlib.compress(result.encode('utf-8'))).decode('utf-8'), result)

    def test_specific_length(self):
        """Test the function with a specific length"""
        result = task_func(50)
        # Check if the result is a valid base64 string
        self.assertEqual(base64.b64encode(zlib.compress(result.encode('utf-8'))).decode('utf-8'), result)

    def test_string_length(self):
        """Ensure the generated string is of the specified length before compression"""
        test_length = 75
        random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=test_length))
        compressed_string = zlib.compress(random_string.encode('utf-8'))
        encoded_compressed = base64.b64encode(compressed_string).decode('utf-8')
        self.assertEqual(encoded_compressed, task_func(test_length))
        
        # Additional check: if the raw string can be obtained back
        self.assertEqual(zlib.decompress(base64.b64decode(encoded_compressed)).decode('utf-8'), random_string)

    def test_empty_string(self):
        """Test function to handle zero length"""
        result = task_func(0)
        self.assertEqual(result, base64.b64encode(zlib.compress(b'')).decode('utf-8'))

    def test_randomness(self):
        """Ensure that multiple calls with same parameters return different results"""
        first_result = task_func(50)
        second_result = task_func(50)
        self.assertNotEqual(first_result, second_result)

if __name__ == '__main__':
    unittest.main()