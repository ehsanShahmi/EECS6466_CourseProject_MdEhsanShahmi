import unittest
import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Here is your prompt:
def task_func(page_title):
    """
    Create a word cloud from the text of a Wikipedia page.

    Parameters:
    page_title (str): The title of the Wikipedia page.

    Returns:
    matplotlib.axes.Axes: The Axes object of the plotted data. Is None if there is no wikipedia page with the title given as input.

    Requirements:
    - wikipedia
    - wordcloud.WordCloud
    - matplotlib.pyplot

    Example:
    >>> ax = task_func('Python (programming language)')
    """

    try:
        text = wikipedia.page(page_title).content
    except Exception as e:
        print(f"An error occured: {e}")
        return None
    wordcloud = WordCloud().generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    ax = plt.gca()
    return ax

class TestTaskFunc(unittest.TestCase):
    
    def test_valid_page_title(self):
        ax = task_func('Python (programming language)')
        self.assertIsNotNone(ax, "Expected a valid Axes object for a valid page title.")

    def test_empty_page_title(self):
        ax = task_func('')
        self.assertIsNone(ax, "Expected None for an empty page title.")

    def test_non_existent_page_title(self):
        ax = task_func('This page does not exist123456789')
        self.assertIsNone(ax, "Expected None for a non-existent page title.")

    def test_special_characters_page_title(self):
        ax = task_func('Café')
        self.assertIsNotNone(ax, "Expected a valid Axes object for a page title with special characters.")

    def test_numeric_page_title(self):
        ax = task_func('2021')
        self.assertIsNotNone(ax, "Expected a valid Axes object for a numeric page title.")

if __name__ == '__main__':
    unittest.main()