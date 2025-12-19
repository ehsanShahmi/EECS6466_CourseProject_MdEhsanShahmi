import unittest
import tempfile
import os
import json
import numpy as np

# Provided prompt
def task_func(data_list, json_file_name="mean_values.json"):
    """
    Calculate the mean of the numeric values for each position in the provided data list 
    and return the results. Optionally, the results can be exported to a specified JSON file.
    
    Parameters:
    - data_list (list of tuples): List of data tuples where each tuple contains a string followed by numeric values.
    - json_file_name (str, optional): Name of the JSON file to export the results. Defaults to 'mean_values.json'.

    Returns:
    - dict: A dictionary with keys in the format 'Position {i}' and values being the mean of the numeric values 
            at position i in the provided data list.
    """
    unzipped_data = list(itertools.zip_longest(*data_list, fillvalue=np.nan))
    mean_values = [np.nanmean(column) for column in unzipped_data[1:]]

    results = {'Position {}'.format(i+1): mean_value for i, mean_value in enumerate(mean_values)}
    
    with open(json_file_name, 'w') as f:
        json.dump(results, f)

    return results

class TestTaskFunc(unittest.TestCase):
    
    def test_basic_case(self):
        result = task_func([('a', 1, 2), ('b', 2, 3), ('c', 3, 4)])
        expected = {'Position 1': 2.0, 'Position 2': 3.0}
        self.assertEqual(result, expected)

    def test_empty_data_list(self):
        result = task_func([])
        expected = {}
        self.assertEqual(result, expected)

    def test_mixed_numeric_values(self):
        result = task_func([('a', np.nan, 2), ('b', 3, 4), ('c', 5, np.nan)])
        expected = {'Position 1': 4.0, 'Position 2': 3.0}
        self.assertEqual(result, expected)

    def test_export_to_json(self):
        json_file = tempfile.NamedTemporaryFile(delete=False)
        try:
            task_func([('a', 1, 2), ('b', 2, 3)], json_file.name)
            with open(json_file.name, 'r') as f:
                data = json.load(f)
                expected = {'Position 1': 1.5, 'Position 2': 2.5}
                self.assertEqual(data, expected)
        finally:
            os.remove(json_file.name)
    
    def test_various_tuples(self):
        result = task_func([('x', 10, 20), ('y', 30, 40), ('z', 50, 60), ('w', 70, np.nan)])
        expected = {'Position 1': 40.0, 'Position 2': 40.0}
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()