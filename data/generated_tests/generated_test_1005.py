import unittest
import os
import urllib.request
import zipfile
import shutil


class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.valid_url = 'http://www.example.com/data.zip'  # Replace with an actual URL for testing
        self.invalid_url = 'http://www.nonexistenturl.com/data.zip'
        self.save_path = 'test_downloaded_file.zip'
        self.extract_path = 'test_extracted_files'
        self.zip_file_path = 'sample.zip'  # Pre-created sample ZIP file for testing

        # Create a sample ZIP file for valid testing
        with zipfile.ZipFile(self.zip_file_path, 'w') as zipf:
            zipf.writestr('example.txt', b'This is a test file.')

    def tearDown(self):
        # Clean up any files and directories created during tests
        if os.path.exists(self.save_path):
            os.remove(self.save_path)
        if os.path.exists(self.extract_path):
            shutil.rmtree(self.extract_path)
        if os.path.exists(self.zip_file_path):
            os.remove(self.zip_file_path)

    def test_valid_url(self):
        # This test assumes that you would replace the valid URL with an actual accessible one.
        result = task_func(self.zip_file_path, self.save_path, self.extract_path)
        self.assertEqual(result, self.extract_path)
        self.assertTrue(os.path.exists(self.extract_path))

    def test_invalid_url(self):
        result = task_func(self.invalid_url, self.save_path, self.extract_path)
        self.assertTrue(result.startswith("URL Error:"))

    def test_extraction_folder_creation(self):
        task_func(self.zip_file_path, self.save_path, self.extract_path)
        self.assertTrue(os.path.exists(self.extract_path))

    def test_removal_of_zip_after_extraction(self):
        task_func(self.zip_file_path, self.save_path, self.extract_path)
        self.assertFalse(os.path.exists(self.save_path))

    def test_multiple_calls(self):
        # Call the function twice to ensure it cleans up correctly each time
        task_func(self.zip_file_path, self.save_path, self.extract_path)
        self.assertTrue(os.path.exists(self.extract_path))
        
        # Call it again to check if it still works as expected
        task_func(self.zip_file_path, self.save_path, self.extract_path)
        self.assertTrue(os.path.exists(self.extract_path))


if __name__ == '__main__':
    unittest.main()