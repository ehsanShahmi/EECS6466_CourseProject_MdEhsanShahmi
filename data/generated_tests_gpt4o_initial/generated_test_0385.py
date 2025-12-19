import unittest
from collections import Counter
import matplotlib.pyplot as plt

FRUITS = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit']

def task_func(fruit_dict):
    """
    Given a constant list of fruits in FRUITS, and a dictionary 'fruit_dict' with keys as people's names and values 
    as their favorite fruit names, record the frequency of each fruits' occurence. Return a bar chart of the number 
    of fruits for each fruit type and return the dictionary with fruit names as keys and their counts as values. 

    Parameters:
    fruit_dict (dict): The dictionary with keys as people's names and values as fruit names.

    Returns:
    dict: A dictionary with fruit names as keys and their counts as values.
    matplotlib.axes.Axes: The axes object of the plot.
    """
    fruit_list = [item for item in fruit_dict.values() if isinstance(item, str) and item in FRUITS]
    fruit_counter = Counter(fruit_list)
    
    plt.bar(fruit_counter.keys(), fruit_counter.values())
    return Counter([item for item in fruit_dict.values() if isinstance(item, str)]), plt.gca()

class TestTaskFunction(unittest.TestCase):
    
    def test_basic_fruit_counts(self):
        fruit_dict = {'John': 'Apple', 'Alice': 'Banana', 'Bob': 'Cherry', 'Charlie': 'Date', 'David': 'Apple'}
        expected_freq = {'Apple': 2, 'Banana': 1, 'Cherry': 1, 'Date': 1}
        freq, ax = task_func(fruit_dict)
        self.assertEqual(dict(freq), expected_freq)

    def test_multiple_people_same_fruit(self):
        fruit_dict = {'John': 'Apple', 'Alice': 'Apple', 'Bob': 'Apple'}
        expected_freq = {'Apple': 3}
        freq, ax = task_func(fruit_dict)
        self.assertEqual(dict(freq), expected_freq)

    def test_no_fruit(self):
        fruit_dict = {'John': 'Carrot', 'Alice': 'Potato', 'Bob': 'Iceberg'}
        expected_freq = {}
        freq, ax = task_func(fruit_dict)
        self.assertEqual(dict(freq), expected_freq)

    def test_fruit_with_non_string_keys(self):
        fruit_dict = {1: 'Apple', 2: 'Banana', 3: 'Cherry'}
        expected_freq = {'Apple': 1, 'Banana': 1, 'Cherry': 1}
        freq, ax = task_func(fruit_dict)
        self.assertEqual(dict(freq), expected_freq)

    def test_ignore_invalid_fruits(self):
        fruit_dict = {'John': 'Apple', 'Alice': 'Banana', 'Bob': 'Mango', 'Charlie': 'Date'}
        expected_freq = {'Apple': 1, 'Banana': 1, 'Date': 1}
        freq, ax = task_func(fruit_dict)
        self.assertEqual(dict(freq), expected_freq)

if __name__ == '__main__':
    unittest.main()