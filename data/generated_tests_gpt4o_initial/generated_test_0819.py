import unittest
import time
import random


def task_func(iterations=5, min_delay=1.0, max_delay=2.0, seed=None):
    """
    Simulates a delay and then returns a message indicating the elapsed time. This is repeated for a specified number of iterations.
    
    For each iteration the delay is randomly sampled from a uniform distribution specified by min_delay and max_delay. After each iteration the message: '{delay} seconds have passed', where {delay} is replaces with the actual delay of the iteration with 2 positions after the decimal point, is saved to an array.

    The function returns a list of all messages, as well as the total delay.

    Parameters:
    - iterations (int): The number of times the delay and message should be simulated. Default is 5.
    - min_delay (float): The duration (in seconds) of the delay between messages. Default is 1.0.
    - max_delay (float): The max delay of each iteration in seconds. Default is 2.0
    - seed (float): The seed used for random sampling the delays for each iteration. Defalut is None.

    Returns:
    - list of str: A list of messages indicating the elapsed time for each iteration.
    - float: The total amount of delay

    Raises:
    - ValueError: If iterations is not a positive integer or if min_delay/max_delay is not a positive floating point value.

    Requirements:
    - time
    - random
    """

    random.seed(seed)

    # Input validation
    if not isinstance(iterations, int) or iterations <= 0:
        raise ValueError("iterations must be a positive integer.")
    if not isinstance(min_delay, (int, float)) or min_delay <= 0:
        raise ValueError("min_delay must be a positive floating point value.")
    if not isinstance(max_delay, (int, float)) or max_delay <= min_delay:
        raise ValueError("max_delay must be a floating point value larger than min_delay.")

    total_delay = 0
    messages = []

    for _ in range(iterations):
        delay = random.uniform(min_delay, max_delay)
        total_delay += delay
        time.sleep(delay)
        message_string = f'{delay:.2f} seconds have passed'
        messages.append(message_string)
    
    return messages, total_delay


class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        messages, delay = task_func()
        self.assertEqual(len(messages), 5)
        self.assertTrue(all(1.0 <= float(msg.split()[0]) <= 2.0 for msg in messages))
        self.assertAlmostEqual(delay, sum(float(msg.split()[0]) for msg in messages), places=2)

    def test_custom_iterations(self):
        messages, delay = task_func(iterations=3)
        self.assertEqual(len(messages), 3)
        self.assertTrue(all(1.0 <= float(msg.split()[0]) <= 2.0 for msg in messages))
        self.assertAlmostEqual(delay, sum(float(msg.split()[0]) for msg in messages), places=2)

    def test_invalid_iterations(self):
        with self.assertRaises(ValueError):
            task_func(iterations=0)

        with self.assertRaises(ValueError):
            task_func(iterations=-1)

        with self.assertRaises(ValueError):
            task_func(iterations='a')

    def test_invalid_delay_values(self):
        with self.assertRaises(ValueError):
            task_func(min_delay=-1.0)

        with self.assertRaises(ValueError):
            task_func(max_delay=0.5, min_delay=1.0)

    def test_seed_value_consistency(self):
        random.seed(123)
        messages1, delay1 = task_func(3, 1.0, 1.5, seed=123)
        random.seed(123)
        messages2, delay2 = task_func(3, 1.0, 1.5, seed=123)
        self.assertEqual(messages1, messages2)
        self.assertAlmostEqual(delay1, delay2, places=2)


if __name__ == '__main__':
    unittest.main()