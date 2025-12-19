import numpy as np
import matplotlib.pyplot as plt
import unittest

def task_func():
    """
    Draws the linear equation y = 2x + 1 on a 2D plot for x values ranging from -10 to 10, and marks the solution for x = 2 with a green 'o' (circle) marker.

    The plot includes:
    - A red line representing the equation y = 2x + 1, labeled as 'y=2x+1', for x in [-10, 10].
    - A green circle marker indicating the solution at x = 2, y = 5.
    - Title: 'Solution of the equation y=2x+1 at x=2'
    - X-axis labeled as 'x', with a range from -10 to 10.
    - Y-axis labeled as 'y', with a range automatically adjusted based on the equation.
    - A legend indicating labels for the equation and the solution point.

    Returns:
        matplotlib.axes.Axes: An object representing the plot with specified features and ranges.
    """
    X = np.linspace(-10, 10, 400)  # X range specified
    y = 2 * X + 1

    fig, ax = plt.subplots()
    ax.plot(X, y, '-r', label='y=2x+1')
    
    solution_y = 2 * 2 + 1  # y value at x = 2
    ax.plot(2, solution_y, 'go', label='Solution at x=2')
    
    ax.set_title('Solution of the equation y=2x+1 at x=2')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_xlim([-10, 10])  # Explicitly setting the x-axis range
    ax.legend(loc='best')
    ax.grid()

    return ax

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.ax = task_func()

    def test_title(self):
        self.assertEqual(self.ax.get_title(), 'Solution of the equation y=2x+1 at x=2')
        
    def test_x_label(self):
        self.assertEqual(self.ax.get_xlabel(), 'x')
    
    def test_y_label(self):
        self.assertEqual(self.ax.get_ylabel(), 'y')
    
    def test_x_limits(self):
        x_limits = self.ax.get_xlim()
        self.assertEqual(x_limits[0], -10)
        self.assertEqual(x_limits[1], 10)
    
    def test_solution_point(self):
        # Check that the solution point is at (2, 5)
        lines = self.ax.get_lines()
        # The solution point should be a green circle marker
        solution_point = lines[1]  # Auto-index; assuming it is the second plotted line.
        self.assertEqual(solution_point.get_marker(), 'o')
        self.assertEqual(solution_point.get_color(), 'g')
        xdata, ydata = solution_point.get_data()
        self.assertEqual(xdata[0], 2)  # x value at solution point
        self.assertEqual(ydata[0], 5)  # y value at solution point

if __name__ == '__main__':
    unittest.main()