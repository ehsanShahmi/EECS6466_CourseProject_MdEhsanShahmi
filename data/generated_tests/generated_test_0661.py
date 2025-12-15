import unittest
import numpy as np
import pandas as pd
import seaborn as sns
from io import BytesIO
import matplotlib.pyplot as plt

# Constants
LABELS = ['H\u2082O', 'O\u2082', 'CO\u2082', 'N\u2082', 'Ar']

# The provided prompt code is not to be modified or run

class TestTaskFunc(unittest.TestCase):

    def test_shape_of_dataframe(self):
        x = [np.array([1, 2]), np.array([3, 4])]
        y = [np.array([5, 6]), np.array([7, 8])]
        labels = ['H2O', 'O2']
        ax, df = task_func(x, y, labels)
        self.assertEqual(df.shape, (len(labels), 4), "DataFrame shape is incorrect.")

    def test_correct_labels(self):
        x = [np.array([1]), np.array([2])]
        y = [np.array([3]), np.array([4])]
        labels = ['H2O', 'O2']
        ax, df = task_func(x, y, labels)
        self.assertListEqual(list(df.index), labels, "DataFrame labels do not match.")

    def test_data_content(self):
        x = [np.array([1, 2]), np.array([3, 4])]
        y = [np.array([5, 6]), np.array([7, 8])]
        labels = ['H2O', 'O2']
        ax, df = task_func(x, y, labels)
        expected_data = [[1, 2, 5, 6], [3, 4, 7, 8]]
        pd.testing.assert_frame_equal(df.values, expected_data, check_dtype=False)

    def test_heatmap_return_type(self):
        x = [np.array([1]), np.array([2])]
        y = [np.array([3]), np.array([4])]
        labels = ['H2O', 'O2']
        ax, df = task_func(x, y, labels)
        self.assertIsInstance(ax, sns.matrix.Heatmap, "Return type is not a seaborn heatmap.")

    def test_heatmap_display(self):
        x = [np.array([1, 2]), np.array([3, 4])]
        y = [np.array([5, 6]), np.array([7, 8])]
        labels = ['H2O', 'O2']
        ax, df = task_func(x, y, labels)
        
        # Save the heatmap to a BytesIO object to test if it can be rendered
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        self.assertGreater(buf.getbuffer().nbytes, 0, "Heatmap did not render correctly.")

# Run the test suite
if __name__ == '__main__':
    unittest.main()