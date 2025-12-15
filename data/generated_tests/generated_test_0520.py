import collections
import matplotlib.pyplot as plt
import unittest

def task_func(data):
    """
    Combine a list of dictionaries with the same keys (fruit names) into a single dictionary,
    calculate the total turnover for each fruit, and return a bar chart's axes with colors representing
    different fruits. The colors are selected from: 'red', 'yellow', 'green', 'blue', 'purple'. The function
    ensures that sales quantity must not be negative, throwing a ValueError if encountered.

    Parameters:
    data (list): A list of dictionaries. The keys are fruit names and the values are sales quantities.
                 Sales quantity must not be negative.

    Returns:
    total_sales (dict): A dictionary containing the total sales for each fruit.
    ax (matplotlib.container.BarContainer): A bar chart of total fruit sales, or None if data is empty

    Requirements:
    - collections
    - matplotlib.pyplot
    """

    if not data:
        return dict(), None

    all_keys = set().union(*data)
    for d in data:
        for k, v in d.items():
            if v < 0:
                raise ValueError("Sales quantity must not be negative.")

    combined_dict = dict((k, [d.get(k, 0) for d in data]) for k in all_keys)
    total_sales = {k: sum(v) for k, v in combined_dict.items()}
    total_sales = dict(collections.OrderedDict(sorted(total_sales.items())))
    labels, values = zip(*total_sales.items())

    # Define colors dynamically to handle different numbers of fruit types
    colors = ["red", "yellow", "green", "blue", "purple"] * (len(labels) // 5 + 1)

    ax = plt.bar(labels, values, color=colors[: len(labels)])
    plt.xlabel("Fruit")
    plt.ylabel("Total Sales")
    plt.title("Total Fruit Sales")

    return total_sales, ax

class TestTaskFunc(unittest.TestCase):

    def test_empty_data(self):
        sales, plot = task_func([])
        self.assertEqual(sales, {})
        self.assertIsNone(plot)

    def test_single_entry(self):
        sales, plot = task_func([{'apple': 10, 'banana': 20}])
        self.assertEqual(sales, {'apple': 10, 'banana': 20})
        self.assertIsNotNone(plot)

    def test_multiple_entries(self):
        sales, plot = task_func([
            {'apple': 10, 'banana': 15},
            {'apple': 5, 'banana': 10},
            {'apple': 8, 'banana': 5}
        ])
        self.assertEqual(sales, {'apple': 23, 'banana': 30})
        self.assertIsNotNone(plot)

    def test_negative_sales(self):
        with self.assertRaises(ValueError) as context:
            task_func([{'apple': 10, 'banana': -5}])
        self.assertEqual(str(context.exception), "Sales quantity must not be negative.")

    def test_ordered_totals(self):
        sales, plot = task_func([
            {'banana': 10, 'apple': 5},
            {'cherry': 7, 'banana': 15},
            {'banana': 5, 'cherry': 2, 'apple': 3}
        ])
        self.assertEqual(sales, {'apple': 8, 'banana': 30, 'cherry': 9})
        self.assertIsNotNone(plot)

if __name__ == '__main__':
    unittest.main()