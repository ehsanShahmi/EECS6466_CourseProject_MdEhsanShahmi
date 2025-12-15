import unittest
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.container import BarContainer

# Here is your prompt:
import numpy as np
import random
import matplotlib.pyplot as plt

# Constants
LETTERS = list("abcdefghijklmnopqrstuvwxyz")
NUMBERS = list(range(1, 27))


def task_func(n_pairs=26):
    """
    This function generates and displays a bar chart representing random letter-number pairs.
    Each bar corresponds to a unique pair, formed by combining a letter from 'a' to 'z' with a number
    from 1 to 26. The function randomly shuffles these pairs and assigns a random count to each.

    Parameters:
    - n_pairs (int, optional): The number of letter-number pairs to display in the bar chart.
      The value must be an integer between 1 and 26, inclusive. The default value is 26, which
      includes one pair for each letter in the alphabet.

    Returns:
    - matplotlib.container.BarContainer: This object represents the bar chart created by the function.
      Each bar in the chart is labeled with its corresponding letter-number pair (e.g., 'a:1', 'b:2').
      The title of the chart is "Random Letter:Number Pairs Chart", the x-axis label is "Letter:Number Pairs",
      and the y-axis label is "Counts".

    Raises:
    - ValueError: If 'n_pairs' is outside the range of 1 to 26, inclusive. This ensures that the function
      operates within the bounds of the predefined letters ('a' to 'z') and numbers (1 to 26).

    Requirements:
    - numpy
    - matplotlib
    - random

    Notes:
    - Each call to this function will likely produce a different chart because it shuffles the order
      of the pairs and assigns random counts to them.
    - The random counts assigned to each pair range from 1 to 9.

    Example:
    >>> ax = task_func(5)
    >>> [bar.get_label() for bar in ax]
    ['d:4', 'b:2', 'c:3', 'e:5', 'a:1']
    """

    if n_pairs > 26 or n_pairs < 1:
        raise ValueError("n_pairs should be between 1 and 26")

    pairs = [f"{letter}:{number}" for letter, number in zip(LETTERS, NUMBERS)][:n_pairs]
    random.seed(42)
    random.shuffle(pairs)
    counts = np.random.randint(1, 10, size=n_pairs)

    bars = plt.bar(pairs, counts)

    # Set label for each bar
    for bar, pair in zip(bars, pairs):
        bar.set_label(pair)

    plt.xlabel("Letter:Number Pairs")
    plt.ylabel("Counts")
    plt.title("Random Letter:Number Pairs Chart")

    return bars


class TestTaskFunc(unittest.TestCase):
    def test_return_type(self):
        """Test that the function returns a BarContainer."""
        result = task_func(10)
        self.assertIsInstance(result, BarContainer)

    def test_correct_number_of_pairs(self):
        """Test that the function generates the correct number of letter-number pairs."""
        n_pairs = 5
        result = task_func(n_pairs)
        self.assertEqual(len(result), n_pairs)

    def test_labels_format(self):
        """Test that the labels of the bars are in the correct format."""
        n_pairs = 3
        result = task_func(n_pairs)
        expected_labels = [f"{LETTERS[i]}:{NUMBERS[i]}" for i in range(n_pairs)]
        actual_labels = [bar.get_label() for bar in result]
        self.assertEqual(set(expected_labels), set(actual_labels))

    def test_value_error_high_n_pairs(self):
        """Test that ValueError is raised when n_pairs is greater than 26."""
        with self.assertRaises(ValueError):
            task_func(27)

    def test_value_error_low_n_pairs(self):
        """Test that ValueError is raised when n_pairs is less than 1."""
        with self.assertRaises(ValueError):
            task_func(0)


if __name__ == '__main__':
    unittest.main()