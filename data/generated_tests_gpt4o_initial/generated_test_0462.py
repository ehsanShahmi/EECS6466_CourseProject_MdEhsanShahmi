import pandas as pd
import random
import unittest
import matplotlib.pyplot as plt

def task_func(num_rows=100, categories=["a", "b", "c", "d", "e"], random_seed=42):
    """
    Create a Pandas DataFrame with specified number of rows. Each row contains a randomly
    selected category from the provided categories list and a random integer between 1 and 100.

    The function also generates a bar chart visualizing the counts of each category in the DataFrame
    and returns both the DataFrame and the bar chart.

    Parameters:
    - num_rows (int): Number of rows in the DataFrame. Default is 100. Must be at least 1.
    - categories (list): List of categories to choose from. Default is ['a', 'b', 'c', 'd', 'e'].
    - random_seed (int): Seed for random number generation to ensure reproducibility. Default is 42.

    Returns:
    - pd.DataFrame: A pandas DataFrame with randomly generated category data.
    - matplotlib.pyplot.Axes: A bar chart visualizing the category counts, with the title 'Category Counts'.

    Raises:
    - ValueError: If num_rows is less than 1.
    """
    if num_rows <= 0:
        raise ValueError("num_rows must not be negative")

    random.seed(random_seed)

    df = pd.DataFrame(
        {
            "Category": [
                categories[random.randint(0, len(categories) - 1)]
                for _ in range(num_rows)
            ],
            "Value": [random.randint(1, 100) for _ in range(num_rows)],
        }
    )

    ax = (
        df["Category"]
        .value_counts()
        .plot(kind="bar", title="Category Counts", figsize=(10, 6))
    )

    return df, ax

class TestTaskFunction(unittest.TestCase):

    def test_default_parameters(self):
        df, ax = task_func()
        self.assertEqual(df.shape[0], 100)
        self.assertEqual(df.shape[1], 2)
        self.assertTrue(set(df['Category']).issubset({'a', 'b', 'c', 'd', 'e'}))
        self.assertTrue((df['Value'] >= 1).all() and (df['Value'] <= 100).all())

    def test_custom_row_count(self):
        df, ax = task_func(num_rows=10)
        self.assertEqual(df.shape[0], 10)

    def test_invalid_row_count(self):
        with self.assertRaises(ValueError):
            task_func(num_rows=0)
        with self.assertRaises(ValueError):
            task_func(num_rows=-5)

    def test_categories_selection(self):
        df, ax = task_func(categories=["x", "y", "z"])
        self.assertTrue(set(df['Category']).issubset({'x', 'y', 'z'}))

    def test_random_seed_reproducibility(self):
        df1, ax1 = task_func(random_seed=1)
        df2, ax2 = task_func(random_seed=1)
        pd.testing.assert_frame_equal(df1, df2)

if __name__ == '__main__':
    unittest.main()