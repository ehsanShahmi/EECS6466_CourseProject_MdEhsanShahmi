import subprocess
import os
import time
import glob
import unittest

def task_func(r_script_path: str, output_path: str, duration: int) -> (bool, str):
    """
    This function executes an R script and verifies if the output file is generated within a given duration.
    
    Parameters:
    - r_script_path (str): The absolute path to the R script to be executed.
    - output_path (str): The absolute path where the output CSV file is expected to be generated.
    - duration (int): The time, in seconds, within which the output file should be generated.
    
    Returns:
    - tuple containing:
      - bool: True if the output file is generated within the specified duration, False otherwise.
      - str: A message indicating whether the file was generated successfully or not. If the generation is successful, the message will be 'File generated successfully within the specified duration.'; otherwise, it will be 'File not generated within the specified duration.'
    
    Requirements:
    - subprocess
    - os
    - time
    - glob
    
    Example:
    >>> task_func('/path_to_script/MyrScript.r', '/path_to_output/', 10)
    (True, 'File generated successfully within the specified duration.')
    >>> task_func('/path_to_script/InvalidScript.r', '/path_to_output/', 5)
    (False, 'File not generated within the specified duration.')
    """

               # Construct the command to run the R script
    command = f'/usr/bin/Rscript --vanilla {r_script_path}'
    
    # Execute the R script
    subprocess.call(command, shell=True)
    
    # Initialize the start time
    start_time = time.time()
    
    # Construct the search pattern for the output CSV file
    search_pattern = os.path.join(output_path, '*.csv')
    
    # Continuously check if the output file is generated within the specified duration
    while time.time() - start_time < duration:
        if glob.glob(search_pattern):
            return True, 'File generated successfully within the specified duration.'
        time.sleep(0.1)
    
    # Return False with a message if the file is not generated within the specified duration
    return False, 'File not generated within the specified duration.'

class TestTaskFunc(unittest.TestCase):

    def test_valid_r_script_execution(self):
        result = task_func('/path_to_script/MyrScript.r', '/path_to_output/', 10)
        self.assertEqual(result, (True, 'File generated successfully within the specified duration.'))

    def test_invalid_r_script_execution(self):
        result = task_func('/path_to_script/InvalidScript.r', '/path_to_output/', 5)
        self.assertEqual(result, (False, 'File not generated within the specified duration.'))

    def test_output_file_created_within_duration(self):
        # Assuming we have a script that runs quickly and generates the output.
        result = task_func('/path_to_script/QuickScript.r', '/path_to_output/', 2)
        self.assertTrue(result[0])
        self.assertIn('File generated successfully', result[1])

    def test_no_output_file_created_after_duration(self):
        # Using a script that deliberately doesn't create an output file.
        result = task_func('/path_to_script/NoOutputScript.r', '/path_to_output/', 2)
        self.assertFalse(result[0])
        self.assertIn('File not generated within the specified duration.', result[1])

    def test_timeout_exceeded_for_output_file(self):
        # Assuming we execute an R script that takes longer than the specified duration.
        result = task_func('/path_to_script/LongRunningScript.r', '/path_to_output/', 1)
        self.assertFalse(result[0])
        self.assertIn('File not generated within the specified duration.', result[1])


if __name__ == '__main__':
    unittest.main()