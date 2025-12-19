import unittest
import pandas as pd
import base64

def task_func(df):
    """
    Encodes a dict of list as a Base64 string. The dict is first converted to a Pandas DataFrame.
    Then convert the data frame to CSV format and encoded to bytes, finally encoded it to a Base64 string.

    Parameters:
        df (dict of list): A dictionary where the key 'Word' maps to a list of strings.

    Returns:
        str: The Base64 encoded string of the DataFrame's CSV representation.
    """
    df = pd.DataFrame(df)
    csv = df.to_csv(index=False)
    csv_bytes = csv.encode('utf-8')
    base64_bytes = base64.b64encode(csv_bytes)
    base64_string = base64_bytes.decode('utf-8')

    return base64_string

class TestTaskFunc(unittest.TestCase):

    def test_basic_functionality(self):
        df = {'A': [1, 2], 'B': [3, 4]}
        result = task_func(df)
        expected_csv = "A,B\n1,3\n2,4\n"
        expected_encoded = base64.b64encode(expected_csv.encode('utf-8')).decode('utf-8')
        self.assertEqual(result, expected_encoded)

    def test_empty_dataframe(self):
        df = {'A': [], 'B': []}
        result = task_func(df)
        expected_csv = "A,B\n"
        expected_encoded = base64.b64encode(expected_csv.encode('utf-8')).decode('utf-8')
        self.assertEqual(result, expected_encoded)

    def test_single_row_dataframe(self):
        df = {'A': [1], 'B': [2]}
        result = task_func(df)
        expected_csv = "A,B\n1,2\n"
        expected_encoded = base64.b64encode(expected_csv.encode('utf-8')).decode('utf-8')
        self.assertEqual(result, expected_encoded)

    def test_unicode_characters(self):
        df = {'A': ['apple', 'orange'], 'B': ['banana', 'grape']}
        result = task_func(df)
        expected_csv = "A,B\napple,banana\norange,grape\n"
        expected_encoded = base64.b64encode(expected_csv.encode('utf-8')).decode('utf-8')
        self.assertEqual(result, expected_encoded)

    def test_large_dataframe(self):
        df = {'A': list(range(1000)), 'B': list(range(1000, 2000))}
        result = task_func(df)
        expected_csv = ','.join(['A,B'] + [f"{i},{i + 1000}" for i in range(1000)]) + "\n"
        expected_encoded = base64.b64encode(expected_csv.encode('utf-8')).decode('utf-8')
        self.assertEqual(result, expected_encoded)

if __name__ == '__main__':
    unittest.main()