import os
import unittest

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        # Create a temporary log file for testing
        self.log_file_path = 'test_log_file.log'
        with open(self.log_file_path, 'w') as log:
            log.write("INFO 11:30:00 This is an info message\n")
            log.write("ERROR 11:30:10 This is an error message\n")
            log.write("WARNING 11:35:10 This is a warning message\n")
            log.write("ERROR 11:35:20 Another error occurred\n")
            log.write("INFO 11:40:00 This is another info message\n")
    
    def tearDown(self):
        # Remove the temporary log file after tests
        if os.path.exists(self.log_file_path):
            os.remove(self.log_file_path)

    def test_keywords_found(self):
        result = task_func(self.log_file_path, ['ERROR', 'WARNING'])
        expected = [
            '               ERROR :               11:30:10 : This is an error message',
            '             WARNING :               11:35:10 : This is a warning message',
            '               ERROR :               11:35:20 : Another error occurred'
        ]
        self.assertListEqual(result, expected)

    def test_no_keywords_found(self):
        result = task_func(self.log_file_path, ['DEBUG'])
        expected = []
        self.assertListEqual(result, expected)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_file.log', ['ERROR'])

    def test_unexpected_line_format(self):
        with open(self.log_file_path, 'a') as log:
            log.write("INVALID LINE FORMAT\n")
        result = task_func(self.log_file_path, ['ERROR'])
        expected = [
            '               ERROR :               11:30:10 : This is an error message',
            '               ERROR :               11:35:20 : Another error occurred',
            'Line format unexpected: INVALID LINE FORMAT'
        ]
        self.assertListEqual(result, expected)

    def test_multiple_keywords(self):
        result = task_func(self.log_file_path, ['INFO', 'ERROR', 'WARNING'])
        expected = [
            '               ERROR :               11:30:10 : This is an error message',
            '             WARNING :               11:35:10 : This is a warning message',
            '                INFO :               11:30:00 : This is an info message',
            '                INFO :               11:40:00 : This is another info message',
            '               ERROR :               11:35:20 : Another error occurred'
        ]
        self.assertListEqual(result, expected)

if __name__ == '__main__':
    unittest.main()