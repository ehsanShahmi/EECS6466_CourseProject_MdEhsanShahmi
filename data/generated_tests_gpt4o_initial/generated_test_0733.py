import unittest
import re
import string

def task_func(content):
    """Count the non-stop words in a sentence without the last word.

    Parameters:
    - content (str): The sentence to count non-stopwords from.

    Returns:
    - count (int): The count of non-stopwords.
    """
    STOPWORDS = set([
        "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", 
        "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", 
        "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", 
        "theirs", "themselves", "what", "which", "who", "whom", "this", "that", 
        "these", "those", "is", "are", "was", "were", "be", "been", "being", "have", 
        "has", "had", "having", "do", "does", "did", "doing", "an", "the", "and", 
        "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", 
        "for", "with", "about", "against", "between", "into", "through", "during", 
        "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", 
        "on", "off", "over", "under", "again", "further", "then", "once"
    ])

    content = content.split(' ')
    if len(content) > 1:
        content = content[:-1]
    else:
        content = []
    words = [word.strip(string.punctuation).lower() for word in re.split(r'\W+', ' '.join(content)) if word]
    non_stopwords = [word for word in words if word not in STOPWORDS]
    count = len(non_stopwords)

    return count

class TestTaskFunc(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(task_func(''), 0)  # No words to count

    def test_single_word_non_stopword(self):
        self.assertEqual(task_func('hello'), 0)  # Last word is non-stopword, should not count

    def test_single_word_stopword(self):
        self.assertEqual(task_func('i'), 0)  # Last word is a stopword, should not count

    def test_multiple_words_mixed(self):
        self.assertEqual(task_func('this is a test sentence'), 2)  # "test", "sentence" are non-stopwords

    def test_sentence_with_punctuation(self):
        self.assertEqual(task_func('Hello, world! How are you?'), 1)  # "Hello", "world", "How" are non-stopwords

if __name__ == '__main__':
    unittest.main()