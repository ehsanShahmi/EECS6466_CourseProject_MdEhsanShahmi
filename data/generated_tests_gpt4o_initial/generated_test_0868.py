import unittest
from itertools import cycle
from random import choice, seed


def task_func(n_colors, colors=['Red', 'Green', 'Blue', 'Yellow', 'Purple'], rng_seed=None):
    """
    Generates a list representing a color pattern. The pattern consists of 'n_colors' elements 
    and alternates between a cyclic sequence of colors as defined in the parameter 'colors',
    and random colors from the same list.
    Optionally, a seed for the random number generator can be provided for repeatable randomness.

    If n_colors is smaller than or equal to zero an empty list is returned.

    Parameters:
    n_colors (int): The number of colors to include in the pattern. This number indicates the total 
                    elements in the returned list, alternating between cyclic and random colors.
    colors (list of str, optional): The list of colors to generate from. 
                Defaults to  ['Red', 'Green', 'Blue', 'Yellow', 'Purple'].
    rng_seed (int, optional): A seed for the random number generator to ensure repeatability of the color selection. 
                              If 'None', the randomness is based on system time or other sources of entropy.

    Returns:
    list: A list representing the color pattern. Each element of the list is a string indicating 
          the color. For example, with n_colors=4 and a specific seed, the result could be consistent 
          across calls with the same seed.

    Requirements:
    - itertools
    - random

    Examples:
    >>> color_pattern = task_func(4, rng_seed=123)
    >>> print(color_pattern)
    ['Red', 'Red', 'Green', 'Blue']

    >>> colors = ['Brown', 'Green', 'Black']
    >>> color_pattern = task_func(12, colors=colors, rng_seed=42)
    >>> print(color_pattern)
    ['Brown', 'Black', 'Green', 'Brown', 'Black', 'Brown', 'Brown', 'Black', 'Green', 'Green', 'Black', 'Brown']
    """

           
    # Setting the seed for the random number generator
    if rng_seed is not None:
        seed(rng_seed)

    color_cycle = cycle(colors)
    color_pattern = []

    for _ in range(n_colors):
        color = next(color_cycle) if _ % 2 == 0 else choice(colors)
        color_pattern.append(color)

    return color_pattern


class TestTaskFunc(unittest.TestCase):

    def test_zero_colors(self):
        """Test when n_colors is 0, should return an empty list."""
        result = task_func(0)
        self.assertEqual(result, [])

    def test_negative_colors(self):
        """Test when n_colors is negative, should return an empty list."""
        result = task_func(-5)
        self.assertEqual(result, [])

    def test_colors_with_default(self):
        """Test when n_colors is 4 with default colors."""
        result = task_func(4, rng_seed=123)
        expected = ['Red', 'Red', 'Green', 'Blue']
        self.assertEqual(result, expected)

    def test_custom_colors(self):
        """Test with a custom set of colors."""
        colors = ['Brown', 'Green', 'Black']
        result = task_func(12, colors=colors, rng_seed=42)
        expected = ['Brown', 'Black', 'Green', 'Brown', 'Black', 
                    'Brown', 'Brown', 'Black', 'Green', 'Green', 
                    'Black', 'Brown']
        self.assertEqual(result, expected)

    def test_repeated_seed(self):
        """Test that the same input with the same seed produces the same output."""
        color_pattern1 = task_func(6, rng_seed=100)
        color_pattern2 = task_func(6, rng_seed=100)
        self.assertEqual(color_pattern1, color_pattern2)


if __name__ == '__main__':
    unittest.main()