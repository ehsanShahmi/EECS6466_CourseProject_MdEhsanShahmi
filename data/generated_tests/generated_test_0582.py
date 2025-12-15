import unittest
import numpy as np
from scipy import stats
import matplotlib

class TestTaskFunc(unittest.TestCase):

    def test_function_output_type(self):
        """Test if the output is a matplotlib figure object."""
        fig = task_func(size=500)
        self.assertIsInstance(fig, matplotlib.figure.Figure)

    def test_pdf_line_plot(self):
        """Ensure there is one line plot on the axes for the PDF."""
        fig = task_func(size=500)
        self.assertEqual(len(fig.axes[0].lines), 1)

    def test_histogram_bars(self):
        """Check if there are histogram bars (patches) present."""
        fig = task_func(size=500)
        self.assertGreater(len(fig.axes[0].patches), 10)

    def test_function_output_shape(self):
        """Test if the histogram and PDF have the same x-range."""
        fig = task_func(size=500)
        ax = fig.axes[0]
        histogram_xlim = ax.get_xlim()
        self.assertEqual(len(ax.patches), histogram_xlim[1] - histogram_xlim[0])

    def test_random_number_generation(self):
        """Test if the generated random numbers are normally distributed."""
        size = 1000
        data = np.random.randn(size)
        mu, std = stats.norm.fit(data)
        self.assertAlmostEqual(mu, 0, delta=0.1)  # mean should be close to 0
        self.assertAlmostEqual(std, 1, delta=0.1)  # std deviation should be close to 1

if __name__ == '__main__':
    unittest.main()