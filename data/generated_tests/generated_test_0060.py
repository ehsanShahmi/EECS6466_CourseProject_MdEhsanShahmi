import unittest
import os
import json
import pandas as pd

# Here is your prompt:
def task_func(result, csv_file_path="test.csv", json_file_path="test.json"):
    """
    Save the list of dictionaries provided in the 'result' parameter to a CSV file (without index) and a JSON file.

    Parameters:
    - result (list): A list of dictionaries.
    - csv_file_path (str): A path to a CSV file.
    - json_file_path (str): A path to a JSON file.

    Returns:
    None

    Requirements:
    - pandas
    - json

    Example:
    >>> result = [{"hi": 7, "bye": 4, "from_user": 0}, {1: 2, 3: 4, 5: 6}]
    >>> task_func(result, 'test.csv', 'test.json')
    """

    # Save to CSV
    df = pd.DataFrame(result)
    df.to_csv(csv_file_path, index=False)

    # Save to JSON
    with open(json_file_path, 'w') as f:
        json.dump(result, f, indent=4)

    return None


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.test_csv = 'test.csv'
        self.test_json = 'test.json'
        self.result_data = [{"hi": 7, "bye": 4, "from_user": 0}, {"hi": 1, "bye": 2}]
    
    def tearDown(self):
        try:
            os.remove(self.test_csv)
            os.remove(self.test_json)
        except FileNotFoundError:
            pass

    def test_csv_creation(self):
        task_func(self.result_data, self.test_csv, self.test_json)
        self.assertTrue(os.path.isfile(self.test_csv), "CSV file was not created.")

    def test_json_creation(self):
        task_func(self.result_data, self.test_csv, self.test_json)
        self.assertTrue(os.path.isfile(self.test_json), "JSON file was not created.")

    def test_csv_content(self):
        task_func(self.result_data, self.test_csv, self.test_json)
        df = pd.read_csv(self.test_csv)
        expected_df = pd.DataFrame(self.result_data)
        pd.testing.assert_frame_equal(df, expected_df, check_dtype=True)

    def test_json_content(self):
        task_func(self.result_data, self.test_csv, self.test_json)
        with open(self.test_json, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, self.result_data, "JSON content does not match expected result.")

    def test_empty_result(self):
        task_func([], self.test_csv, self.test_json)
        df = pd.read_csv(self.test_csv)
        self.assertTrue(df.empty, "CSV file is not empty for an empty input list.")
        with open(self.test_json, 'r') as f:
            data = json.load(f)
        self.assertEqual(data, [], "JSON content is not empty for an empty input list.")


if __name__ == '__main__':
    unittest.main()