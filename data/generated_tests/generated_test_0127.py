import os
import shutil
import glob
import hashlib
import unittest

def task_func(ROOT_DIR, DEST_DIR, SPECIFIC_HASH):
    """
    Moves all files from a specified root directory (ROOT_DIR) to a target directory (DEST_DIR) if they match a specific hash value (SPECIFIC_HASH).
    The function calculates the MD5 hash of each file in ROOT_DIR and moves it if the hash matches SPECIFIC_HASH.

    Parameters:
        ROOT_DIR (str): The path to the root directory from which files will be moved.
        DEST_DIR (str): The path to the destination directory where files will be moved to.
        SPECIFIC_HASH (str): The specific MD5 hash value files must match to be moved.

    Returns:
        int: The number of files moved to the target directory.

    Note:
        The function assumes the existence of the root directory. The existence of DEST_DIR is ensured by the function.

    Requirements:
    - os
    - shutil
    - glob
    - hashlib
    """

    files_moved = 0

    os.makedirs(DEST_DIR, exist_ok=True)
    for filename in glob.glob(os.path.join(ROOT_DIR, '*')):
        if not os.path.exists(filename) or os.path.isdir(filename):
            continue
        with open(filename, 'rb') as f:
            file_hash = hashlib.md5(f.read()).hexdigest()
        if file_hash == SPECIFIC_HASH:
            shutil.move(filename, DEST_DIR)
            files_moved += 1
    return files_moved

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.test_root = 'test_root'
        self.test_dest = 'test_dest'
        os.makedirs(self.test_root, exist_ok=True)
        os.makedirs(self.test_dest, exist_ok=True)
        self.test_file_1 = os.path.join(self.test_root, 'file1.txt')
        self.test_file_2 = os.path.join(self.test_root, 'file2.txt')

        with open(self.test_file_1, 'wb') as f:
            f.write(b'This is a test file.')  # This file will not match the test hash
        with open(self.test_file_2, 'wb') as f:
            f.write(b'This file has a known MD5 hash')  # Modify the content to match a specific hash if needed
        
    def tearDown(self):
        shutil.rmtree(self.test_root)
        shutil.rmtree(self.test_dest)
    
    def test_no_files_moved(self):
        specific_hash = 'd41d8cd98f00b204e9800998ecf8427e'  # Example of a hash that does not match
        result = task_func(self.test_root, self.test_dest, specific_hash)
        self.assertEqual(result, 0)

    def test_some_files_moved(self):
        # Create a file with a specific hash
        specific_hash = hashlib.md5(b'This file has a known MD5 hash').hexdigest()
        result = task_func(self.test_root, self.test_dest, specific_hash)
        self.assertTrue(result > 0)

    def test_destination_directory_created(self):
        specific_hash = hashlib.md5(b'This file has a known MD5 hash').hexdigest()
        task_func(self.test_root, self.test_dest, specific_hash)
        self.assertTrue(os.path.exists(self.test_dest))

    def test_leaving_non_matching_files(self):
        specific_hash = hashlib.md5(b'This file has a known MD5 hash').hexdigest()
        task_func(self.test_root, self.test_dest, specific_hash)
        self.assertTrue(os.path.isfile(self.test_file_1))

    def test_move_multiple_matching_files(self):
        # Create another file that matches the specific hash
        additional_file = os.path.join(self.test_root, 'file3.txt')
        with open(additional_file, 'wb') as f:
            f.write(b'This file has a known MD5 hash')  # Same content to match the hash
            
        specific_hash = hashlib.md5(b'This file has a known MD5 hash').hexdigest()
        result = task_func(self.test_root, self.test_dest, specific_hash)
        self.assertEqual(result, 2)  # Expecting two files to be moved

if __name__ == '__main__':
    unittest.main()