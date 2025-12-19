import numpy as np
import random
import unittest

def task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL):
    """
    Generates a palindrome sentence using random words from a specified pool. The sentence's length is randomly
    chosen between a minimum (MIN_WORDS) and maximum (MAX_WORDS) number of words. The function ensures that the
    sentence reads the same forwards and backwards.

    Parameters:
    MIN_WORDS (int): Minimum number of words in the palindrome sentence.
    MAX_WORDS (int): Maximum number of words in the palindrome sentence.
    WORDS_POOL (list): List of words to choose from for generating the palindrome.

    Returns:
    str: The generated palindrome sentence.

    Requirements:
    - numpy
    - random

    Examples:
    Generate a palindrome sentence and check if it's indeed a palindrome.
    >>> MIN_WORDS, MAX_WORDS, WORDS_POOL = 3, 10, ['apple', 'banana', 'racecar', 'world', 'level', 'madam', 'radar', 'rotor']
    >>> sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    >>> re_sentence = " ".join(sentence.split()[::-1])
    >>> sentence == re_sentence
    True

    Check if the generated sentence length is within the specified range.
    >>> sentence = task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL)
    >>> MIN_WORDS <= len(sentence.split()) <= MAX_WORDS
    True
    """

    sentence_length = np.random.randint(MIN_WORDS, MAX_WORDS + 1)
    first_half = [random.choice(WORDS_POOL) for _ in range(sentence_length // 2)]

    # For odd-length sentences, add a middle word
    if sentence_length % 2 == 1:
        middle_word = [random.choice(WORDS_POOL)]
        second_half = first_half[::-1]
        sentence = first_half + middle_word + second_half
    else:
        second_half = first_half[::-1]
        sentence = first_half + second_half

    return ' '.join(sentence)

class TestPalindromeSentenceGeneration(unittest.TestCase):

    def setUp(self):
        self.WORDS_POOL = ['apple', 'banana', 'racecar', 'world', 'level', 'madam', 'radar', 'rotor']

    def test_palindrome_property(self):
        MIN_WORDS, MAX_WORDS = 3, 10
        sentence = task_func(MIN_WORDS, MAX_WORDS, self.WORDS_POOL)
        re_sentence = " ".join(sentence.split()[::-1])
        self.assertEqual(sentence, re_sentence)

    def test_length_within_range(self):
        MIN_WORDS, MAX_WORDS = 3, 10
        sentence = task_func(MIN_WORDS, MAX_WORDS, self.WORDS_POOL)
        self.assertTrue(MIN_WORDS <= len(sentence.split()) <= MAX_WORDS)

    def test_odd_length_palindrome(self):
        MIN_WORDS, MAX_WORDS = 3, 10
        random.seed(0)  # set seed for reproducibility
        sentence = task_func(MIN_WORDS, MAX_WORDS, self.WORDS_POOL)
        words = sentence.split()
        mid_index = len(words) // 2
        
        # Check if first half of the sentence matches the reversed second half
        if len(words) % 2 == 1:  # odd length
            first_half = words[:mid_index]
            second_half = words[mid_index+1:][::-1]
        else:  # even length
            first_half = words[:mid_index]
            second_half = words[mid_index:][::-1]
        
        self.assertEqual(first_half, second_half)

    def test_even_length_palindrome(self):
        MIN_WORDS, MAX_WORDS = 4, 10
        random.seed(0)  # set seed for reproducibility
        sentence = task_func(MIN_WORDS, MAX_WORDS, self.WORDS_POOL)
        words = sentence.split()
        mid_index = len(words) // 2
        
        # Check if first half of the sentence matches the reversed second half
        first_half = words[:mid_index]
        second_half = words[mid_index:][::-1]
        
        self.assertEqual(first_half, second_half)

    def test_empty_words_pool(self):
        MIN_WORDS, MAX_WORDS = 1, 5
        empty_pool = []
        with self.assertRaises(IndexError):
            task_func(MIN_WORDS, MAX_WORDS, empty_pool)

if __name__ == '__main__':
    unittest.main()