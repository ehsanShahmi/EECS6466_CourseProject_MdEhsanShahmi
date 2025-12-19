import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
import unittest

def task_func(image, sigma=2):
    """
    Apply a Gaussian filter to a given image and draw the original and filtered images side by side.

    Parameters:
    - image (numpy.ndarray): The input image to apply the filter on.
    - sigma (float, optional): The sigma value for the Gaussian filter. Default is 2.

    Returns:
    - ax (matplotlib.axes.Axes): Axes object containing the plot. Two plots with titles 'Original' and 'Filtered'. 
    - filtered_image (numpy.ndarray): The numpy array of pixel values for the filtered image.

    Raises:
    - ValueError: If sigma is non-positive.
    - TypeError: If the input is not a numpy array.
    """
    
    if not isinstance(image, np.ndarray):
        raise TypeError("The image must be a numpy array.")
    if sigma <= 0:
        raise ValueError("Sigma must be positive.")

    filtered_image = gaussian_filter(image, sigma=sigma)

    fig, ax = plt.subplots(1, 2, figsize=(10, 5))

    ax[0].imshow(image, cmap=plt.cm.gray)
    ax[0].set_title('Original')

    ax[1].imshow(filtered_image, cmap=plt.cm.gray)
    ax[1].set_title('Filtered')

    return ax, filtered_image

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.image = np.random.rand(100, 100)  # Random test image
        self.image_invalid = "not an image"
        
    def test_valid_input(self):
        ax, filtered_image = task_func(self.image, sigma=2)
        self.assertEqual(ax[0].get_title(), 'Original')
        self.assertEqual(ax[1].get_title(), 'Filtered')
        self.assertIsInstance(filtered_image, np.ndarray)
        self.assertEqual(filtered_image.shape, self.image.shape)

    def test_sigma_positive(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.image, sigma=0)
        self.assertEqual(str(context.exception), "Sigma must be positive.")

    def test_sigma_negative(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.image, sigma=-1)
        self.assertEqual(str(context.exception), "Sigma must be positive.")

    def test_invalid_image_type(self):
        with self.assertRaises(TypeError) as context:
            task_func(self.image_invalid)
        self.assertEqual(str(context.exception), "The image must be a numpy array.")

    def test_sigma_default_value(self):
        ax, filtered_image = task_func(self.image)  # Test default sigma
        self.assertEqual(ax[0].get_title(), 'Original')
        self.assertEqual(ax[1].get_title(), 'Filtered')
        self.assertIsInstance(filtered_image, np.ndarray)

if __name__ == '__main__':
    unittest.main()