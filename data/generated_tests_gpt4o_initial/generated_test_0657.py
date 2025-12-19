import unittest
import nltk
from gensim.models import Word2Vec

# Here is your prompt:
import re
import nltk
from gensim.models import Word2Vec
# Constants
ALPHANUMERIC = re.compile('[\W_]+')


def task_func(texts, stopwords=None):
    """
    Generate word vectors from a list of texts using the gensim Word2Vec model and nltk.corpus.stopwords.
    The texts are first cleaned by removing all non-alphanumeric characters except space,
    lowercased, and stop words are removed.

    Parameters:
    texts (list): A list of strings.
    stopwords (list, optional): A list of stopwords to be removed. If not provided, nltk's stopwords will be used.

    Returns:
    Word2Vec: A trained Word2Vec model.

    Requirements:
    - re
    - nltk
    - gensim

    Example:
    >>> texts = ["Hello, World!", "Machine Learning is great", "Python is my favorite programming language"]
    >>> model = task_func(texts)
    >>> vector = model.wv['python']
    """
    
    if stopwords is None:
        stopwords = nltk.corpus.stopwords.words('english')
        
    cleaned_texts = [ALPHANUMERIC.sub(' ', text).lower() for text in texts]
    tokenized_texts = [[word for word in text.split() if word not in stopwords] for text in cleaned_texts]
    
    # Handle empty texts input by returning an untrained Word2Vec model
    if not tokenized_texts:
        return Word2Vec(vector_size=100)

    model = Word2Vec(sentences=tokenized_texts, vector_size=100, window=5, min_count=1, workers=4)

    return model


class TestTaskFunction(unittest.TestCase):

    def test_basic_functionality(self):
        texts = ["Hello, World!", "Machine Learning is great", "Python is my favorite programming language"]
        model = task_func(texts)
        self.assertIn('python', model.wv.key_to_index)

    def test_stopwords_removal(self):
        texts = ["This is a test", "Testing the removal of stopwords"]
        stopwords = ['this', 'is', 'of']
        model = task_func(texts, stopwords=stopwords)
        self.assertNotIn('this', model.wv.key_to_index)
        self.assertNotIn('is', model.wv.key_to_index)
        self.assertNotIn('of', model.wv.key_to_index)

    def test_empty_texts(self):
        texts = []
        model = task_func(texts)
        self.assertEqual(len(model.wv), 0)

    def test_non_alphanumeric_chars(self):
        texts = ["Hello!!! @World #2023 *&^%$", "Test - with different punctuations."]
        model = task_func(texts)
        self.assertIn('hello', model.wv.key_to_index)
        self.assertIn('world', model.wv.key_to_index)

    def test_case_insensitivity(self):
        texts = ["Python is great", "python IS even better!"]
        model = task_func(texts)
        self.assertIn('python', model.wv.key_to_index)
        self.assertEqual(model.wv['python'].all(), model.wv['great'].all())

if __name__ == '__main__':
    unittest.main()