import unittest
import rsa
import urllib.request

def task_func(url):
    """
    Generates RSA public and private keys, retrieves the content from the specified URL, calculates
    its SHA256 hash, and signs the hash with the private key. Returns the public key and the signed hash
    as a hexadecimal string.

    Parameters:
    url (str): The URL whose content is to be fetched and signed.

    Returns:
    rsa.PublicKey: The RSA public key.
    str: The hexadecimal string of the signed SHA256 hash of the URL content.
    bytes: The hashed URL content, for verification purpose

    Raises:
    ValueError: If there's an issue reaching the server (e.g., network error, invalid URL)
                or if the server returns an HTTP error.
    rsa.pkcs1.VerificationError: If there's a failure in signing the hash with the RSA private key.
    urllib.error.URLError: If the server is not reachable

    Requirements:
    - rsa
    - urllib.request
    - hashlib.sha256

    Examples:
    >>> pub_key, signed_hash, hash_value = task_func('https://www.example.com')
    >>> isinstance(pub_key, rsa.PublicKey)
    True
    >>> isinstance(signed_hash, str)
    True
    >>> isinstance(hash_value, bytes)
    True
    """

    try:
        (pub_key, priv_key) = rsa.newkeys(512)

        response = urllib.request.urlopen(url)
        content = response.read()
        hash_value = sha256(content).digest()
        
        signed_hash = rsa.sign(hash_value, priv_key, 'SHA-256').hex()

        return pub_key, signed_hash, hash_value
    except urllib.error.HTTPError as e:
        raise ValueError(f"Server returned an HTTP error: {e.code} {e.reason}") from e
    except urllib.error.URLError as e:
        raise urllib.error.URLError(f"Failed to reach the server. URL might be invalid: {e}") from e
    except rsa.pkcs1.VerificationError as e:
        raise rsa.pkcs1.VerificationError(f"Failed to sign the hash: {e}") from e    

class TestTaskFunc(unittest.TestCase):

    def test_valid_url(self):
        """ Test with a valid URL to ensure proper functioning. """
        pub_key, signed_hash, hash_value = task_func('https://www.example.com')
        self.assertIsInstance(pub_key, rsa.PublicKey)
        self.assertIsInstance(signed_hash, str)
        self.assertIsInstance(hash_value, bytes)

    def test_invalid_url(self):
        """ Test with an invalid URL to raise ValueError. """
        with self.assertRaises(ValueError):
            task_func('invalid_url')

    def test_nonexistent_url(self):
        """ Test with a URL that doesn't exist to raise URLError. """
        with self.assertRaises(urllib.error.URLError):
            task_func('http://nonexistent.url')

    def test_http_error(self):
        """ Test with a URL that causes an HTTP error. """
        with self.assertRaises(ValueError):
            task_func('https://httpstat.us/404')  # A 404 error example

    def test_network_error(self):
        """ Test with a URL that will simulate a network error. """
        with self.assertRaises(urllib.error.URLError):
            task_func('http://localhost:12345')  # Assuming nothing is running on this port

if __name__ == '__main__':
    unittest.main()