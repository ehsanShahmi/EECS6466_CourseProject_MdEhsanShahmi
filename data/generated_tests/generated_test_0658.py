import re
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import unittest

# Make sure to download NLTK stopwords
nltk.download('stopwords')

# Define a regex pattern for matching all non-alphanumeric characters
ALPHANUMERIC = re.compile('[\W_]+')

# Load NLTK's list of English stop words
STOPWORDS = nltk.corpus.stopwords.words('english')

def task_func(texts):
    """
    Creates a document-term matrix (DTM) from a list of text documents using CountVectorizer from Scikit-learn.
    Texts are preprocessed by removing non-alphanumeric characters (excluding spaces),
    converting to lowercase, and excluding English stop words defined in NLTK.
    """
    cleaned_texts = [ALPHANUMERIC.sub(' ', text).lower() for text in texts]
    tokenized_texts = [' '.join(word for word in text.split() if word not in STOPWORDS) for text in cleaned_texts]
    
    vectorizer = CountVectorizer()
    dtm = vectorizer.fit_transform(tokenized_texts)
    dtm_df = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out() if hasattr(vectorizer, 'get_feature_names_out') else vectorizer.get_feature_names())
    
    return dtm_df

class TestTaskFunc(unittest.TestCase):

    def test_empty_input(self):
        """Test that an empty list returns an empty DataFrame."""
        result = task_func([])
        self.assertTrue(result.empty)
    
    def test_single_document(self):
        """Test that a single document returns the correct DTM with one term."""
        texts = ["Hello world"]
        expected = pd.DataFrame([[1]], columns=["hello", "world"])
        result = task_func(texts)
        pd.testing.assert_frame_equal(result, expected)

    def test_multiple_documents(self):
        """Test that multiple documents are correctly processed into DTM."""
        texts = ["Hello world", "Machine learning is great"]
        expected = pd.DataFrame([[1, 1, 0, 0, 0, 0],
                                  [0, 0, 1, 1, 1, 1]], 
                                 columns=["great", "hello", "learning", "machine", "world", "is"])
        result = task_func(texts)
        pd.testing.assert_frame_equal(result, expected)

    def test_removal_of_stopwords(self):
        """Test that stop words are removed correctly from the documents."""
        texts = ["I love programming in Python"]
        expected = pd.DataFrame([[1, 1]], columns=["love", "programming", "python"])
        result = task_func(texts)
        pd.testing.assert_frame_equal(result, expected)

    def test_non_alphanumeric_handling(self):
        """Test that non-alphanumeric characters are removed from the documents."""
        texts = ["Hello, world!! Welcome to the universe."]
        expected = pd.DataFrame([[1, 1, 1, 1]], columns=["hello", "to", "universe", "welcome", "world"])
        result = task_func(texts)
        pd.testing.assert_frame_equal(result, expected)

if __name__ == "__main__":
    unittest.main()