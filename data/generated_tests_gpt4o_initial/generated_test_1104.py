import subprocess
import os
import threading
import unittest

def task_func(script_path: str, timeout: int = 60) -> str:
    """
    Execute a specified python code with a given timeout. If the script execution exceeds the timeout, it is terminated.

    Parameters:
    - script_path (str): The path to the Python code to be executed.
    - timeout (int): The maximum allowed time (in seconds) for the script execution. Default is 60 seconds.

    Returns:
    - str: A message indicating if the code was terminated due to timeout or executed successfully. The message is either "Script executed successfully." or "Terminating process due to timeout."

    Requirements:
    - subprocess
    - os
    - threading

    Examples:
    >>> task_func('/pathto/MyrScript.py')
    'Script executed successfully.'
    
    >>> task_func('/pathto/LongRunningScript.py', 30)
    'Terminating process due to timeout.'

    Note:
    - If the script was terminated due to timeout it will return "Script executed successfully.", otherwise "Terminating process due to timeout."

    Raise:
    - The code will raise FileNotFoundError if the file is not exist.
    """

    def target():
        subprocess.call(['python', script_path])

    thread = threading.Thread(target=target)
    thread.start()

    thread.join(timeout)

    if thread.is_alive():
        os.system(f'pkill -f "{script_path}"')
        thread.join()
        return 'Terminating process due to timeout.'
    else:
        return 'Script executed successfully.'

class TestTaskFunction(unittest.TestCase):

    def test_script_execution_success(self):
        # Create a temporary script that finishes quickly
        with open('quick_script.py', 'w') as f:
            f.write("print('Hello, World!')")
        result = task_func('quick_script.py')
        self.assertEqual(result, 'Script executed successfully.')
        os.remove('quick_script.py')

    def test_script_execution_timeout(self):
        # Create a temporary script that runs indefinitely
        with open('long_script.py', 'w') as f:
            f.write("import time; time.sleep(100)")
        result = task_func('long_script.py', timeout=2)
        self.assertEqual(result, 'Terminating process due to timeout.')
        os.remove('long_script.py')

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_script.py')

    def test_script_execution_with_custom_timeout(self):
        # Create another temporary script that finishes fast
        with open('another_quick_script.py', 'w') as f:
            f.write("print('Done')")
        result = task_func('another_quick_script.py', timeout=5)
        self.assertEqual(result, 'Script executed successfully.')
        os.remove('another_quick_script.py')

    def test_timeout_with_no_timeout(self):
        # Create a temporary script that finishes quickly without specified timeout
        with open('fast_script.py', 'w') as f:
            f.write("import time; time.sleep(1); print('Finished')")
        result = task_func('fast_script.py')
        self.assertEqual(result, 'Script executed successfully.')
        os.remove('fast_script.py')

if __name__ == '__main__':
    unittest.main()