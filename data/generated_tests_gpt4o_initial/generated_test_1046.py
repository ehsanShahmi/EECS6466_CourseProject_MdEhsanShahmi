import unittest
import pandas as pd

# Constants
EMPLOYEES = ["John", "Alice", "Bob", "Charlie", "Dave"]

class TestTaskFunc(unittest.TestCase):

    def test_return_type(self):
        """Test if the function returns a DataFrame."""
        result = task_func('2023-06-15')
        self.assertIsInstance(result, pd.DataFrame)

    def test_correct_columns(self):
        """Test if the DataFrame has the correct columns 'Employee' and 'Date'."""
        result = task_func('2023-06-15')
        self.assertListEqual(list(result.columns), ['Employee', 'Date'])

    def test_number_of_rows(self):
        """Test if the DataFrame has the correct number of rows."""
        result = task_func('2023-06-15')
        self.assertEqual(len(result), len(EMPLOYEES) * 10)  # 5 employees * 10 dates

    def test_date_range(self):
        """Test if the generated dates are within the expected range for a specific start date."""
        start_date = pd.to_datetime('2023-06-15')
        result = task_func('2023-06-15')
        expected_dates = pd.date_range(start_date, periods=10).tolist()

        # Extracting dates from the DataFrame
        generated_dates = result['Date'].unique()

        # Check if generated unique dates match the expected dates
        for employee in EMPLOYEES:
            employee_dates = result[result['Employee'] == employee]['Date'].tolist()
            self.assertListEqual(employee_dates, expected_dates)

    def test_input_format(self):
        """Test if an incorrect date format raises a ValueError."""
        with self.assertRaises(ValueError):
            task_func('15-06-2023')  # Invalid format

if __name__ == '__main__':
    unittest.main()