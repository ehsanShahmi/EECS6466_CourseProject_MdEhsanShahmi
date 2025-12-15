import unittest
import numpy as np
from io import StringIO
import sys
import matplotlib.pyplot as plt

class TestParabolaPlot(unittest.TestCase):

    def test_parabola_shape(self):
        X = np.linspace(-10, 10, 400)
        Y = X**2
        
        # Check the shape of the generated data
        self.assertEqual(X.shape, (400,))
        self.assertEqual(Y.shape, (400,))

    def test_parabola_range(self):
        X = np.linspace(-10, 10, 400)
        Y = X**2
        
        # Check that the Y values are in the expected range
        self.assertGreaterEqual(np.min(Y), 0)  # y = x^2 is always >= 0
        self.assertEqual(np.max(Y), 100)       # max y occurs at x = 10 or x = -10

    def test_plot_title(self):
        plt.figure()
        plt.plot(np.linspace(-10, 10, 400), np.linspace(-10, 10, 400)**2)
        plt.title('y = x^2')
        
        # Check the title of the current plot
        self.assertEqual(plt.gca().title.get_text(), 'y = x^2')

    def test_axes_labels(self):
        plt.figure()
        plt.plot(np.linspace(-10, 10, 400), np.linspace(-10, 10, 400)**2)
        plt.xlabel('x')
        plt.ylabel('y')
        
        # Check x and y axis labels
        self.assertEqual(plt.gca().get_xlabel(), 'x')
        self.assertEqual(plt.gca().get_ylabel(), 'y')

    def test_grid_enabled(self):
        plt.figure()
        plt.plot(np.linspace(-10, 10, 400), np.linspace(-10, 10, 400)**2)
        plt.grid(True)
        
        # Check if grid is enabled
        self.assertTrue(plt.gca().xaxis._gridOnMajor)
        self.assertTrue(plt.gca().yaxis._gridOnMajor)

if __name__ == '__main__':
    unittest.main()