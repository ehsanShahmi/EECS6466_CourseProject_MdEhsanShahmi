import unittest
import os
import shutil

# Here is your prompt:
import subprocess
import shutil
import os

def task_func(script_path: str, temp_dir: str) -> str:
    """
    Execute a given Python code in a temporary directory.
    
    Parameters:
    - script_path (str): The path to the Python code that needs to be executed.
    - temp_dir (str): The path for the code to copy the Python code
    
    Returns:
    - str: String indicating the success or failure of the script execution.
    
    Requirements:
    - subprocess
    - shutil
    - os
    
    Example:
    >>> task_func('/path/to/example_script.py')
    'Script executed successfully!'
    
    Note: 
    - If the Python code can be run successfully return "Script executed successfully!", otherwise "Script execution failed!"
    """
    try:
        shutil.copy(script_path, temp_dir)
        temp_script_path = os.path.join(temp_dir, os.path.basename(script_path))
        result = subprocess.call(["python", temp_script_path])
        print(result)
        if result == 0:
            return "Script executed successfully!"
        else:
            return "Script execution failed!"
    except Exception as e:
        return "Script execution failed!" 

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = "temp_test_dir"
        os.makedirs(self.temp_dir, exist_ok=True)
        self.valid_script = "valid_script.py"
        self.invalid_script = "invalid_script.py"

        # Create a valid Python script
        with open(self.valid_script, "w") as f:
            f.write("print('Hello, World!')")  # This should execute successfully

        # Create an invalid Python script
        with open(self.invalid_script, "w") as f:
            f.write("print('Hello, World!')")
            f.write("a = 1 / 0")  # This will cause a ZeroDivisionError

    def tearDown(self):
        # Remove the temporary directory and scripts after tests
        if os.path.exists(self.temp_dir):
            shutil.rmtree(self.temp_dir)
        if os.path.exists(self.valid_script):
            os.remove(self.valid_script)
        if os.path.exists(self.invalid_script):
            os.remove(self.invalid_script)

    def test_valid_script_execution(self):
        result = task_func(self.valid_script, self.temp_dir)
        self.assertEqual(result, "Script executed successfully!")

    def test_invalid_script_execution(self):
        result = task_func(self.invalid_script, self.temp_dir)
        self.assertEqual(result, "Script execution failed!")

    def test_non_existent_script(self):
        result = task_func("non_existent_script.py", self.temp_dir)
        self.assertEqual(result, "Script execution failed!")

    def test_empty_script(self):
        empty_script = "empty_script.py"
        with open(empty_script, "w") as f:
            f.write("")  # Create an empty script
        result = task_func(empty_script, self.temp_dir)
        self.assertEqual(result, "Script execution failed!")
        os.remove(empty_script)

    def test_copy_and_execute_script(self):
        # Ensure the script is copied to temp directory before execution
        result = task_func(self.valid_script, self.temp_dir)
        self.assertEqual(result, "Script executed successfully!")
        self.assertTrue(os.path.exists(os.path.join(self.temp_dir, self.valid_script)))

if __name__ == '__main__':
    unittest.main()