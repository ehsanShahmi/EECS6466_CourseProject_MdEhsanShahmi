import unittest
from matplotlib.axes import Axes
from matplotlib import pyplot as plt
from your_module import Object, task_func  # Replace 'your_module' with the actual module name where the code is located


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.objects = [Object(value=i) for i in range(10)]

    def test_return_type(self):
        ax = task_func(self.objects, 'value')
        self.assertIsInstance(ax, Axes, "Return type should be matplotlib.axes._axes.Axes")

    def test_histogram_length(self):
        ax = task_func(self.objects, 'value')
        counts = ax.patches  # Getting the histogram bars
        self.assertEqual(len(counts), 30, "Number of histogram bins should be 30 by default")

    def test_histogram_values(self):
        ax = task_func(self.objects, 'value')

        # Get the heights of the histogram bars
        heights = [patch.get_height() for patch in ax.patches]

        # Check that heights are non-negative
        self.assertTrue(all(h >= 0 for h in heights), "Histogram counts should be non-negative")

    def test_histogram_title(self):
        ax = task_func(self.objects, 'value')
        self.assertEqual(ax.title.get_text(), 'Histogram of attribute values', "Histogram title should be 'Histogram of attribute values'")

    def test_histogram_labels(self):
        ax = task_func(self.objects, 'value')
        self.assertEqual(ax.get_xlabel(), 'Attribute Value', "X-axis label should be 'Attribute Value'")
        self.assertEqual(ax.get_ylabel(), 'Count', "Y-axis label should be 'Count'")


if __name__ == '__main__':
    unittest.main()