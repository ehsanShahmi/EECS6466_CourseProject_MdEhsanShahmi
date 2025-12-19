from unittest import TestCase, main
import pandas as pd
import numpy as np

class TestTaskFunc(TestCase):
    
    def setUp(self):
        # Sample data to use in the tests
        self.valid_data = pd.DataFrame({
            'Column1': [1, 2, 3, 4, 5],
            'Column2': [2, 4, 6, 8, 10],
        })
        self.invalid_data = pd.DataFrame({
            'ColumnA': [1, 2, 3],
            'ColumnB': [3, 2, 1],
        })
    
    def test_valid_input(self):
        """Test with valid input data."""
        result, ax = task_func(self.valid_data, 'Column1', 'Column2')
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 5)
    
    def test_column_existence(self):
        """Test if ValueError is raised if columns do not exist."""
        with self.assertRaises(ValueError):
            task_func(self.invalid_data, 'Column1', 'Column2')
    
    def test_slope_intercept(self):
        """Check if the computed slope and intercept are correct."""
        result, _ = task_func(self.valid_data, 'Column1', 'Column2')
        slope, intercept = result[0], result[1]
        self.assertAlmostEqual(slope, 2.0)
        self.assertAlmostEqual(intercept, 0.0)
    
    def test_r_value(self):
        """Check the r-value for perfect correlation."""
        result, _ = task_func(self.valid_data, 'Column1', 'Column2')
        r_value = result[2]
        self.assertAlmostEqual(r_value, 1.0)
    
    def test_standard_error(self):
        """Check if the standard error is a non-negative value."""
        result, _ = task_func(self.valid_data, 'Column1', 'Column2')
        std_err = result[4]
        self.assertGreaterEqual(std_err, 0)

if __name__ == '__main__':
    main()