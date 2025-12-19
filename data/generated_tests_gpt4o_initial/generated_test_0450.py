import unittest
from unittest.mock import patch
import numpy as np
from task import task_func  # Assuming task_func is defined in a file named task.py


class TestTaskFunc(unittest.TestCase):

    @patch('matplotlib.pyplot.savefig')
    def test_default_parameters(self, mock_savefig):
        distances, plot = task_func()
        self.assertEqual(distances.shape, (200, 200))
        self.assertIsNotNone(plot)
        self.assertIsInstance(plot, plt.Axes)

    @patch('matplotlib.pyplot.savefig')
    def test_custom_n_samples(self, mock_savefig):
        distances, plot = task_func(n_samples=100)
        self.assertEqual(distances.shape[0], 100)
        self.assertEqual(distances.shape[1], 100)

    @patch('matplotlib.pyplot.savefig')
    def test_custom_centers(self, mock_savefig):
        distances, plot = task_func(centers=3)
        self.assertEqual(plot.collections[0].get_array().max(), 2)  # Check if centers are correctly colored

    @patch('matplotlib.pyplot.savefig')
    def test_plot_saved(self, mock_savefig):
        plot_path = 'dummy_path.png'
        distances, plot = task_func(plot_path=plot_path)
        mock_savefig.assert_called_once_with(plot_path)

    def test_random_seed_effect(self):
        distances1, _ = task_func(random_seed=42)
        distances2, _ = task_func(random_seed=42)
        np.testing.assert_array_equal(distances1, distances2)


if __name__ == '__main__':
    unittest.main()