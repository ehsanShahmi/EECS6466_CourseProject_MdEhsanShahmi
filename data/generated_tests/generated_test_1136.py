import unittest
import os
import csv

class TestTaskFunction(unittest.TestCase):
    
    def test_default_functionality(self):
        """Test the function with default parameters."""
        from your_module import task_func  # Replace "your_module" with the actual module name
        result = task_func()
        self.assertEqual(result, 'emails.csv')
        self.assertTrue(os.path.exists('emails.csv'))
        with open('emails.csv', newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(header, ['Emails'])
    
    def test_custom_url(self):
        """Test the function with a custom URL."""
        from your_module import task_func  # Replace "your_module" with the actual module name
        result = task_func(url="http://another-example.com", csv_path="another_emails.csv")
        self.assertEqual(result, 'another_emails.csv')
        self.assertTrue(os.path.exists('another_emails.csv'))
        with open('another_emails.csv', newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(header, ['Emails'])

    def test_empty_email_csv(self):
        """Test the function when no emails are found on the page."""
        from your_module import task_func  # Replace "your_module" with the actual module name
        result = task_func(url="http://httpbin.org/status/200", csv_path="empty_emails.csv")
        self.assertEqual(result, 'empty_emails.csv')
        self.assertTrue(os.path.exists('empty_emails.csv'))
        with open('empty_emails.csv', newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(header, ['Emails'])
            emails = list(reader)
            self.assertEqual(emails, [])
    
    def test_invalid_url(self):
        """Test the function with an invalid URL."""
        from your_module import task_func  # Replace "your_module" with the actual module name
        with self.assertRaises(requests.exceptions.RequestException):
            task_func(url="http://invalid-url")

    def test_custom_regex(self):
        """Test the function with a custom regex pattern."""
        from your_module import task_func  # Replace "your_module" with the actual module name
        valid_url = "http://test.com/valid_emails"
        result = task_func(url=valid_url, csv_path="custom_regex_emails.csv", regex=r'\b[A-Za-z0-9._%+-]+@test\.com\b')
        self.assertEqual(result, 'custom_regex_emails.csv')
        self.assertTrue(os.path.exists('custom_regex_emails.csv'))
        with open('custom_regex_emails.csv', newline='') as f:
            reader = csv.reader(f)
            header = next(reader)
            self.assertEqual(header, ['Emails'])
            # add more specific assertions depending on the expected valid emails from the test URL

if __name__ == '__main__':
    unittest.main()