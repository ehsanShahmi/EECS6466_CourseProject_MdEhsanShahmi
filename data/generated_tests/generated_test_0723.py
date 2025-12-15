import unittest
import os
import urllib.request

# Here is your prompt:
import urllib.request
from bs4 import BeautifulSoup
import csv
import os

# Constants
CSV_FILE_PATH = 'scraped_data.csv'

def task_func(url):
    """
    Scrape data from a given URL and save the scraped data to a CSV file.

    Parameters:
    - url (str): The URL to scrape data from.

    Returns:
    - CSV_FILE_PATH (str): The path of the CSV file where the scraped data is saved.

    Requirements:
    - urllib
    - bs4
    - csv
    - os

    Example:
    >>> task_func('http://www.example.com/')
    'scraped_data.csv'
    """

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')

    data = []
    table = soup.find('table', attrs={'class':'data-table'})
    table_rows = table.find_all('tr')

    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text for tr in td]
        data.append(row)
    
    if os.path.exists(CSV_FILE_PATH):
        os.remove(CSV_FILE_PATH)

    with open(CSV_FILE_PATH, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    
    return CSV_FILE_PATH

class TestTaskFunc(unittest.TestCase):

    def test_valid_url(self):
        url = 'http://www.example.com/'
        result = task_func(url)
        self.assertEqual(result, 'scraped_data.csv')
        self.assertTrue(os.path.exists('scraped_data.csv'))

    def test_nonexistent_url(self):
        url = 'http://www.nonexistentwebsite.com/'
        with self.assertRaises(urllib.error.URLError):
            task_func(url)

    def test_csv_file_creation(self):
        url = 'http://www.example.com/'
        task_func(url)
        self.assertTrue(os.path.isfile('scraped_data.csv'))
        os.remove('scraped_data.csv')  # Clean up after the test

    def test_csv_file_content(self):
        url = 'http://www.example.com/'
        task_func(url)
        with open('scraped_data.csv', 'r') as f:
            reader = csv.reader(f)
            content = list(reader)
            self.assertGreater(len(content), 0)  # Ensure there is some content
        os.remove('scraped_data.csv')  # Clean up after the test

    def test_csv_file_overwrite(self):
        url = 'http://www.example.com/'
        task_func(url)
        content_before = []
        with open('scraped_data.csv', 'r') as f:
            reader = csv.reader(f)
            content_before = list(reader)
        
        # Call the function again to overwrite
        task_func(url)
        content_after = []
        with open('scraped_data.csv', 'r') as f:
            reader = csv.reader(f)
            content_after = list(reader)
        
        # Ensure that the content is still there (for demonstration, we expect data to be the same)
        self.assertEqual(content_before, content_after)  # In real case, this may not hold.

if __name__ == '__main__':
    unittest.main()