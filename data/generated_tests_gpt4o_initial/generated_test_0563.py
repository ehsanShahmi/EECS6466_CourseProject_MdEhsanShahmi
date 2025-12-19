import unittest
import os
import shutil
import ctypes

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = 'test_dlls'
        self.destination_dir = 'destination_dir'
        os.makedirs(self.test_dir, exist_ok=True)
        os.makedirs(self.destination_dir, exist_ok=True)
        
        # Create a dummy DLL file for testing (This won't actually be a DLL)
        self.dll_file_path = os.path.join(self.test_dir, 'dummy.dll')
        with open(self.dll_file_path, 'w') as f:
            f.write('Dummy data for DLL')

        # Create a second dummy DLL file to test moving
        self.second_dll_file_path = os.path.join(self.test_dir, 'dummy2.dll')
        with open(self.second_dll_file_path, 'w') as f:
            f.write('Second dummy data for DLL')

    def tearDown(self):
        # Remove the directories after tests
        shutil.rmtree(self.test_dir, ignore_errors=True)
        shutil.rmtree(self.destination_dir, ignore_errors=True)

    def test_load_dll(self):
        """ Test whether the function returns the correct DLL name """
        loaded_dll = task_func(self.dll_file_path, self.destination_dir)
        self.assertEqual(loaded_dll, 'dummy.dll')  # The loaded dll name should match

    def test_move_dll_files(self):
        """ Test whether DLL files are moved to the destination directory """
        task_func(self.dll_file_path, self.destination_dir)
        self.assertTrue(os.path.isfile(os.path.join(self.destination_dir, 'dummy.dll')))
        self.assertTrue(os.path.isfile(os.path.join(self.destination_dir, 'dummy2.dll')))
    
    def test_dll_file_not_found(self):
        """ Test behavior when the DLL file is not found """
        with self.assertRaises(OSError):
            task_func('non_existing.dll', self.destination_dir)

    def test_empty_destination_directory(self):
        """ Test that no files are moved if the directory is empty """
        empty_dir = 'empty_dir'
        os.makedirs(empty_dir, exist_ok=True)
        task_func(self.dll_file_path, empty_dir)
        self.assertFalse(os.path.isfile(os.path.join(empty_dir, 'dummy.dll')))
        shutil.rmtree(empty_dir)

    def test_multiple_dll_files_moving(self):
        """ Test moving multiple DLL files at once """
        task_func(self.dll_file_path, self.destination_dir)
        task_func(self.second_dll_file_path, self.destination_dir)
        self.assertTrue(os.path.isfile(os.path.join(self.destination_dir, 'dummy.dll')))
        self.assertTrue(os.path.isfile(os.path.join(self.destination_dir, 'dummy2.dll')))

if __name__ == '__main__':
    unittest.main()