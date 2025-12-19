import unittest
from unittest.mock import patch, call
import subprocess
import os


class TestTaskFunc(unittest.TestCase):
    @patch('subprocess.check_output')
    @patch('os.kill')
    @patch('time.sleep', return_value=None)  # Mock sleep to avoid waiting
    def test_no_processes_found(self, mock_sleep, mock_kill, mock_check_output):
        mock_check_output.side_effect = subprocess.CalledProcessError(1, 'pgrep')
        result = task_func('non_existing_process')
        self.assertEqual(result, 0)
        mock_kill.assert_not_called()

    @patch('subprocess.check_output')
    @patch('os.kill')
    @patch('time.sleep', return_value=None)
    def test_single_process_found(self, mock_sleep, mock_kill, mock_check_output):
        mock_check_output.return_value = b'1234\n'  # Mock a single PID
        result = task_func('existing_process')
        self.assertEqual(result, 1)
        mock_kill.assert_called_once_with(1234, signal.SIGTERM)

    @patch('subprocess.check_output')
    @patch('os.kill')
    @patch('time.sleep', return_value=None)
    def test_multiple_processes_found(self, mock_sleep, mock_kill, mock_check_output):
        mock_check_output.return_value = b'1234\n5678\n91011\n'  # Mock multiple PIDs
        result = task_func('existing_process')
        self.assertEqual(result, 3)
        self.assertEqual(mock_kill.call_count, 3)
        mock_kill.assert_has_calls([call(1234, signal.SIGTERM), 
                                     call(5678, signal.SIGTERM), 
                                     call(91011, signal.SIGTERM)])

    @patch('subprocess.check_output')
    @patch('os.kill')
    @patch('time.sleep', return_value=None)
    def test_empty_output(self, mock_sleep, mock_kill, mock_check_output):
        mock_check_output.return_value = b''  # Mock empty output
        result = task_func('existing_process')
        self.assertEqual(result, 0)
        mock_kill.assert_not_called()

    @patch('subprocess.check_output')
    @patch('os.kill')
    @patch('time.sleep', return_value=None)
    def test_exception_handling(self, mock_sleep, mock_kill, mock_check_output):
        mock_check_output.side_effect = subprocess.CalledProcessError(1, 'pgrep')
        result = task_func('process_with_error_handling')
        self.assertEqual(result, 0)
        mock_kill.assert_not_called()


if __name__ == '__main__':
    unittest.main()