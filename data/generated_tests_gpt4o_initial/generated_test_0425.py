import unittest
import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Here is your prompt:
def task_func(image_path='image.jpg', histogram_path='histogram.png'):
    """
    Read an image, create a histogram of the image pixel intensities, save the histogram as a PNG file, 
    and return the histogram plot object. The function also displays the original image and its histogram.
    The limit to the size of the image depends on the hardware capabilities of the system you are working on. 
    A possible size of an image is 20x20. 

    Parameters:
    - image_path (str): Path to the image file. Defaults to 'image.jpg'.
    - histogram_path (str): Path to save the histogram PNG file. Defaults to 'histogram.png'.

    Returns:
    - matplotlib.axes.Axes: The Axes object of the histogram plot.

    Raises:
    - FileNotFoundError: If the image file does not exist at the specified path.

    Requirements:
    - opencv
    - os
    - matplotlib.pyplot

    Example:
    >>> create_dummy_image('image.jpg')
    >>> histogram_axes = task_func('image.jpg', 'histogram.png')
    >>> os.remove('histogram.png')
    >>> os.remove('image.jpg')
    >>> histogram_axes.title.get_text()
    'Grayscale Histogram'
    """

    if not os.path.exists(image_path):
        raise FileNotFoundError(f"No image found at {image_path}")

    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of Pixels")
    axes = plt.plot(hist)[0].axes
    plt.savefig(histogram_path)
    return axes


def create_dummy_image(file_path):
    """Creates a simple black image for testing purposes."""
    img = np.zeros((20, 20), dtype=np.uint8)
    cv2.imwrite(file_path, img)


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Create a dummy image for testing."""
        self.image_path = 'test_image.jpg'
        self.histogram_path = 'test_histogram.png'
        create_dummy_image(self.image_path)

    def tearDown(self):
        """Remove test files after each test."""
        if os.path.exists(self.image_path):
            os.remove(self.image_path)
        if os.path.exists(self.histogram_path):
            os.remove(self.histogram_path)

    def test_file_not_found(self):
        """Test for FileNotFoundError when the image file does not exist."""
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_image.jpg')

    def test_histogram_creation(self):
        """Test if the histogram file is created successfully."""
        task_func(self.image_path, self.histogram_path)
        self.assertTrue(os.path.exists(self.histogram_path))

    def test_histogram_properties(self):
        """Test if the histogram plot has the correct title."""
        axes = task_func(self.image_path, self.histogram_path)
        self.assertEqual(axes.title.get_text(), 'Grayscale Histogram')

    def test_image_loaded_grayscale(self):
        """Test if the image is loaded in grayscale mode."""
        task_func(self.image_path, self.histogram_path)
        img = cv2.imread(self.image_path, cv2.IMREAD_GRAYSCALE)
        self.assertEqual(len(img.shape), 2)  # Grayscale image has 2 dimensions


if __name__ == "__main__":
    unittest.main()