import numpy as np
import unittest

class TestTaskFunc(unittest.TestCase):

    def test_correct_output_shape(self):
        """ Test if the output shape is correct """
        X = np.linspace(-10, 10, 1000)
        result = task_func(X)
        self.assertEqual(result.shape, X.shape)

    def test_correct_output_type(self):
        """ Test if the output is of the correct type """
        X = np.linspace(-10, 10, 1000)
        result = task_func(X)
        self.assertIsInstance(result, np.ndarray)

    def test_type_error_on_invalid_input(self):
        """ Test if TypeError is raised for non-numpy input """
        with self.assertRaises(TypeError):
            task_func("not_a_numpy_array")

    def test_output_values(self):
        """ Test if the output values are complex numbers """
        X = np.linspace(-10, 10, 1000)
        result = task_func(X)
        self.assertTrue(np.iscomplexobj(result))

    def test_real_part_mean(self):
        """ Test if the mean of the real part is close to the expected value """
        X = np.linspace(-10, 10, 1000)
        result = task_func(X)
        real_mean = np.mean(result.real)
        self.assertAlmostEqual(real_mean, 0, delta=0.1)  # Expecting close to 0

if __name__ == '__main__':
    unittest.main()