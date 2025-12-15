import os
import shutil
import unittest

# Prompt provided code
def task_func(directory, backup_directory):
    copied_files = []

    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            src = os.path.join(directory, filename)
            dst = os.path.join(backup_directory, filename)
            shutil.copy(src, dst)
            copied_files.append(dst)

    return copied_files

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        """Setting up test directories and files."""
        self.test_dir = 'test_source'
        self.backup_dir = 'test_backup'
        os.makedirs(self.test_dir, exist_ok=True)

    def tearDown(self):
        """Cleaning up after tests."""
        shutil.rmtree(self.test_dir, ignore_errors=True)
        shutil.rmtree(self.backup_dir, ignore_errors=True)

    def test_empty_directory(self):
        """Test when the source directory is empty."""
        result = task_func(self.test_dir, self.backup_dir)
        self.assertEqual(result, [])
    
    def test_single_json_file(self):
        """Test backing up a single JSON file."""
        with open(os.path.join(self.test_dir, 'file1.json'), 'w') as f:
            f.write('{}')
        result = task_func(self.test_dir, self.backup_dir)
        self.assertEqual(len(result), 1)
        self.assertTrue(result[0].endswith('file1.json'))

    def test_multiple_json_files(self):
        """Test backing up multiple JSON files."""
        for i in range(5):
            with open(os.path.join(self.test_dir, f'file{i}.json'), 'w') as f:
                f.write('{}')
        result = task_func(self.test_dir, self.backup_dir)
        self.assertEqual(len(result), 5)
        self.assertTrue(all(file.endswith('.json') for file in result))

    def test_no_json_files(self):
        """Test when the directory contains no JSON files."""
        with open(os.path.join(self.test_dir, 'file1.txt'), 'w') as f:
            f.write('This is a text file.')
        result = task_func(self.test_dir, self.backup_dir)
        self.assertEqual(result, [])

    def test_backup_directory_creation(self):
        """Test if the backup directory is created if it doesn't exist."""
        result = task_func(self.test_dir, self.backup_dir)
        self.assertTrue(os.path.exists(self.backup_dir))

if __name__ == '__main__':
    unittest.main()