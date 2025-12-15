import unittest
import os
import shutil

# Here is your prompt:
import re
import os
import string
import random

def task_func(input_string, directory='./text_files'):
    """
    Split a multi-line string into separate strings, remove special characters, and save each string as a separate text file.
    
    Parameters:
    - input_string (str): The multi-line string to be split and saved.
    - directory (str): The directory where the text files will be saved. Default is './text_files'.
    
    Returns:
    - file_paths (list): A list of file paths where the text is saved.
    
    Requirements:
    - re
    - os
    - string
    - random 
    
    Example:
    >>> task_func('line a\nfollows by line b\n...bye\n')
    ['./text_files/12345.txt', './text_files/67890.txt', './text_files/11223.txt']
    """

    lines = input_string.split('\n')
    file_paths = []
    for line in lines:
        line = re.sub('['+string.punctuation+']', '', line)
        filename = str(random.randint(10000, 99999)) + '.txt'
        filepath = os.path.join(directory, filename)
        file_paths.append(filepath)
        with open(filepath, 'w') as file:
            file.write(line)
    return file_paths


class TestTaskFunc(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.test_dir = './test_text_files'
        if not os.path.exists(cls.test_dir):
            os.makedirs(cls.test_dir)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    def test_empty_string(self):
        """Test passing an empty string to the function."""
        result = task_func('', self.test_dir)
        self.assertEqual(result, [])
        self.assertEqual(len(os.listdir(self.test_dir)), 0)

    def test_single_line_input(self):
        """Test passing a single line of text."""
        input_string = 'This is a test.'
        result = task_func(input_string, self.test_dir)
        self.assertEqual(len(result), 1)
        self.assertTrue(os.path.isfile(result[0]))
        with open(result[0], 'r') as file:
            content = file.read()
        self.assertEqual(content, 'This is a test')

    def test_multiple_lines_input(self):
        """Test passing multiple lines of text."""
        input_string = 'Line one.\nLine two!\nLine three?'
        result = task_func(input_string, self.test_dir)
        self.assertEqual(len(result), 3)
        for filepath in result:
            self.assertTrue(os.path.isfile(filepath))

    def test_special_characters_removal(self):
        """Test that special characters are removed from input."""
        input_string = 'Hello, World!\nThis... is a test@#$.'
        result = task_func(input_string, self.test_dir)
        self.assertEqual(len(result), 2)
        with open(result[0], 'r') as file:
            content1 = file.read()
        with open(result[1], 'r') as file:
            content2 = file.read()
        self.assertEqual(content1, 'Hello World')
        self.assertEqual(content2, 'This is a test')

    def test_directory_creation(self):
        """Test that files are created in the specified directory."""
        input_string = 'Line one.\nLine two.'
        result = task_func(input_string, self.test_dir)
        for filepath in result:
            self.assertTrue(filepath.startswith(self.test_dir))
            self.assertTrue(os.path.isfile(filepath))

if __name__ == '__main__':
    unittest.main()