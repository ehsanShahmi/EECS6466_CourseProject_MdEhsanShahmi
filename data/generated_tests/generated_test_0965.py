import os
import unittest
import shutil

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary source and target directory for testing
        self.source_directory = 'test_source'
        self.target_directory = 'test_target'
        os.makedirs(self.source_directory, exist_ok=True)
    
    def tearDown(self):
        # Clean up the directories after the test
        if os.path.exists(self.source_directory):
            shutil.rmtree(self.source_directory)
        if os.path.exists(self.target_directory):
            shutil.rmtree(self.target_directory)
    
    def test_no_source_directory(self):
        # Test moving files with a non-existing source directory
        result = task_func('non_existing_source', self.target_directory)
        self.assertEqual(result, 0)
        
    def test_no_target_directory(self):
        # Test moving files when target directory does not exist (it should be created)
        test_files = ['1000.txt', '1001.txt', '1002.txt', 'not_a_match.txt']
        for file in test_files:
            open(os.path.join(self.source_directory, file), 'a').close()
        
        result = task_func(self.source_directory, self.target_directory)
        self.assertEqual(result, 3)  # Only 3 files match the pattern
        self.assertTrue(os.path.exists(self.target_directory))
        self.assertEqual(len(os.listdir(self.target_directory)), 3)
    
    def test_existing_target_directory(self):
        # Test moving files when target directory already exists
        os.makedirs(self.target_directory, exist_ok=True)
        test_files = ['2000.txt', '2001.txt', 'not_a_match.txt']
        for file in test_files:
            open(os.path.join(self.source_directory, file), 'a').close()
        
        result = task_func(self.source_directory, self.target_directory)
        self.assertEqual(result, 2)  # 2 files match the pattern
        self.assertEqual(len(os.listdir(self.target_directory)), 2)
    
    def test_invalid_source_directory(self):
        # Test with an invalid source directory (not a directory)
        open('invalid_source.txt', 'a').close()  # Create a file, not a directory
        result = task_func('invalid_source.txt', self.target_directory)
        self.assertEqual(result, 0)
        os.remove('invalid_source.txt')  # Clean up the file created
    
    def test_pattern_matching(self):
        # Test using a specific pattern to match files
        custom_pattern = r'200[0-9]'  # Matches files like 2000.txt, 2001.txt
        
        test_files = ['2000.txt', '2001.txt', 'not_a_match.txt', '3000.txt']
        for file in test_files:
            open(os.path.join(self.source_directory, file), 'a').close()
        
        result = task_func(self.source_directory, self.target_directory, pattern=custom_pattern)
        self.assertEqual(result, 2)  # Only 2000.txt and 2001.txt match the pattern

if __name__ == '__main__':
    unittest.main()