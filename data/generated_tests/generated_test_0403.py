import unittest
import numpy as np
import os

# Here is your prompt:
from PIL import Image, ImageFilter
import cv2
import numpy as np
import os

def task_func(img_path, blur_radius=5):
    """
    Open an RGB image from a specific path, apply a blur filter, convert it to grayscale, and then display both the original and the edited images side by side.
    Returns numpy arrays representing both the original and the processed images.

    Parameters:
    - img_path (str): The path of the image file.
    - blur_radius (int): The radius of the Gaussian blur filter. Default is 5.

    Returns:
    - tuple: A tuple containing two numpy arrays, the first representing the original image and 
             the second representing the blurred and grayscaled image.

    Raises:
    - FileNotFoundError: If the image file does not exist at the specified path.

    Requirements:
    - PIL
    - opencv-python
    - numpy
    - os

    Example:
    >>> image_path = 'sample.png'
    >>> create_dummy_image(image_path=image_path)
    >>> original, processed = task_func(image_path)
    >>> os.remove(image_path)
    """

    if not os.path.exists(img_path):
        raise FileNotFoundError(f"No file found at {img_path}")

    img = Image.open(img_path)
    img = img.convert("RGB")

    blurred_img = img.filter(ImageFilter.GaussianBlur(blur_radius))
    grey_img = cv2.cvtColor(np.array(blurred_img), cv2.COLOR_RGB2GRAY)

    return np.array(img), np.array(grey_img)


class TestImageProcessing(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Create a dummy image file for testing purposes."""
        cls.image_path = 'test_image.png'
        cls.image_size = (100, 100)
        cls.dummy_image = Image.new('RGB', cls.image_size, color='red')
        cls.dummy_image.save(cls.image_path)

    @classmethod
    def tearDownClass(cls):
        """Remove the dummy image file after tests."""
        if os.path.exists(cls.image_path):
            os.remove(cls.image_path)

    def test_task_func_outputs(self):
        """Test if the task_func returns correct shape outputs."""
        original, processed = task_func(self.image_path)
        self.assertEqual(original.shape, (100, 100, 3))
        self.assertEqual(processed.shape, (100, 100))

    def test_task_func_blur_effect(self):
        """Test that processed image is different from the original."""
        original, processed = task_func(self.image_path)
        # Check if the processed image is indeed grayscale (single channel)
        self.assertEqual(processed.ndim, 2)
        self.assertFalse(np.array_equal(original, processed))

    def test_task_func_file_not_found(self):
        """Test if task_func raises FileNotFoundError for non-existent file."""
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_image.png')

    def test_task_func_default_blur_radius(self):
        """Test if the function works with the default blur radius."""
        original, processed = task_func(self.image_path)
        self.assertIsNotNone(processed)

    def test_task_func_custom_blur_radius(self):
        """Test if the function works with a custom blur radius."""
        original, processed = task_func(self.image_path, blur_radius=10)
        self.assertIsNotNone(processed)
        self.assertFalse(np.array_equal(original, processed))


if __name__ == '__main__':
    unittest.main()