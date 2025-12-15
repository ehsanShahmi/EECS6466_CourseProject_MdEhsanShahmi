import unittest
import numpy as np
import cv2
import os
import matplotlib.pyplot as plt

class TestImageBlurring(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dummy_img_path = "test_image.jpg"
        cls.dummy_img = np.random.randint(0, 255, (20, 20, 3), dtype=np.uint8)
        cv2.imwrite(cls.dummy_img_path, cls.dummy_img)

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.dummy_img_path):
            os.remove(cls.dummy_img_path)

    def test_blur_with_valid_kernel_size(self):
        blurred_img, ax_original, ax_blurred = task_func(self.dummy_img_path, 5)
        self.assertEqual(blurred_img.shape, self.dummy_img.shape)
        self.assertIsInstance(ax_original, plt.Axes)
        self.assertIsInstance(ax_blurred, plt.Axes)

    def test_blur_with_negative_kernel_size(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.dummy_img_path, -3)
        self.assertEqual(str(context.exception), "kernel_size must be a positive integer")

    def test_blur_with_zero_kernel_size(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.dummy_img_path, 0)
        self.assertEqual(str(context.exception), "kernel_size must be a positive integer")

    def test_blur_with_non_integer_kernel_size(self):
        with self.assertRaises(ValueError) as context:
            task_func(self.dummy_img_path, 2.5)
        self.assertEqual(str(context.exception), "kernel_size must be a positive integer")

    def test_blur_with_invalid_image_path(self):
        with self.assertRaises(FileNotFoundError) as context:
            task_func("invalid_image.jpg", 3)
        self.assertTrue("No image found at invalid_image.jpg" in str(context.exception))

if __name__ == '__main__':
    unittest.main()