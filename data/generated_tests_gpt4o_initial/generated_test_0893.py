import unittest
import re
from datetime import time

def task_func(logs: list):
    """
    Analyze the given list of logs for the occurrence of errors and calculate the average time of occurrence of errors.
    
    Parameters:
    - logs (list): A list of log strings.
    
    Returns:
    - list: A list of times when errors occurred.
    - time: The average time of occurrence of these errors.
    
    Requirements:
    - re
    - datetime
    
    Example:
    >>> task_func(['2021-06-15 09:45:00 ERROR: Failed to connect to database',\
            '2021-06-15 10:15:00 WARNING: Low disk space',\
            '2021-06-15 10:35:00 INFO: Backup completed successfully'])
    ([datetime.time(9, 45)], datetime.time(9, 45))
    """

               
    error_times = []
    total_time = 0

    for log in logs:
        if "ERROR" in log:
            time_match = re.search(r'(\d{2}):(\d{2}):\d{2}', log)
            if time_match:
                hour, minute = map(int, time_match.groups())
                error_times.append(time(hour, minute))
                total_time += hour * 60 + minute

    if error_times:
        avg_hour = (total_time // len(error_times)) // 60
        avg_minute = (total_time // len(error_times)) % 60
        avg_time = time(avg_hour, avg_minute)
    else:
        avg_time = time(0, 0)

    return error_times, avg_time

class TestTaskFunc(unittest.TestCase):
    
    def test_no_errors(self):
        logs = [
            '2021-06-15 10:15:00 WARNING: Low disk space',
            '2021-06-15 10:35:00 INFO: Backup completed successfully'
        ]
        expected = ([], time(0, 0))
        self.assertEqual(task_func(logs), expected)

    def test_single_error(self):
        logs = [
            '2021-06-15 09:45:00 ERROR: Failed to connect to database'
        ]
        expected = ([time(9, 45)], time(9, 45))
        self.assertEqual(task_func(logs), expected)

    def test_multiple_errors(self):
        logs = [
            '2021-06-15 09:45:00 ERROR: Failed to connect to database',
            '2021-06-15 10:05:00 ERROR: Timeout occurred',
            '2021-06-15 10:25:00 WARNING: Low memory'
        ]
        expected = ([time(9, 45), time(10, 5)], time(9, 55))
        self.assertEqual(task_func(logs), expected)

    def test_errors_at_midnight(self):
        logs = [
            '2021-06-15 00:00:00 ERROR: System crashed',
            '2021-06-15 01:30:00 ERROR: Disk failure'
        ]
        expected = ([time(0, 0), time(1, 30)], time(0, 45))
        self.assertEqual(task_func(logs), expected)

    def test_errors_with_invalid_time(self):
        logs = [
            '2021-06-15 15:30:00 ERROR: Could not open file',
            '2021-06-15 18:00:00 ERROR: Network unresponsive',
            'Invalid log entry',
            '2021-06-15 18:30:00 INFO: Task completed'
        ]
        expected = ([time(15, 30), time(18, 0)], time(16, 15))
        self.assertEqual(task_func(logs), expected)

if __name__ == '__main__':
    unittest.main()