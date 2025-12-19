import unittest
import os
import json
from datetime import datetime
from unittest.mock import patch, MagicMock

# Here is your prompt:
import subprocess
import os
import json
from datetime import datetime

def task_func(script_name='backup.sh', log_file='/home/user/backup_log.json'):
    """
    Runs the provided backup shell script and logs the start time, end time, and exit status 
    in a specified JSON log file.
    
    Parameters:
    - script_name (str): The name of the shell script to run. Default is 'backup.sh'.
    - log_file (str): The path to the JSON log file where the execution details will be recorded. Default is '/home/user/backup_log.json'.
    
    Returns:
    dict: A dictionary containing:
        - 'start_time': The start time of the script execution in the format '%Y-%m-%d %H:%M:%S'.
        - 'end_time': The end time of the script execution in the format '%Y-%m-%d %H:%M:%S'.
        - 'exit_status': The exit status of the script execution (0 for success, other values indicate an error).
    
    Raises:
    - FileNotFoundError: If the script file does not exist.
    - RuntimeError: If there is an error executing the script.
        
    Requirements:
    - subprocess
    - os
    - datetime
    - json
    
    Example:
    >>> task_func()
    {'start_time': '2023-09-19 14:30:00', 'end_time': '2023-09-19 14:35:00', 'exit_status': 0}
    """

    log_data = {}

    if not os.path.isfile(script_name):
        raise FileNotFoundError(f"Script {script_name} does not exist.")

    start_time = datetime.now()
    log_data['start_time'] = start_time.strftime('%Y-%m-%d %H:%M:%S')

    try:
        exit_status = subprocess.call(['./' + script_name])
    except Exception as e:
        raise RuntimeError(f"Failed to run {script_name}: {str(e)}")

    end_time = datetime.now()
    log_data['end_time'] = end_time.strftime('%Y-%m-%d %H:%M:%S')
    log_data['exit_status'] = exit_status

    with open(log_file, 'w') as f:
        json.dump(log_data, f)
    
    return log_data

class TestTaskFunc(unittest.TestCase):

    @patch('os.path.isfile')
    def test_script_not_found(self, mock_isfile):
        mock_isfile.return_value = False
        with self.assertRaises(FileNotFoundError):
            task_func(script_name='non_existent.sh')

    @patch('os.path.isfile')
    @patch('subprocess.call')
    def test_script_success(self, mock_call, mock_isfile):
        mock_isfile.return_value = True
        mock_call.return_value = 0  # Simulating successful execution
        result = task_func(script_name='backup.sh', log_file='test_log.json')
        self.assertIn('start_time', result)
        self.assertIn('end_time', result)
        self.assertEqual(result['exit_status'], 0)

    @patch('os.path.isfile')
    @patch('subprocess.call')
    def test_script_failure(self, mock_call, mock_isfile):
        mock_isfile.return_value = True
        mock_call.return_value = 1  # Simulating failed execution
        result = task_func(script_name='backup.sh', log_file='test_log.json')
        self.assertIn('start_time', result)
        self.assertIn('end_time', result)
        self.assertEqual(result['exit_status'], 1)

    @patch('os.path.isfile')
    @patch('subprocess.call')
    def test_script_exception(self, mock_call, mock_isfile):
        mock_isfile.return_value = True
        mock_call.side_effect = Exception("Execution error")  # Simulating exception
        with self.assertRaises(RuntimeError):
            task_func(script_name='backup.sh')

    @patch('os.path.isfile')
    @patch('subprocess.call')
    def test_log_file_creation(self, mock_call, mock_isfile):
        mock_isfile.return_value = True
        mock_call.return_value = 0  # Simulating successful execution
        log_file_path = 'test_log.json'
        result = task_func(script_name='backup.sh', log_file=log_file_path)
        
        with open(log_file_path, 'r') as f:
            log_data = json.load(f)
        self.assertEqual(log_data['exit_status'], 0)
        os.remove(log_file_path)  # Cleanup

if __name__ == '__main__':
    unittest.main()