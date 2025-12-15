import subprocess
import platform
import time
import unittest

def task_func(url):
    """
    Open a web page in the default web browser in a background process.

    Parameters:
    url (str): The URL of the webpage to be opened.

    Returns:
    int: The return code of the subprocess.

    Requirements:
    - subprocess
    - platform
    - time

    Example:
    >>> task_func('https://www.google.com')
    0
    """

    if platform.system() == 'Darwin':
        cmd = 'open'
    elif platform.system() == 'Windows':
        cmd = 'start'
    else:
        cmd = 'xdg-open'

    # Open webpage in a background process
    process = subprocess.Popen([cmd, url], shell=True)

    # Wait for the process to complete
    while process.poll() is None:
        time.sleep(1)

    return process.returncode

class TestTaskFunc(unittest.TestCase):

    def test_valid_url(self):
        """Test with a valid URL."""
        self.assertEqual(task_func('https://www.google.com'), 0)

    def test_invalid_url(self):
        """Test with an invalid URL."""
        self.assertNotEqual(task_func('invalid-url'), 0)

    def test_localhost_url(self):
        """Test with localhost URL."""
        self.assertEqual(task_func('http://localhost:8000'), 0)

    def test_empty_url(self):
        """Test with an empty URL."""
        with self.assertRaises(IndexError):
            task_func('')

    def test_url_with_special_chars(self):
        """Test with URL containing special characters."""
        self.assertEqual(task_func('https://www.example.com/?q=test%20case'), 0)

if __name__ == '__main__':
    unittest.main()