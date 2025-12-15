from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import os
import unittest

# Here is your prompt:
def task_func(img_path, angle):
    """
    Open an image, rotate it around a certain angle, and then display both the original and the rotated images side by side. 
    Additionally, return both images as numpy arrays.

    Parameters:
    img_path (str): The path of the image file.
    angle (float): The angle to rotate the image (in degrees).

    Returns:
    tuple: A tuple containing two numpy arrays, the first representing the original image and 
           the second representing the rotated image. Expands the rotated image to make it large enough to hold the entire rotated image.

    Raises:
    FileNotFoundError: If the image file does not exist at the specified path.

    Requirements:
    - PIL
    - matplotlib
    - numpy
    - os

    Example:
    >>> img_path = 'sample.png'
    >>> create_dummy_image(image_path=img_path)
    >>> original_img_array, rotated_img_array = task_func(img_path, 45)
    >>> os.remove(img_path)
    """

    if not os.path.exists(img_path):
        raise FileNotFoundError(f"No file found at {img_path}")
    
    img = Image.open(img_path)
    rotated_img = img.rotate(angle, expand=True)

    # Convert images to numpy arrays
    original_img_array = np.array(img)
    rotated_img_array = np.array(rotated_img)
    
    # Display original and rotated images side by side
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title('Original Image')
    plt.subplot(1, 2, 2)
    plt.imshow(rotated_img)
    plt.title('Rotated Image')

    return original_img_array, rotated_img_array


class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        # Create a dummy image to be used for testing
        self.img_path = 'test_image.png'
        self.create_dummy_image(self.img_path)

    def tearDown(self):
        # Remove the created image after tests
        if os.path.exists(self.img_path):
            os.remove(self.img_path)

    def create_dummy_image(self, img_path):
        # Create a simple 100x100 red image for testing
        img = Image.new('RGB', (100, 100), color='red')
        img.save(img_path)

    def test_valid_rotation(self):
        original_img_array, rotated_img_array = task_func(self.img_path, 90)
        self.assertEqual(original_img_array.shape, (100, 100, 3))
        self.assertEqual(rotated_img_array.shape, (100, 100, 3))

    def test_non_existent_image(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_image.png', 45)

    def test_rotation_angle(self):
        original_img_array, rotated_img_array = task_func(self.img_path, 45)
        self.assertIsInstance(original_img_array, np.ndarray)
        self.assertIsInstance(rotated_img_array, np.ndarray)

    def test_image_contents(self):
        original_img_array, rotated_img_array = task_func(self.img_path, 180)
        self.assertNotEqual(np.array_equal(original_img_array, rotated_img_array), True)

    def test_image_shape_after_rotation(self):
        original_img_array, rotated_img_array = task_func(self.img_path, 45)
        self.assertGreater(rotated_img_array.shape[0], original_img_array.shape[0])
        self.assertGreater(rotated_img_array.shape[1], original_img_array.shape[1])


if __name__ == '__main__':
    unittest.main()