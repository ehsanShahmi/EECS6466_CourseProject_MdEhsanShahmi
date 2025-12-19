import random
from datetime import datetime
import matplotlib.pyplot as plt
import unittest

# Here is your prompt:
def task_func(epoch_milliseconds, seed=None):
    """
    Generate and draw a sales trend for different categories from a particular epoch milliseconds
    to the current UTC time.

    The function selects category from ['Electronics', 'Clothing', 'Home', 'Books', 'Sports'].
    Each day's sales are randomly determined between 10 and 50 units for each category.
    The plot's x-axis represents 'Days since (the start date)', and the y-axis represents 'Sales' units.

    Parameters:
    - epoch_milliseconds (int): Start time. Must be positive and before current time.
    - seed (int, optional): Seed for random number generation. Default is None (no seed).

    Returns:
    - sales_data (dict): Sales data for different categories over days.
    - ax (plt.Axes): The plot depicting the sales trend.

    Raises:
    - ValueError: If the start time is negative or after the current time.
    
    Requirements:
    - random
    - datetime.datetime
    - matplotlib

    Example:
    >>> random.seed(42)
    >>> sales_data, ax = task_func(1236472051807, seed=42)
    >>> type(sales_data)
    <class 'dict'>
    >>> list(sales_data['Electronics'])[:3]
    [50, 24, 47]
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    """

    CATEGORIES = ["Electronics", "Clothing", "Home", "Books", "Sports"]

    if seed is not None:
        random.seed(seed)

    if epoch_milliseconds < 0:
        raise ValueError("Start time cannot be negative.")

    start_time = datetime.utcfromtimestamp(epoch_milliseconds / 1000.0)
    current_time = datetime.utcnow()
    days_diff = (current_time - start_time).days
    if days_diff <= 0:
        raise ValueError("Start date must be before current time.")

    sales_data = {category: [0] * days_diff for category in CATEGORIES}

    for i in range(days_diff):
        for category in CATEGORIES:
            sales = random.randint(10, 50)
            sales_data[category][i] += sales

    fig, ax = plt.subplots()
    for category, sales in sales_data.items():
        ax.plot(range(days_diff), sales, label=category)

    ax.set_xlabel("Days since " + start_time.strftime("%Y-%m-%d %H:%M:%S"))
    ax.set_ylabel("Sales")
    ax.legend()

    return sales_data, ax


class TestTaskFunc(unittest.TestCase):

    def test_negative_epoch(self):
        with self.assertRaises(ValueError) as context:
            task_func(-1236472051807)
        self.assertEqual(str(context.exception), "Start time cannot be negative.")

    def test_future_epoch(self):
        future_epoch = int(datetime.utcnow().timestamp() * 1000) + 100000
        with self.assertRaises(ValueError) as context:
            task_func(future_epoch)
        self.assertEqual(str(context.exception), "Start date must be before current time.")

    def test_valid_epoch(self):
        epoch = int(datetime.utcnow().timestamp() * 1000) - 10000000  # 10 days ago
        sales_data, ax = task_func(epoch)
        self.assertIsInstance(sales_data, dict)
        self.assertIn("Electronics", sales_data)
        self.assertEqual(len(sales_data["Electronics"]), 10)  # Check if data length matches days_diff

    def test_sales_range(self):
        epoch = int(datetime.utcnow().timestamp() * 1000) - 10000000  # 10 days ago
        sales_data, _ = task_func(epoch)
        for sales in sales_data.values():
            for sale in sales:
                self.assertGreaterEqual(sale, 10)  # Sales should be at least 10
                self.assertLessEqual(sale, 50)     # Sales should be at most 50

    def test_plot_generated(self):
        epoch = int(datetime.utcnow().timestamp() * 1000) - 10000000  # 10 days ago
        sales_data, ax = task_func(epoch)
        self.assertIsInstance(ax, plt.Axes)  # Ensure an Axes object is returned
        self.assertIsNotNone(ax.get_lines())  # Ensure the plot has lines (sales data)

if __name__ == '__main__':
    unittest.main()