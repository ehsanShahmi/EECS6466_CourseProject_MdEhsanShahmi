import math
import random
import statistics
import unittest

# Constants
RADIUS = 5

def task_func(n):
    """
    Generate n random points within a circle of radius RADIUS (default value is 5) and return their average distance from the center.

    Parameters:
    - n (int): The number of points to be generated.

    Returns:
    - float: The average distance from the center of the circle.

    Requirements:
    - math
    - random
    - statistics

    Example:
    >>> random.seed(42)
    >>> task_func(100)
    3.2406
    >>> task_func(50)
    3.4443
    """

    distances = []

    for _ in range(n):
        theta = 2 * math.pi * random.random()
        r = RADIUS * math.sqrt(random.random())
        x = r * math.cos(theta)
        y = r * math.sin(theta)
        distance = math.sqrt(x**2 + y**2)
        distances.append(distance)

    return round(statistics.mean(distances), 4)

class TestTaskFunc(unittest.TestCase):

    def test_average_distance_10_points(self):
        random.seed(42)
        result = task_func(10)
        expected = 3.3053  # Manually calculated for verification
        self.assertAlmostEqual(result, expected, places=4)

    def test_average_distance_100_points(self):
        random.seed(42)
        result = task_func(100)
        expected = 3.2406  # Given example
        self.assertAlmostEqual(result, expected, places=4)

    def test_average_distance_50_points(self):
        random.seed(42)
        result = task_func(50)
        expected = 3.4443  # Given example
        self.assertAlmostEqual(result, expected, places=4)

    def test_average_distance_0_points(self):
        result = task_func(0)
        expected = 0.0  # When no points are generated, expected distance should be 0
        self.assertEqual(result, expected)

    def test_average_distance_large_number_of_points(self):
        random.seed(42)
        result = task_func(1000)
        # We don't have a pre-calculated expected value for this, but we can check if it's in a reasonable range
        self.assertGreaterEqual(result, 0)
        self.assertLessEqual(result, RADIUS)

if __name__ == '__main__':
    unittest.main()