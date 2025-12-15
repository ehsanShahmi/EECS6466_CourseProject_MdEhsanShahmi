import os
import glob
import unittest
from unittest.mock import patch, MagicMock

# Here is your prompt:
def task_func(directory_path):
    """
    Reverse the order of words in all the filenames of a directory, where words are separated by periods.
    
    Parameters:
    - directory_path (str): The path to the directory.

    Returns:
    - new_filenames (list[str]): A list of new filenames after renaming.

    Requirements:
    - os
    - glob

    Example:
    Given filenames in directory: ["hello.world.txt", "sample.data.csv"]
    >>> task_func('/path/to/directory')
    ["txt.world.hello", "csv.data.sample"]
    """

    new_filenames = []
    for filename in glob.glob(os.path.join(directory_path, '*')):
        base_name = os.path.basename(filename)
        new_base_name = '.'.join(base_name.split('.')[::-1])
        os.rename(filename, os.path.join(directory_path, new_base_name))
        new_filenames.append(new_base_name)
    return new_filenames

class TestTaskFunc(unittest.TestCase):

    @patch('glob.glob')
    @patch('os.rename')
    def test_no_files(self, mock_rename, mock_glob):
        mock_glob.return_value = []
        result = task_func('/mock/directory')
        self.assertEqual(result, [])

    @patch('glob.glob')
    @patch('os.rename')
    def test_single_file(self, mock_rename, mock_glob):
        mock_glob.return_value = ['/mock/directory/hello.world.txt']
        result = task_func('/mock/directory')
        mock_rename.assert_called_once_with(
            '/mock/directory/hello.world.txt',
            '/mock/directory/txt.world.hello'
        )
        self.assertEqual(result, ['txt.world.hello'])

    @patch('glob.glob')
    @patch('os.rename')
    def test_multiple_files(self, mock_rename, mock_glob):
        mock_glob.return_value = [
            '/mock/directory/file.one.txt',
            '/mock/directory/photo.two.jpg'
        ]
        result = task_func('/mock/directory')
        self.assertEqual(mock_rename.call_count, 2)
        mock_rename.assert_any_call(
            '/mock/directory/file.one.txt',
            '/mock/directory/txt.one.file'
        )
        mock_rename.assert_any_call(
            '/mock/directory/photo.two.jpg',
            '/mock/directory.jpg.two.photo'
        )
        self.assertEqual(result, ['txt.one.file', 'jpg.two.photo'])

    @patch('glob.glob')
    @patch('os.rename')
    def test_only_extensions(self, mock_rename, mock_glob):
        mock_glob.return_value = ['/mock/directory/.hiddenfile', '/mock/directory/.anotherfile.']
        result = task_func('/mock/directory')
        self.assertEqual(mock_rename.call_count, 2)
        mock_rename.assert_any_call(
            '/mock/directory/.hiddenfile',
            '/mock/directory.hiddenfile'
        )
        mock_rename.assert_any_call(
            '/mock/directory/.anotherfile.',
            '/mock/directory..anotherfile'
        )
        self.assertEqual(result, ['hiddenfile', '..anotherfile'])

    @patch('glob.glob')
    @patch('os.rename')
    def test_files_with_no_dots(self, mock_rename, mock_glob):
        mock_glob.return_value = ['/mock/directory/filename']
        result = task_func('/mock/directory')
        mock_rename.assert_called_once_with(
            '/mock/directory/filename',
            '/mock/directory.filename'
        )
        self.assertEqual(result, ['filename'])

if __name__ == '__main__':
    unittest.main()