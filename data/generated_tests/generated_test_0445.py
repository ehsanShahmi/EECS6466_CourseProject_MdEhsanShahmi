import numpy as np
import unittest
from scipy.spatial import Voronoi
from task_module import task_func  # Assuming the function is saved in a file named task_module.py

class TestVoronoiDiagram(unittest.TestCase):
    
    def test_correct_output_types(self):
        points = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        vor, ax = task_func(points)
        self.assertIsInstance(vor, Voronoi, "Output should be a Voronoi object")
        self.assertIsNotNone(ax, "Output axes should not be None")

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            task_func("invalid input")

    def test_insufficient_points(self):
        points = np.array([[0, 0], [1, 1]])  # Only two points
        with self.assertRaises(ValueError):
            task_func(points)

    def test_invalid_point_shape(self):
        points = np.array([[0, 0, 0], [1, 1, 1], [2, 2, 2]])  # 3D points
        with self.assertRaises(ValueError):
            task_func(points)

    def test_voronoi_with_random_seed(self):
        points = np.array([[0, 0], [1, 1], [2, 2]])
        vor1, _ = task_func(points, seed=42)
        vor2, _ = task_func(points, seed=42)
        np.testing.assert_array_equal(vor1.vertices, vor2.vertices, "Vertices should be the same with the same random seed.")

if __name__ == '__main__':
    unittest.main()