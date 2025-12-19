import unittest
import os
import zipfile
import shutil

# Here is your prompt:
import re
import os
import zipfile

def task_func(directory, pattern=r'^(.*?)-\d+\.zip$'):
    """
    Unzip all zip files in a directory whose name matches a certain pattern by splitting the filename the last time "-" occurs and using the prefix part of the filename as the directory to extract.
    
    Parameters:
    - directory (str): The directory where the zip files are located.
    - pattern (str): Regex pattern to match zip files.

    Returns:
    - list: A list of directories where the files were extracted.

    Requirements:
    - os
    - re
    - zipfile

    Example:
    >>> task_func('/tmp/my_data')
    ('/tmp/backup/backup_20230827010101', [])
    """

    extracted_dirs = []
    for filename in os.listdir(directory):
        match = re.match(pattern, filename)
        if match:
            file_path = os.path.join(directory, filename)
            # Use the part before the first '-' as the directory name.
            base_name = match.group(1)
            extract_path = os.path.join(directory, base_name)
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(extract_path)
            if extract_path not in extracted_dirs:
                extracted_dirs.append(extract_path)
                os.makedirs(extract_path, exist_ok=True)  # Ensure the directory is created
    return extracted_dirs


class TestTaskFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_dir = 'test_data'
        os.makedirs(cls.test_dir, exist_ok=True)

        # Create test zip files
        cls.zip_file_1 = os.path.join(cls.test_dir, 'backup-20230827010101.zip')
        cls.zip_file_2 = os.path.join(cls.test_dir, 'data-20230827010102.zip')
        cls.zip_file_3_non_matching = os.path.join(cls.test_dir, 'nonmatchingfile.zip')

        with zipfile.ZipFile(cls.zip_file_1, 'w') as zipf:
            zipf.writestr('dummy.txt', 'data')
        
        with zipfile.ZipFile(cls.zip_file_2, 'w') as zipf:
            zipf.writestr('dummy_data.txt', 'data')

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.test_dir)

    def test_extract_valid_zip(self):
        expected_dirs = [os.path.join(self.test_dir, 'backup')]
        extracted_dirs = task_func(self.test_dir)
        self.assertEqual(sorted(extracted_dirs), sorted(expected_dirs), "Extraction of valid zip files failed.")

    def test_multiple_zips(self):
        expected_dirs = [os.path.join(self.test_dir, 'backup'), os.path.join(self.test_dir, 'data')]
        extracted_dirs = task_func(self.test_dir)
        self.assertEqual(sorted(extracted_dirs), sorted(expected_dirs), "Multiple zip files extraction failed.")

    def test_no_matching_zips(self):
        os.rename(self.zip_file_1, self.zip_file_3_non_matching)  # Rename to non-matching
        extracted_dirs = task_func(self.test_dir)
        self.assertEqual(extracted_dirs, [], "Should return an empty list when no zips match the pattern.")

    def test_extract_path_creation(self):
        task_func(self.test_dir)
        backup_dir_exists = os.path.isdir(os.path.join(self.test_dir, 'backup'))
        data_dir_exists = os.path.isdir(os.path.join(self.test_dir, 'data'))
        self.assertTrue(backup_dir_exists, "Backup directory was not created.")
        self.assertTrue(data_dir_exists, "Data directory was not created.")

    def test_function_with_custom_pattern(self):
        custom_pattern = r'^(data).*?\.zip$'
        extracted_dirs = task_func(self.test_dir, custom_pattern)
        self.assertEqual(extracted_dirs, [os.path.join(self.test_dir, 'data')], "Custom pattern extraction failed.")


if __name__ == '__main__':
    unittest.main()