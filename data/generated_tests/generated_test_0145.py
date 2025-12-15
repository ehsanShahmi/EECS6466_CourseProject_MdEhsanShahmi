import csv
import os
import unittest
from ipaddress import IPv4Network

def task_func(ip_range, csv_path):
    """
    Generates a CSV file listing all IP addresses in the specified IP range.
    Each IP address is written as a row in the CSV file.

    Requirements:
    - csv
    - ipaddress.IPv4Network

    Parameters:
        ip_range (str): The IP range in CIDR notation (e.g., "192.168.0.0/16").
        csv_path (str): The path where the CSV file will be saved.

    Returns:
        str: The path to the generated CSV file.

    Examples:
    >>> csv_path = task_func('192.168.0.0/16', 'file.csv')
    >>> isinstance(csv_path, str)
    True
    >>> csv_path.endswith('.csv')
    True
    """

    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['IP Address']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for ip in IPv4Network(ip_range):
            writer.writerow({'IP Address': str(ip)})

    return csv_path

class TestTaskFunc(unittest.TestCase):

    def test_valid_ip_range(self):
        csv_path = 'test_valid_ip_range.csv'
        result = task_func('192.168.0.0/30', csv_path)
        self.assertEqual(result, csv_path)
        self.assertTrue(os.path.isfile(csv_path))
        
        # Clean up
        os.remove(csv_path)

    def test_multiple_ips_in_csv(self):
        csv_path = 'test_multiple_ips_in_csv.csv'
        task_func('192.168.1.0/29', csv_path)
        
        with open(csv_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            ips = [row['IP Address'] for row in reader]
        
        expected_ips = ['192.168.1.0', '192.168.1.1', '192.168.1.2', '192.168.1.3', 
                        '192.168.1.4', '192.168.1.5', '192.168.1.6', '192.168.1.7']
        
        self.assertEqual(ips, expected_ips)
        
        # Clean up
        os.remove(csv_path)

    def test_invalid_ip_range(self):
        csv_path = 'test_invalid_ip_range.csv'
        with self.assertRaises(ValueError):
            task_func('999.999.999.999/16', csv_path)

    def test_empty_csv_file(self):
        csv_path = 'test_empty_csv_file.csv'
        result = task_func('192.168.2.0/32', csv_path)

        self.assertEqual(result, csv_path)
        
        with open(csv_path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['IP Address'], '192.168.2.0')

        # Clean up
        os.remove(csv_path)

    def test_csv_file_creation(self):
        csv_path = 'test_csv_file_creation.csv'
        task_func('10.0.0.0/24', csv_path)

        self.assertTrue(os.path.isfile(csv_path))

        # Clean up
        os.remove(csv_path)

if __name__ == '__main__':
    unittest.main()