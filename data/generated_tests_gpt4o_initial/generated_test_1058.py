import unittest
import itertools
import seaborn as sns
import matplotlib.pyplot as plt

# Constants from the original prompt
SHAPES = [
    "Circle",
    "Square",
    "Triangle",
    "Rectangle",
    "Pentagon",
    "Hexagon",
    "Heptagon",
    "Octagon",
    "Nonagon",
    "Decagon",
]
COLORS = [
    "Red",
    "Blue",
    "Green",
    "Yellow",
    "Black",
    "White",
    "Purple",
    "Orange",
    "Pink",
    "Brown",
]

class TestTaskFunc(unittest.TestCase):

    def test_default_num_pairs(self):
        """Test if the function outputs the correct number of shape-color pairs by default."""
        ax = task_func()
        self.assertEqual(len(ax.patches), 10)

    def test_exceed_max_pairs(self):
        """Test if the function limits the number of pairs to the maximum possible (100)."""
        ax = task_func(150)
        self.assertEqual(len(ax.patches), 100)

    def test_minimum_pairs(self):
        """Test if the function returns at least 1 pair when num_pairs is set to 0."""
        ax = task_func(0)
        self.assertEqual(len(ax.patches), 0)

    def test_custom_num_pairs(self):
        """Test if the function outputs the correct number of pairs for a custom input."""
        ax = task_func(5)
        self.assertEqual(len(ax.patches), 5)

    def test_correct_labels(self):
        """Test if the function generates the correct labels for the first few pairs."""
        ax = task_func(10)
        expected_labels = [f"{s}:{c}" for s, c in itertools.product(SHAPES, COLORS)][:10]
        actual_labels = [tick.get_text() for tick in ax.get_xticklabels()]
        self.assertListEqual(actual_labels, expected_labels)

if __name__ == '__main__':
    unittest.main()