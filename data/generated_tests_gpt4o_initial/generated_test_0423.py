import numpy as np
import cv2
import os
import unittest

class TestTaskFunction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Create a dummy image for testing purposes."""
        cls.image_path = 'test_image.jpg'
        cls.image_height = 20
        cls.image_width = 20
        # Create a 20x20 grayscale image with random values
        dummy_image = np.random.randint(0, 256, (cls.image_height, cls.image_width), dtype=np.uint8)
        cv2.imwrite(cls.image_path, dummy_image)

    @classmethod
    def tearDownClass(cls):
        """Remove the dummy image after testing."""
        if os.path.exists(cls.image_path):
            os.remove(cls.image_path)

    def test_successful_execution(self):
        """Test to check if function executes successfully with valid input."""
        original_img_array, binary_img_array = task_func(self.image_path, 128)
        self.assertEqual(original_img_array.shape, (self.image_height, self.image_width))
        self.assertEqual(binary_img_array.shape, (self.image_height, self.image_width))

    def test_file_not_found(self):
        """Test to check if FileNotFoundError is raised for non-existent file."""
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_image.jpg', 128)

    def test_invalid_threshold_type(self):
        """Test to check if ValueError is raised for invalid threshold type (not integer)."""
        with self.assertRaises(ValueError):
            task_func(self.image_path, 'invalid_threshold')

    def test_threshold_out_of_range(self):
        """Test to check if ValueError is raised for threshold value outside the range (0-255)."""
        with self.assertRaises(ValueError):
            task_func(self.image_path, -1)  # Below range
        with self.assertRaises(ValueError):
            task_func(self.image_path, 256)  # Above range

    def test_threshold_boundary_values(self):
        """Test to check function output at the boundary threshold values (0 and 255)."""
        original_img_array_0, binary_img_array_0 = task_func(self.image_path, 0)
        original_img_array_255, binary_img_array_255 = task_func(self.image_path, 255)
        
        # Check binary image shapes
        self.assertEqual(binary_img_array_0.shape, (self.image_height, self.image_width))
        self.assertEqual(binary_img_array_255.shape, (self.image_height, self.image_width))
        
        # Check if binary image is fully white for threshold 0 (all values > 0 become white)
        self.assertTrue(np.all(binary_img_array_0 == 255)
        # Check if binary image is fully black for threshold 255 (all values <= 255 become black)
        self.assertTrue(np.all(binary_img_array_255 == 0))

if __name__ == '__main__':
    unittest.main()