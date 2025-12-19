import unittest
import os
import configparser

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up a test configuration file and directory for the tests."""
        # Create a temporary project directory
        self.test_project_dir = 'test_project'
        os.makedirs(self.test_project_dir, exist_ok=True)

        # Create a sample file in the project directory
        sample_file_path = os.path.join(self.test_project_dir, 'sample_file.txt')
        with open(sample_file_path, 'w') as f:
            f.write('This is a test file.')

        # Create a config file that references the project directory
        self.config_file_path = 'test_config.ini'
        self.config = configparser.ConfigParser()
        self.config['Project'] = {'directory': self.test_project_dir}
        with open(self.config_file_path, 'w') as configfile:
            self.config.write(configfile)

        # Set the archive directory
        self.archive_dir = 'archive_test'
        os.makedirs(self.archive_dir, exist_ok=True)

    def tearDown(self):
        """Clean up after tests."""
        shutil.rmtree(self.test_project_dir, ignore_errors=True)
        shutil.rmtree(self.archive_dir, ignore_errors=True)
        if os.path.isfile(self.config_file_path):
            os.remove(self.config_file_path)

    def test_archive_creation_success(self):
        """Test if the archive is created successfully."""
        result = task_func(self.config_file_path, self.archive_dir)
        self.assertTrue(result)
        archive_file = f'{self.archive_dir}/{os.path.basename(self.test_project_dir)}.zip'
        self.assertTrue(os.path.isfile(archive_file))

    def test_directory_not_exist(self):
        """Test for FileNotFoundError if project directory does not exist."""
        invalid_config = configparser.ConfigParser()
        invalid_config['Project'] = {'directory': 'non_existing_directory'}
        with open('invalid_config.ini', 'w') as configfile:
            invalid_config.write(configfile)

        with self.assertRaises(FileNotFoundError):
            task_func('invalid_config.ini')

        os.remove('invalid_config.ini')

    def test_invalid_config_file(self):
        """Test for FileNotFoundError if config file does not exist."""
        with self.assertRaises(FileNotFoundError):
            task_func('non_existing_config.ini')

    def test_zip_creation_failure(self):
        """Test for Exception if ZIP archive cannot be created."""
        invalid_archive_dir = '/non_writable_directory/'
        with self.assertRaises(Exception):
            task_func(self.config_file_path, invalid_archive_dir)

if __name__ == '__main__':
    unittest.main()