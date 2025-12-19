import unittest
from unittest.mock import patch, MagicMock
import os
import subprocess
from datetime import datetime

# Here is your prompt:
import subprocess
import os
import time
from datetime import datetime


def task_func(script_dir, scripts, delay):
    """
    Execute a list of bash scripts with a specified delay between each script.

    Parameters:
    script_dir (str): Path to the directory containing the scripts.
    scripts (list): List of script filenames to be executed. Must not be empty.
                    If a script is not found, the function raises a FileNotFoundError.
    delay (int): The delay in seconds between each script execution. Must at least 0.

    Returns:
    list: A list of timestamps indicating the start time of each script execution.

    Raises:
    - ValueError: If the delay is negative or no scripts are provided.
    
    Requirements:
    - subprocess
    - os
    - time
    - datetime.datetime

    Example:
    >>> task_func('/path/to/scripts/', ['script1.sh', 'script2.sh'], 5)
    ['2023-09-09 10:10:10', '2023-09-09 10:10:15']
    """

               if delay < 0:
        raise ValueError("delay cannot be negative.")
    if not scripts:
        raise ValueError("No scripts provided.")
    start_times = []
    for script in scripts:
        script_path = os.path.join(script_dir, script)
        start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        start_times.append(start_time)

        result = subprocess.call(script_path, shell=True)
        if result != 0:
            raise FileNotFoundError(f"Script not found: {script_path}")

        time.sleep(delay)
    return start_times

class TestTaskFunction(unittest.TestCase):

    @patch('os.path.join', side_effect=lambda a, b: f"{a}/{b}")
    @patch('subprocess.call', return_value=0)
    @patch('time.sleep', return_value=None)  # To avoid actual sleeping
    def test_successful_execution(self, mock_sleep, mock_call, mock_join):
        result = task_func('/path/to/scripts', ['script1.sh', 'script2.sh'], 5)
        self.assertEqual(len(result), 2)
    
    @patch('subprocess.call', side_effect=FileNotFoundError("Script not found"))
    def test_file_not_found(self, mock_call):
        with self.assertRaises(FileNotFoundError):
            task_func('/path/to/scripts', ['non_existent_script.sh'], 5)

    def test_empty_script_list(self):
        with self.assertRaises(ValueError) as context:
            task_func('/path/to/scripts', [], 5)
        self.assertEqual(str(context.exception), "No scripts provided.")

    def test_negative_delay(self):
        with self.assertRaises(ValueError) as context:
            task_func('/path/to/scripts', ['script.sh'], -1)
        self.assertEqual(str(context.exception), "delay cannot be negative.")

    @patch('subprocess.call', return_value=0)
    @patch('time.sleep', return_value=None)
    def test_execution_timestamps(self, mock_sleep, mock_call):
        with patch('datetime.datetime') as mock_datetime:
            mock_datetime.now.return_value.strftime.return_value = '2023-09-09 10:10:10'
            result = task_func('/path/to/scripts', ['script1.sh'], 5)
            self.assertEqual(result, ['2023-09-09 10:10:10'])

if __name__ == '__main__':
    unittest.main()