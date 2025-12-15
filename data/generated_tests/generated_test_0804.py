import os
import unittest
from datetime import datetime

# Constants
LOG_DIR = './logs'

def task_func(metrics, filename, log_dir=LOG_DIR):
    """
    This function writes a dictionary of metrics to a specified log file, appending a timestamp to each entry.
    
    Parameters:
    - metrics (dict): A dictionary containing metric names as keys and their corresponding values.
    - filename (str): The name of the file to which the metrics will be logged.
    - log_dir (str, optional): The directory where the log file is stored. Default is './logs'.
    
    Returns:
    - bool: True if the metrics were successfully written to the file, False otherwise.
    
    Requirements:
    - os
    - datetime
    
    Examples:
    >>> metrics = {'accuracy': 0.98, 'loss': 0.05}
    >>> task_func(metrics, 'metrics.log')
    An error occurred: [Errno 2] No such file or directory: './logs/metrics.log'
    False
    
    >>> metrics = {'precision': 0.75, 'recall': 0.80}
    >>> task_func(metrics, 'evaluation.log')
    An error occurred: [Errno 2] No such file or directory: './logs/evaluation.log'
    False
    """

           
    if not isinstance(metrics, dict):
        raise ValueError("Metrics must be a dictionary")
    if not isinstance(filename, str):
        raise ValueError("Filename must be a string")
    
    try:
        with open(os.path.join(log_dir, filename), 'a') as f:
            f.write(f'{datetime.now()}\n')
            for key, value in metrics.items():
                f.write(f'{key}: {value}\n')
            f.write('\n')
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create the log directory if it does not exist
        if not os.path.exists(LOG_DIR):
            os.makedirs(LOG_DIR)

    def tearDown(self):
        # Clean up log files after tests
        for file in os.listdir(LOG_DIR):
            file_path = os.path.join(LOG_DIR, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

    def test_valid_metrics_logging(self):
        metrics = {'accuracy': 0.98, 'loss': 0.05}
        result = task_func(metrics, 'metrics.log')
        self.assertTrue(result)

        with open(os.path.join(LOG_DIR, 'metrics.log'), 'r') as f:
            content = f.read()
            self.assertIn('accuracy: 0.98', content)
            self.assertIn('loss: 0.05', content)

    def test_invalid_metrics_type(self):
        with self.assertRaises(ValueError) as context:
            task_func('invalid_metrics', 'metrics.log')
        self.assertEqual(str(context.exception), "Metrics must be a dictionary")

    def test_invalid_filename_type(self):
        with self.assertRaises(ValueError) as context:
            task_func({'accuracy': 0.95}, 123)
        self.assertEqual(str(context.exception), "Filename must be a string")

    def test_logging_to_nonexistent_directory(self):
        os.rmdir(LOG_DIR)  # Remove the directory for this test
        metrics = {'accuracy': 0.85, 'loss': 0.1}
        result = task_func(metrics, 'new_metrics.log')
        self.assertFalse(result)

    def test_logging_empty_metrics(self):
        metrics = {}
        result = task_func(metrics, 'empty_metrics.log')
        self.assertTrue(result)

        with open(os.path.join(LOG_DIR, 'empty_metrics.log'), 'r') as f:
            content = f.read()
            self.assertIn('{}'.format(datetime.now().date()), content)


if __name__ == '__main__':
    unittest.main()