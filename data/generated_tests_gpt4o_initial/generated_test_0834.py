import binascii
import io
import gzip
import unittest

def task_func(compressed_hex):
    """
    Uncompress a gzip-compressed hexadecimal string and decrypt the result to UTF-8.
    
    Parameters:
    - compressed_hex (str): The gzip-compressed hexadecimal string.
    
    Returns:
    - decoded_string (str): The decoded and decompressed string in UTF-8 format, or an error message.
    
    Requirements:
    - binascii
    - io
    - gzip
    
    Example:
    >>> task_func('1f8b08000000000002ff0b49494e55560304000000ffff8b202d0b000000')
    'Error during decompression: CRC check failed 0xff000000 != 0x41449975'
    """
    try:
        compressed_bytes = binascii.unhexlify(compressed_hex)
        decompressed_bytes = gzip.GzipFile(fileobj=io.BytesIO(compressed_bytes)).read()
        decoded_string = decompressed_bytes.decode('utf-8')
        return decoded_string
    except gzip.BadGzipFile as e:
        return "Error during decompression: " + str(e)

class TestTaskFunc(unittest.TestCase):
    
    def test_valid_compressed_hex(self):
        # Test with a valid gzip-compressed hex string
        compressed_hex = '1f8b08000000000002ff0b48656c6c6f20576f726c64210000c56b2f8d6c00000000'
        self.assertEqual(task_func(compressed_hex), 'Hello World')

    def test_invalid_compressed_hex_crc_fail(self):
        # Test with an invalid gzip-compressed hex string that fails CRC check
        compressed_hex = '1f8b08000000000002ff0b49494e55560304000000ffff8b202d0b000000'
        self.assertEqual(task_func(compressed_hex), 'Error during decompression: CRC check failed 0xff000000 != 0x41449975')

    def test_not_a_gzip_file(self):
        # Test with a hex string that doesn't represent a proper gzip file
        compressed_hex = '1234567890abcdef'
        self.assertIn("Error during decompression", task_func(compressed_hex))

    def test_empty_string(self):
        # Test with an empty input string
        compressed_hex = ''
        self.assertIn("Error during decompression", task_func(compressed_hex))

    def test_non_hexadecimal_string(self):
        # Test with a non-hexadecimal string
        compressed_hex = 'xyzzy'
        with self.assertRaises(binascii.Error):
            task_func(compressed_hex)

if __name__ == '__main__':
    unittest.main()