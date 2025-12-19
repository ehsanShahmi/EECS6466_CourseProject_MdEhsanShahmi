import re
import pandas as pd
import unittest

STOPWORDS = ["Those", "are", "the", "words", "to", "ignore"]

def task_func(text):
    sentences = re.split(r"\.\s*", text)
    sentence_counts = {}

    for i, sentence in enumerate(sentences):
        if sentence.strip() == "":
            continue
        words = re.split(r"\s+", sentence.lower())
        words = [word for word in words if word not in STOPWORDS]
        sentence_counts[f"Sentence {i+1}"] = len(words)

    sentence_counts = pd.Series(sentence_counts)
    return sentence_counts

class TestTaskFunc(unittest.TestCase):
    def test_basic_sentences(self):
        text = "This is a sample sentence. This sentence contains sample words."
        expected_result = pd.Series({"Sentence 1": 5, "Sentence 2": 5})
        pd.testing.assert_series_equal(task_func(text), expected_result)

    def test_empty_string(self):
        text = ""
        expected_result = pd.Series(dtype='int')
        pd.testing.assert_series_equal(task_func(text), expected_result)

    def test_no_valid_sentences(self):
        text = "Those are words to ignore."
        expected_result = pd.Series(dtype='int')
        pd.testing.assert_series_equal(task_func(text), expected_result)

    def test_multiple_sentences_with_stopwords(self):
        text = "Hello world. Those are just words. This is a simple test."
        expected_result = pd.Series({"Sentence 1": 2, "Sentence 2": 0, "Sentence 3": 5})
        pd.testing.assert_series_equal(task_func(text), expected_result)

    def test_sentences_with_only_stopwords(self):
        text = "To ignore those words."
        expected_result = pd.Series(dtype='int')
        pd.testing.assert_series_equal(task_func(text), expected_result)

if __name__ == '__main__':
    unittest.main()