import os
import re
import pandas as pd
import unittest
from unittest.mock import patch, mock_open

def task_func(pattern: str, directory: str, output_csv: str) -> pd.DataFrame:
    """
    Searches for files in the specified directory that match a given regex pattern.
    This function walks through the directory, matches filenames against the pattern,
    and saves the matched file paths to a CSV file. It returns a DataFrame of these paths
    with colomn 'File Path'.

    Parameters:
    - pattern (str): Regex pattern to match filenames.
    - directory (str): Directory to search for files.
    - output_csv (str): CSV file path to save matched file paths.

    Returns:
    - pd.DataFrame: DataFrame with a single column 'File Path' of matched paths.
    """
    matched_paths = []
    for root, _, files in os.walk(directory):
        for file in files:
            if re.match(pattern, file):
                matched_paths.append(os.path.join(root, file))

    df = pd.DataFrame(matched_paths, columns=['File Path'])
    df.to_csv(output_csv, index=False)

    return df

class TestTaskFunction(unittest.TestCase):

    @patch("os.walk")
    def test_match_txt_files(self, mock_walk):
        mock_walk.return_value = [
            ('/path/to/search', ('subdir',), ('file1.txt', 'file2.jpeg')),
        ]
        expected_df = pd.DataFrame({'File Path': ['/path/to/search/file1.txt']})
        
        result_df = task_func(r'.*\.txt$', '/path/to/search', 'matched_files.csv')
        
        pd.testing.assert_frame_equal(result_df, expected_df)

    @patch("os.walk")
    def test_match_png_files(self, mock_walk):
        mock_walk.return_value = [
            ('/path/to/search', ('subdir',), ('file1.png', 'file2.txt')),
        ]
        expected_df = pd.DataFrame({'File Path': ['/path/to/search/file1.png']})
        
        result_df = task_func(r'.*\.png$', '/path/to/search', 'matched_files.csv')
        
        pd.testing.assert_frame_equal(result_df, expected_df)

    @patch("os.walk")
    def test_no_matching_files(self, mock_walk):
        mock_walk.return_value = [
            ('/path/to/search', ('subdir',), ('file1.docx', 'file2.jpeg')),
        ]
        expected_df = pd.DataFrame(columns=['File Path'])

        result_df = task_func(r'.*\.txt$', '/path/to/search', 'matched_files.csv')

        pd.testing.assert_frame_equal(result_df, expected_df)

    @patch("os.walk")
    def test_complex_pattern_matching(self, mock_walk):
        mock_walk.return_value = [
            ('/path/to/search', ('subdir',), ('file1.txt', 'file2.doc', 'image.png', 'file1.txt.backup')),
        ]
        expected_df = pd.DataFrame({'File Path': ['/path/to/search/file1.txt', '/path/to/search/file1.txt.backup']})
        
        result_df = task_func(r'file1\.txt.*$', '/path/to/search', 'matched_files.csv')
        
        pd.testing.assert_frame_equal(result_df, expected_df)

    @patch("os.walk")
    @patch("pandas.DataFrame.to_csv")
    def test_csv_save_called(self, mock_to_csv, mock_walk):
        mock_walk.return_value = [
            ('/path/to/search', ('subdir',), ('file1.txt',)),
        ]

        task_func(r'.*\.txt$', '/path/to/search', 'matched_files.csv')
        
        mock_to_csv.assert_called_once_with('matched_files.csv', index=False)

if __name__ == '__main__':
    unittest.main()