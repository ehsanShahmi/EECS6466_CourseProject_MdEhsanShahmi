import unittest
import os
import shutil
import warnings

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create a temp source and destination directory for testing."""
        self.source_dir = 'source_dir'
        self.dest_dir = 'dest_dir'
        os.makedirs(self.source_dir, exist_ok=True)
        os.makedirs(self.dest_dir, exist_ok=True)

        # Create test files
        self.test_files = ['file1.txt', 'file2.csv', 'file3.jpg']
        for file in self.test_files:
            with open(os.path.join(self.source_dir, file), 'w') as f:
                f.write('test')

    def tearDown(self):
        """Clean up the directories after tests."""
        shutil.rmtree(self.source_dir, ignore_errors=True)
        shutil.rmtree(self.dest_dir, ignore_errors=True)

    def test_transfer_txt_and_csv_files(self):
        """Test transferring .txt and .csv files."""
        transferred = task_func(self.source_dir, self.dest_dir, ['.txt', '.csv'])
        self.assertEqual(transferred, ['file1.txt', 'file2.csv'])

    def test_no_files_transferred(self):
        """Test transfer when no matching file types exist."""
        transferred = task_func(self.source_dir, self.dest_dir, ['.png'])
        self.assertEqual(transferred, [])

    def test_partial_transfer(self):
        """Test transfer partially with one valid extension."""
        transferred = task_func(self.source_dir, self.dest_dir, ['.txt'])
        self.assertEqual(transferred, ['file1.txt'])

    def test_warning_on_move_failure(self):
        """Test warning when trying to move non-existing file."""
        with self.assertRaises(Warning) as context:
            task_func(self.source_dir, self.dest_dir, ['.nonexistent'])
        self.assertIn("Unable to move file", str(context.exception))

    def test_empty_extension_list(self):
        """Test transfer with an empty extension list."""
        transferred = task_func(self.source_dir, self.dest_dir, [])
        self.assertEqual(transferred, [])

if __name__ == '__main__':
    unittest.main()