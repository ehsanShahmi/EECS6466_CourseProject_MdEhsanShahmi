import unittest
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import statistics

# Here is your prompt:
def task_func(sales_data):
    """
    Plot sales trends for five products over a year, highlighting variability with standard deviation shading
    with 'Month' on x-axis and 'Sales' on y-axis.

    Parameters:
    - sales_data (pd.DataFrame): DataFrame with sales data, expected columns: 'Month', 'Product A' to 'Product E'.

    Returns:
    - ax (matplotlib.axes.Axes): Axes object with the sales trends plot.

    Requirements:
    - matplotlib.pyplot
    - statistics

    Example:
    >>> import pandas as pd, numpy as np
    >>> sales_data = pd.DataFrame({
    ...     'Month': range(1, 13),
    ...     'Product A': np.random.randint(100, 200, size=12),
    ...     'Product B': np.random.randint(150, 250, size=12),
    ...     'Product C': np.random.randint(120, 220, size=12),
    ...     'Product D': np.random.randint(130, 230, size=12),
    ...     'Product E': np.random.randint(140, 240, size=12)
    ... })
    >>> ax = task_func(sales_data)
    >>> plt.show()  # Displays the plot
    """

    fig, ax = plt.subplots()
    for label in sales_data.columns[1:]:  # Skipping 'Month' column
        monthly_sales = sales_data[label]
        std_dev = statistics.stdev(monthly_sales)

        ax.plot(sales_data['Month'], monthly_sales, label=label)
        ax.fill_between(sales_data['Month'],
                        monthly_sales - std_dev,
                        monthly_sales + std_dev,
                        alpha=0.2)

    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.set_title('Monthly Sales Trends with Standard Deviation')
    ax.legend()

    # Set x-ticks to be explicit months from the DataFrame
    ax.set_xticks(sales_data['Month'])

    return ax

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        # Setting up a basic DataFrame to be used in tests
        self.sales_data = pd.DataFrame({
            'Month': list(range(1, 13)),
            'Product A': np.random.randint(100, 200, size=12),
            'Product B': np.random.randint(150, 250, size=12),
            'Product C': np.random.randint(120, 220, size=12),
            'Product D': np.random.randint(130, 230, size=12),
            'Product E': np.random.randint(140, 240, size=12)
        })

    def test_output_type(self):
        ax = task_func(self.sales_data)
        self.assertIsInstance(ax, plt.Axes)

    def test_plot_has_correct_title(self):
        ax = task_func(self.sales_data)
        self.assertEqual(ax.get_title(), 'Monthly Sales Trends with Standard Deviation')

    def test_x_axis_label(self):
        ax = task_func(self.sales_data)
        self.assertEqual(ax.get_xlabel(), 'Month')

    def test_y_axis_label(self):
        ax = task_func(self.sales_data)
        self.assertEqual(ax.get_ylabel(), 'Sales')

    def test_legend_contains_product_labels(self):
        ax = task_func(self.sales_data)
        legend_labels = [text.get_text() for text in ax.get_legend().get_texts()]
        expected_labels = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
        for label in expected_labels:
            self.assertIn(label, legend_labels)

if __name__ == '__main__':
    unittest.main()