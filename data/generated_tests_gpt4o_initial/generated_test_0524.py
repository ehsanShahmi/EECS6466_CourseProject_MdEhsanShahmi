from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
import unittest

def task_func(data):
    """
    Calculate statistical measurements (mean and standard deviation) of the values associated with
    each key in a list of dictionaries, and visualize mean and standard deviation with bar charts.

    Parameters:
    data (list): The list of dictionaries. Must not be empty. Each dictionary must have numeric values.

    Returns:
    tuple:
        - dict: A dictionary with keys and their corresponding mean and standard deviation.
        - list: A list of matplotlib Axes objects for each key's visualization.

    Requirements:
    - numpy
    - matplotlib.pyplot
    - collections.defaultdict
    
    Raises:
    - ValueError: If the input data is empty.
    - TypeError: If the input is not a list of dictionaries or if any value in the dictionaries is not numeric.
    
    Example:
    >>> stats, axes = task_func([{'cat': 1, 'dog': 3}, {'cat' : 2, 'dog': 5}, {'cat' : 3, 'dog': 7}])
    >>> stats
    {'cat': {'mean': 2.0, 'std': 0.816496580927726}, 'dog': {'mean': 5.0, 'std': 1.632993161855452}}
    >>> axes
    [<Axes: title={'center': 'Statistics of cat'}, ylabel='Value'>, <Axes: title={'center': 'Statistics of dog'}, ylabel='Value'>]
    """
    
    if not data:
        raise ValueError("Input data is empty.")
    if not isinstance(data, list) or not all(isinstance(d, dict) for d in data):
        raise TypeError("Input must be a list of dictionaries.")
    for d in data:
        if not all(isinstance(value, (int, float)) for value in d.values()):
            raise TypeError("All values in the dictionaries must be numeric.")

    stats = defaultdict(list)
    for d in data:
        for key, value in d.items():
            stats[key].append(value)

    result = {k: {"mean": np.mean(v), "std": np.std(v)} for k, v in stats.items()}

    # Visualization
    axes = []
    for key in result:
        fig, ax = plt.subplots()
        ax.bar(x=["mean", "std"], height=result[key].values())
        ax.set_title(f"Statistics of {key}")
        ax.set_ylabel("Value")
        axes.append(ax)

    return result, axes

class TestTaskFunc(unittest.TestCase):

    def test_empty_input(self):
        """Test the function raises ValueError for empty input."""
        with self.assertRaises(ValueError):
            task_func([])

    def test_non_list_input(self):
        """Test the function raises TypeError for non-list input."""
        with self.assertRaises(TypeError):
            task_func("not a list")

    def test_non_dict_in_list(self):
        """Test the function raises TypeError for non-dictionary elements in list."""
        with self.assertRaises(TypeError):
            task_func([{'cat': 1}, "not a dict"])

    def test_non_numeric_values(self):
        """Test the function raises TypeError for non-numeric values in the dictionaries."""
        with self.assertRaises(TypeError):
            task_func([{'cat': 1, 'dog': 'not a number'}])

    def test_valid_input(self):
        """Test that the function calculates the mean and std correctly for valid input."""
        data = [{'cat': 1, 'dog': 3}, {'cat': 2, 'dog': 5}, {'cat': 3, 'dog': 7}]
        expected_stats = {
            'cat': {'mean': 2.0, 'std': 0.816496580927726},
            'dog': {'mean': 5.0, 'std': 1.632993161855452}
        }
        stats, axes = task_func(data)
        self.assertEqual(stats, expected_stats)
        self.assertEqual(len(axes), len(expected_stats))

if __name__ == '__main__':
    unittest.main()