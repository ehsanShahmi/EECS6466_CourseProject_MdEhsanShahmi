import unittest
from unittest.mock import patch, MagicMock

# Provided prompt
import mechanize
from bs4 import BeautifulSoup


def task_func(url, form_id, data):
    """
    Submits a form on a given webpage using mechanize and extracts the title of the response page.

    Parameters:
        url (str): The URL of the webpage containing the form.
        form_id (int): The index of the form to be submitted.
        data (dict): A dictionary containing form data keys and values.

    Returns:
        str: The title of the page resulting from the form submission.

    Notes:
        - If the page has no title, it returns 'No Title'.

    Requirements:
        - mechanize
        - bs4.BeautifulSoup

    Examples:
        >>> data = {'username': 'admin', 'password': 'password'}
        >>> title = task_func('https://www.example.com/login', 0, data)
        >>> isinstance(title, str)
        True
    """

    br = mechanize.Browser()
    br.open(url)
    br.select_form(nr=form_id)

    for key, value in data.items():
        br[key] = value

    response = br.submit()

    soup = BeautifulSoup(response.read(), 'html.parser')
    title = soup.title.string if soup.title else 'No Title'

    return title


class TestTaskFunction(unittest.TestCase):

    @patch('mechanize.Browser')
    def test_valid_form_submission_with_title(self, mock_browser):
        mock_response = MagicMock()
        mock_response.read.return_value = b'<html><head><title>Success</title></head></html>'
        mock_browser.return_value.submit.return_value = mock_response
        
        title = task_func('http://example.com', 0, {'username': 'test', 'password': 'test'})
        self.assertEqual(title, 'Success')

    @patch('mechanize.Browser')
    def test_valid_form_submission_without_title(self, mock_browser):
        mock_response = MagicMock()
        mock_response.read.return_value = b'<html><head></head></html>'
        mock_browser.return_value.submit.return_value = mock_response
        
        title = task_func('http://example.com', 0, {'username': 'test', 'password': 'test'})
        self.assertEqual(title, 'No Title')

    @patch('mechanize.Browser')
    def test_invalid_form_submission(self, mock_browser):
        mock_response = MagicMock()
        mock_response.read.return_value = b'<html><head><title>Error</title></head></html>'
        mock_browser.return_value.submit.return_value = mock_response
        
        title = task_func('http://example.com', 0, {'username': 'invalid', 'password': 'invalid'})
        self.assertEqual(title, 'Error')

    @patch('mechanize.Browser')
    def test_empty_title(self, mock_browser):
        mock_response = MagicMock()
        mock_response.read.return_value = b'<html><head><title></title></head></html>'
        mock_browser.return_value.submit.return_value = mock_response
        
        title = task_func('http://example.com', 0, {'username': 'test', 'password': 'test'})
        self.assertEqual(title, 'No Title')

    @patch('mechanize.Browser')
    def test_no_form_available(self, mock_browser):
        mock_response = MagicMock()
        mock_response.read.return_value = b'<html><head><title>No Form Available</title></head></html>'
        mock_browser.return_value.submit.return_value = mock_response
        
        title = task_func('http://example.com', 0, {'username': 'test', 'password': 'test'})
        self.assertEqual(title, 'No Form Available')


if __name__ == '__main__':
    unittest.main()