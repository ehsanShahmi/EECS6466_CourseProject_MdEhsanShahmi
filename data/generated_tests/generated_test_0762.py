import unittest
import os
import zipfile
import codecs

# Here is your prompt:
import codecs
import os
import zipfile


def task_func(directory_name="latin_files",
          content='Sopetón',
          file_names=['file1.txt', 'file2.txt', 'file3.txt'],
          encoding="latin-1"):
    '''
    Create a directory with the given name, create specified .txt files. Encode
    the content using the specified encoding and write it into all .txt files, 
    then zip the directory. 

    Args:
    directory_name (str): The name of the directory to be created.
    content (str, optional): The content which should be written to each .txt file.
                             Defaults to 'Sopetón'.
    file_names (list): List of .txt file names to be created.
                       Defaults to ['file1.txt', 'file2.txt', 'file3.txt'].
    encoding (str): The encoding type for the files. Default is 'latin-1'.

    Returns:
    str: The zipped file name.

    Requirements:
    - codecs
    - os
    - zipfile

    Example:
    >>> zipped_file = task_func("latin_files", "test", ["file1.txt", "file2.txt", "file3.txt"])
    >>> print(zipped_file)
    latin_files.zip

    >>> zipped_file = task_func(directory_name="directorio", content='hi', file_names=["custom1.txt", "custom2.txt"], encoding='utf-8')
    >>> print(zipped_file)
    directorio.zip
    '''

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.test_directory = "test_latin_files"
    
    def tearDown(self):
        for file in os.listdir(self.test_directory):
            os.remove(os.path.join(self.test_directory, file))
        os.rmdir(self.test_directory)
    
    def test_default_functionality(self):
        expected_zip = task_func(self.test_directory)
        self.assertTrue(os.path.isfile(expected_zip))
        self.assertTrue(zipfile.is_zipfile(expected_zip))

    def test_custom_content(self):
        content = "Hello World"
        expected_zip = task_func(self.test_directory, content=content)
        with zipfile.ZipFile(expected_zip, 'r') as zipf:
            file_list = zipf.namelist()
            for filename in file_list:
                with zipf.open(filename) as f:
                    file_content = f.read().decode('latin-1')
                    self.assertEqual(file_content, content)

    def test_multiple_files_created(self):
        file_names = ["test1.txt", "test2.txt"]
        expected_zip = task_func(self.test_directory, file_names=file_names)
        with zipfile.ZipFile(expected_zip, 'r') as zipf:
            self.assertEqual(sorted(zipf.namelist()), sorted(file_names))

    def test_encoding(self):
        content = "Sopetón"
        expected_zip = task_func(self.test_directory, content=content, encoding="utf-8")
        with zipfile.ZipFile(expected_zip, 'r') as zipf:
            file_list = zipf.namelist()
            for filename in file_list:
                with zipf.open(filename) as f:
                    file_content = f.read().decode('utf-8')
                    self.assertEqual(file_content, content)

    def test_directory_creation(self):
        expected_zip = task_func(self.test_directory)
        self.assertTrue(os.path.isdir(self.test_directory))

if __name__ == '__main__':
    unittest.main()