import pandas as pd
import regex as re
import seaborn as sns
import matplotlib.pyplot as plt
import unittest

COLUMN_NAMES = ["Name", "Email", "Age", "Country"]

def task_func(text):
    """
    Extract data from a text and create a Pandas DataFrame.
    The text contains several lines, each formatted as 'Name: John Doe, Email: john.doe@example.com, Age: 30, Country: USA'.
    Plot the age distribution using seaborn.

    The data is extracted using the regular expression pattern:
    "Name: (.*?), Email: (.*?), Age: (.*?), Country: (.*?)($|\n)"
    and the resulting DataFrame has columns: ['Name', 'Email', 'Age', 'Country']

    Parameters:
    text (str): The text to analyze.

    Returns:
    DataFrame: A pandas DataFrame with extracted data.
    """
    pattern = r"Name: (.*?), Email: (.*?), Age: (.*?), Country: (.*?)($|\n)"
    matches = re.findall(pattern, text)
    data = []
    for match in matches:
        data.append(match[:-1])
    df = pd.DataFrame(data, columns=COLUMN_NAMES)
    df["Age"] = df["Age"].astype(int)
    sns.histplot(data=df, x="Age")
    plt.show()
    return df

class TestTaskFunc(unittest.TestCase):

    def test_valid_input(self):
        text = 'Name: John Doe, Email: john.doe@example.com, Age: 30, Country: USA\nName: Jane Doe, Email: jane.doe@example.com, Age: 25, Country: UK'
        df = task_func(text)
        self.assertEqual(df.shape[0], 2)
        self.assertListEqual(list(df.columns), COLUMN_NAMES)

    def test_empty_input(self):
        text = ''
        df = task_func(text)
        self.assertEqual(df.shape[0], 0)

    def test_single_entry(self):
        text = 'Name: Alice Smith, Email: alice.smith@example.com, Age: 28, Country: Canada'
        df = task_func(text)
        self.assertEqual(df.shape[0], 1)
        self.assertEqual(df['Name'].iloc[0], 'Alice Smith')
        self.assertEqual(df['Email'].iloc[0], 'alice.smith@example.com')
        self.assertEqual(df['Age'].iloc[0], 28)
        self.assertEqual(df['Country'].iloc[0], 'Canada')

    def test_invalid_age(self):
        text = 'Name: Bob Brown, Email: bob.brown@example.com, Age: invalid_age, Country: Australia'
        with self.assertRaises(ValueError):
            task_func(text)

    def test_missing_fields(self):
        text = 'Name: Charlie White, Email: charlie.white@example.com, Age: 22'
        df = task_func(text)
        self.assertEqual(df.shape[0], 0)  # Should not match and result in an empty DataFrame

if __name__ == '__main__':
    unittest.main()