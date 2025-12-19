import os
import unittest
from pathlib import Path
import shutil

# Here is your prompt:

def task_func(source_directory: str, target_directory: str):
    """
    Moves files with specific extensions from a source directory to a target directory,
    handling naming conflicts by renaming duplicates.

    Parameters:
    - source_directory (str): The absolute or relative path of the source directory.
    - target_directory (str): The absolute or relative path of the target directory.
                              This function will create it if it does not exist.

    Returns:
    - int: The number of files successfully moved.

    Raises:
    - FileNotFoundError: If source_directory does not exist.

    Requirements:
    - os
    - pathlib
    - glob
    - shutil

    Notes:
    - This function scans the source directory recursively to find files.
    - Files are filtered by the extensions: ".txt", ".docx", ".xlsx", ".csv".
    - Renaming of files due to naming conflicts follows the pattern '<original_name>-n.<extension>'.

    Examples:
    >>> task_func('./source_folder', './target_folder')
    3
    >>> task_func('./empty_folder', './target_folder')
    0
    """
    moved_files = 0

    if not os.path.exists(source_directory):
        raise FileNotFoundError("source_directory must exist.")

    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for extension in [".txt", ".docx", ".xlsx", ".csv"]:
        filepaths = glob.glob(
            os.path.join(source_directory, "**", "*" + extension), recursive=True
        )
        for filepath in filepaths:
            filename = Path(filepath).name
            stem = Path(filepath).stem
            target_filepath = os.path.join(target_directory, filename)

            count = 1
            while os.path.exists(target_filepath):
                new_filename = f"{stem}-{count}{extension}"
                target_filepath = os.path.join(target_directory, new_filename)
                count += 1

            shutil.move(filepath, target_filepath)
            moved_files += 1

    return moved_files


class TestTaskFunction(unittest.TestCase):

    def setUp(self):
        self.test_source = './test_source'
        self.test_target = './test_target'
        
        os.makedirs(self.test_source, exist_ok=True)
        os.makedirs(self.test_target, exist_ok=True)

    def tearDown(self):
        shutil.rmtree(self.test_source, ignore_errors=True)
        shutil.rmtree(self.test_target, ignore_errors=True)

    def test_move_files(self):
        with open(os.path.join(self.test_source, 'file1.txt'), 'w') as f:
            f.write("Test file 1")
        with open(os.path.join(self.test_source, 'file2.docx'), 'w') as f:
            f.write("Test file 2")
            
        moved_count = task_func(self.test_source, self.test_target)
        self.assertEqual(moved_count, 2)
        self.assertTrue(os.path.exists(os.path.join(self.test_target, 'file1.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.test_target, 'file2.docx')))

    def test_no_files_to_move(self):
        moved_count = task_func(self.test_source, self.test_target)
        self.assertEqual(moved_count, 0)

    def test_empty_source_directory(self):
        os.rmdir(self.test_source)  # Remove the directory to make it empty
        with self.assertRaises(FileNotFoundError):
            task_func(self.test_source, self.test_target)

    def test_file_conflict_handling(self):
        with open(os.path.join(self.test_source, 'file1.txt'), 'w') as f:
            f.write("Duplicate test file")
        with open(os.path.join(self.test_target, 'file1.txt'), 'w') as f:
            f.write("Existing file in target")
        
        moved_count = task_func(self.test_source, self.test_target)
        self.assertEqual(moved_count, 1)
        self.assertTrue(os.path.exists(os.path.join(self.test_target, 'file1-1.txt')))

if __name__ == '__main__':
    unittest.main()