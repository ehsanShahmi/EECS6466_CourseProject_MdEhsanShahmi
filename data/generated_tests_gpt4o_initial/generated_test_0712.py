import os
import shutil
import glob
import unittest

# Here is your prompt:
# import os
# import shutil
# import glob

# def task_func(source_dir, dest_dir, extension):
#     """
#     Move all files with a particular extension from one directory to another.
    
#     Parameters:
#     - source_dir (str): The source directory.
#     - dest_dir (str): The destination directory.
#     - extension (str): The file extension.

#     Returns:
#     - result (int): The count of files that were moved. 

#     Requirements:
#     - os
#     - shutil
#     - glob
        
#     Example:
#     >>> task_func('path_to_source_dir', 'path_to_dest_dir', '.txt')
#     10
#     """

#             files = glob.glob(os.path.join(source_dir, f'*.{extension}'))
    
#     for file in files:
#         shutil.move(file, dest_dir)
        
#     result = len(files)

#     return result

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create temporary directories and files for testing."""
        self.source_dir = 'test_source'
        self.dest_dir = 'test_dest'
        os.makedirs(self.source_dir, exist_ok=True)
        os.makedirs(self.dest_dir, exist_ok=True)

        # Create sample files for testing
        self.test_files = ['file1.txt', 'file2.txt', 'file3.doc', 'file4.txt', 'file5.pdf']
        for file in self.test_files:
            with open(os.path.join(self.source_dir, file), 'w') as f:
                f.write('This is a test file.')

    def tearDown(self):
        """Remove the directories created for testing."""
        shutil.rmtree(self.source_dir, ignore_errors=True)
        shutil.rmtree(self.dest_dir, ignore_errors=True)

    def test_move_txt_files(self):
        """Test moving .txt files from source to destination."""
        result = task_func(self.source_dir, self.dest_dir, 'txt')
        self.assertEqual(result, 3)
        self.assertEqual(len(os.listdir(self.dest_dir)), 3)

    def test_move_doc_files(self):
        """Test moving .doc files from source to destination."""
        result = task_func(self.source_dir, self.dest_dir, 'doc')
        self.assertEqual(result, 1)
        self.assertEqual(len(os.listdir(self.dest_dir)), 1)

    def test_move_pdf_files(self):
        """Test moving .pdf files from source to destination."""
        result = task_func(self.source_dir, self.dest_dir, 'pdf')
        self.assertEqual(result, 1)
        self.assertEqual(len(os.listdir(self.dest_dir)), 1)
    
    def test_no_files_moved(self):
        """Test moving a file type that doesn't exist in the source directory."""
        result = task_func(self.source_dir, self.dest_dir, 'jpg')
        self.assertEqual(result, 0)
        self.assertEqual(len(os.listdir(self.dest_dir)), 0)

    def test_only_move_existing_files(self):
        """Test moving files and ensure that already moved files are not moved again."""
        task_func(self.source_dir, self.dest_dir, 'txt')
        result = task_func(self.source_dir, self.dest_dir, 'txt')
        self.assertEqual(result, 0)
        self.assertEqual(len(os.listdir(self.dest_dir)), 3)

if __name__ == '__main__':
    unittest.main()