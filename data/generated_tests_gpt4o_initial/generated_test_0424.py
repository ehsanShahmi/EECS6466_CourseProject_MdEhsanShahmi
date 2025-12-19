import unittest
import numpy as np
import os

class TestTaskFunc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.image_path = 'test_image.jpg'
        cls.create_dummy_image(cls.image_path, (10, 10, 3))

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.image_path):
            os.remove(cls.image_path)
        for i in range(1, 4):  # Assuming there will be at most 3 cluster images created
            cluster_image = f'cluster_{i}.jpg'
            if os.path.exists(cluster_image):
                os.remove(cluster_image)

    @staticmethod
    def create_dummy_image(image_path, shape):
        """ Create a dummy RGB image for testing purposes. """
        dummy_image = np.random.randint(0, 256, size=shape, dtype=np.uint8)
        cv2.imwrite(image_path, cv2.cvtColor(dummy_image, cv2.COLOR_RGB2BGR))

    def test_image_reading(self):
        original_img, segmented_img = task_func(self.image_path, n_clusters=3)
        self.assertEqual(original_img.shape, (10, 10, 3))
        self.assertEqual(segmented_img.shape, (10, 10, 3))

    def test_n_clusters_one(self):
        original_img, segmented_img = task_func(self.image_path, n_clusters=1)
        np.testing.assert_array_equal(original_img, segmented_img)

    def test_invalid_image_path(self):
        with self.assertRaises(FileNotFoundError):
            task_func('invalid_path.jpg', n_clusters=3)

    def test_invalid_n_clusters(self):
        with self.assertRaises(ValueError):
            task_func(self.image_path, n_clusters=0)
        
        with self.assertRaises(ValueError):
            task_func(self.image_path, n_clusters=-1)

    def test_cluster_images_created(self):
        original_img, segmented_img = task_func(self.image_path, n_clusters=3)
        for i in range(1, 4):
            self.assertTrue(os.path.exists(f'cluster_{i}.jpg'))

if __name__ == '__main__':
    unittest.main()