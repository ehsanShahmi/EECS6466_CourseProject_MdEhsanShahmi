import unittest
from unittest.mock import patch, mock_open, MagicMock
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup


class TestTaskFunc(unittest.TestCase):
    
    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_scraping_links(self, mock_file, mock_get):
        # Simulating a simple HTML response with 3 links
        mock_get.return_value.text = '''
        <html>
            <body>
                <a href="/link1">Link 1</a>
                <a href="/link2">Link 2</a>
                <a href="https://www.example.com/link3">Link 3</a>
            </body>
        </html>
        '''
        from my_module import task_func  # Assuming function is in my_module
        
        result = task_func('/mywebpage')
        
        self.assertEqual(result, 3)
        mock_file().write.assert_any_call(['https://www.example.com/link1'])
        mock_file().write.assert_any_call(['https://www.example.com/link2'])
        mock_file().write.assert_any_call(['https://www.example.com/link3'])

    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_handling_no_links(self, mock_file, mock_get):
        # Simulating an HTML response with no links
        mock_get.return_value.text = '<html><body></body></html>'
        from my_module import task_func
        
        result = task_func('/emptywebpage')
        
        self.assertEqual(result, 0)
        mock_file().write.assert_not_called()
    
    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_absolute_links_only(self, mock_file, mock_get):
        # Simulating mixed links in the response
        mock_get.return_value.text = '''
        <html>
            <body>
                <a href="https://www.example.com/link1">Link 1</a>
                <a href="/link2">Link 2</a>
                <a href="http://www.another.com/link3">Link 3</a>
            </body>
        </html>
        '''
        from my_module import task_func
        
        result = task_func('/mywebpage')
        
        self.assertEqual(result, 3)
        mock_file().write.assert_any_call(['https://www.example.com/link1'])
        mock_file().write.assert_any_call(['https://www.example.com/link2'])
        mock_file().write.assert_any_call(['http://www.another.com/link3'])
    
    @patch('requests.get')
    @patch('builtins.open', new_callable=mock_open)
    def test_duplicates_are_removed(self, mock_file, mock_get):
        # Simulating HTML with duplicate links
        mock_get.return_value.text = '''
        <html>
            <body>
                <a href="/link1">Link 1</a>
                <a href="/link1">Link 1 Duplicate</a>
                <a href="/link2">Link 2</a>
            </body>
        </html>
        '''
        from my_module import task_func
        
        result = task_func('/mywebpage')
        
        self.assertEqual(result, 2)
        mock_file().write.assert_any_call(['https://www.example.com/link1'])
        mock_file().write.assert_any_call(['https://www.example.com/link2'])

    @patch('requests.get')
    def test_invalid_url_handling(self, mock_get):
        # Simulating a network error
        mock_get.side_effect = requests.exceptions.RequestException
        
        from my_module import task_func
        
        with self.assertRaises(requests.exceptions.RequestException):
            task_func('/mywebpage')


if __name__ == '__main__':
    unittest.main()