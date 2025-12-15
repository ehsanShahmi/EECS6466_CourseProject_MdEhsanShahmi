import random
import string
import unittest

# Constants
LETTERS = string.ascii_letters
DIGITS = string.digits

def task_func(length, num_digits):
    """
    Generate a random password with a specified length and number of digits.

    The function creates a random password consisting of letters and digits. The total length of the password
    and the number of digits in it are specified by the user. The characters in the password are randomly
    shuffled to ensure variability.

    Parameters:
    - length (int): The total length of the password. Must be a positive integer.
    - num_digits (int): The number of digits to be included in the password. Must be a non-negative integer and
                      less than or equal to the total length of the password.

    Returns:
    - str: A string representing the randomly generated password.
    """
    random.seed(42)
    if length <= 0:
        raise ValueError("Length must be a positive integer.")
    if not (0 <= num_digits <= length):
        raise ValueError("num_digits must be a non-negative integer and less than or equal to length.")

    password = []
    for _ in range(length - num_digits):
        password.append(random.choice(LETTERS))
    for _ in range(num_digits):
        password.append(random.choice(DIGITS))

    random.shuffle(password)

    return ''.join(password)

class TestPasswordGeneration(unittest.TestCase):

    def test_generate_password_length(self):
        """Test if the generated password has the correct length."""
        length = 10
        num_digits = 3
        password = task_func(length, num_digits)
        self.assertEqual(len(password), length)

    def test_generate_password_digits_count(self):
        """Test if the generated password contains the correct number of digits."""
        length = 10
        num_digits = 3
        password = task_func(length, num_digits)
        digit_count = sum(c in DIGITS for c in password)
        self.assertEqual(digit_count, num_digits)

    def test_generate_password_letters_count(self):
        """Test if the generated password contains the correct number of letters."""
        length = 10
        num_digits = 3
        password = task_func(length, num_digits)
        letter_count = sum(c in LETTERS for c in password)
        self.assertEqual(letter_count, length - num_digits)

    def test_password_length_zero(self):
        """Test if ValueError is raised for length of zero."""
        with self.assertRaises(ValueError) as context:
            task_func(0, 0)
        self.assertEqual(str(context.exception), "Length must be a positive integer.")

    def test_invalid_num_digits(self):
        """Test if ValueError is raised for invalid num_digits."""
        with self.assertRaises(ValueError) as context:
            task_func(5, 6)
        self.assertEqual(str(context.exception), "num_digits must be a non-negative integer and less than or equal to length.")

if __name__ == '__main__':
    unittest.main()