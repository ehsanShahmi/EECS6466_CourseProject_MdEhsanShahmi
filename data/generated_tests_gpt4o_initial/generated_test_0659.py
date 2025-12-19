import unittest
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Here is your prompt:
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def task_func(x, y, labels):
    """
    Draw normal distributions for multiple 'x' and 'y' arrays with labels.
    Each pair (x, y) represents a different chemical compound in the 'labels' list.

    Parameters:
    x (list): List of numpy arrays representing the x-values of the data points.
    y (list): List of numpy arrays representing the y-values of the data points.
    labels (list): List of strings representing the labels for the chemical compounds.

    Returns:
    fig: Matplotlib figure object.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - scipy.stats

    Example:
    >>> x = [np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])]
    >>> y = [np.array([4,5,6]), np.array([7,8,9]), np.array([10,11,12])]
    >>> labels = ['H₂O', 'O₂', 'CO₂']
    >>> fig = task_func(x, y, labels)
    """
    fig, ax = plt.subplots()

    for i in range(len(x)):
        mu = np.mean(y[i])
        sigma = np.std(y[i])
        pdf = stats.norm.pdf(x[i], mu, sigma)
        ax.plot(x[i], pdf, label=labels[i])
    
    ax.legend()
    
    return fig


class TestTaskFunc(unittest.TestCase):
    
    def test_valid_input(self):
        x = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        y = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        labels = ['A', 'B']
        fig = task_func(x, y, labels)
        self.assertIsInstance(fig, plt.Figure)

    def test_empty_input(self):
        x = []
        y = []
        labels = []
        fig = task_func(x, y, labels)
        self.assertIsInstance(fig, plt.Figure)
    
    def test_single_distribution(self):
        x = [np.array([1, 2, 3])]
        y = [np.array([2, 3, 4])]
        labels = ['Test']
        fig = task_func(x, y, labels)
        canvas = FigureCanvas(fig)
        canvas.draw()
        self.assertEqual(len(fig.axes), 1)

    def test_different_lengths(self):
        x = [np.array([1, 2, 3]), np.array([4, 5])]
        y = [np.array([1, 2, 3]), np.array([4, 5, 6])]
        labels = ['A', 'B']
        with self.assertRaises(IndexError):
            task_func(x, y, labels)

    def test_labels_match_length(self):
        x = [np.array([1, 2, 3])]
        y = [np.array([4, 5, 6])]
        labels = ['A', 'B']
        with self.assertRaises(ValueError):
            task_func(x, y, labels)


if __name__ == '__main__':
    unittest.main()