import unittest
import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

# Here is your prompt:
# 
# import time
# import random
# import matplotlib.pyplot as plt
# from scipy.stats import kurtosis
#
# def task_func(intervals=100, seed=0):
# """
# Generates a series of random numbers over a specified number of intervals with a delay of 1 second between 
# each interval. It then plots these numbers as a function of elapsed time and returns the Axes object along
# with the kurtosis value of the generated numbers.
# 
# Parameters:
# - intervals (int, optional): Number of intervals for generating random numbers. Default is 100.
# 
# Returns:
# - matplotlib.axes.Axes: The Axes object representing the plot.
# - float: The kurtosis value of the generated numbers.
# 
# Requirements:
# - time
# - random
# - matplotlib.pyplot
# 
# Example:
# >>> ax, kurtosis = task_func(5)
# >>> type(ax)
# <class 'matplotlib.axes._axes.Axes'>
# """
# 
# random.seed(seed)
# times = []
# numbers = []
# 
# try:
# for _ in range(intervals):
# time.sleep(1)
# times.append(time.time())
# numbers.append(random.random())
# except KeyboardInterrupt:
# print('Interrupted by user')
# 
# kurtosis_value = kurtosis(numbers, nan_policy='omit')
# # Initialize a fresh figure
# plt.figure()
# fig, ax = plt.subplots()
# ax.plot(times, numbers)
# return ax, kurtosis_value

class TestTaskFunction(unittest.TestCase):

    def test_default_intervals(self):
        ax, kurtosis_value = task_func()
        self.assertIsInstance(ax, plt.Axes)
        self.assertIsInstance(kurtosis_value, float)

    def test_custom_intervals(self):
        ax, kurtosis_value = task_func(intervals=10)
        self.assertIsInstance(ax, plt.Axes)
        self.assertIsInstance(kurtosis_value, float)
        self.assertEqual(len(kurtosis_value), 10)

    def test_different_seed(self):
        random.seed(42)
        ax1, kurtosis1 = task_func(intervals=10, seed=42)
        random.seed(42)
        ax2, kurtosis2 = task_func(intervals=10, seed=42)
        self.assertListEqual(kurtosis1, kurtosis2)
        self.assertEqual(ax1.lines[0].get_ydata().tolist(), ax2.lines[0].get_ydata().tolist())

    def test_kurtosis_value(self):
        _, kurtosis_value = task_func(intervals=100)
        self.assertIsInstance(kurtosis_value, float)
        self.assertTrue(kurtosis_value >= -1)  # Expecting some range for kurtosis

    def test_interrupted_execution(self):
        with self.assertRaises(KeyboardInterrupt):
            task_func(intervals=10)  # Simulating a keyboard interrupt doesn't work in unittest, this is a placeholder

if __name__ == '__main__':
    unittest.main()