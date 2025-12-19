import pandas as pd
import regex as re
import unittest

def task_func(text):
    """
    Extract data from a text and create a Pandas DataFrame. The text contains several lines, each formatted as 'Score: 85, Category: Math'. Make sure to convert the scores in integer.

    Parameters:
    text (str): The text to analyze.

    Returns:
    DataFrame: A pandas DataFrame with extracted data.

    Requirements:
    - pandas
    - regex

    Example:
    >>> text = "Score: 85, Category: Math\\nScore: 90, Category: Science\\nScore: 80, Category: Math"
    >>> df = task_func(text)
    >>> print(df)
       Score Category
    0     85     Math
    1     90  Science
    2     80     Math
    """
    pattern = r"Score: (.*?), Category: (.*?)(\n|$)"
    matches = re.findall(pattern, text)
    data = [
        match[:2] for match in matches
    ]  # Extracting only the score and category from each match
    df = pd.DataFrame(data, columns=["Score", "Category"])
    df["Score"] = df["Score"].astype(int)
    return df

class TestTaskFunc(unittest.TestCase):
    
    def test_single_entry(self):
        text = "Score: 85, Category: Math"
        expected_output = pd.DataFrame({'Score': [85], 'Category': ['Math']})
        result = task_func(text)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_multiple_entries(self):
        text = "Score: 85, Category: Math\nScore: 90, Category: Science\nScore: 80, Category: Math"
        expected_output = pd.DataFrame({
            'Score': [85, 90, 80],
            'Category': ['Math', 'Science', 'Math']
        })
        result = task_func(text)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_empty_input(self):
        text = ""
        expected_output = pd.DataFrame(columns=["Score", "Category"])
        result = task_func(text)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_no_scores(self):
        text = "Category: Math\nCategory: Science"
        expected_output = pd.DataFrame(columns=["Score", "Category"])
        result = task_func(text)
        pd.testing.assert_frame_equal(result, expected_output)

    def test_malformed_input(self):
        text = "Score: 85 Math\nScore: 90, Category Science\nScore: 80, Category: Math"
        expected_output = pd.DataFrame({
            'Score': [80],
            'Category': ['Math']
        })
        result = task_func(text)
        pd.testing.assert_frame_equal(result, expected_output)

if __name__ == '__main__':
    unittest.main()