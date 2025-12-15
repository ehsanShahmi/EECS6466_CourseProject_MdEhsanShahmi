import os
import shutil
import unittest

# Here is your prompt:
import os
import shutil

def task_func(src_dir, dest_dir, extension):
    """
    Move all files with a particular extension from one directory to another.

    Parameters:
    - src_dir (str): The source directory.
    - dest_dir (str): The destination directory.
    - extension (str): The file extension.

    Returns:
    - files_moved (int): The number of files moved.

    Requirements:
    - os
    - shutil

    Example:
    >>> task_func('/path/to/src', '/path/to/dest', '.txt')
    """

    files_moved = 0

    for file_name in os.listdir(src_dir):
        if file_name.endswith(extension):
            shutil.move(os.path.join(src_dir, file_name), os.path.join(dest_dir, file_name))
            files_moved += 1

    return files_moved

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.src_dir = 'test_src'
        self.dest_dir = 'test_dest'
        os.makedirs(self.src_dir, exist_ok=True)
        os.makedirs(self.dest_dir, exist_ok=True)

        # Create test files in the source directory
        with open(os.path.join(self.src_dir, 'file1.txt'), 'w') as f:
            f.write('This is a test file 1.')
        with open(os.path.join(self.src_dir, 'file2.txt'), 'w') as f:
            f.write('This is a test file 2.')
        with open(os.path.join(self.src_dir, 'file3.jpg'), 'w') as f:
            f.write('This is an image file.')

    def tearDown(self):
        # Clean up created directories and files after each test
        shutil.rmtree(self.src_dir)
        shutil.rmtree(self.dest_dir)

    def test_move_txt_files(self):
        moved_files = task_func(self.src_dir, self.dest_dir, '.txt')
        self.assertEqual(moved_files, 2)
        self.assertTrue(os.path.exists(os.path.join(self.dest_dir, 'file1.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.dest_dir, 'file2.txt')))
        self.assertFalse(os.path.exists(os.path.join(self.src_dir, 'file1.txt')))
        self.assertFalse(os.path.exists(os.path.join(self.src_dir, 'file2.txt')))

    def test_move_no_files(self):
        moved_files = task_func(self.src_dir, self.dest_dir, '.png')
        self.assertEqual(moved_files, 0)

    def test_move_files_with_different_extension(self):
        moved_files = task_func(self.src_dir, self.dest_dir, '.jpg')
        self.assertEqual(moved_files, 1)
        self.assertTrue(os.path.exists(os.path.join(self.dest_dir, 'file3.jpg')))
        self.assertFalse(os.path.exists(os.path.join(self.src_dir, 'file3.jpg')))

    def test_move_files_to_non_existent_directory(self):
        invalid_dest_dir = 'non_existent_dest'
        moved_files = task_func(self.src_dir, invalid_dest_dir, '.txt')
        self.assertEqual(moved_files, 0)  # Should not move any files, as destination is invalid

if __name__ == '__main__':
    unittest.main()