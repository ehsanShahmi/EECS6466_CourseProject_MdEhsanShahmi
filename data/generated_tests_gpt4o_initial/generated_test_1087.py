import unittest
import numpy as np
import os

class TestTaskFunc(unittest.TestCase):

    def test_default_params(self):
        skewness, kurtosis, plot_paths = task_func()
        self.assertIsInstance(skewness, float)
        self.assertIsInstance(kurtosis, float)
        self.assertEqual(plot_paths, [])

    def test_custom_mean(self):
        mean = 100000.0
        skewness, kurtosis, plot_paths = task_func(mean=mean)
        self.assertIsInstance(skewness, float)
        self.assertIsInstance(kurtosis, float)
        self.assertEqual(plot_paths, [])

    def test_custom_std_dev(self):
        std_dev = 10.0
        skewness, kurtosis, plot_paths = task_func(std_dev=std_dev)
        self.assertIsInstance(skewness, float)
        self.assertIsInstance(kurtosis, float)
        self.assertEqual(plot_paths, [])

    def test_save_plots(self):
        skewness, kurtosis, plot_paths = task_func(save_plots=True)
        self.assertIsInstance(skewness, float)
        self.assertIsInstance(kurtosis, float)
        self.assertEqual(len(plot_paths), 2)
        self.assertIn("histogram_plot.png", plot_paths)
        self.assertIn("qq_plot.png", plot_paths)

    def test_plot_files_exist(self):
        task_func(save_plots=True)
        self.assertTrue(os.path.exists("histogram_plot.png"))
        self.assertTrue(os.path.exists("qq_plot.png"))
        # Cleanup
        os.remove("histogram_plot.png")
        os.remove("qq_plot.png")
        
if __name__ == '__main__':
    unittest.main()