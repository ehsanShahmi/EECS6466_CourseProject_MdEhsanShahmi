import unittest
from itertools import zip_longest
from scipy.spatial import distance

def task_func(points):
    """
    Calculate the Euclidean distances between consecutive points in a provided 
    list of 2D coordinates.

    This function takes a list of tuples, where each tuple contains two numbers
    representing a point in 2D space. It computes the Euclidean distance between
    each consecutive pair of points.

    If an empty list or a single point is passed, the function returns an empty list.
    If a tuple contains just one number it is assumed that both coordinates are equal to this number.
    Example: (2) == (2, 2)

    Parameters:
    points (list of tuples): A list of tuples where each tuple contains two 
                             numbers (x, y), representing a point in 2D space.

    Returns:
    list of floats: A list containing the Euclidean distances between 
                    consecutive points. Each distance is a float.
    
    Requirements:
    - itertools
    - scipy.spatial

    Example:
    >>> task_func([(1, 2), (3, 4), (5, 6), (7, 8)])
    [2.8284271247461903, 2.8284271247461903, 2.8284271247461903]

    >>> task_func([(1, 2), (4), (-1.2, 4)])
    [3.605551275463989, 5.2]
    """
    distances = []
    for point1, point2 in zip_longest(points, points[1:]):
        if point2 is not None:
            distances.append(distance.euclidean(point1, point2))
            
    return distances

class TestTaskFunc(unittest.TestCase):

    def test_multiple_points(self):
        self.assertAlmostEqual(task_func([(1, 2), (3, 4), (5, 6), (7, 8)]), [2.8284271247461903, 2.8284271247461903, 2.8284271247461903])

    def test_single_point(self):
        self.assertEqual(task_func([(1, 2)]), [])

    def test_empty_list(self):
        self.assertEqual(task_func([]), [])

    def test_point_with_one_value(self):
        self.assertAlmostEqual(task_func([(1, 2), (4), (-1.2, 4)]), [3.605551275463989, 5.2])

    def test_negative_coordinates(self):
        self.assertAlmostEqual(task_func([(-1, -2), (-3, -4), (-5, -6)]), [2.8284271247461903, 2.8284271247461903])

if __name__ == '__main__':
    unittest.main()