import os
import unittest
import shutil

# Here is your prompt:
import re
import os
import shutil

def task_func(source_dir, target_dir, file_pattern=r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b'):
    """
    Look for files that match the pattern of the regular expression '(? <! Distillr)\\\\ AcroTray\\.exe' in the directory 'C:\\ SomeDir\\'. If found, write these file paths to a configuration file.

    Parameters:
    - source_dir (str): The path to the source directory.
    - target_dir (str): The path to the target directory.
    - file_pattern (str, optional): The regular expression pattern that filenames must match in order
                                   to be moved. Default is r'\b[A-Za-z0-9]+\.(txt|doc|docx)\b',
                                   which matches filenames that consist of alphanumeric characters
                                   and have extensions txt, doc, or docx.

    Returns:
    - str: Path to the created configuration file.

    Requirements:
    - re
    - os
    - shtuil

    Example:
    >>> task_func('/path/to/source', '/path/to/target')
    3
    """

               if not os.path.exists(source_dir):
        raise FileNotFoundError("The source directory does not exist.")
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    moved_files_count = 0

    for filename in os.listdir(source_dir):
        if re.match(file_pattern, filename):
            shutil.move(os.path.join(source_dir, filename), os.path.join(target_dir, filename))
            moved_files_count += 1

    return moved_files_count


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.source_dir = 'test_source'
        self.target_dir = 'test_target'
        if not os.path.exists(self.source_dir):
            os.makedirs(self.source_dir)
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)

    def tearDown(self):
        shutil.rmtree(self.source_dir)
        shutil.rmtree(self.target_dir)

    def test_move_txt_file(self):
        with open(os.path.join(self.source_dir, 'testfile.txt'), 'w') as f:
            f.write("This is a test.")
        result = task_func(self.source_dir, self.target_dir)
        self.assertEqual(result, 1)
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, 'testfile.txt')))
        self.assertFalse(os.path.exists(os.path.join(self.source_dir, 'testfile.txt')))

    def test_move_doc_file(self):
        with open(os.path.join(self.source_dir, 'testfile.doc'), 'w') as f:
            f.write("This is a test document.")
        result = task_func(self.source_dir, self.target_dir)
        self.assertEqual(result, 1)
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, 'testfile.doc')))
        self.assertFalse(os.path.exists(os.path.join(self.source_dir, 'testfile.doc')))

    def test_no_files_to_move(self):
        result = task_func(self.source_dir, self.target_dir)
        self.assertEqual(result, 0)

    def test_move_multiple_files(self):
        with open(os.path.join(self.source_dir, 'file1.txt'), 'w') as f:
            f.write("File 1")
        with open(os.path.join(self.source_dir, 'file2.doc'), 'w') as f:
            f.write("File 2")
        result = task_func(self.source_dir, self.target_dir)
        self.assertEqual(result, 2)
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, 'file1.txt')))
        self.assertTrue(os.path.exists(os.path.join(self.target_dir, 'file2.doc')))
        self.assertFalse(os.path.exists(os.path.join(self.source_dir, 'file1.txt')))
        self.assertFalse(os.path.exists(os.path.join(self.source_dir, 'file2.doc')))

    def test_invalid_source_directory(self):
        with self.assertRaises(FileNotFoundError):
            task_func('invalid_source_dir', self.target_dir)

if __name__ == '__main__':
    unittest.main()