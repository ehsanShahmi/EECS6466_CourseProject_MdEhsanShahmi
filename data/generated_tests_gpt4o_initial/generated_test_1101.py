import unittest
import os
import subprocess
import time
import glob

# Here is your prompt:
import subprocess
import os
import glob
import time


def task_func(test_dir):
    """
    Run all Python codes in a specific directory and return their execution times.

    Parameters:
    - script_path (str): Path to the directory for Python code(s) to be executed.
    
    Returns:
    dict: A dictionary with the script names as keys and their execution times as values.

    Requirements:
    - subprocess
    - os
    - glob
    - time

    Example:
    >>> task_func("/mnt/data/mix_files/")
    {'script1.py': 0.04103803634643555, "script2.py": 5}
    """

    execution_times = {}
    py_scripts = glob.glob(os.path.join(test_dir, '*.py'))

    for py_script in py_scripts:
        start_time = time.time()
        subprocess.call(['python', py_script])
        end_time = time.time()
        execution_times[os.path.basename(py_script)] = end_time - start_time

    return execution_times


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.test_dir = 'test_scripts'
        os.makedirs(self.test_dir, exist_ok=True)

        # Creating sample Python scripts for testing
        with open(os.path.join(self.test_dir, 'script1.py'), 'w') as f:
            f.write('print("Script 1 Running")\n')

        with open(os.path.join(self.test_dir, 'script2.py'), 'w') as f:
            f.write('print("Script 2 Running")\n')
        
        with open(os.path.join(self.test_dir, 'script3.py'), 'w') as f:
            f.write('import time\n'
                    'time.sleep(1)\n')  # A script that takes 1 second to run

    def tearDown(self):
        # Remove the temporary directory and its contents
        for file in glob.glob(os.path.join(self.test_dir, '*')):
            os.remove(file)
        os.rmdir(self.test_dir)

    def test_script_execution_times(self):
        execution_times = task_func(self.test_dir)
        # Check if the execution times are calculated and not empty
        self.assertTrue(len(execution_times) > 0)
        self.assertIn('script1.py', execution_times)
        self.assertIn('script2.py', execution_times)

    def test_for_exact_execution_time(self):
        execution_times = task_func(self.test_dir)
        self.assertTrue(0 <= execution_times['script3.py'] < 2)  # Allowing a margin

    def test_no_python_scripts(self):
        empty_dir = 'empty_test_dir'
        os.makedirs(empty_dir, exist_ok=True)
        execution_times = task_func(empty_dir)
        self.assertEqual(execution_times, {})  # Expecting an empty dictionary
        os.rmdir(empty_dir)

    def test_multiple_script_execution(self):
        execution_times = task_func(self.test_dir)
        self.assertEqual(len(execution_times), 3)  # Check if all 3 scripts are executed
        self.assertIn('script1.py', execution_times)
        self.assertIn('script2.py', execution_times)
        self.assertIn('script3.py', execution_times)


if __name__ == '__main__':
    unittest.main()