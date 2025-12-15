import unittest
import os
import numpy as np
import cv2

# Here is your prompt:
#
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# import numpy as np
# import cv2
# import os
#
# def task_func(file_path, onpick):
#     """
#     Draw the color histogram of an image in 3D and call a function when a data point is selected.
#
#     Parameters:
#     file_path (str): The path to the image file.
#     onpick (function): The function to be called when a data point is picked.
#
#     Returns:
#     matplotlib.axes.Axes: The Axes object of the 3D plot.
#
#     Raises:
#     FileNotFoundError: If the image file does not exist.
#     
#     Requirements:
#     - matplotlib
#     - mpl_toolkits.mplot3d
#     - numpy
#     - cv2
#     - os
#     - tempfile
#     
#     Example:
#     >>> def onpick(event):
#     ...     ind = event.ind
#     ...     print(f'You picked data point(s) {ind}')
#     >>> np.random.seed(42)
#     >>> dummy_img_path = 'image.jpg'
#     >>> dummy_img = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)
#     >>> cv2.imwrite(dummy_img_path, dummy_img)
#     True
#     >>> ax = task_func('image.jpg', onpick)
#     >>> os.remove(dummy_img_path)
#     """
#
#               if not os.path.exists(file_path):
#         raise FileNotFoundError(f"No file found at {file_path}")
#
#     img = cv2.imread(file_path)
#     color = ('b', 'g', 'r')
#     fig = plt.figure()
#     ax = Axes3D(fig)
#
#     for i, col in enumerate(color):
#         hist = cv2.calcHist([img], [i], None, [256], [0, 256])
#         ax.plot(np.arange(256), hist, color=col)
#
#     fig.canvas.mpl_connect('pick_event', onpick)
#
#     # plt.show()
#
#     return ax


class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        self.dummy_img_path = 'temp_image.jpg'
        self.dummy_img = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)
        cv2.imwrite(self.dummy_img_path, self.dummy_img)

    def tearDown(self):
        if os.path.exists(self.dummy_img_path):
            os.remove(self.dummy_img_path)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_image.jpg', lambda x: None)

    def test_valid_image_returns_axes(self):
        ax = task_func(self.dummy_img_path, lambda x: None)
        self.assertIsNotNone(ax)
        self.assertTrue(isinstance(ax, Axes3D))

    def test_histogram_colors(self):
        ax = task_func(self.dummy_img_path, lambda x: None)
        handles, _ = ax.get_legend_handles_labels()
        colors = ['b', 'g', 'r']
        self.assertEqual([handle.get_color() for handle in handles], colors)

    def test_onpick_function_called(self):
        picked = []
        
        def onpick(event):
            picked.append(event.ind)
        
        ax = task_func(self.dummy_img_path, onpick)
        fig = ax.figure
        fig.canvas.draw()
        
        # Simulate a pick event
        event = type('Event', (object,), {'ind': [1]})
        fig.canvas.trigger_event('pick_event', event)
        
        self.assertEqual(picked, [[1]])

    def test_histogram_range(self):
        ax = task_func(self.dummy_img_path, lambda x: None)
        for i, color in enumerate(['b', 'g', 'r']):
            hist = ax.get_lines()[i].get_data()[1]
            self.assertTrue(np.all(hist >= 0))  # Histogram values should be >= 0
            self.assertTrue(np.all(hist <= 20))  # Since we have a 20x20 image, max value should be <= 20


if __name__ == '__main__':
    unittest.main()