import unittest
import time
import numpy as np

# Here is your prompt
def task_func(samples=10, delay=0.1):
    """
    Make a delay for a given amount of time for a specified number of samples,
    measure the actual delay and calculate the statistical properties of the
    delay times.

    Parameters:
    - samples (int): Number of samples for which the delay is measured.
                     Default is 10.
    - delay (float): Amount of time (in seconds) for each delay.
                     Default is 0.1 second.

    Returns:
    tuple: The mean and standard deviation of the delay times.

    Requirements:
    - time
    - numpy

    Example:
    >>> mean, std = task_func(samples=5, delay=0.05)
    >>> print(f'Mean: %.3f, Std: %.1f' % (mean, std))
    Mean: 0.050, Std: 0.0
    >>> mean, std = task_func(100, 0.001)
    >>> print(f'Mean: %.3f, Std: %.4f' % (mean, std))
    Mean: 0.001, Std: 0.0000
    """

    delay_times = []

    for _ in range(samples):
        t1 = time.time()
        time.sleep(delay)
        t2 = time.time()
        delay_times.append(t2 - t1)

    delay_times = np.array(delay_times)

    mean = np.mean(delay_times)
    std = np.std(delay_times)

    return mean, std


class TestTaskFunc(unittest.TestCase):
    
    def test_default_parameters(self):
        mean, std = task_func()
        self.assertAlmostEqual(mean, 0.1, delta=0.01)
        self.assertAlmostEqual(std, 0.0, delta=0.01)

    def test_custom_samples(self):
        mean, std = task_func(samples=5, delay=0.05)
        self.assertAlmostEqual(mean, 0.05, delta=0.01)
        self.assertTrue(std < 0.01)

    def test_multiple_samples(self):
        samples = 1000
        delay = 0.001
        mean, std = task_func(samples=samples, delay=delay)
        self.assertAlmostEqual(mean, delay, delta=0.0005)
        self.assertTrue(std < 0.0005)

    def test_large_delay(self):
        mean, std = task_func(samples=5, delay=1)
        self.assertAlmostEqual(mean, 1, delta=0.1)
        self.assertTrue(std < 0.1)

    def test_zero_samples(self):
        with self.assertRaises(ValueError):
            task_func(samples=0)

if __name__ == '__main__':
    unittest.main()