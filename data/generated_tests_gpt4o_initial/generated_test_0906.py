import unittest
import os
import zipfile

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.source_dir = './test_source/'
        self.target_dir = './test_target/'
        os.makedirs(self.source_dir, exist_ok=True)
        os.makedirs(self.target_dir, exist_ok=True)

    def tearDown(self):
        if os.path.exists(self.source_dir):
            for file in os.listdir(self.source_dir):
                os.remove(os.path.join(self.source_dir, file))
            os.rmdir(self.source_dir)
        if os.path.exists(self.target_dir):
            for file in os.listdir(self.target_dir):
                os.remove(os.path.join(self.target_dir, file))
            os.rmdir(self.target_dir)

    def test_archive_creation(self):
        with open(os.path.join(self.source_dir, 'file1_processed.txt'), 'w') as f:
            f.write('Test content')
        archive_path = task_func(self.source_dir, self.target_dir)
        self.assertTrue(os.path.exists(archive_path))
    
    def test_archive_contains_processed_files(self):
        with open(os.path.join(self.source_dir, 'file1_processed.txt'), 'w') as f:
            f.write('Test content')
        with open(os.path.join(self.source_dir, 'file2.txt'), 'w') as f:
            f.write('Test content')
        task_func(self.source_dir, self.target_dir)
        
        with zipfile.ZipFile(os.path.join(self.target_dir, 'archive.zip'), 'r') as archive:
            processed_files = [file for file in archive.namelist() if 'file1_processed.txt' in file]
            self.assertEqual(len(processed_files), 1)
    
    def test_move_processed_files(self):
        with open(os.path.join(self.source_dir, 'file1_processed.txt'), 'w') as f:
            f.write('Test content')
        task_func(self.source_dir, self.target_dir)
        
        self.assertFalse(os.path.exists(os.path.join(self.source_dir, 'file1_processed.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, 'file1_processed.txt')))
    
    def test_custom_archive_name(self):
        with open(os.path.join(self.source_dir, 'file1_processed.txt'), 'w') as f:
            f.write('Test content')
        archive_name = 'my_archive.zip'
        archive_path = task_func(self.source_dir, self.target_dir, archive_name)
        self.assertTrue(os.path.exists(archive_path))
        self.assertIn(archive_name, archive_path)
    
    def test_no_processed_files(self):
        with open(os.path.join(self.source_dir, 'file2.txt'), 'w') as f:
            f.write('Test content')
        archive_path = task_func(self.source_dir, self.target_dir)
        with zipfile.ZipFile(archive_path, 'r') as archive:
            self.assertEqual(len(archive.namelist()), 0)

if __name__ == '__main__':
    unittest.main()