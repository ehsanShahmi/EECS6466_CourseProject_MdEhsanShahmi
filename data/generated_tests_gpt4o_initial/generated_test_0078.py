import csv
import io
from django.http import HttpRequest, FileResponse
import unittest

def task_func(request, header, csv_data):
    csv_io = io.StringIO()
    writer = csv.writer(csv_io)
    writer.writerow(header)
    writer.writerows(csv_data)
    csv_io.seek(0)

    response = FileResponse(csv_io, as_attachment=True, filename='data.csv')
    response['Content-Type'] = 'text/csv'

    return response

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.request = HttpRequest()
    
    def test_response_content_type(self):
        header = ['id', 'name', 'email']
        csv_data = [['1', 'John Doe', 'john@example.com']]
        response = task_func(self.request, header, csv_data)
        self.assertEqual(response['Content-Type'], 'text/csv')
    
    def test_response_content_disposition(self):
        header = ['id', 'name', 'email']
        csv_data = [['1', 'John Doe', 'john@example.com']]
        response = task_func(self.request, header, csv_data)
        self.assertEqual(response['Content-Disposition'], 'attachment; filename="data.csv"')
    
    def test_csv_data_format(self):
        header = ['id', 'name', 'email']
        csv_data = [['1', 'John Doe', 'john@example.com'], ['2', 'Jane Doe', 'jane@example.com']]
        response = task_func(self.request, header, csv_data)
        
        expected_output = "id,name,email\r\n1,John Doe,john@example.com\r\n2,Jane Doe,jane@example.com\r\n"
        self.assertEqual(response.streaming_content.read().decode('utf-8'), expected_output)
    
    def test_empty_csv_data(self):
        header = ['id', 'name', 'email']
        csv_data = []
        response = task_func(self.request, header, csv_data)
        
        expected_output = "id,name,email\r\n"
        self.assertEqual(response.streaming_content.read().decode('utf-8'), expected_output)
    
    def test_multiple_rows_csv(self):
        header = ['id', 'name', 'email']
        csv_data = [['1', 'John Doe', 'john@example.com'], ['2', 'Jane Doe', 'jane@example.com'], ['3', 'Jim Doe', 'jim@example.com']]
        response = task_func(self.request, header, csv_data)
        
        expected_output = "id,name,email\r\n1,John Doe,john@example.com\r\n2,Jane Doe,jane@example.com\r\n3,Jim Doe,jim@example.com\r\n"
        self.assertEqual(response.streaming_content.read().decode('utf-8'), expected_output)

if __name__ == '__main__':
    unittest.main()