import unittest
import os
import shutil
import tempfile
from glob import glob

# Provided code (do not modify)
def task_func(src_folder, dst_folder):
    """Compress all files in the specified source folder and move the compressed files to a destination folder.
    This operation is executed as a background process using the 'gzip' command.

    Parameters:
    src_folder (str): The path of the source folder containing the files to be compressed.
    dst_folder (str): The path of the destination folder where the compressed files will be moved.

    Returns:
    dict: A dictionary containing:
        - 'success': A boolean indicating if all files were compressed and moved successfully.
        - 'message': A descriptive message about the operation's result.
        - 'failed_files': A list of filenames that failed to compress or move.
    """
    # Check if source and destination folders exist
    if not os.path.isdir(src_folder):
        raise ValueError(f"Source folder '{src_folder}' does not exist.")
    if not os.path.isdir(dst_folder):
        raise ValueError(f"Destination folder '{dst_folder}' does not exist.")
    
    processes = []
    failed_files = []

    # Compress files in a background process
    for file in glob(os.path.join(src_folder, '*')):
        process = subprocess.Popen(['gzip', file])
        processes.append((process, file))

    # Wait for all processes to complete
    for process, file in processes:
        retcode = process.wait()
        if retcode != 0:
            failed_files.append(os.path.basename(file))

    # Move compressed files to destination folder
    for file in glob(os.path.join(src_folder, '*.gz')):
        try:
            shutil.move(file, dst_folder)
        except Exception as e:
            failed_files.append(os.path.basename(file))

    if failed_files:
        return {'success': False, 'message': 'Some files failed to compress or move.', 'failed_files': failed_files}
    else:
        return {'success': True, 'message': 'All files compressed and moved successfully.', 'failed_files': []}


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.src_folder = tempfile.mkdtemp()
        self.dst_folder = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.src_folder)
        shutil.rmtree(self.dst_folder)

    def test_empty_source_folder(self):
        result = task_func(self.src_folder, self.dst_folder)
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], 'All files compressed and moved successfully.')
        self.assertEqual(result['failed_files'], [])

    def test_single_file_compression(self):
        with open(os.path.join(self.src_folder, 'file1.txt'), 'w') as f:
            f.write('This is a test file.')
        result = task_func(self.src_folder, self.dst_folder)
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], 'All files compressed and moved successfully.')
        self.assertEqual(result['failed_files'], [])
        self.assertTrue(os.path.exists(os.path.join(self.dst_folder, 'file1.txt.gz')))

    def test_multiple_file_compression(self):
        for i in range(3):
            with open(os.path.join(self.src_folder, f'file{i}.txt'), 'w') as f:
                f.write(f'This is file {i}.')
        result = task_func(self.src_folder, self.dst_folder)
        self.assertTrue(result['success'])
        self.assertEqual(result['message'], 'All files compressed and moved successfully.')
        self.assertEqual(result['failed_files'], [])
        for i in range(3):
            self.assertTrue(os.path.exists(os.path.join(self.dst_folder, f'file{i}.txt.gz')))

    def test_non_existing_source_folder(self):
        with self.assertRaises(ValueError) as context:
            task_func('non_existing_folder', self.dst_folder)
        self.assertIn("Source folder 'non_existing_folder' does not exist.", str(context.exception))

    def test_non_existing_destination_folder(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.src_folder, 'non_existing_folder')
        self.assertIn("Destination folder 'non_existing_folder' does not exist.", str(context.exception))


if __name__ == '__main__':
    unittest.main()