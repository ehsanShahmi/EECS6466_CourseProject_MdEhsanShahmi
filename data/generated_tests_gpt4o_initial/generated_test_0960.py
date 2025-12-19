import unittest
import string
import random

def task_func(text, seed=None):
    """
    Generates a password that mirrors the structure of the given text by replacing alphabetic
    characters with random ascii lowercase letters, digits with random single-digit numbers,
    spaces wth either a random digit or random lowercase letter at equal probabilities, and
    leaving other characters unchanged.

    Parameters:
    - text (str): The text to be mirrored in the generated password. Must not be empty.
    - seed (int, optional): Seed for the random number generator. Defaults to None (not set).

    Returns:
    - str: The generated password.

    Raises:
    - ValueError: If the input text is empty.

    Requirements:
    - random
    - string

    Note:
    - This function does not handle high Unicode characters and focuses only on ASCII values.

    Examples:
    >>> task_func("hello world! 123", 0)
    'mbqmp3jytre!v553'
    >>> task_func("apple321#", seed=42)
    'uahev901#'
    """

    if seed is not None:
        random.seed(seed)
    if not text:
        raise ValueError("text cannot be empty.")
    password = ""
    for char in text:
        random_lowercase = random.choice(string.ascii_lowercase)
        random_digit = random.choice(string.digits)
        if char.isalpha():
            password += random_lowercase
        elif char.isdigit():
            password += random_digit
        elif char == " ":
            if random.random() < 0.5:
                password += random_lowercase
            else:
                password += random_digit
        else:
            password += char
    return password


class TestTaskFunction(unittest.TestCase):
    
    def test_empty_string(self):
        with self.assertRaises(ValueError):
            task_func("")
    
    def test_structure_with_seed(self):
        result = task_func("password 123", seed=10)
        self.assertEqual(len(result), len("password 123"))
        self.assertTrue(all(c in string.ascii_lowercase + string.digits + " " for c in result))
    
    def test_structure_without_seed(self):
        result = task_func("test string 101", seed=None)
        self.assertEqual(len(result), len("test string 101"))
        self.assertTrue(all(c in string.ascii_lowercase + string.digits + " " for c in result))
    
    def test_special_characters(self):
        result = task_func("hello world! 123$", seed=5)
        self.assertIn("!", result)
        self.assertIn("$", result)
    
    def test_numeric_input(self):
        result = task_func("12345", seed=7)
        self.assertEqual(len(result), 5)  # Assuming it returns random digits
        self.assertTrue(all(c in string.digits for c in result))


if __name__ == "__main__":
    unittest.main()