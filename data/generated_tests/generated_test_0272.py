import cgi
import http.server
import json
import unittest
from http.client import HTTPConnection

def task_func():
    """
    The function creates an HTTP POST request handler for processing incoming data. The data is expected to be in JSON format with a key 'data'. The handler responds with a 200 success message if the data is valid, or an error message otherwise.

    Notes:
    - If the 'Content-Type' header is not 'application/json', the server responds with a 400 Bad Request status and a JSON object:
      {"status": "error", "message": "Content-Type header is not application/json"}.
    - If the received JSON object does not contain a 'data' key, the response is a 400 Bad Request with a JSON object:
      {"status": "error", "message": "No data received"}.
    - For successfully processed requests, the server responds with a 200 OK status and a JSON object:
      {"status": "success", "message": "Data received successfully."}.

    Returns:
    class: A class that is a subclass of http.server.BaseHTTPRequestHandler, designed to handle HTTP POST requests.
    """
    class PostRequestHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
            
            # Define error response directly within the method
            error_response = {
                'status': 'error',
                'message': ''  # This will be modified based on the error condition
            }
            
            if ctype != 'application/json':
                self.send_response(400)
                self.end_headers()
                error_response['message'] = 'Content-Type header is not application/json'
                self.wfile.write(json.dumps(error_response).encode())
                return

            length = int(self.headers.get('content-length'))
            message = json.loads(self.rfile.read(length))
            
            if 'data' not in message:
                self.send_response(400)
                self.end_headers()
                error_response['message'] = 'No data received'
                self.wfile.write(json.dumps(error_response).encode())
                return

            # Define success response directly within the method
            success_response = {
                'status': 'success',
                'message': 'Data received successfully.'
            }
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(success_response).encode())

    return PostRequestHandler

class TestPostRequestHandler(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.port = 8080
        cls.handler = task_func()
        cls.server = http.server.HTTPServer(('localhost', cls.port), cls.handler)

    @classmethod
    def tearDownClass(cls):
        cls.server.server_close()

    def setUp(self):
        self.conn = HTTPConnection('localhost', self.port)

    def tearDown(self):
        self.conn.close()

    def test_invalid_content_type(self):
        self.conn.request('POST', '/', body=json.dumps({'data': 'test'}), headers={'Content-Type': 'text/plain'})
        response = self.conn.getresponse()
        self.assertEqual(response.status, 400)
        response_data = json.loads(response.read())
        self.assertEqual(response_data, {'status': 'error', 'message': 'Content-Type header is not application/json'})

    def test_no_data_key(self):
        self.conn.request('POST', '/', body=json.dumps({}), headers={'Content-Type': 'application/json'})
        response = self.conn.getresponse()
        self.assertEqual(response.status, 400)
        response_data = json.loads(response.read())
        self.assertEqual(response_data, {'status': 'error', 'message': 'No data received'})

    def test_valid_request(self):
        self.conn.request('POST', '/', body=json.dumps({'data': 'test data'}), headers={'Content-Type': 'application/json'})
        response = self.conn.getresponse()
        self.assertEqual(response.status, 200)
        response_data = json.loads(response.read())
        self.assertEqual(response_data, {'status': 'success', 'message': 'Data received successfully.'})

    def test_empty_json(self):
        self.conn.request('POST', '/', body='{}', headers={'Content-Type': 'application/json'})
        response = self.conn.getresponse()
        self.assertEqual(response.status, 400)
        response_data = json.loads(response.read())
        self.assertEqual(response_data, {'status': 'error', 'message': 'No data received'})

    def test_no_content_type_header(self):
        self.conn.request('POST', '/', body=json.dumps({'data': 'test data'}), headers={})
        response = self.conn.getresponse()
        self.assertEqual(response.status, 400)
        response_data = json.loads(response.read())
        self.assertEqual(response_data, {'status': 'error', 'message': 'Content-Type header is not application/json'})

if __name__ == '__main__':
    unittest.main()