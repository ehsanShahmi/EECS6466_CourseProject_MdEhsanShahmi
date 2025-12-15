import unittest
import os
import csv
from pathlib import Path

# Here is your prompt:
import re
import os
from pathlib import Path
import csv

def task_func(directory: str, pattern: str = r'^(.*?)-\d+\.csv$') -> list:

    """
    Processes CSV files in a directory based on a specified pattern and creates new files with altered names while preserving the content, you've laid out a solid foundation with your initial tests.

    Parameters:
    - directory (str): The path to the directory containing the CSV files to be processed. 
    - pattern (str, optional): A regular expression pattern that the filenames of interest should match.

    Returns:
    - new_files (list): A list of strings, where each string is the filename of a new CSV file created by the function.

    Requirements:
    - re
    - os
    - pathlib
    - csv

    Example:
    >>> task_func("/mnt/data/test_data")
    ['Shan.csv', 'Shannon.csv']
    """

           
    file_dir = Path(directory)
    file_pattern = re.compile(pattern)
    new_files = []
    
    for filename in os.listdir(file_dir):
        match = file_pattern.match(filename)
        if match is not None:
            prefix = match.group(1)
            new_filename = f'{prefix}.csv'
            with open(file_dir / filename, 'r') as infile, open(file_dir / new_filename, 'w') as outfile:
                reader = csv.reader(infile)
                writer = csv.writer(outfile)
                writer.writerows(reader)
            new_files.append(new_filename)
    
    return new_files

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.test_dir = Path('./test_data')
        self.test_dir.mkdir(exist_ok=True)

        # Create test CSV files
        self.csv_filenames = [
            'Shan-1.csv',
            'Shannon-2.csv',
            'InvalidFile.txt',
            'Shan-3.csv'
        ]
        for filename in self.csv_filenames:
            with open(self.test_dir / filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['header1', 'header2'])
                writer.writerow(['data1', 'data2'])

    def tearDown(self):
        # Clean up: remove files created
        for filename in os.listdir(self.test_dir):
            file_path = self.test_dir / filename
            if file_path.is_file():
                file_path.unlink()
        self.test_dir.rmdir()

    def test_basic_functionality(self):
        expected_files = ['Shan.csv', 'Shannon.csv']
        result = task_func(str(self.test_dir))
        self.assertCountEqual(result, expected_files)

    def test_invalid_file_extension(self):
        result = task_func(str(self.test_dir))
        self.assertNotIn('InvalidFile.csv', result)

    def test_no_matching_files(self):
        # Create a directory with non-matching files
        invalid_dir = Path('./invalid_data')
        invalid_dir.mkdir(exist_ok=True)
        with open(invalid_dir / 'no_match.txt', 'w') as f:
            f.write('This file should not be processed.')

        result = task_func(str(invalid_dir))
        self.assertEqual(result, [])
        invalid_dir.rmdir()

    def test_pattern_customization(self):
        customized_pattern = r'^(.*?)-\d+\.csv$'
        # Ensure we can provide a custom pattern and still match
        result = task_func(str(self.test_dir), pattern=customized_pattern)
        self.assertCountEqual(result, ['Shan.csv', 'Shannon.csv'])

    def test_preserving_content(self):
        task_func(str(self.test_dir))
        with open(self.test_dir / 'Shan.csv', 'r') as f:
            reader = csv.reader(f)
            content = list(reader)
            self.assertEqual(content, [['header1', 'header2'], ['data1', 'data2']])
        
        with open(self.test_dir / 'Shannon.csv', 'r') as f:
            reader = csv.reader(f)
            content = list(reader)
            self.assertEqual(content, [['header1', 'header2'], ['data1', 'data2']])

if __name__ == '__main__':
    unittest.main()