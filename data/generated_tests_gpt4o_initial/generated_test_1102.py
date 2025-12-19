import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime

# The provided function as per the prompt
import subprocess
import shlex
from datetime import datetime

def task_func(script_path: str) -> dict:
    '''
    Run an R script and return the start time, end time, decoded stdout, and decoded stderr as a dictionary.
    
    Requirements:
    - subprocess
    - shlex
    - datetime
    
    Parameters:
    - script_path (str): Path to the R script to be executed.
    
    Returns:
    - dict: A dictionary containing the start time, end time, stdout, and stderr of the script run.
    
    Example:
    >>> task_func("/path/to/script.r")
    {
        'Start Time': '2023-09-26 14:30:00',
        'End Time': '2023-09-26 14:32:00',
        'Stdout': 'Script output here...',
        'Stderr': 'Any errors here...'
    }
    '''

    start_time = datetime.now()
    process = subprocess.Popen(shlex.split(f"/usr/bin/Rscript --vanilla {script_path}"),
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    end_time = datetime.now()

    log_details = {
        'Start Time': str(start_time),
        'End Time': str(end_time),
        'Stdout': stdout.decode('utf-8'),
        'Stderr': stderr.decode('utf-8')
    }
    
    return log_details


class TestTaskFunc(unittest.TestCase):

    @patch('subprocess.Popen')
    def test_successful_script_run(self, mock_popen):
        # Mocking the subprocess to simulate successful script execution
        mock_process = MagicMock()
        mock_process.communicate.return_value = (b'Success Output', b'')
        mock_popen.return_value = mock_process

        result = task_func("success_script.r")

        self.assertIn('Start Time', result)
        self.assertIn('End Time', result)
        self.assertEqual(result['Stdout'], 'Success Output')
        self.assertEqual(result['Stderr'], '')

    @patch('subprocess.Popen')
    def test_script_with_errors(self, mock_popen):
        # Mocking the subprocess to simulate error in script execution
        mock_process = MagicMock()
        mock_process.communicate.return_value = (b'', b'Error Output')
        mock_popen.return_value = mock_process

        result = task_func("error_script.r")

        self.assertIn('Start Time', result)
        self.assertIn('End Time', result)
        self.assertEqual(result['Stdout'], '')
        self.assertEqual(result['Stderr'], 'Error Output')

    @patch('subprocess.Popen')
    def test_runtime_values(self, mock_popen):
        # Mocking the subprocess
        mock_process = MagicMock()
        mock_process.communicate.return_value = (b'Test Output', b'')
        mock_popen.return_value = mock_process

        result = task_func("test_script.r")
        
        start_time = datetime.strptime(result['Start Time'], '%Y-%m-%d %H:%M:%S.%f')
        end_time = datetime.strptime(result['End Time'], '%Y-%m-%d %H:%M:%S.%f')
        
        self.assertTrue(end_time > start_time)
        self.assertEqual(result['Stdout'], 'Test Output')
        self.assertEqual(result['Stderr'], '')

    @patch('subprocess.Popen')
    def test_invalid_script_path(self, mock_popen):
        # Mocking the subprocess to raise an error due to invalid script path
        mock_process = MagicMock()
        mock_process.communicate.side_effect = OSError("No such file or directory")
        mock_popen.return_value = mock_process

        with self.assertRaises(OSError):
            task_func("invalid_script.r")

    @patch('subprocess.Popen')
    def test_empty_stdout_and_stderr(self, mock_popen):
        # Mocking the subprocess with empty output and error
        mock_process = MagicMock()
        mock_process.communicate.return_value = (b'', b'')
        mock_popen.return_value = mock_process

        result = task_func("empty_output_script.r")

        self.assertIn('Start Time', result)
        self.assertIn('End Time', result)
        self.assertEqual(result['Stdout'], '')
        self.assertEqual(result['Stderr'], '')


if __name__ == '__main__':
    unittest.main()