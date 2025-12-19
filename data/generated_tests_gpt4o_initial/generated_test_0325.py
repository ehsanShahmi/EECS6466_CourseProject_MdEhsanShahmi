import unittest
import os
import tempfile
from pathlib import Path
import glob

# Here is your prompt:
# import re
# import os
# from pathlib import Path
# import glob

# def task_func(directory_path: str, regex_pattern: str = r'\\(.+?\\)|\\w') -> dict:
#     """
#     Extracts matches from all text files in a specified directory based on a regular expression pattern. 
#     It captures whatever is between parentheses as a single match, and any character outside the parentheses 
#     as individual matches in the string.

#     Parameters:
#     - directory_path (str): The path to the directory containing the text files.
#     - regex_pattern (str): The regular expression pattern to use for matching. Defaults to REGEX_PATTERN.

#     Returns:
#     - dict: A dictionary where keys are file names (without path) and values are lists of matches extracted from the files.

#     Requirements:
#     - Utilizes libraries: re, os, pathlib.Path, and glob.glob

#     Example:
#     >>> matches = task_func('/path/to/directory') # Test with fictional directory path
#     >>> print(matches)
#     {}
#     """

#                # Constants
#     FILE_PATTERN = '*.txt'
#     match_dict = {}
#     file_paths = glob.glob(os.path.join(directory_path, FILE_PATTERN))
#     for file_path in file_paths:
#         with open(file_path, 'r') as file:
#             content = file.read()
#             matches = re.findall(regex_pattern, content)
#             match_dict[Path(file_path).name] = matches

#     return match_dict


class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.TemporaryDirectory()
        
    def tearDown(self):
        # Cleanup temporary directory
        self.test_dir.cleanup()

    def test_empty_directory(self):
        # Test with an empty directory
        result = task_func(self.test_dir.name)
        self.assertEqual(result, {})

    def test_text_file_no_matches(self):
        # Create a text file with content that does not match the regex
        with open(os.path.join(self.test_dir.name, 'test1.txt'), 'w') as f:
            f.write("This is a test without special characters.")
        result = task_func(self.test_dir.name)
        self.assertEqual(result, {'test1.txt': []})

    def test_text_file_with_matches(self):
        # Create a text file with content that has matches
        with open(os.path.join(self.test_dir.name, 'test2.txt'), 'w') as f:
            f.write("Some text with (matches) and other text.")
        result = task_func(self.test_dir.name)
        self.assertIn('test2.txt', result)
        self.assertIn(['matches'], result['test2.txt'])

    def test_multiple_text_files(self):
        # Create multiple text files
        with open(os.path.join(self.test_dir.name, 'test3.txt'), 'w') as f:
            f.write("First file with (match1).")
        with open(os.path.join(self.test_dir.name, 'test4.txt'), 'w') as f:
            f.write("Second file with (match2) and (match3).")
        result = task_func(self.test_dir.name)
        self.assertEqual(len(result), 2)
        self.assertIn('test3.txt', result)
        self.assertIn('test4.txt', result)
        self.assertIn(['match1'], result['test3.txt'])
        self.assertIn(['match2', 'match3'], result['test4.txt'])

    def test_file_with_special_characters(self):
        # Create a text file with special characters
        with open(os.path.join(self.test_dir.name, 'test5.txt'), 'w') as f:
            f.write("Special characters (hello@world) and more.")
        result = task_func(self.test_dir.name)
        self.assertIn('test5.txt', result)
        self.assertIn(['hello@world'], result['test5.txt'])


if __name__ == '__main__':
    unittest.main()