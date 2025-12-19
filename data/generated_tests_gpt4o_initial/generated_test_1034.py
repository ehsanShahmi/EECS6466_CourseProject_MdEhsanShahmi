import pandas as pd
import numpy as np
import unittest
from matplotlib import pyplot as plt

CATEGORIES = ["Electronics", "Clothing", "Home Decor", "Automotive", "Books"]

def task_func(s1, s2):
    """
    Compares and visualizes the sales data of two stores for predefined categories.
    The function generates a bar plot for categories where both stores have sales exceeding a specified threshold.
    The Euclidean distance between the two series is also computed.
    
    Parameters:
    s1 (pd.Series): Sales data for store 1, indexed by categories.
    s2 (pd.Series): Sales data for store 2, indexed by categories.

    Returns:
    matplotlib.axes.Axes or None: A bar plot for categories where both stores' sales exceed the threshold of 200,
    or None if no such categories exist.
    float: The Euclidean distance between the two series or 0.0 if no categories meet the threshold.
    """
    high_sales_categories = s1.index[(s1 > 200) & (s2 > 200)]

    if high_sales_categories.empty:
        return None, 0.0

    df = pd.DataFrame(
        {"Store 1": s1[high_sales_categories], "Store 2": s2[high_sales_categories]}
    )

    edit_distance = np.linalg.norm(df["Store 1"] - df["Store 2"])
    
    ax = df.plot(kind="bar", title="Sales Comparison Above Threshold in Categories")
    return ax, edit_distance

class TestTaskFunc(unittest.TestCase):

    def test_sales_above_threshold(self):
        np.random.seed(seed=32)
        s1 = pd.Series([250, 300, 150, 400, 500], index=CATEGORIES)
        s2 = pd.Series([300, 250, 400, 220, 600], index=CATEGORIES)
        ax, edit_distance = task_func(s1, s2)
        self.assertIsNotNone(ax)
        self.assertGreater(edit_distance, 0)

    def test_no_sales_above_threshold(self):
        s1 = pd.Series([100, 150, 140, 180, 190], index=CATEGORIES)
        s2 = pd.Series([150, 180, 120, 160, 170], index=CATEGORIES)
        ax, edit_distance = task_func(s1, s2)
        self.assertIsNone(ax)
        self.assertEqual(edit_distance, 0.0)

    def test_sales_equal_threshold(self):
        s1 = pd.Series([200, 250, 300, 200, 400], index=CATEGORIES)
        s2 = pd.Series([200, 150, 250, 300, 100], index=CATEGORIES)
        ax, edit_distance = task_func(s1, s2)
        self.assertIsNotNone(ax)
        self.assertGreater(edit_distance, 0)
    
    def test_large_sales(self):
        s1 = pd.Series([1000, 1200, 500, 800, 1100], index=CATEGORIES)
        s2 = pd.Series([900, 1300, 700, 2000, 1300], index=CATEGORIES)
        ax, edit_distance = task_func(s1, s2)
        self.assertIsNotNone(ax)
        self.assertGreater(edit_distance, 0)

    def test_varying_sales(self):
        s1 = pd.Series([50, 250, 300, 600, 50], index=CATEGORIES)
        s2 = pd.Series([100, 260, 310, 20, 280], index=CATEGORIES)
        ax, edit_distance = task_func(s1, s2)
        self.assertIsNotNone(ax)
        self.assertGreater(edit_distance, 0)

if __name__ == '__main__':
    unittest.main()