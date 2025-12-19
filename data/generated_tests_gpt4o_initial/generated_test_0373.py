import unittest
import numpy as np

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Sample data for the tests
        self.l1 = np.array([1, 4, 9, 16, 25])
        self.x1 = np.array([1, 2, 3, 4, 5])
        
        self.l2 = np.array([2, 8, 18, 32, 50])
        self.x2 = np.array([1, 2, 3, 4, 5])
        
        self.l3 = np.array([0, 1, 4, 9, 16])
        self.x3 = np.array([0, 1, 2, 3, 4])
        
        self.l4 = np.array([1, 2, 3, 4, 5])
        self.x4 = np.array([1, 1.5, 2, 2.5, 3])
        
        self.l5 = np.array([2, 4, 6, 8, 10])
        self.x5 = np.array([1, 2, 3, 4, 5])

    def test_fit_parameters_shape(self):
        params, _ = task_func(self.l1, self.x1)
        self.assertEqual(params.shape[0], 2, "Fitted parameters should have length 2.")

    def test_fitted_values_shape(self):
        _, fitted_values = task_func(self.l1, self.x1)
        self.assertEqual(fitted_values.shape, self.l1.shape, "Fitted values should match the shape of the input data.")

    def test_plot_return_type(self):
        _, _, ax = task_func(self.l1, self.x1, plot=True)
        self.assertIsNotNone(ax, "Axes object should be returned when plot is True.")

    def test_non_square_fit(self):
        params, fitted_values = task_func(self.l2, self.x2)
        expected_fitted_values = np.array([2, 8, 18, 32, 50])
        np.testing.assert_almost_equal(fitted_values, expected_fitted_values, decimal=1, 
                                       err_msg="Fitted values do not match expected for non-square data.")

    def test_zero_case(self):
        params, fitted_values = task_func(self.l3, self.x3)
        expected_fitted_values = np.array([0, 1, 4, 9, 16])
        np.testing.assert_almost_equal(fitted_values, expected_fitted_values, decimal=1, 
                                       err_msg="Fitted values do not match expected for zero case data.")

if __name__ == '__main__':
    unittest.main()