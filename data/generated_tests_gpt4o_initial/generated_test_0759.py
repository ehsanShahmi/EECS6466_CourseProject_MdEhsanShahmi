import os
import unittest

# Here is your prompt:
import os
import shutil
import fnmatch

def task_func(source_directory, destination_directory, file_pattern):
    """
    Moves all files that match a particular pattern from one directory to another.
    
    Functionality:
    - Moves files from 'source_directory' to 'destination_directory' based on a filename pattern 'file_pattern'.
    
    Parameters:
    - source_directory (str): The path to the source directory from which files will be moved.
    - destination_directory (str): The path to the destination directory to which files will be moved.
    - file_pattern (str): The file pattern to match (e.g., '*.txt' for all text files).
    
    Returns:
    - Returns a list of filenames that were moved.
    
    Requirements:
    - os
    - shutil
    - fnmatch
    
    Example:
    >>> task_func('/path/to/source', '/path/to/destination', '*.txt')
    ['task_func_data/file1.txt', 'task_func_data/file2.txt']
    """

    moved_files = []
    for path, dirs, files in os.walk(source_directory):
        for filename in fnmatch.filter(files, file_pattern):
            shutil.move(os.path.join(path, filename), os.path.join(destination_directory, filename))
            moved_files.append(filename)
    return moved_files

class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        """Create temporary directories and test files for the tests."""
        self.source_directory = 'test_source'
        self.destination_directory = 'test_destination'
        os.makedirs(self.source_directory, exist_ok=True)
        os.makedirs(self.destination_directory, exist_ok=True)
        # Create sample files
        with open(os.path.join(self.source_directory, 'file1.txt'), 'w') as f:
            f.write('Sample file 1')
        with open(os.path.join(self.source_directory, 'file2.txt'), 'w') as f:
            f.write('Sample file 2')
        with open(os.path.join(self.source_directory, 'file3.jpg'), 'w') as f:
            f.write('Sample image file')

    def tearDown(self):
        """Remove temporary directories and files after tests."""
        shutil.rmtree(self.source_directory, ignore_errors=True)
        shutil.rmtree(self.destination_directory, ignore_errors=True)

    def test_move_txt_files(self):
        """Test moving .txt files from source to destination directory."""
        moved_files = task_func(self.source_directory, self.destination_directory, '*.txt')
        self.assertEqual(sorted(moved_files), sorted(['file1.txt', 'file2.txt']))
        self.assertTrue(all(os.path.exists(os.path.join(self.destination_directory, f)) for f in moved_files))

    def test_move_non_existent_files(self):
        """Test behavior when moving non-existent file types."""
        moved_files = task_func(self.source_directory, self.destination_directory, '*.png')
        self.assertEqual(moved_files, [])
        self.assertEqual(len(os.listdir(self.destination_directory)), 0)

    def test_move_files_with_no_matching_pattern(self):
        """Test moving files with a pattern that matches no files."""
        moved_files = task_func(self.source_directory, self.destination_directory, '*.pdf')
        self.assertEqual(moved_files, [])
        self.assertEqual(len(os.listdir(self.destination_directory)), 0)

    def test_move_files_with_mixed_patterns(self):
        """Test moving .txt files while .jpg files remain untouched."""
        moved_files = task_func(self.source_directory, self.destination_directory, '*.txt')
        self.assertEqual(sorted(moved_files), sorted(['file1.txt', 'file2.txt']))
        self.assertEqual(len(os.listdir(self.source_directory)), 1)  # Only file3.jpg should remain

    def test_source_directory_empty_after_move(self):
        """Test that the source directory is empty after moving all matching files."""
        task_func(self.source_directory, self.destination_directory, '*.txt')
        self.assertEqual(len(os.listdir(self.source_directory)), 1)  # Only file3.jpg should remain

if __name__ == '__main__':
    unittest.main()