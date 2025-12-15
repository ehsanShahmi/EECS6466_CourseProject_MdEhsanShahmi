import unittest
import os
import shutil

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Set up temporary directories for tests
        self.src_dir = './test_src'
        self.dst_dir = './test_dst'
        os.makedirs(self.src_dir, exist_ok=True)
        os.makedirs(self.dst_dir, exist_ok=True)

    def tearDown(self):
        # Clean up the temporary directories after tests
        shutil.rmtree(self.src_dir)
        shutil.rmtree(self.dst_dir)

    def test_copy_txt_files(self):
        # Prepare test files
        with open(os.path.join(self.src_dir, 'file1.txt'), 'w') as f:
            f.write('This is a test .txt file.')
        with open(os.path.join(self.src_dir, 'file2.docx'), 'w') as f:
            f.write('This is a test .docx file.')
        with open(os.path.join(self.src_dir, 'file3.pdf'), 'w') as f:
            f.write('This is a test .pdf file.')
        
        # Call the function
        task_func(self.src_dir, self.dst_dir)
        
        # Check if the correct files are copied
        self.assertTrue(os.path.exists(os.path.join(self.dst_dir, 'file1.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.dst_dir, 'file2.docx')))
        self.assertFalse(os.path.exists(os.path.join(self.dst_dir, 'file3.pdf')))

    def test_empty_source_directory(self):
        # Call the function on an empty source directory
        task_func(self.src_dir, self.dst_dir)
        
        # Check if destination directory is still empty
        self.assertEqual(len(os.listdir(self.dst_dir)), 0)

    def test_copy_no_matching_files(self):
        # Prepare a non-matching test file
        with open(os.path.join(self.src_dir, 'file4.jpg'), 'w') as f:
            f.write('This is a test .jpg file.')

        # Call the function
        task_func(self.src_dir, self.dst_dir)

        # Check if destination directory is still empty
        self.assertEqual(len(os.listdir(self.dst_dir)), 0)

    def test_multiple_matching_files(self):
        # Prepare multiple matching files
        with open(os.path.join(self.src_dir, 'file5.txt'), 'w') as f:
            f.write('Test file 1')
        with open(os.path.join(self.src_dir, 'file6.txt'), 'w') as f:
            f.write('Test file 2')
        
        # Call the function
        task_func(self.src_dir, self.dst_dir)
        
        # Check if the correct files are copied
        self.assertTrue(os.path.exists(os.path.join(self.dst_dir, 'file5.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.dst_dir, 'file6.txt')))

    def test_copy_to_non_existent_destination(self):
        # Prepare test files
        with open(os.path.join(self.src_dir, 'file7.txt'), 'w') as f:
            f.write('Test file for non-existent destination.')
        
        # Create a non-existent destination directory
        non_existent_dst = './non_existent_dst'
        
        # Call the function and check for exception
        with self.assertRaises(FileNotFoundError):
            task_func(self.src_dir, non_existent_dst)

if __name__ == '__main__':
    unittest.main()