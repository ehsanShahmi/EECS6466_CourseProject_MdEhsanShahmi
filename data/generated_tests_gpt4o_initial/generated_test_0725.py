import unittest
import os
import codecs

# Here is your prompt:
import codecs
import os
import glob

# Constants
DIRECTORY_PATH = './files/'

def task_func(directory=DIRECTORY_PATH, from_encoding='cp1251', to_encoding='utf8'):
    """
    Convert the encoding of all text files in a specified directory from one encoding to another. 
    The function modifies the files in-place.
    
    Parameters:
    - directory (str): The directory where the text files are located. Default is './files/'.
    - from_encoding (str): The original encoding of the text files. Default is 'cp1251'.
    - to_encoding (str): The encoding to which the text files should be converted. Default is 'utf8'.
    
    Returns:
    - None
    
    Requirements:
    - codecs
    - os
    - glob
    
    Example:
    >>> task_func('./files/', 'cp1251', 'utf8')  # Converts all .txt files in './files/' from 'cp1251' to 'utf8'
    >>> task_func('./other_files/', 'utf8', 'ascii')  # Converts all .txt files in './other_files/' from 'utf8' to 'ascii'
    """
    for filename in glob.glob(os.path.join(directory, '*.txt')):
        with codecs.open(filename, 'r', from_encoding) as file:
            content = file.read()

        with codecs.open(filename, 'w', to_encoding) as file:
            file.write(content)

class TestEncodingConversion(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Set up a temporary directory for testing
        cls.test_dir = './files/'
        if not os.path.exists(cls.test_dir):
            os.makedirs(cls.test_dir)
        # Create test files with various encodings
        cls.create_test_file('test1.txt', 'Hello, World!', 'cp1251')
        cls.create_test_file('test2.txt', 'Привет, мир!', 'utf16')

    @classmethod
    def tearDownClass(cls):
        # Clean up test files
        for filename in glob.glob(os.path.join(cls.test_dir, '*.txt')):
            os.remove(filename)
        os.rmdir(cls.test_dir)
    
    @classmethod
    def create_test_file(cls, filename, content, encoding):
        with codecs.open(os.path.join(cls.test_dir, filename), 'w', encoding=encoding) as f:
            f.write(content)

    def test_conversion_cp1251_to_utf8(self):
        task_func(self.test_dir, 'cp1251', 'utf8')
        with codecs.open(os.path.join(self.test_dir, 'test1.txt'), 'r', 'utf8') as f:
            content = f.read()
        self.assertEqual(content, 'Hello, World!')

    def test_conversion_utf16_to_utf8(self):
        task_func(self.test_dir, 'utf16', 'utf8')
        with codecs.open(os.path.join(self.test_dir, 'test2.txt'), 'r', 'utf8') as f:
            content = f.read()
        self.assertEqual(content, 'Привет, мир!')

    def test_no_files_in_directory(self):
        empty_dir = './empty_directory/'
        if not os.path.exists(empty_dir):
            os.makedirs(empty_dir)
        task_func(empty_dir, 'cp1251', 'utf8')
        self.assertEqual(len(glob.glob(os.path.join(empty_dir, '*.txt'))), 0)
        os.rmdir(empty_dir)

    def test_conversion_non_existent_file(self):
        task_func(self.test_dir, 'nonexistent_encoding', 'utf8')
        with self.assertRaises(LookupError):
            with codecs.open(os.path.join(self.test_dir, 'test1.txt'), 'r', 'nonexistent_encoding') as f:
                f.read()

    def test_conversion_to_non_utf_encoding(self):
        task_func(self.test_dir, 'utf8', 'ascii')
        with codecs.open(os.path.join(self.test_dir, 'test1.txt'), 'r', 'ascii') as f:
            content = f.read()
        self.assertEqual(content, 'Hello, World!')    

if __name__ == '__main__':
    unittest.main()