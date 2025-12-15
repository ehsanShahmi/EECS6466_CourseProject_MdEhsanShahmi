import unittest
import numpy as np
import cv2
import os

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.dummy_image_path = 'dummy_image.png'
        np.random.seed(48)
        self.dummy_image = np.random.randint(0, 256, (10, 10), dtype=np.uint8)
        cv2.imwrite(self.dummy_image_path, self.dummy_image)

    def tearDown(self):
        if os.path.exists(self.dummy_image_path):
            os.remove(self.dummy_image_path)

    def test_histogram_shape(self):
        histogram = task_func(self.dummy_image_path)
        self.assertEqual(histogram.shape, (256,))

    def test_histogram_values(self):
        histogram = task_func(self.dummy_image_path)
        for count in histogram:
            self.assertGreaterEqual(count, 0)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func('non_existent_image.png')

    def test_invalid_image_file(self):
        invalid_image_path = 'invalid_image.txt'
        with open(invalid_image_path, 'w') as f:
            f.write("This is not an image.")
        with self.assertRaises(ValueError):
            task_func(invalid_image_path)
        os.remove(invalid_image_path)

    def test_histogram_sum(self):
        histogram = task_func(self.dummy_image_path)
        self.assertEqual(np.sum(histogram), self.dummy_image.size)

if __name__ == '__main__':
    unittest.main()