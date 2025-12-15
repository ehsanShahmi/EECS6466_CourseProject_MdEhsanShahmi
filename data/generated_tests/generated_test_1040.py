import socket
import select
import queue
from datetime import datetime, timedelta
import unittest
from unittest.mock import patch, MagicMock

class TestTaskFunc(unittest.TestCase):

    @patch('socket.socket')
    def test_server_initialization(self, mock_socket):
        # Mock server socket to test initialization
        mock_server = MagicMock()
        mock_socket.return_value = mock_server
        
        # Call the function
        result = task_func("localhost", 12345, 1024, 1)
        
        # Verify server binding and listening
        mock_server.bind.assert_called_with(("localhost", 12345))
        mock_server.listen.assert_called_with(5)
        self.assertIn("Server started on localhost:12345.", result)

    @patch('socket.socket')
    @patch('select.select')
    def test_server_run_duration(self, mock_select, mock_socket):
        # Mock server behavior and select function
        mock_server = MagicMock()
        mock_socket.return_value = mock_server
        mock_select.return_value = ([], [], [])
        
        # Call the function
        result = task_func("localhost", 12345, 1024, 3)
        
        # Verify the run duration message
        self.assertIn("Ran for 3 seconds.", result)

    @patch('socket.socket')
    @patch('select.select')
    def test_receive_and_send_data(self, mock_select, mock_socket):
        # Mock server behavior
        mock_server = MagicMock()
        mock_socket.return_value = mock_server
        
        fake_connection = MagicMock()
        fake_connection.recv.return_value = b"Hello"
        mock_select.return_value = ([fake_connection], [], [])

        # Call the function
        task_func("localhost", 12345, 1024, 1)
        
        # Verify that data is received and sent
        fake_connection.recv.assert_called_with(1024)

    @patch('socket.socket')
    @patch('select.select')
    def test_server_exception_handling(self, mock_select, mock_socket):
        # Simulate an exception during socket operations
        mock_server = MagicMock()
        mock_socket.return_value = mock_server
        mock_select.side_effect = Exception("Socket error")

        # Call the function and ensure it handles exceptions gracefully
        try:
            result = task_func("localhost", 12345, 1024, 1)
        except Exception:
            result = "Exception handled"
        
        self.assertEqual(result, "Exception handled")

    @patch('socket.socket')
    def test_close_server_socket(self, mock_socket):
        mock_server = MagicMock()
        mock_socket.return_value = mock_server
        
        # Call the function
        task_func("localhost", 12345, 1024, 1)

        # Verify that the server socket is closed at the end
        mock_server.close.assert_called_once()

if __name__ == "__main__":
    unittest.main()