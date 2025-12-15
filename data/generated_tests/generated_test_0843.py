import random
import re
import unittest

# Constants
WORD_LIST = ["sample", "text", "contains", "several", "words", "including"]

def task_func(n_sentences):
    """
    Generate a string of random sentences using a predefined word list. 
    Each sentence is guaranteed to have one period at the end, and no period within the sentence.
    The generated sentences will be concatenated into a single string, 
    with all letters in lowercase and all non-alphanumeric characters except spaces removed.

    Parameters:
    - n_sentences (int): The number of sentences to generate.

    Returns:
    - str: A string containing the generated sentences in lowercase 
         with non-alphanumeric characters removed (except for single periods ending sentences).
    
    Requirements:
    - random
    - re
    """

    sentences = []
    for _ in range(n_sentences):
        sentence_len = random.randint(5, 10)
        sentence = " ".join(random.choice(WORD_LIST) for _ in range(sentence_len)) + "."
        sentences.append(sentence)

    # Join sentences and ensure no extra spaces around periods
    text = " ".join(sentences)
    # Remove unwanted characters, ensure only letters, spaces, or periods remain
    text = re.sub(r'[^\w\s.]', '', text).lower()
    # Normalize spaces ensuring single space between words and no trailing spaces before periods
    text = re.sub(r'\s+\.', '.', text)
    text = re.sub(r'\s+', ' ', text)

    return text.strip()

class TestTaskFunc(unittest.TestCase):
    
    def test_single_sentence(self):
        """Test that a single sentence is generated correctly."""
        random.seed(1)  # Set seed for reproducibility
        result = task_func(1)
        self.assertTrue(result.endswith('.'))
        self.assertEqual(len(result.split()), 6)  # Considering a length of 5-10 words

    def test_multiple_sentences(self):
        """Test that multiple sentences are generated."""
        random.seed(1)  # Set seed for reproducibility
        result = task_func(3)
        sentences = result.split('.')
        self.assertEqual(len(sentences), 4)  # Three sentences + one empty after last period
        for sentence in sentences[:-1]:
            self.assertTrue(sentence)  # Ensure no empty sentences

    def test_no_extra_spaces(self):
        """Check that there are no extra spaces around periods."""
        random.seed(2)  # Set seed for reproducibility
        result = task_func(2)
        self.assertNotIn(' .', result)  # Reject spaces before period
        self.assertNotIn('. ', result)  # Reject spaces after period

    def test_string_is_lowercase(self):
        """Test that the generated string is all lowercase."""
        random.seed(3)  # Set seed for reproducibility
        result = task_func(1)
        self.assertEqual(result, result.lower())

    def test_contains_only_valid_characters(self):
        """Test that the output string contains only alphanumeric characters, spaces, and periods."""
        random.seed(4)  # Set seed for reproducibility
        result = task_func(2)
        valid_characters = re.match(r'^[a-zA-Z0-9\s.]*$', result)
        self.assertIsNotNone(valid_characters)  # Should match the regex for valid characters

if __name__ == '__main__':
    unittest.main()