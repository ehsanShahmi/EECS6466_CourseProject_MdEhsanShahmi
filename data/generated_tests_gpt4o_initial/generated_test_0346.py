import subprocess
import os
import sys
import time
import unittest
import tempfile

class TestTaskFunc(unittest.TestCase):
    
    def test_script_execution_success(self):
        script_path = tempfile.NamedTemporaryFile(suffix='.py', delete=False).name
        with open(script_path, 'w') as f:
            f.write('import sys; sys.exit(0)')
        self.assertEqual(task_func(script_path), 0)
        os.remove(script_path)

    def test_script_execution_failure(self):
        script_path = tempfile.NamedTemporaryFile(suffix='.py', delete=False).name
        with open(script_path, 'w') as f:
            f.write('import sys; sys.exit(1)')
        with self.assertRaises(subprocess.CalledProcessError):
            task_func(script_path)
        os.remove(script_path)

    def test_script_not_exist(self):
        with self.assertRaises(ValueError):
            task_func('non_existent_script.py')

    def test_non_waiting_execution(self):
        script_path = tempfile.NamedTemporaryFile(suffix='.py', delete=False).name
        with open(script_path, 'w') as f:
            f.write('import sys; sys.exit(0)')
        self.assertIsNone(task_func(script_path, wait=False))
        os.remove(script_path)

    def test_script_with_arguments(self):
        script_path = tempfile.NamedTemporaryFile(suffix='.py', delete=False).name
        with open(script_path, 'w') as f:
            f.write('import sys; sys.exit(int(sys.argv[1]))')
        self.assertEqual(task_func(script_path, True, '0'), 0)
        self.assertEqual(task_func(script_path, True, '1'), 1)
        os.remove(script_path)

if __name__ == '__main__':
    unittest.main()