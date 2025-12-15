import os
import unittest
from unittest.mock import patch, mock_open

OUTPUT_DIR = './output'

# Here is your prompt:
import binascii
import hashlib
import re


def task_func(directory: str, pattern: str = r"(?<!Distillr)\\AcroTray\.exe") -> dict:
    """
    Searches for files within the specified directory matching a given regex pattern
    and computes a SHA256 hash of each file's content.

    Parameters:
    - directory (str): Directory to search for files.
    - pattern (str): Regex pattern that filenames must match. Default pattern matches 'AcroTray.exe'.

    Returns:
    - dict: A dictionary with file paths as keys and their SHA256 hashes as values.

    Requirements:
    - re
    - hashlib
    - binascii

    Example:
    >>> task_func(OUTPUT_DIR)
    {}
    """

    hashes = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if re.search(pattern, file):
                path = os.path.join(root, file)
                with open(path, 'rb') as f:
                    data = f.read()
                    hash_digest = hashlib.sha256(data).digest()
                    hashes[path] = binascii.hexlify(hash_digest).decode()
    return hashes


class TestTaskFunction(unittest.TestCase):

    @patch("os.walk")
    @patch("builtins.open", new_callable=mock_open, read_data=b"sample data")
    def test_matching_file_found(self, mock_file, mock_walk):
        mock_walk.return_value = [('./', [], ['AcroTray.exe'])]
        expected_hash = hashlib.sha256(b"sample data").hexdigest()
        result = task_func(OUTPUT_DIR)
        self.assertEqual(result, {'./AcroTray.exe': expected_hash})

    @patch("os.walk")
    def test_no_matching_file(self, mock_walk):
        mock_walk.return_value = [('./', [], ['otherfile.txt'])]
        result = task_func(OUTPUT_DIR)
        self.assertEqual(result, {})

    @patch("os.walk")
    @patch("builtins.open", new_callable=mock_open, read_data=b"data to hash")
    def test_multiple_matching_files(self, mock_file, mock_walk):
        mock_walk.return_value = [('./', [], ['AcroTray.exe', 'AcroTray2.exe'])]
        expected_hash1 = hashlib.sha256(b"data to hash").hexdigest()
        mock_file.side_effect = [mock_open(read_data=b"data to hash").return_value,
                                  mock_open(read_data=b"data to hash").return_value]
        result = task_func(OUTPUT_DIR)
        self.assertEqual(
            result,
            {'./AcroTray.exe': expected_hash1, './AcroTray2.exe': expected_hash1}
        )

    @patch("os.walk")
    @patch("builtins.open", new_callable=mock_open, read_data=b"")
    def test_empty_file(self, mock_file, mock_walk):
        mock_walk.return_value = [('./', [], ['AcroTray.exe'])]
        expected_hash = hashlib.sha256(b"").hexdigest()
        result = task_func(OUTPUT_DIR)
        self.assertEqual(result, {'./AcroTray.exe': expected_hash})

    @patch("os.walk")
    def test_special_characters_in_filename(self, mock_walk):
        mock_walk.return_value = [('./', [], ['DistillrAcroTray.exe'])]
        result = task_func(OUTPUT_DIR)
        self.assertEqual(result, {})


if __name__ == '__main__':
    unittest.main()