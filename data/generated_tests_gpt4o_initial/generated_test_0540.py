import unittest
from matplotlib import pyplot as plt
from collections import Counter
import numpy as np
import itertools

# Here is your prompt:
def task_func(list_of_menuitems, title="Menu Distribution", color="blue", width=1.0):
    """
    Given a nested list of menu items, flatten the list using itertool chain, count the occurrences of each item, then
    plot a histogram with an alphabetically sorted x-axis labeled as "Menu Items" and y-axis as "Frequency".

    Parameters:
    - list_of_menuitems (list): A non-empty nested list of menu items. Each element is a list of menu item strings.
    - title (str, optional): The title of the histogram plot. Default is "Menu Distribution".
    - color (str, optional): The color of the bars in the histogram. Default is "blue".
    - width (float, optional): The width of the bars in the histogram. Default is 1.0.

    Returns:
    - ax (object): An Axes object representing the histogram plot.

    Requirements:
    - collections.Counter
    - numpy
    - matplotlib.pyplot
    - itertools

    Example:
    >>> task_func([['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']])
    <Axes: title={'center': 'Menu Distribution'}, xlabel='Menu Items', ylabel='Frequency'>
    >>> task_func(['Burger'], title='A Title', color='red', width=5.0)
    <Axes: title={'center': 'A Title'}, xlabel='Menu Items', ylabel='Frequency'>
    """

               # Flatten the list
    flat_list = list(itertools.chain(*list_of_menuitems))

    # Count the occurrences of each menu item
    counter = Counter(flat_list)
    labels, values = zip(*sorted(counter.items(), key=lambda x: x[0]))
    indexes = np.arange(len(labels))

    # Plot the histogram
    fig, ax = plt.subplots()
    ax.bar(indexes, values, width, color=color)
    ax.set_xticklabels(labels)
    ax.set_xlabel("Menu Items")
    ax.set_ylabel("Frequency")
    ax.set_title(title)

    return ax

class TestTaskFunc(unittest.TestCase):
    
    def test_basic_functionality(self):
        ax = task_func([['Pizza', 'Burger'], ['Pizza', 'Coke'], ['Pasta', 'Coke']])
        self.assertEqual(ax.get_title(), 'Menu Distribution')
        self.assertIn('Burger', [x.get_text() for x in ax.get_xticklabels()])

    def test_custom_title(self):
        ax = task_func([['Burger']], title='Food Items')
        self.assertEqual(ax.get_title(), 'Food Items')

    def test_custom_color(self):
        ax = task_func([['Pizza', 'Burger']], color='red')
        for bar in ax.patches:
            self.assertEqual(bar.get_facecolor()[0:3], (1.0, 0.0, 0.0))  # RGB for red

    def test_single_item(self):
        ax = task_func([['Burger']])
        self.assertEqual(len(ax.patches), 1)
        self.assertEqual(ax.patches[0].get_height(), 1)  # Frequency of the single item

    def test_empty_nested_list_raises_exception(self):
        with self.assertRaises(ValueError):
            task_func([])

if __name__ == '__main__':
    unittest.main()