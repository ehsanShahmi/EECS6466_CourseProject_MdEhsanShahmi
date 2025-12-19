import unittest
import os
import shutil
import hashlib

# Here is your prompt:
import os
import glob
import hashlib

def task_func(source_dir, target_dir, prefix='#Hash: '):
    """
    Computes the MD5 hash of each file's content in the specified `source_dir`, prepends the hash along with a prefix 
    to the original content, and writes the modified content to new files in the `target_dir`. 
    Existing files with the same name in `target_dir` are overwritten.

    Parameters:
    - source_dir (str): The directory containing the files to be processed. Must exist.
    - target_dir (str): The directory where the processed files will be written. Created if it does not exist.
    - prefix (str): The prefix to prepend before the hash in each new file. Default is '#Hash: '.

    Returns:
    - list: A list of paths to the newly created files in the `target_dir`, each with the hash prepended.

    Requirements:
    - os
    - glob
    - hashlib

    Raises:
    FileNotFoundError if the source directory does not exist.
    """

    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist.")
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    new_files = []
    for file_path in glob.glob(os.path.join(source_dir, '*')):
        with open(file_path, 'r') as infile:
            content = infile.read()
        
        hash_object = hashlib.md5(content.encode())
        new_file_path = os.path.join(target_dir, os.path.basename(file_path))
        
        with open(new_file_path, 'w') as outfile:
            outfile.write(f"{prefix}{hash_object.hexdigest()}\n{content}")
        
        new_files.append(new_file_path)
    
    return new_files

class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        self.source_dir = 'test_source'
        self.target_dir = 'test_target'
        os.makedirs(self.source_dir, exist_ok=True)

        # Create sample files
        with open(os.path.join(self.source_dir, 'file1.txt'), 'w') as f:
            f.write('Hello World')
        
        with open(os.path.join(self.source_dir, 'file2.txt'), 'w') as f:
            f.write('Goodbye World')

    def tearDown(self):
        shutil.rmtree(self.source_dir)
        if os.path.exists(self.target_dir):
            shutil.rmtree(self.target_dir)

    def test_file_creation(self):
        result_files = task_func(self.source_dir, self.target_dir)
        self.assertEqual(len(result_files), 2)
        for file in result_files:
            self.assertTrue(os.path.isfile(file))

    def test_file_content(self):
        task_func(self.source_dir, self.target_dir)
        with open(os.path.join(self.target_dir, 'file1.txt'), 'r') as f:
            content = f.read()
            expected_hash = hashlib.md5('Hello World'.encode()).hexdigest()
            expected_content = f"#Hash: {expected_hash}\nHello World"
            self.assertEqual(content, expected_content)

    def test_overwrite_files(self):
        task_func(self.source_dir, self.target_dir)
        with open(os.path.join(self.target_dir, 'file1.txt'), 'r') as f:
            original_content = f.read()

        # Modify the source file content
        with open(os.path.join(self.source_dir, 'file1.txt'), 'w') as f:
            f.write('Modified Content')

        task_func(self.source_dir, self.target_dir)

        with open(os.path.join(self.target_dir, 'file1.txt'), 'r') as f:
            new_content = f.read()
            new_expected_hash = hashlib.md5('Modified Content'.encode()).hexdigest()
            new_expected_content = f"#Hash: {new_expected_hash}\nModified Content"
            self.assertEqual(new_content, new_expected_content)

    def test_source_directory_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_directory', self.target_dir)

if __name__ == '__main__':
    unittest.main()