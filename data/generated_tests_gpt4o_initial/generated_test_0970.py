import numpy as np
import matplotlib.pyplot as plt
import unittest

# Test suite for task_func

class TestTaskFunc(unittest.TestCase):

    def test_cumulative_probability_basic(self):
        data = np.array([1, 2, 3, 4, 5])
        ax = task_func(data)
        self.assertEqual(ax.get_title(), 'Cumulative Probability Plot')
        self.assertEqual(ax.get_xlabel(), 'Index')
        self.assertEqual(ax.get_ylabel(), 'Cumulative Probability')
        
    def test_cumulative_probability_all_zeros(self):
        data = np.array([0, 0, 0, 0])
        ax = task_func(data)
        cumulative_prob = np.zeros(len(data))
        for i, line in enumerate(ax.lines[0].get_xydata()):
            self.assertAlmostEqual(line[1], cumulative_prob[i])
    
    def test_cumulative_probability_with_negatives(self):
        data = np.array([1, -2, 3])
        with self.assertRaises(ValueError):
            task_func(data)

    def test_cumulative_probability_with_nans(self):
        data = np.array([float('nan'), 2, 3])
        with self.assertRaises(ValueError):
            task_func(data)

    def test_cumulative_probability_with_non_numeric(self):
        data = np.array(['a', 'b', 'c'])
        with self.assertRaises(TypeError):
            task_func(data)

# Run the test suite
if __name__ == '__main__':
    unittest.main()