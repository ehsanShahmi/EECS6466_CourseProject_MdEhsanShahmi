import re
import json
from collections import defaultdict
import string
import unittest

def task_func(json_string):
    """
    Process a JSON string containing a "text" field: convert to lowercase, remove punctuation, and count word frequency.

    This function takes a JSON string with a field named "text", and returns a dictionary with word counts. 
    It processes the text by converting it to lowercase, removing all punctuation and non-alphanumeric characters 
    (except spaces), and then counting the frequency of each word.

    Parameters:
    - json_string (str): A JSON string with a "text" field to process.

    Returns:
    - dict: A dictionary with words as keys and their frequency counts as values. If the "text" field is missing, 
      returns an empty dictionary.

    Requirements:
    - re
    - json
    - collections
    - string

    Example:
    >>> json_input = '{"text": "Hello world! Hello universe. World, meet universe."}'
    >>> task_func(json_input)
    {'hello': 2, 'world': 2, 'universe': 2, 'meet': 1}

    Notes:
    - Punctuation is removed using the `string.punctuation` constant.
    - The function is case-insensitive and treats words like "Hello" and "hello" as the same word.
    - If the JSON string is malformed or the "text" field is missing, an empty dictionary is returned.
    """

    try:
        # Load JSON and extract text
        data = json.loads(json_string)
        text = data.get('text', '')
    except json.JSONDecodeError:
        return {}

    # Lowercase, remove non-alphanumeric characters except spaces, remove punctuation
    text = re.sub('[^\sa-zA-Z0-9]', '', text).lower().strip()
    text = text.translate({ord(c): None for c in string.punctuation})

    # Count words
    word_counts = defaultdict(int)
    for word in text.split():
        word_counts[word] += 1

    return dict(word_counts)

class TestTaskFunc(unittest.TestCase):
    
    def test_normal_case(self):
        json_input = '{"text": "Hello world! Hello universe. World, meet universe."}'
        expected_output = {'hello': 2, 'world': 2, 'universe': 2, 'meet': 1}
        self.assertEqual(task_func(json_input), expected_output)

    def test_empty_text(self):
        json_input = '{"text": ""}'
        expected_output = {}
        self.assertEqual(task_func(json_input), expected_output)

    def test_malformed_json(self):
        json_input = '{"text": "Hello world!}'
        expected_output = {}
        self.assertEqual(task_func(json_input), expected_output)

    def test_no_text_field(self):
        json_input = '{"not_text": "Hello world!"}'
        expected_output = {}
        self.assertEqual(task_func(json_input), expected_output)

    def test_text_with_punctuation_only(self):
        json_input = '{"text": "!!!???"}'
        expected_output = {}
        self.assertEqual(task_func(json_input), expected_output)

if __name__ == '__main__':
    unittest.main()