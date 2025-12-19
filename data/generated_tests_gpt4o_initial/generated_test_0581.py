import unittest
import matplotlib
import task_module  # Assuming the provided code is saved in a module named task_module

class TestTaskFunc(unittest.TestCase):

    def test_return_type(self):
        ax = task_module.task_func(size=1000, frequency=1)
        self.assertIsInstance(ax, matplotlib.axes.Axes)

    def test_data_point_count(self):
        ax = task_module.task_func(size=1000, frequency=1)
        self.assertEqual(len(ax.lines[0].get_ydata()), 1000)

    def test_y_data_type(self):
        ax = task_module.task_func(size=1000, frequency=1)
        self.assertIsInstance(ax.lines[0].get_ydata()[0], float)

    def test_negative_size(self):
        with self.assertRaises(ValueError):
            task_module.task_func(size=-100, frequency=1)

    def test_zero_frequency(self):
        ax = task_module.task_func(size=1000, frequency=0)
        self.assertTrue(all(y == 0 for y in ax.lines[0].get_ydata()))

if __name__ == '__main__':
    unittest.main()