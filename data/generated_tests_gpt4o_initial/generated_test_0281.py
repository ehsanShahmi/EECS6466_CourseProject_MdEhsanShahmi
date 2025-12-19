import os
import tempfile
import unittest
from collections import Counter

# This is the provided prompt that we will not modify.
def task_func(folder_path: str) -> dict:
    """
    Scan a directory for log files and count the occurrences of each IP address in all files.
    
    Parameters:
    - folder_path (str): The path to the directory containing log files to be scanned.
    
    Returns:
    dict: A dictionary with IP addresses as keys and their counts as values.
    
    Requirements:
    - re
    - os
    - collections.Counter
    
    The function utilizes a regular expression pattern to identify IP addresses in the log files.
    
    Example:
    >>> import tempfile
    >>> temp_dir = tempfile.mkdtemp() # Create a temporary directory that is empty
    >>> task_func(temp_dir)
    {}
    """

    import re
    IP_REGEX = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
    counter = Counter()
    for filename in os.listdir(folder_path):
        if filename.endswith('.log'):
            with open(os.path.join(folder_path, filename)) as file:
                content = file.read()
                ips = re.findall(IP_REGEX, content)
                counter.update(ips)
    return dict(counter)

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        """Create a temporary directory for testing."""
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        """Remove the temporary directory after tests."""
        for filename in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, filename))
        os.rmdir(self.test_dir)
    
    def test_empty_directory(self):
        """Test with an empty directory."""
        result = task_func(self.test_dir)
        self.assertEqual(result, {})
    
    def test_single_log_file_single_ip(self):
        """Test with a single log file containing a single IP address."""
        log_content = "192.168.1.1 - - [12/Dec/2021:12:30:00 +0000] \"GET / HTTP/1.1\" 200 2326"
        with open(os.path.join(self.test_dir, 'test1.log'), 'w') as f:
            f.write(log_content)
        result = task_func(self.test_dir)
        self.assertEqual(result, {'192.168.1.1': 1})

    def test_multiple_log_files_multiple_ips(self):
        """Test with multiple log files containing multiple IP addresses."""
        log_content1 = "192.168.1.1 - - [12/Dec/2021:12:30:00 +0000] \"GET / HTTP/1.1\" 200 2326"
        log_content2 = "10.0.0.1 - - [12/Dec/2021:12:31:00 +0000] \"GET /index.html HTTP/1.1\" 200 2326"
        with open(os.path.join(self.test_dir, 'test1.log'), 'w') as f:
            f.write(log_content1)
        with open(os.path.join(self.test_dir, 'test2.log'), 'w') as f:
            f.write(log_content2)
        result = task_func(self.test_dir)
        self.assertEqual(result, {'192.168.1.1': 1, '10.0.0.1': 1})

    def test_log_file_with_multiple_ip_counts(self):
        """Test log file containing multiple occurrences of the same IP address."""
        log_content = "192.168.1.1 - - [12/Dec/2021:12:30:00 +0000] \"GET / HTTP/1.1\" 200 2326\n"
        log_content += "192.168.1.1 - - [12/Dec/2021:12:30:01 +0000] \"GET / HTTP/1.1\" 200 2326"
        with open(os.path.join(self.test_dir, 'test1.log'), 'w') as f:
            f.write(log_content)
        result = task_func(self.test_dir)
        self.assertEqual(result, {'192.168.1.1': 2})

if __name__ == '__main__':
    unittest.main()