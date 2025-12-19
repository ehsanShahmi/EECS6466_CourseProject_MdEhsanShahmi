import unittest
import os

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        # Create a test file for testing purposes
        self.test_filename = "test.txt"
        with open(self.test_filename, "w") as f:
            f.write("This is a test file.")

    def tearDown(self):
        # Clean up the test file after tests
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_file_found(self):
        request = "GET /test.txt HTTP/1.1"
        expected_response = f"HTTP/1.1 200 OK\r\nContent-Length: {len('This is a test file.')}\r\n\r\nThis is a test file."
        actual_response = task_func(request)
        self.assertEqual(actual_response, expected_response)

    def test_file_not_found(self):
        request = "GET /nonexistent.txt HTTP/1.1"
        expected_response = "HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found"
        actual_response = task_func(request)
        self.assertEqual(actual_response, expected_response)

    def test_invalid_request_format(self):
        request = "INVALID REQUEST"
        expected_response = "HTTP/1.1 400 BAD REQUEST\r\n\r\nBad Request"
        actual_response = task_func(request)
        self.assertEqual(actual_response, expected_response)

    def test_io_error_handling(self):
        # Create a restricted file that cannot be opened
        restricted_filename = "restricted.txt"
        with open(restricted_filename, "w") as f:
            f.write("Restricted content.")
        os.chmod(restricted_filename, 0o000)  # Remove all permissions

        request = "GET /restricted.txt HTTP/1.1"
        expected_response = "HTTP/1.1 500 INTERNAL SERVER ERROR\r\n\r\nInternal Server Error"
        actual_response = task_func(request)
        
        # Restore permissions for cleanup
        os.chmod(restricted_filename, 0o644)
        os.remove(restricted_filename)

        self.assertEqual(actual_response, expected_response)

    def test_multiple_requests(self):
        request1 = "GET /test.txt HTTP/1.1"
        request2 = "GET /nonexistent.txt HTTP/1.1"
        
        expected_response1 = f"HTTP/1.1 200 OK\r\nContent-Length: {len('This is a test file.')}\r\n\r\nThis is a test file."
        expected_response2 = "HTTP/1.1 404 NOT FOUND\r\n\r\nFile Not Found"
        
        actual_response1 = task_func(request1)
        actual_response2 = task_func(request2)
        
        self.assertEqual(actual_response1, expected_response1)
        self.assertEqual(actual_response2, expected_response2)

if __name__ == '__main__':
    unittest.main()