import unittest
import os
from unittest.mock import patch, mock_open

# Redefining the function in the current context

HEADERS = {
    'accept': 'text/json',
    'Content-Type': 'application/json'
}

def task_func(url, directory, metadata):
    files = os.listdir(directory)
    status_codes = []

    for file in files:
        if os.path.isfile(os.path.join(directory, file)):
            with open(os.path.join(directory, file), 'rb') as f:
                files = {'file': f}
                response = requests.post(url, files=files, headers=HEADERS, data=json.dumps(metadata))
                status_codes.append(response.status_code)
                time.sleep(1)

    return status_codes

class TestTaskFunc(unittest.TestCase):

    @patch('os.listdir', return_value=['file1.txt', 'file2.txt'])
    @patch('os.path.isfile', side_effect=lambda x: True)
    @patch('builtins.open', new_callable=mock_open, read_data=b'file content')
    @patch('requests.post')
    def test_successful_file_upload(self, mock_post, mock_open, mock_isfile, mock_listdir):
        mock_post.return_value.status_code = 200
        url = 'https://www.example.com'
        directory = './uploads'
        metadata = {'userId': 'abc'}

        result = task_func(url, directory, metadata)

        self.assertEqual(result, [200, 200])
        self.assertEqual(mock_post.call_count, 2)

    @patch('os.listdir', return_value=[])
    def test_no_files_in_directory(self, mock_listdir):
        url = 'https://www.example.com'
        directory = './uploads'
        metadata = {'userId': 'abc'}

        result = task_func(url, directory, metadata)

        self.assertEqual(result, [])
        
    @patch('os.listdir', return_value=['file1.txt'])
    @patch('os.path.isfile', return_value=False)
    @patch('requests.post')
    def test_no_files_uploaded(self, mock_post, mock_isfile, mock_listdir):
        url = 'https://www.example.com'
        directory = './uploads'
        metadata = {'userId': 'abc'}

        result = task_func(url, directory, metadata)

        self.assertEqual(result, [])
        self.assertEqual(mock_post.call_count, 0)

    @patch('requests.post')
    def test_invalid_url_raises_type_error(self, mock_post):
        url = 'invalid_url'
        directory = './uploads'
        metadata = {'userId': 'abc'}

        with self.assertRaises(TypeError):
            task_func(url, directory, metadata)

    @patch('os.listdir', return_value=['file1.txt'])
    @patch('os.path.isfile', side_effect=FileNotFoundError)
    def test_directory_not_found(self, mock_isfile, mock_listdir):
        url = 'https://www.example.com'
        directory = './invalid_directory'
        metadata = {'userId': 'abc'}

        with self.assertRaises(FileNotFoundError):
            task_func(url, directory, metadata)

if __name__ == '__main__':
    unittest.main()