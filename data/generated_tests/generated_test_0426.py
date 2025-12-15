import unittest
import numpy as np
import os
import cv2

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        """Create a temporary image for testing."""
        self.image_path = 'test_image.jpg'
        self.dummy_image = np.random.randint(0, 256, (20, 20), dtype=np.uint8)
        cv2.imwrite(self.image_path, self.dummy_image)

    def tearDown(self):
        """Remove the test image after each test."""
        if os.path.exists(self.image_path):
            os.remove(self.image_path)
        if os.path.exists('binary_image.jpg'):
            os.remove('binary_image.jpg')

    def test_valid_threshold(self):
        """Test the function with a valid threshold."""
        original_img_array, binary_img_array = task_func(self.image_path, 128)
        self.assertEqual(original_img_array.shape, (20, 20))
        self.assertEqual(binary_img_array.shape, (20, 20))

    def test_threshold_out_of_bounds(self):
        """Test the function with an out-of-bounds threshold."""
        with self.assertRaises(ValueError):
            task_func(self.image_path, -1)
        with self.assertRaises(ValueError):
            task_func(self.image_path, 256)

    def test_non_integer_threshold(self):
        """Test the function with a non-integer threshold."""
        with self.assertRaises(ValueError):
            task_func(self.image_path, 128.5)

    def test_file_not_found(self):
        """Test the function with a non-existing image file."""
        os.remove(self.image_path)
        with self.assertRaises(FileNotFoundError):
            task_func(self.image_path, 128)

    def test_binarization_accuracy(self):
        """Test if binarized image is correctly generated based on the threshold."""
        original_img_array, binary_img_array = task_func(self.image_path, 128)
        expected_binary_array = np.where(original_img_array >= 128, 255, 0).astype('uint8')
        np.testing.assert_array_equal(binary_img_array, expected_binary_array)

if __name__ == '__main__':
    unittest.main()