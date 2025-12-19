import os
import shutil
import csv
import unittest

# Here is your prompt:

def task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=False):
    """
    Scans a directory for CSV files, finds for each file the index of the row with the first cell equal to the target value,
    and optionally moves the processed files to another directory.
    
    Parameters:
    - target_value (str): The value to search for in the first cell of each row. Defaults to '332'.
    - csv_dir (str): The directory to scan for CSV files. Defaults to './csv_files/'.
    - processed_dir (str): The directory to move processed files to. Defaults to './processed_files/'.
    - simulate (bool): If True, the function will simulate file moving without performing the action. Defaults to False.
    
    Returns:
    - result (dict): A dictionary with file names as keys and the row indices as values where the target value was found.
    
    Requirements:
    - os
    - shutil
    - csv
    
    Example:
    >>> task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=True)
    {'file1.csv': 10, 'file2.csv': 15}
    
    The above example assumes that '332' is found at index 10 in 'file1.csv' and index 15 in 'file2.csv' and that the 
    file moving is simulated.
    """

    result = {}

    # Scan the CSV files in the directory
    for filename in os.listdir(csv_dir):
        if filename.endswith('.csv'):
            with open(os.path.join(csv_dir, filename), 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    if row[0] == target_value:
                        result[filename] = i
                        break

            # Move the file to the processed directory if not simulating
            if not simulate:
                shutil.move(os.path.join(csv_dir, filename), processed_dir)
    
    return result


class TestTaskFunc(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        os.makedirs('./csv_files/', exist_ok=True)
        os.makedirs('./processed_files/', exist_ok=True)
        with open('./csv_files/test1.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['321'])
            writer.writerow(['332'])
        with open('./csv_files/test2.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['123'])
            writer.writerow(['456'])
        with open('./csv_files/test3.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['332'])
            writer.writerow(['789'])

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree('./csv_files/')
        shutil.rmtree('./processed_files/')

    def test_target_value_found(self):
        result = task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=True)
        self.assertEqual(result, {'test1.csv': 1, 'test3.csv': 0})

    def test_target_value_not_found(self):
        result = task_func(target_value='999', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=True)
        self.assertEqual(result, {})

    def test_files_moved_on_actual_run(self):
        task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=False)
        self.assertFalse(os.path.exists('./csv_files/test1.csv'))
        self.assertFalse(os.path.exists('./csv_files/test3.csv'))
        self.assertTrue(os.path.exists('./processed_files/test1.csv'))
        self.assertTrue(os.path.exists('./processed_files/test3.csv'))

    def test_csv_directory_empty(self):
        os.rmdir('./csv_files/')
        os.makedirs('./csv_files/')
        result = task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=True)
        self.assertEqual(result, {})

    def test_simulate_does_not_move_files(self):
        task_func(target_value='332', csv_dir='./csv_files/', processed_dir='./processed_files/', simulate=True)
        self.assertTrue(os.path.exists('./csv_files/test1.csv'))
        self.assertTrue(os.path.exists('./csv_files/test3.csv'))
        self.assertFalse(os.path.exists('./processed_files/test1.csv'))
        self.assertFalse(os.path.exists('./processed_files/test3.csv'))


if __name__ == '__main__':
    unittest.main()