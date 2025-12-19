import pandas as pd
import re
from scipy import stats
import unittest
import matplotlib.pyplot as plt

def task_func(text):
    """
    Extracts all names from a given text string that are not surrounded by square brackets 
    and counts the frequency of each extracted name. It then creates a bar chart of the name frequencies and
    returns the name frequencies as a pandas Series and the bar chart plot's axes object along with the skewness 
    and kurtosis of the name frequencies. If the skewness and kurtosis are nan, they are returned as None.
    
    Parameters:
    text (str): The text from which to extract names. Each name should be separated by square brackets containing addresses.
    
    Returns:
    tuple: A tuple containing:
        - pd.Series: A pandas Series with the frequency of each name.
        - Axes: A bar chart plot showing the name frequencies. If no names are found, this will be None.
        - float: The skewness of the name frequencies.
        - float: The kurtosis of the name frequencies.
    
    Requirements:
    - re
    - pandas
    - matplotlib.pyplot
    - scipy.stats

    Example:
    >>> text_input = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
    >>> name_freqs, plot, skew, kurtosis = task_func(text_input)
    >>> print(list(name_freqs.items())[0])
    ('Josie Smith', 1)
    >>> type(plot)
    <class 'matplotlib.axes._axes.Axes'>
    >>> round(kurtosis, 2) is not None
    True
    """

    # Extracting names from the text
    names = re.findall(r'(.*?)(?:\[.*?\]|$)', text)
    names = [name.strip() for name in names if name.strip()]  # Removing any empty or whitespace names

    # Counting name frequencies
    name_freqs = pd.Series(names).value_counts()
    
    # Creating a bar chart of name frequencies if there are names found
    if not name_freqs.empty:
        ax = name_freqs.plot(kind='bar', title="Name Frequencies")
        skewness = stats.skew(name_freqs)
        kurtosis = stats.kurtosis(name_freqs)
    else:
        ax = skewness = kurtosis = None

    if skewness == float('nan'):
        skewness = None
    if kurtosis == float('nan'):
        kurtosis = None
    
    return name_freqs, ax, skewness, kurtosis


class TestTaskFunc(unittest.TestCase):

    def test_single_name(self):
        text_input = "John Doe [123 Main St]"
        name_freqs, plot, skew, kurtosis = task_func(text_input)
        self.assertEqual(name_freqs['John Doe'], 1)
        self.assertIsInstance(plot, plt.Axes)

    def test_multiple_names(self):
        text_input = "Alice [Address] Bob [Address] Alice"
        name_freqs, plot, skew, kurtosis = task_func(text_input)
        self.assertEqual(name_freqs['Alice'], 2)
        self.assertEqual(name_freqs['Bob'], 1)
        self.assertIsInstance(plot, plt.Axes)

    def test_no_names(self):
        text_input = "[123 Main St] [456 Oak St]"
        name_freqs, plot, skew, kurtosis = task_func(text_input)
        self.assertTrue(name_freqs.empty)
        self.assertIsNone(plot)

    def test_names_with_special_characters(self):
        text_input = "Charlie Brown [123 Pine St] Anna-Marie [456 Elm St] Charlie Brown"
        name_freqs, plot, skew, kurtosis = task_func(text_input)
        self.assertEqual(name_freqs['Charlie Brown'], 2)
        self.assertEqual(name_freqs['Anna-Marie'], 1)
        self.assertIsInstance(plot, plt.Axes)

    def test_skewness_and_kurtosis_nan(self):
        text_input = "No Names Here [123 Main St]"
        name_freqs, plot, skew, kurtosis = task_func(text_input)
        self.assertIsNone(skew)
        self.assertIsNone(kurtosis)

if __name__ == '__main__':
    unittest.main()