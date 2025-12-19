import unittest
import os
import urllib.request
import zipfile


# Here is your prompt:
import urllib.request
import os
import zipfile

# Constants
TARGET_DIR = "downloaded_files"
TARGET_ZIP_FILE = "downloaded_files.zip"

def task_func(url):
    """
    Download and extract a zip file from a specified URL to a designated directory.

    Parameters:
    - url (str): The URL of the zip file.

    Returns:
    - str: The path of the directory where the contents of the zip file are extracted.

    Requirements:
      - urllib
      - os
      - zipfile

    Behavior:
    - If the target directory TARGET_DIR does not exist, it is created.
    - The zip file is downloaded from the given URL and saved locally as TARGET_ZIP_FILE.
    - The local zip file TARGET_ZIP_FILE is deleted after extraction.

    Error Handling:
    - The function does not explicitly handle errors that may occur during the download or extraction process.
      Errors such as a failed download, invalid URL, or corrupted zip file will result in an unhandled exception.

    Examples:
    >>> task_func("http://example.com/files.zip")
    'downloaded_files'
    """

    os.makedirs(TARGET_DIR, exist_ok=True)

    # context = ssl._create_unverified_context()
    # urllib.request.urlretrieve(url, TARGET_ZIP_FILE, context=context)
    urllib.request.urlretrieve(url, TARGET_ZIP_FILE)

    with zipfile.ZipFile(TARGET_ZIP_FILE, "r") as zip_ref:
        zip_ref.extractall(TARGET_DIR)

    if os.path.exists(TARGET_ZIP_FILE):
        os.remove(TARGET_ZIP_FILE)

    return TARGET_DIR


class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        """Set up the test environment."""
        self.test_url = "http://example.com/test.zip"
        self.nonexistent_url = "http://example.com/nonexistent.zip"
        self.invalid_url = "not_a_valid_url"
        self.zip_content = "test_file.txt"
        os.makedirs("test_files", exist_ok=True)

        # Create a test zip file
        with zipfile.ZipFile("test.zip", 'w') as zf:
            zf.writestr(self.zip_content, "This is a test file.")
    
    def tearDown(self):
        """Clean up the test environment."""
        if os.path.exists("test.zip"):
            os.remove("test.zip")
        if os.path.exists(TARGET_DIR):
            for file in os.listdir(TARGET_DIR):
                os.remove(os.path.join(TARGET_DIR, file))
            os.rmdir(TARGET_DIR)

    def test_download_and_extract(self):
        """Test downloading and extracting a zip file from a valid URL."""
        with open("test.zip", "rb") as f:
            self.test_url = "http://localhost/test.zip"
            urllib.request.urlopen(self.test_url).write(f.read())  # Simulate hosting the zip file
            
        result = task_func(self.test_url)
        self.assertEqual(result, TARGET_DIR)
        self.assertTrue(os.path.exists(os.path.join(TARGET_DIR, self.zip_content)))

    def test_create_directory(self):
        """Test if target directory is created if it doesn't exist."""
        if os.path.exists(TARGET_DIR):
            os.rmdir(TARGET_DIR)
        
        result = task_func(self.test_url)
        self.assertTrue(os.path.exists(TARGET_DIR))
        self.assertEqual(result, TARGET_DIR)

    def test_invalid_url(self):
        """Test handling of an invalid URL."""
        with self.assertRaises(ValueError):
            task_func(self.invalid_url)

    def test_nonexistent_url(self):
        """Test handling of a nonexistent URL."""
        with self.assertRaises(urllib.error.URLError):
            task_func(self.nonexistent_url)

if __name__ == "__main__":
    unittest.main()