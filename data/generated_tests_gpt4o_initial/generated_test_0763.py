import unittest
import json
import os
import numpy as np
from collections import defaultdict
import csv

# Constants
def task_func(input_file, output_file):
    """
    Read a list of dictionaries from a JSON file, calculate the mean and median for each key, and write the results to a CSV file.
    
    Parameters:
    - input_file (str): The input JSON file name.
    - output_file (str): The output CSV file name.

    Returns:
    - dict: A dictionary where each key is a field from the input JSON and each value is another dictionary with the mean and median of that field.

    Requirements:
    - numpy
    - collections
    - json
    - csv

    Example:
    >>> task_func('data.json', 'stats.csv')
    """
    with open(input_file, 'r') as f:
        data = json.load(f)
    
    stats = defaultdict(list)
    for d in data:
        for key, value in d.items():
            stats[key].append(value)
    
    result = {k: {'mean': np.mean(v), 'median': np.median(v)} for k, v in stats.items()}

    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['key', 'mean', 'median'])
        writer.writeheader()
        for key, values in result.items():
            writer.writerow({'key': key, 'mean': values['mean'], 'median': values['median']})
    
    return result


class TestTaskFunc(unittest.TestCase):
    def setUp(self):
        # Create a temporary input JSON file
        self.input_file = 'test_data.json'
        self.output_file = 'output_stats.csv'
        data = [
            {"a": 1, "b": 2},
            {"a": 3, "b": 4},
            {"a": 5, "b": 6}
        ]
        with open(self.input_file, 'w') as f:
            json.dump(data, f)

    def tearDown(self):
        # Remove the temporary input and output files
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_mean_and_median_computation(self):
        result = task_func(self.input_file, self.output_file)
        expected_result = {
            'a': {'mean': 3.0, 'median': 3.0},
            'b': {'mean': 4.0, 'median': 4.0}
        }
        self.assertEqual(result, expected_result)

    def test_output_csv_format(self):
        task_func(self.input_file, self.output_file)
        with open(self.output_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

        self.assertEqual(len(rows), 2)  # There should be 2 keys
        self.assertIn('a', [row['key'] for row in rows])
        self.assertIn('b', [row['key'] for row in rows])

    def test_invalid_input_json(self):
        with open(self.input_file, 'w') as f:
            f.write('invalid json')
        
        with self.assertRaises(json.JSONDecodeError):
            task_func(self.input_file, self.output_file)

    def test_empty_json_file(self):
        with open(self.input_file, 'w') as f:
            json.dump([] , f)
        
        result = task_func(self.input_file, self.output_file)
        self.assertEqual(result, {})  # No data should return an empty dict

if __name__ == '__main__':
    unittest.main()