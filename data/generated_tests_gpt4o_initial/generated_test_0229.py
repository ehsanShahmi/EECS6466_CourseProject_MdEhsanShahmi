import json
import os
import unittest


# Here is your prompt:
import json
import random
from datetime import datetime, timedelta


# Constants
USERS = ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve']

def task_func(file_path, num_entries, seed=None):
    """
    Create a JSON file on a specific file path with random user activity data.
    The number of entries in the JSON file is determined by num_entries. The written JSON file contains a list of dictionaries, with each dictionary representing a log entry with the following keys: 'user', 'action', and 'timestamp'.

    Parameters:
    file_path (str): The file path where the JSON file should be created.
    num_entries (int): The number of entries of random data to generate.
    seed (int, optional): The seed for random data generation. Default is None.

    Returns:
    str: The file path of the generated JSON file.

    Requirements:
    - os
    - json
    - random
    - datetime

    Example:
    >>> task_func('/tmp/log.json', 100)
    '/tmp/log.json'
    """

               if seed is not None:
        random.seed(seed)
    
    log_entries = []
    current_time = datetime.now()
    for _ in range(num_entries):
        user = random.choice(USERS)
        action = random.choice(['login', 'logout', 'view_page', 'edit_profile', 'post_message'])
        timestamp = current_time.strftime('%Y-%m-%dT%H:%M:%S')
        log_entries.append({'user': user, 'action': action, 'timestamp': timestamp})
        current_time -= timedelta(minutes=random.randint(1, 60))

    with open(file_path, 'w') as json_file:
        json.dump(log_entries, json_file, indent=4)

    return file_path


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.test_file_path = 'test_logs.json'

    def tearDown(self):
        try:
            os.remove(self.test_file_path)
        except OSError:
            pass

    def test_output_file_creation(self):
        """Tests if the function creates the expected output file."""
        result = task_func(self.test_file_path, 10)
        self.assertEqual(result, self.test_file_path)
        self.assertTrue(os.path.exists(self.test_file_path))

    def test_correct_number_of_entries(self):
        """Tests if the created JSON file has the correct number of log entries."""
        num_entries = 50
        task_func(self.test_file_path, num_entries)
        with open(self.test_file_path, 'r') as json_file:
            log_entries = json.load(json_file)
            self.assertEqual(len(log_entries), num_entries)

    def test_entries_structure(self):
        """Tests if each log entry has the expected structure."""
        task_func(self.test_file_path, 5)
        with open(self.test_file_path, 'r') as json_file:
            log_entries = json.load(json_file)
            for entry in log_entries:
                self.assertIn('user', entry)
                self.assertIn('action', entry)
                self.assertIn('timestamp', entry)

    def test_entries_with_seed(self):
        """Tests the function with a seed to ensure reproducibility."""
        seed = 42
        task_func(self.test_file_path, 5, seed)
        with open(self.test_file_path, 'r') as json_file:
            log_entries_a = json.load(json_file)

        task_func(self.test_file_path, 5, seed)
        with open(self.test_file_path, 'r') as json_file:
            log_entries_b = json.load(json_file)

        self.assertEqual(log_entries_a, log_entries_b)

    def test_timestamp_order(self):
        """Tests if the entries' timestamps are in descending order."""
        task_func(self.test_file_path, 10)
        with open(self.test_file_path, 'r') as json_file:
            log_entries = json.load(json_file)
            timestamps = [entry['timestamp'] for entry in log_entries]
            self.assertTrue(all(t1 >= t2 for t1, t2 in zip(timestamps, timestamps[1:])))
            

if __name__ == '__main__':
    unittest.main()