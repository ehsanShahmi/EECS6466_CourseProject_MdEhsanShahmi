import unittest
import socket
import json
from datetime import datetime

SERVER_ADDRESS = "localhost"
BUFFER_SIZE = 1024


def task_func(client_socket):
    response_data = {"message": "Hello", "time": str(datetime.now())}
    response = json.dumps(response_data) + "\n"
    client_socket.send(response.encode("utf-8"))
    client_socket.close()


class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((SERVER_ADDRESS, 0))  # Bind to a free port
        self.server_socket.listen(1)
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(self.server_socket.getsockname())

    def tearDown(self):
        self.client_socket.close()
        self.server_socket.close()

    def test_response_format(self):
        client_socket, _ = self.server_socket.accept()
        task_func(client_socket)
        
        # Receive response
        response = self.client_socket.recv(BUFFER_SIZE).decode("utf-8")
        self.assertTrue(response.endswith("\n"))  # Response should end with a newline
        
        response_data = json.loads(response.strip())
        self.assertIn("message", response_data)
        self.assertIn("time", response_data)
        self.assertEqual(response_data["message"], "Hello")

    def test_time_format(self):
        client_socket, _ = self.server_socket.accept()
        task_func(client_socket)
        
        # Receive response
        response = self.client_socket.recv(BUFFER_SIZE).decode("utf-8")
        response_data = json.loads(response.strip())
        
        time_str = response_data["time"]
        # Check if the time is in a valid format
        try:
            datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S.%f")
        except ValueError:
            self.fail("Time format is invalid")

    def test_multiple_clients(self):
        num_clients = 5
        responses = []

        for _ in range(num_clients):
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect(self.server_socket.getsockname())
            self.server_socket.listen(1)
            client_socket, _ = self.server_socket.accept()
            task_func(client_socket)
            response = client_socket.recv(BUFFER_SIZE).decode("utf-8")
            responses.append(response.strip())

        self.assertEqual(len(responses), num_clients)

    def test_json_response(self):
        client_socket, _ = self.server_socket.accept()
        task_func(client_socket)
        
        # Receive response
        response = self.client_socket.recv(BUFFER_SIZE).decode("utf-8")
        response_data = json.loads(response.strip())
        
        # Check if the response is a valid JSON
        self.assertIsInstance(response_data, dict)
        self.assertIn("time", response_data)
        self.assertIn("message", response_data)

    def test_socket_close(self):
        client_socket, _ = self.server_socket.accept()
        task_func(client_socket)

        # Attempt to read from the closed socket should raise an error
        with self.assertRaises(OSError):
            self.client_socket.recv(BUFFER_SIZE)
          
if __name__ == '__main__':
    unittest.main()