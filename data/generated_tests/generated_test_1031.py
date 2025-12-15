import random
import string
import pandas as pd
import unittest

def task_func(n_rows=1000):
    """
    Generate a histogram of the frequency of the top 30 unique random 3-letter strings.
    The function creates random strings, each consisting of 3 letters from the lowercase English alphabet.
    It then plots a histogram showing the frequencies of the top 30 most common strings among the generated set.

    Parameters:
    - n_rows (int): Number of random 3-letter strings to generate.
    Must be positive. Default is 1000.

    Returns:
    - ax (matplotlib.axes.Axes): A Matplotlib Axes object containing the histogram.
    Each bar represents one of the top 30 most frequent 3-letter strings.

    Raises:
    - ValueError: If `n_rows` is less than or equal to 0.

    Requirements:
    - random
    - string
    - pandas
    
    Example:
    >>> ax = task_func(1000)
    >>> ax.get_title()
    'Top 30 Frequencies of Random 3-Letter Strings'
    """

    # Check if n_rows is positive
    if n_rows <= 0:
        raise ValueError("Number of rows must be greater than 0")

    # Generate random strings
    data = ["".join(random.choices(string.ascii_lowercase, k=3)) for _ in range(n_rows)]
    df = pd.DataFrame(data, columns=["String"])

    # Aggregate and plot the data
    frequency = df["String"].value_counts()
    ax = frequency.head(30).plot(
        kind="bar"
    )  # Limit to the top 30 frequencies for readability
    ax.set_title("Top 30 Frequencies of Random 3-Letter Strings")
    ax.set_xlabel("String")
    ax.set_ylabel("Frequency")

    return ax

class TestTaskFunc(unittest.TestCase):

    def test_default_n_rows(self):
        """Test if the function runs correctly with the default number of rows (1000)."""
        ax = task_func()
        self.assertEqual(ax.get_title(), 'Top 30 Frequencies of Random 3-Letter Strings')

    def test_positive_n_rows(self):
        """Test if the function handles a positive integer as input correctly."""
        ax = task_func(1500)
        self.assertEqual(ax.get_title(), 'Top 30 Frequencies of Random 3-Letter Strings')

    def test_zero_n_rows(self):
        """Test if the function raises ValueError when passed zero as n_rows."""
        with self.assertRaises(ValueError) as context:
            task_func(0)
        self.assertEqual(str(context.exception), "Number of rows must be greater than 0")

    def test_negative_n_rows(self):
        """Test if the function raises ValueError for negative n_rows."""
        with self.assertRaises(ValueError) as context:
            task_func(-100)
        self.assertEqual(str(context.exception), "Number of rows must be greater than 0")

    def test_histogram_length(self):
        """Test that the histogram has at most 30 bars for top frequencies."""
        ax = task_func(1000)
        self.assertLessEqual(len(ax.patches), 30)

if __name__ == '__main__':
    unittest.main()