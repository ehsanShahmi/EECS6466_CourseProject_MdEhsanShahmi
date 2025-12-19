import unittest
import os
import tempfile
from pathlib import Path
import shutil

# Here is your prompt:
import shutil
from pathlib import Path
from typing import List

def task_func(source_dir: str, target_dir: str, extensions: List[str]) -> int:
    '''
    Move all files with certain extensions from one directory to another.

    Parameters:
    - source_dir (str): The directory containing the source files.
    - target_dir (str): The directory to which the files should be moved.
    - extensions (List[str]): The list of file extensions to be moved.

    Returns:
    int: The number of moved files.

    Raises:
    - ValueError: If source_dir or target_dir does not exist.

    Requirements:
    - shutil
    - pathlib.Path

    Example:
    >>> task_func('path/to/source/', 'path/to/target/', ['.jpg', '.png', '.gif'])
    15
    >>> task_func('path/to/source/', 'path/to/target/', ['.txt'])
    1
    ''' 
   
class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create temporary directories
        self.source_dir = tempfile.mkdtemp()
        self.target_dir = tempfile.mkdtemp()
        
        # Create test files
        self.test_files = ['test1.jpg', 'test2.png', 'document.txt', 'image.gif']
        for file_name in self.test_files:
            with open(os.path.join(self.source_dir, file_name), 'w') as f:
                f.write('test data')

    def tearDown(self):
        # Remove temporary directories
        shutil.rmtree(self.source_dir)
        shutil.rmtree(self.target_dir)

    def test_move_files_with_valid_extensions(self):
        moved_count = task_func(self.source_dir, self.target_dir, ['.jpg', '.png'])
        self.assertEqual(moved_count, 2)
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, 'test1.jpg')))
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, 'test2.png')))
    
    def test_move_files_with_single_valid_extension(self):
        moved_count = task_func(self.source_dir, self.target_dir, ['.txt'])
        self.assertEqual(moved_count, 1)
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, 'document.txt')))
    
    def test_no_files_moved_for_invalid_extension(self):
        moved_count = task_func(self.source_dir, self.target_dir, ['.pdf'])
        self.assertEqual(moved_count, 0)

    def test_raise_error_for_nonexistent_source_directory(self):
        with self.assertRaises(ValueError) as context:
            task_func('nonexistent/source', self.target_dir, ['.jpg'])
        self.assertEqual(str(context.exception), "source_dir does not exist.")
    
    def test_raise_error_for_nonexistent_target_directory(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.source_dir, 'nonexistent/target', ['.jpg'])
        self.assertEqual(str(context.exception), "target_dir does not exist.")

if __name__ == '__main__':
    unittest.main()