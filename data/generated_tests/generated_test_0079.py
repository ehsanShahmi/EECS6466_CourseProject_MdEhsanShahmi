import zipfile
import io
from django.http import FileResponse, HttpRequest
from django.conf import settings
import unittest

def task_func(request, file_paths):
    """
    Generates a ZIP file response for a Django HttpRequest, zipping the specified files.
    """
    zip_io = io.BytesIO()
    with zipfile.ZipFile(zip_io, 'w') as zip_file:
        for file_path in file_paths:
            zip_file.writestr(file_path, 'This is the content of {}.'.format(file_path))
    zip_io.seek(0)  # Reset the file pointer to the start of the stream
    response = FileResponse(zip_io, as_attachment=True, filename='files.zip')
    response['Content-Type'] = 'application/zip'
    return response

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.request = HttpRequest()

    def test_response_type(self):
        response = task_func(self.request, ['file1.txt'])
        self.assertIsInstance(response, FileResponse)

    def test_content_type(self):
        response = task_func(self.request, ['file1.txt'])
        self.assertEqual(response['Content-Type'], 'application/zip')

    def test_content_disposition(self):
        response = task_func(self.request, ['file1.txt'])
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="files.zip"')

    def test_zip_contents(self):
        file_paths = ['file1.txt', 'file2.txt']
        response = task_func(self.request, file_paths)
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
            self.assertIn('file1.txt', zip_file.namelist())
            self.assertIn('file2.txt', zip_file.namelist())

    def test_zip_contents_correctness(self):
        file_paths = ['file1.txt', 'file2.txt']
        response = task_func(self.request, file_paths)
        with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
            for file_name in zip_file.namelist():
                with zip_file.open(file_name) as file:
                    content = file.read().decode()
                    self.assertEqual(content, f'This is the content of {file_name}.')
                    
if __name__ == '__main__':
    unittest.main()