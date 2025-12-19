import collections
import itertools
import matplotlib.pyplot as plt
import unittest

# Constants
ITEMS = ['apple', 'banana']

def task_func(a, b, items=ITEMS):
    """
    Combine two lists and record the frequency of predefined items in the combined list.

    Parameters:
    a (list): A list of items.
    b (list): Another list of items.
    items (list, optional): a list of predefined items

    Returns:
    matplotlib.axes.Axes: A bar chart showing the frequency of predefined items in the combined list.
    """
    combined = list(itertools.chain(a, b))
    counter = collections.Counter(combined)
    item_counts = [counter.get(item, 0) for item in items]

    fig, ax = plt.subplots()
    ax.bar(items, item_counts, color='skyblue')
    ax.set_xlabel('Items')
    ax.set_ylabel('Frequency')
    ax.set_title('Item Frequency in Combined List')
    plt.xticks(rotation=45)
    plt.tight_layout()

    return ax

class TestTaskFunc(unittest.TestCase):
    
    def test_empty_lists(self):
        """Test with both input lists being empty."""
        ax = task_func([], [])
        self.assertEqual(ax.patches[0].get_height(), 0)  # apple
        self.assertEqual(ax.patches[1].get_height(), 0)  # banana

    def test_no_predefined_items(self):
        """Test with input lists containing no predefined items."""
        ax = task_func(['cherry', 'date'], ['elderberry'])
        self.assertEqual(ax.patches[0].get_height(), 0)  # apple
        self.assertEqual(ax.patches[1].get_height(), 0)  # banana

    def test_some_predefined_items(self):
        """Test with some predefined items only in input lists."""
        ax = task_func(['apple', 'cherry'], ['banana', 'banana', 'apple'])
        self.assertEqual(ax.patches[0].get_height(), 2)  # apple
        self.assertEqual(ax.patches[1].get_height(), 2)  # banana

    def test_all_predefined_items(self):
        """Test with all predefined items in the input lists."""
        ax = task_func(['apple', 'banana'], ['banana', 'apple', 'banana'])
        self.assertEqual(ax.patches[0].get_height(), 2)  # apple
        self.assertEqual(ax.patches[1].get_height(), 3)  # banana

    def test_mixed_items(self):
        """Test with a mix of predefined and non-predefined items."""
        ax = task_func(['apple', 'orange', 'banana'], ['kiwi', 'pear', 'banana'])
        self.assertEqual(ax.patches[0].get_height(), 1)  # apple
        self.assertEqual(ax.patches[1].get_height(), 2)  # banana

if __name__ == '__main__':
    unittest.main()