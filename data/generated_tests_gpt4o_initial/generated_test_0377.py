import unittest
from texttable import Texttable
import os
import psutil

def task_func():
    """
    Generates a table displaying the system's CPU usage, memory usage, and disk usage.

    Returns:
        A string representation of a table with the columns of 'Item' and 'Value',
        and the following system information:
        - CPU Usage (%)
        - Memory Usage (%)
        - Disk Usage (%)

    Requirements:
    - texttable.Texttable
    - os
    - psutil

    Examples:
    >>> table_str = task_func()
    >>> isinstance(table_str, str)
    True
    >>> 'CPU Usage (%)' in table_str and 'Memory Usage (%)' in table_str
    True
    """

    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage(os.sep)

    table = Texttable()
    table.add_rows([
        ['Item', 'Value'],
        ['CPU Usage (%)', cpu_usage],
        ['Memory Usage (%)', memory_info.percent],
        ['Disk Usage (%)', disk_usage.percent]
    ])
    return table.draw()

class TestTaskFunc(unittest.TestCase):

    def test_return_type(self):
        result = task_func()
        self.assertIsInstance(result, str, "The return type should be a string.")

    def test_table_structure(self):
        result = task_func()
        self.assertIn('Item', result, "The table should contain a header 'Item'.")
        self.assertIn('Value', result, "The table should contain a header 'Value'.")

    def test_cpu_usage_exists(self):
        result = task_func()
        self.assertIn('CPU Usage (%)', result, "The table should include 'CPU Usage (%)'.")

    def test_memory_usage_exists(self):
        result = task_func()
        self.assertIn('Memory Usage (%)', result, "The table should include 'Memory Usage (%)'.")

    def test_disk_usage_exists(self):
        result = task_func()
        self.assertIn('Disk Usage (%)', result, "The table should include 'Disk Usage (%)'.")

if __name__ == '__main__':
    unittest.main()