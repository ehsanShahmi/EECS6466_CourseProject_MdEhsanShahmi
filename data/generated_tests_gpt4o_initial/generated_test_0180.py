import os
import numpy as np
from PIL import Image
from skimage.transform import resize
import matplotlib.pyplot as plt
import unittest

# Here is your prompt:
def task_func(img_path, scale_factors=[0.5, 0.75, 1.5, 2.0]):
    """
    Open an image file and scale it by different scaling factors.
    Display each scaled image using matplotlib and return the scaled images with their Axes.

    Parameters:
    img_path (str): Path to the image file.
    scale_factors (list): List of scaling factors to apply. Default is [0.5, 0.75, 1.5, 2.0].

    Returns:
    list of tuples: Each tuple contains (matplotlib.axes.Axes, numpy.ndarray) representing the Axes and the pixel values of the scaled image.

    Raises:
    FileNotFoundError: If the image file cannot be found.

    Requirements:
    - PIL
    - numpy
    - scikit-image
    - matplotlib.pyplot
    - os

    Example:
    >>> dummy_img_path = "sample.png"
    >>> Image.fromarray(np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)).save(dummy_img_path)
    >>> result = task_func('sample.png')
    >>> os.remove(dummy_img_path)
    >>> for ax, img in result:
    ...     print(ax.get_title(), img.shape)
    Scale factor: 0.5 (10, 10, 3)
    Scale factor: 0.75 (15, 15, 3)
    Scale factor: 1.5 (30, 30, 3)
    Scale factor: 2.0 (40, 40, 3)
    """

    if not os.path.exists(img_path):
        raise FileNotFoundError(f"No file found at {img_path}")

    im = Image.open(img_path)
    img_arr = np.array(im)
    results = []

    for scale_factor in scale_factors:
        scaled_img_arr = resize(img_arr, (int(im.height * scale_factor), int(im.width * scale_factor)),
                                mode='reflect', anti_aliasing=True)
        fig, ax = plt.subplots()
        ax.imshow(scaled_img_arr)
        ax.set_title(f'Scale factor: {scale_factor}')
        results.append((ax, scaled_img_arr))
    # plt.show()
    return results

class TestImageScaling(unittest.TestCase):
    
    def setUp(self):
        # Create a dummy image for testing
        self.dummy_img_path = "test_image.png"
        self.dummy_image = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)
        Image.fromarray(self.dummy_image).save(self.dummy_img_path)

    def tearDown(self):
        # Remove dummy image after tests
        if os.path.exists(self.dummy_img_path):
            os.remove(self.dummy_img_path)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func("non_existent_image.png")

    def test_scale_factors_length(self):
        result = task_func(self.dummy_img_path)
        self.assertEqual(len(result), 4)  # The default scale factors length is 4

    def test_scaled_image_shapes(self):
        result = task_func(self.dummy_img_path)
        expected_shapes = [(10, 10, 3), (15, 15, 3), (30, 30, 3), (40, 40, 3)]
        
        for i, (ax, img) in enumerate(result):
            self.assertEqual(img.shape, expected_shapes[i])

    def test_axes_titles(self):
        result = task_func(self.dummy_img_path)
        expected_titles = ['Scale factor: 0.5', 'Scale factor: 0.75', 'Scale factor: 1.5', 'Scale factor: 2.0']
        
        for i, (ax, img) in enumerate(result):
            self.assertEqual(ax.get_title(), expected_titles[i])

    def test_image_data_type(self):
        result = task_func(self.dummy_img_path)
        for _, img in result:
            self.assertEqual(img.dtype, np.float64)  # The output should be of type float64 due to resize

if __name__ == '__main__':
    unittest.main()