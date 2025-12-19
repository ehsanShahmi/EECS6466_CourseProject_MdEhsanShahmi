import json
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
import unittest

def task_func(input_file):
    """
    Reads a JSON file containing a list of dictionaries. For each key across all dictionaries,
    calculates the mean and median of its values using numpy. Visualizes the mean and median
    using bar charts. Returns the results and plots.

    Parameters:
        - input_file (str): Path to the input JSON file containing a list of dictionaries.

    Returns:
        - result (dict): each key corresponds to those in the input dictionaries, and the corresponding
          value is another dict with keys 'mean' and 'median', representing the calculated statistics.
        - plots  (list[matplotlib.axes._axes.Axes]): A list of bar charts, one for
          each key in the dictionaries, visualizing the mean and median values.

    Requirements:
        - json
        - numpy
        - collections.defaultdict
        - matplotlib.pyplot

    Example:
    >>> results, plots = task_func("sample_data.json")
    >>> type(plots[0])
    <class 'matplotlib.axes._axes.Axes'>
    >>> results
    {'a': {'mean': 3.0, 'median': 3.0}, 'b': {'mean': 6.0, 'median': 6.0}}
    """

    with open(input_file, "r") as f:
        data = json.load(f)

    stats = defaultdict(list)
    for d in data:
        for key, value in d.items():
            stats[key].append(value)

    result = {k: {"mean": np.mean(v), "median": np.median(v)} for k, v in stats.items()}

    plots = []
    for key, values in result.items():
        _, ax = plt.subplots()
        ax.bar(["mean", "median"], [values["mean"], values["median"]])
        ax.set_title(f"Statistics of {key}")
        plots.append(ax)
    return result, plots

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Create a temporary JSON file for testing
        self.test_file = 'test_data.json'
        with open(self.test_file, 'w') as f:
            json.dump([
                {"a": 1, "b": 2},
                {"a": 3, "b": 4},
                {"a": 5, "b": 6}
            ], f)

    def test_mean_and_median(self):
        results, plots = task_func(self.test_file)
        self.assertEqual(results['a']['mean'], 3.0)
        self.assertEqual(results['a']['median'], 3.0)
        self.assertEqual(results['b']['mean'], 4.0)
        self.assertEqual(results['b']['median'], 4.0)

    def test_plot_type(self):
        results, plots = task_func(self.test_file)
        self.assertIsInstance(plots[0], plt.Axes)
        self.assertIsInstance(plots[1], plt.Axes)

    def test_empty_input(self):
        empty_test_file = 'empty_test_data.json'
        with open(empty_test_file, 'w') as f:
            json.dump([], f)
        
        results, plots = task_func(empty_test_file)
        self.assertEqual(results, {})
        self.assertEqual(plots, [])

    def test_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            task_func("nonexistent_file.json")

    def tearDown(self):
        import os
        try:
            os.remove(self.test_file)
        except Exception:
            pass
        try:
            os.remove('empty_test_data.json')
        except Exception:
            pass

if __name__ == '__main__':
    unittest.main()