import requests
from bs4 import BeautifulSoup
import unittest

def task_func(url, tag):
    """
    Scrape a web page for the first occurrence of a specified HTML tag and return its text content.

    Parameters:
    url (str): The URL of the website to scrape.
    tag (str): The HTML tag to find and retrieve text from.

    Returns:
    str: The text content of the specified HTML tag if found, otherwise returns None.

    Requirements:
    - requests
    - bs4.BeautifulSoup

    Example:
    >>> task_func("https://www.google.com/", "title")
    'Google'
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    tag_content = soup.find(tag)
    
    return tag_content.string if tag_content else None


class TestTaskFunc(unittest.TestCase):
    
    def test_valid_tag(self):
        """Test with a valid URL and tag that is expected to be found."""
        result = task_func("https://www.google.com/", "title")
        self.assertEqual(result, "Google")  # Assuming 'Google' is the title of the page
    
    def test_invalid_tag(self):
        """Test with a valid URL and a tag that does not exist."""
        result = task_func("https://www.google.com/", "non_existing_tag")
        self.assertIsNone(result)  # Should return None for a nonexistent tag

    def test_empty_tag(self):
        """Test with a valid URL and an empty tag string."""
        result = task_func("https://www.google.com/", "")
        self.assertIsNone(result)  # An empty tag should also return None

    def test_invalid_url(self):
        """Test with an invalid URL."""
        with self.assertRaises(requests.exceptions.RequestException):
            task_func("https://invalid-url", "title")  # Expect an exception for invalid URL
    
    def test_http_redirect(self):
        """Test with a URL that results in an HTTP redirect."""
        result = task_func("http://www.example.com", "h1")  # Redirects to example.com
        self.assertEqual(result, "Example Domain")  # Assuming 'Example Domain' is in the <h1> tag

if __name__ == '__main__':
    unittest.main()