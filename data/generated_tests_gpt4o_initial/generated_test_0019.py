import os
import unittest

# Here is your prompt:
import os
import glob
import zipfile

def task_func(directory):
    """
    Zips all files (not including subdirectories) located in the specified directory and returns the path to the created zip file.
    
    Parameters:
    directory (str): The directory path containing the files to be zipped.
    
    Returns:
    str: The path to the generated zip file. Returns None if the directory does not contain any files.
    
    Raises:
    FileNotFoundError: if the specified directory does not exist

    Requirements:
    - os
    - glob
    - zipfile
    
    Notes:
    - The zip name is always 'files.zip'

    Example:
    >>> path = task_func('/path/to/files')
    >>> isinstance(path, str)
    True
    """

    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' not found.")
    files = [f for f in glob.glob(os.path.join(directory, '*')) if os.path.isfile(f)]
    if not files:
        return None
    zip_file_path = os.path.join(directory, 'files.zip')
    with zipfile.ZipFile(zip_file_path, 'w') as zipf:
        for file in files:
            zipf.write(file, os.path.basename(file))
    
    return zip_file_path


class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.test_dir = 'test_directory'
        self.empty_dir = 'empty_directory'
        os.makedirs(self.test_dir, exist_ok=True)
        os.makedirs(self.empty_dir, exist_ok=True)
        self.test_file_path = os.path.join(self.test_dir, 'test_file.txt')
        with open(self.test_file_path, 'w') as f:
            f.write('This is a test file.')

    def tearDown(self):
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
        os.rmdir(self.test_dir)
        os.rmdir(self.empty_dir)

    def test_zip_creation(self):
        zip_path = task_func(self.test_dir)
        self.assertTrue(os.path.exists(zip_path))
        self.assertTrue(zip_path.endswith('files.zip'))

    def test_zip_empty_directory(self):
        zip_path = task_func(self.empty_dir)
        self.assertIsNone(zip_path)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_directory')

    def test_zip_contains_files(self):
        task_func(self.test_dir)
        with zipfile.ZipFile(os.path.join(self.test_dir, 'files.zip'), 'r') as zipf:
            file_list = zipf.namelist()
            self.assertIn('test_file.txt', file_list)

    def test_zip_without_subdirectories(self):
        sub_dir = os.path.join(self.test_dir, 'sub_directory')
        os.makedirs(sub_dir)
        with open(os.path.join(sub_dir, 'sub_file.txt'), 'w') as f:
            f.write('This is a subdirectory file.')
        
        zip_path = task_func(self.test_dir)
        with zipfile.ZipFile(zip_path, 'r') as zipf:
            file_list = zipf.namelist()
            self.assertNotIn('sub_directory/sub_file.txt', file_list)


if __name__ == '__main__':
    unittest.main()