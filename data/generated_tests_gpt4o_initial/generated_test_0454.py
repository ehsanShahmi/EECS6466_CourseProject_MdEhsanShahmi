import os
import shutil
import glob
import unittest

def task_func(src_dir, dest_dir, ext):
    """
    Moves files with a specified extension from a source directory to a destination directory. 
    This function searches for files in the source directory that match the given extension.
    If a file with the same name already exists in the destination directory, it is not moved.

    Parameters:
    - src_dir (str): The source directory path.
    - dest_dir (str): The destination directory path.
    - ext (str): The file extension to search for (without the leading dot).

    Returns:
    - list: A list of the full paths of files that were successfully moved. If a file was not moved
            because it already exists in the destination directory, it will not be included in this list.

    Raises:
    FileNotFoundError: if either the source or destination directory does not exist
            
    Requirements:
    - os
    - shutil
    - glob
    """
    if not os.path.exists(dest_dir):
        raise FileNotFoundError(f"Destination directory '{dest_dir}' does not exist.")
    if not os.path.exists(src_dir):
        raise FileNotFoundError(f"Source directory '{src_dir}' does not exist.")

    files_moved = []
    files = glob.glob(os.path.join(src_dir, '*.' + ext))
    for file in files:
        filename = os.path.basename(file)
        dest_file_path = os.path.join(dest_dir, filename)
        if not os.path.exists(dest_file_path):
            shutil.move(file, dest_dir)
            files_moved.append(dest_file_path)
    return files_moved

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.src_dir = './test_src'
        self.dest_dir = './test_dest'
        self.ext = 'txt'
        os.makedirs(self.src_dir, exist_ok=True)
        os.makedirs(self.dest_dir, exist_ok=True)
        self.test_file = os.path.join(self.src_dir, 'test_file.txt')
        with open(self.test_file, 'w') as f:
            f.write('This is a test file.')

    def tearDown(self):
        shutil.rmtree(self.src_dir)
        shutil.rmtree(self.dest_dir)

    def test_move_single_file(self):
        moved_files = task_func(self.src_dir, self.dest_dir, self.ext)
        self.assertEqual(len(moved_files), 1)
        self.assertTrue(os.path.isfile(os.path.join(self.dest_dir, 'test_file.txt')))
        
    def test_move_no_files(self):
        new_src_dir = './new_src'
        os.makedirs(new_src_dir, exist_ok=True)
        moved_files = task_func(new_src_dir, self.dest_dir, self.ext)
        self.assertEqual(moved_files, [])
        shutil.rmtree(new_src_dir)

    def test_move_existing_file(self):
        shutil.move(self.test_file, self.dest_dir)  # Move the file first
        moved_files = task_func(self.src_dir, self.dest_dir, self.ext)
        self.assertEqual(len(moved_files), 0)
        self.assertTrue(os.path.isfile(os.path.join(self.dest_dir, 'test_file.txt')))
        
    def test_invalid_source_directory(self):
        with self.assertRaises(FileNotFoundError):
            task_func('./invalid_src', self.dest_dir, self.ext)

    def test_invalid_destination_directory(self):
        with self.assertRaises(FileNotFoundError):
            task_func(self.src_dir, './invalid_dest', self.ext)

if __name__ == '__main__':
    unittest.main()