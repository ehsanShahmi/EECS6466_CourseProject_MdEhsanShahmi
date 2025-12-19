import os
import glob
import csv
import unittest
from unittest.mock import mock_open, patch

# Here is your prompt:
import os
import glob
import csv

def task_func(directory_path, file_extension='.csv'):
    """
    Reads all files with a specified extension in a given directory and returns their data in a dictionary.
    - Reads all files with the specified extension in the given directory.
    - Uses the filename without the extension as a key in the output dictionary.
    - The value for each key is a list of rows from the file, where each row is represented as a list of values.

    Parameters:
    - directory_path (str): The path to the directory containing the files.
    - file_extension (str, optional): The file extension to look for. Default is '.csv'.

    Returns:
    - Returns a dictionary where each key is the filename (without extension) and the value is a list of rows from the file.

    Requirements:
    - os
    - glob
    - csv

    Example:
    >>> data = task_func('/home/user/data')
    >>> print(data['file1'])
    [['header1', 'header2'], ['row1_col1', 'row1_col2'], ['row2_col1', 'row2_col2']]
    
    >>> data = task_func('/home/user/data', '.txt')
    >>> print(data)
    {}
    """

    data = {}

    for file in glob.glob(os.path.join(directory_path, '*' + file_extension)):
        filename = os.path.splitext(os.path.basename(file))[0]
        with open(file, 'r') as f:
            reader = csv.reader(f)
            data[filename] = list(reader)

    return data

class TestTaskFunc(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='header1,header2\nrow1_col1,row1_col2\nrow2_col1,row2_col2')
    @patch('glob.glob', return_value=['/fake/path/file1.csv'])
    def test_single_csv_file(self, mock_glob, mock_open):
        expected = {'file1': [['header1', 'header2'], ['row1_col1', 'row1_col2'], ['row2_col1', 'row2_col2']]}
        result = task_func('/fake/path')
        self.assertEqual(result, expected)

    @patch('builtins.open', new_callable=mock_open, read_data='header1;header2\nrow1_col1;row1_col2\nrow2_col1;row2_col2')
    @patch('glob.glob', return_value=['/fake/path/file2.csv'])
    def test_semicolon_in_csv(self, mock_glob, mock_open):
        expected = {'file2': [['header1;header2'], ['row1_col1;row1_col2'], ['row2_col1;row2_col2']]}
        result = task_func('/fake/path')
        self.assertEqual(result, expected)

    @patch('glob.glob', return_value=[])
    def test_no_files_found(self, mock_glob):
        result = task_func('/fake/path')
        self.assertEqual(result, {})

    @patch('builtins.open', new_callable=mock_open, read_data='col1,col2\ndata1,data2\n')
    @patch('glob.glob', side_effect=[['/fake/path/file3.csv'], ['/fake/path/file4.csv']])
    def test_multiple_csv_files(self, mock_glob, mock_open):
        mock_open.side_effect = [
            mock_open(read_data='col1,col2\ndata1,data2\n').return_value,
            mock_open(read_data='headerA,headerB\nvalue1,value2\n').return_value
        ]
        
        expected = {
            'file3': [['col1', 'col2'], ['data1', 'data2']],
            'file4': [['headerA', 'headerB'], ['value1', 'value2']],
        }
        result = task_func('/fake/path')
        self.assertEqual(result, expected)

    @patch('glob.glob', return_value=['/fake/path/file5.txt'])
    def test_different_file_extension(self, mock_glob):
        result = task_func('/fake/path', '.txt')
        self.assertEqual(result, {})  # Expecting empty dict since .txt file is not to be processed


if __name__ == '__main__':
    unittest.main()