import unittest
import string
import random

# Here is your prompt:
def task_func(length, random_seed=None):
    """
    Generate a random string of a given length, with each character being either
    a parenthesis (from the set "(){}[]") 
    or a lowercase English character.
    For function uses a optional random_seed when sampling characters.

    Parameters:
    length (int): The length of the string to generate.
    random_seed (int): Random seed for rng. Used in picking random characters.
                       Defaults to None.

    Returns:
    str: The generated string.

    Requirements:
    - string
    - random

    Note: The function uses the internal string constant BRACKETS for 
          definition of the bracket set.

    Example:
    >>> string = task_func(10, random_seed=1)
    >>> print(string)
    ieqh]{[yng
    
    >>> string = task_func(34, random_seed=42)
    >>> print(string)
    hbrpoigf)cbfnobm(o{rak)vrjnvgfygww

    >>> string = task_func(23, random_seed=1)
    >>> print(string)
    ieqh]{[yng]by)a{rogubbb
    """

    random.seed(random_seed)
    # Constants
    BRACKETS = "(){}[]"
    return ''.join(random.choice(string.ascii_lowercase + BRACKETS) for _ in range(length))


class TestTaskFunc(unittest.TestCase):

    def test_length_of_string(self):
        """Test that the generated string has the correct length."""
        result = task_func(10, random_seed=1)
        self.assertEqual(len(result), 10)

    def test_generated_string_contains_valid_characters(self):
        """Test that the generated string contains only valid characters."""
        valid_chars = string.ascii_lowercase + "(){}[]"
        result = task_func(50, random_seed=2)
        self.assertTrue(all(char in valid_chars for char in result))

    def test_same_output_with_same_seed(self):
        """Test that calling the function with the same seed produces the same output."""
        seed = 5
        result1 = task_func(20, random_seed=seed)
        result2 = task_func(20, random_seed=seed)
        self.assertEqual(result1, result2)

    def test_empty_string(self):
        """Test that calling the function with length 0 returns an empty string."""
        result = task_func(0, random_seed=3)
        self.assertEqual(result, "")

    def test_output_with_different_seeds(self):
        """Test that calling the function with different seeds produces different outputs."""
        result1 = task_func(15, random_seed=4)
        result2 = task_func(15, random_seed=5)
        self.assertNotEqual(result1, result2)


if __name__ == '__main__':
    unittest.main()