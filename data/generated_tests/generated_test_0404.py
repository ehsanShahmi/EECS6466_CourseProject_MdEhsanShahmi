import unittest
import cv2
import numpy as np
import os

# Here is your prompt:
import cv2
import numpy as np
import os

def task_func(img_path):
    """
    Open an RGB image, convert it to grayscale, find contours using the cv2 library, and return the original image and contours.

    Parameters:
    - img_path (str): The path of the image file.

    Returns:
    - tuple: A tuple containing the original image as a numpy array and a list of contours.

    Raises:
    - FileNotFoundError: If the image file does not exist at the specified path.

    Requirements:
    - opencv-python
    - numpy
    - os

    Example:
    >>> img_path = 'sample.png'
    >>> create_dummy_image(image_path=img_path)
    >>> img, contours = task_func(img_path)
    >>> os.remove(img_path)
    """

               if not os.path.exists(img_path):
        raise FileNotFoundError(f"No file found at {img_path}")
    
    img = cv2.imread(img_path)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Find contours
    contours, _ = cv2.findContours(gray_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return np.array(img), contours

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        # Create a dummy image for testing
        self.test_image_path = 'test_image.png'
        self.create_dummy_image(self.test_image_path)
    
    def create_dummy_image(self, image_path):
        # Create a simple black square on a white background
        img = np.ones((100, 100, 3), dtype=np.uint8) * 255
        cv2.rectangle(img, (20, 20), (80, 80), (0, 0, 0), -1)  # Draw a black square
        cv2.imwrite(image_path, img)
    
    def test_valid_image(self):
        img, contours = task_func(self.test_image_path)
        self.assertIsInstance(img, np.ndarray)
        self.assertEqual(len(contours), 1)
    
    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_image.png')

    def test_grayscale_conversion(self):
        img, contours = task_func(self.test_image_path)
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        self.assertEqual(gray_img.shape, (100, 100))
    
    def test_contour_shape(self):
        img, contours = task_func(self.test_image_path)
        self.assertTrue(isinstance(contours, list))
        self.assertGreater(len(contours), 0)
    
    def tearDown(self):
        if os.path.exists(self.test_image_path):
            os.remove(self.test_image_path)

if __name__ == '__main__':
    unittest.main()