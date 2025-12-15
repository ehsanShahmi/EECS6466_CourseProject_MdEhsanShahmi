import unittest
import os
from pathlib import Path
import re
import tarfile

# Here is your prompt:
import re
from pathlib import Path
import tarfile

# Constants
PATTERN = r"(?<!Distillr)\\\\AcroTray\.exe"
DIRECTORY = r"C:\\SomeDir\\"

def task_func(directory=DIRECTORY, file_pattern=PATTERN):
    """
    Look for files that match the pattern of the regular expression '(? <! Distillr)\\\\ AcroTray\\.exe' in the directory 'C:\\ SomeDir\\'. If found, archive these files in a tar file.

    Parameters:
    - directory: The directory to search for files matching a specified pattern. The function will iterate over all files within this directory, including subdirectories.
    - file_pattern: A regular expression pattern used to match filenames. Files whose names match this pattern will be added to an archive (tar file).

    Returns:
    - str: Path to the created tar file.

    Requirements:
    - re
    - pathlib
    - tarfile

    Example:
    >>> f_680('/path/to/source', '/path/to/target')
    """

               tar_path = Path(directory) / 'archive.tar'
    with tarfile.open(tar_path, 'w') as tar:
        for path in Path(directory).rglob('*'):
            if re.match(file_pattern, path.name):
                try:
                    tar.add(path, arcname=path.relative_to(directory))
                except PermissionError as e:
                    print(f"Skipping {path} due to permission error: {e}")
    return str(tar_path)

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up a temporary directory for testing."""
        self.test_dir = Path('./test_directory')
        self.test_dir.mkdir(parents=True, exist_ok=True)
        self.test_file_valid = self.test_dir / 'AcroTray.exe'
        self.test_file_invalid = self.test_dir / 'Distillr_AcroTray.exe'
        self.test_file_other = self.test_dir / 'other_file.txt'
        self.test_file_valid.touch()  # Create a valid test file
        self.test_file_invalid.touch()  # Create an invalid test file
        self.test_file_other.touch()  # Create another test file

    def tearDown(self):
        """Clean up the test directory after tests."""
        for item in self.test_dir.iterdir():
            item.unlink()
        self.test_dir.rmdir()

    def test_valid_file_archived(self):
        """Test that valid files are archived correctly."""
        result = task_func(directory=str(self.test_dir), file_pattern=PATTERN)
        self.assertTrue(Path(result).is_file())
        with tarfile.open(result) as tar:
            members = tar.getmembers()
            self.assertIn('AcroTray.exe', (m.name for m in members))

    def test_invalid_file_not_archived(self):
        """Test that invalid files are not archived."""
        result = task_func(directory=str(self.test_dir), file_pattern=PATTERN)
        with tarfile.open(result) as tar:
            members = tar.getmembers()
            self.assertNotIn('Distillr_AcroTray.exe', (m.name for m in members))

    def test_other_file_not_archived(self):
        """Test that files that do not match the pattern are not archived."""
        result = task_func(directory=str(self.test_dir), file_pattern=PATTERN)
        with tarfile.open(result) as tar:
            members = tar.getmembers()
            self.assertNotIn('other_file.txt', (m.name for m in members))

    def test_empty_directory(self):
        """Test that no files are archived in an empty directory."""
        empty_dir = Path('./empty_test_directory')
        empty_dir.mkdir(exist_ok=True)
        result = task_func(directory=str(empty_dir), file_pattern=PATTERN)
        self.assertTrue(Path(result).is_file())
        with tarfile.open(result) as tar:
            members = tar.getmembers()
            self.assertEqual(members, []
        empty_dir.rmdir()

if __name__ == '__main__':
    unittest.main()