import os
import shutil
import unittest
import tempfile

def task_func(src_folder, backup_dir):
    """
    Backs up a given source folder to the specified backup directory, then deletes the source folder.
    
    Parameters:
    src_folder (str): The path of the source folder to be backed up and deleted.
    backup_dir (str): The path of the directory where the source folder will be backed up.
    
    Returns:
    bool: True if the operation is successful, False otherwise.
    
    Requirements:
    - os
    - shutil
    
    Raises:
    - ValueError: If the source folder does not exist.
    - Exception: If an error occurs while deleting the source folder.
    """
    # Check if source folder exists
    if not os.path.isdir(src_folder):
        raise ValueError(f"Source folder '{src_folder}' does not exist.")
    
    # Backup folder
    backup_folder = os.path.join(backup_dir, os.path.basename(src_folder))
    shutil.copytree(src_folder, backup_folder)
    
    # Delete source folder
    try:
        shutil.rmtree(src_folder)
        return True
    except Exception as e:
        print(f"Error while deleting source folder: {e}")
        return False

class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        self.src_folder = tempfile.mkdtemp()
        self.backup_dir = tempfile.mkdtemp()
        self.file_path = os.path.join(self.src_folder, 'sample.txt')
        
        with open(self.file_path, 'w') as f:
            f.write('This is a sample file.')

    def test_backup_success(self):
        result = task_func(self.src_folder, self.backup_dir)
        self.assertTrue(result)
        self.assertTrue(os.path.isdir(os.path.join(self.backup_dir, 'sample.txt')))

    def test_source_folder_not_exist(self):
        with self.assertRaises(ValueError):
            task_func('/non/existent/folder', self.backup_dir)

    def test_empty_backup_dir(self):
        result = task_func(self.src_folder, self.backup_dir)
        self.assertTrue(result)
        self.assertTrue(os.path.isdir(os.path.join(self.backup_dir, 'sample.txt')))
        
    def test_source_folder_deleted_after_backup(self):
        task_func(self.src_folder, self.backup_dir)
        self.assertFalse(os.path.isdir(self.src_folder))

    def test_error_on_delete_source_folder(self):
        # Make the src folder read-only to simulate deletion error
        os.chmod(self.src_folder, stat.S_IREAD)
        with self.assertRaises(PermissionError):
            task_func(self.src_folder, self.backup_dir)

if __name__ == '__main__':
    unittest.main()