import pandas as pd
import os
import unittest

# Here is your prompt:
def task_func(original_file_location="test.xlsx", new_file_location="new_test.xlsx", sheet_name="Sheet1"):
    """
    Copies data from an Excel spreadsheet into a new Excel file, then reads the new Excel file and returns its contents.

    Parameters:
    - original_file_location (str): Path to the original Excel file. Defaults to 'test.xlsx'.
    - new_file_location (str): Path to save the new Excel file. Defaults to 'new_test.xlsx'.
    - sheet_name (str): Name of the sheet to load data from. Defaults to 'Sheet1'.

    Returns:
    - DataFrame: A pandas DataFrame representing the content of the new Excel file.

    Raises:
    - FileNotFoundError: If the original Excel file does not exist at the specified path.
    - ValueError: If the specified sheet does not exist in the workbook.

    Requirements:
    - pandas
    - os

    Example:
    >>> file_path, file_new_path, sheet_name = 'test.xlsx', 'new_test.xlsx', 'Sheet1'
    >>> create_dummy_excel(file_path, sheet_name)
    >>> df = task_func(file_path, file_new_path, sheet_name)
    >>> os.remove(file_path)
    >>> os.remove(file_new_path)
    """

    if not os.path.exists(original_file_location):
        raise FileNotFoundError(f"No file found at {original_file_location}")

    # Read data from the original Excel file
    try:
        original_df = pd.read_excel(original_file_location, sheet_name=sheet_name)
    except ValueError as e:
        raise ValueError(f"Error reading sheet: {e}")

    # Write data to a new Excel file
    original_df.to_excel(new_file_location, index=False)

    # Read and return data from the new Excel file
    new_df = pd.read_excel(new_file_location)
    return new_df

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a dummy Excel file for testing
        self.file_path = "test.xlsx"
        self.new_file_path = "new_test.xlsx"
        self.sheet_name = "Sheet1"
        data = {"Column1": [1, 2], "Column2": [3, 4]}
        df = pd.DataFrame(data)
        df.to_excel(self.file_path, index=False, sheet_name=self.sheet_name)

    def tearDown(self):
        # Remove created files after tests
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        if os.path.exists(self.new_file_path):
            os.remove(self.new_file_path)

    def test_valid_conversion(self):
        df = task_func(self.file_path, self.new_file_path, self.sheet_name)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(df.shape, (2, 2))  # Check if it has the correct shape

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            task_func("non_existent_file.xlsx", self.new_file_path, self.sheet_name)

    def test_sheet_not_found(self):
        df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        df.to_excel(self.file_path, index=False, sheet_name="OtherSheet")
        with self.assertRaises(ValueError):
            task_func(self.file_path, self.new_file_path, self.sheet_name)

    def test_output_file_created(self):
        task_func(self.file_path, self.new_file_path, self.sheet_name)
        self.assertTrue(os.path.exists(self.new_file_path))

    def test_data_in_output_file(self):
        task_func(self.file_path, self.new_file_path, self.sheet_name)
        df = pd.read_excel(self.new_file_path)
        expected_data = {"Column1": [1, 2], "Column2": [3, 4]}
        expected_df = pd.DataFrame(expected_data)
        pd.testing.assert_frame_equal(df, expected_df)

if __name__ == "__main__":
    unittest.main()