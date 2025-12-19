import unittest
from unittest.mock import patch
import time
from datetime import datetime
from random import randint
import matplotlib.pyplot as plt

# Here is your prompt:

def task_func(duration):
    """
    Generate and draw random data in real time for the specified duration.

    Parameters:
    - duration (int): The duration in seconds for which data is to be generated and plotted.

    Returns:
    - tuple: A tuple containing two lists.
        - The first list contains timestamps (as strings) in the format '%H:%M:%S.%f'.
        - The second list contains the generated random values.

    Requirements:
    - datetime
    - time
    - random
    - matplotlib.pyplot

    Example:
    >>> type(task_func(1))
    <class 'tuple'>
    """

    # Constants
    VALUES_RANGE = (0, 100)
    PLOT_INTERVAL = 0.1

    plt.ion()
    x_data = []
    y_data = []

    end_time = time.time() + duration
    while time.time() < end_time:
        x_data.append(datetime.now().strftime('%H:%M:%S.%f'))
        y_data.append(randint(*VALUES_RANGE))

        plt.clf()
        plt.plot(x_data, y_data)
        plt.draw()
        plt.pause(PLOT_INTERVAL)

    plt.ioff()
    plt.show()

    return x_data, y_data


class TestTaskFunc(unittest.TestCase):

    @patch('time.sleep', return_value=None)  # Mocking sleep to speed up tests
    def test_return_type(self, mock_sleep):
        result = task_func(1)
        self.assertIsInstance(result, tuple)
        
    @patch('time.sleep', return_value=None)  # Mocking sleep to speed up tests
    def test_return_length(self, mock_sleep):
        x_data, y_data = task_func(1)
        self.assertEqual(len(x_data), len(y_data))

    @patch('time.sleep', return_value=None)  # Mocking sleep to speed up tests
    def test_generated_values_range(self, mock_sleep):
        x_data, y_data = task_func(1)
        for value in y_data:
            self.assertTrue(0 <= value <= 100)

    @patch('time.sleep', return_value=None)  # Mocking sleep to speed up tests
    def test_unique_timestamps(self, mock_sleep):
        x_data, y_data = task_func(1)
        self.assertEqual(len(x_data), len(set(x_data)))

    @patch('time.sleep', return_value=None)  # Mocking sleep to speed up tests
    def test_duration(self, mock_sleep):
        start_time = time.time()
        task_func(2)
        end_time = time.time()
        self.assertTrue(end_time - start_time >= 2)


if __name__ == '__main__':
    unittest.main()