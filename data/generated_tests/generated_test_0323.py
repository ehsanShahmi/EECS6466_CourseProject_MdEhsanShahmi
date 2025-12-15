import re
import numpy as np
from collections import Counter
from sklearn.mixture import GaussianMixture
import unittest

def task_func(text, num_gaussians=1, seed=42):
    '''
    Extract names from a string that aren't enclosed by square brackets, 
    tokenize the names into words, and count the frequency of each word.
    Finally, fit a mixture of num_gaussians 1-D Gaussian distributions to 
    the word frequencies and return the means and variances of the fitted 
    Gaussians.
    
    Parameters:
    text (str): The text from which to extract names and count word frequencies.
    num_gaussians (int, Optional): The number of Gaussian distributions to fit to 
                                   the word frequencies. Defaults to 1.
    seed (int, Optional): The seed for the random number generator. Defaults to 42.
    
    Returns:
    dict: A dictionary with the frequency of each word.
    
    Requirements:
    - re module for regular expression operations.
    - numpy for setting the random seed.
    - collections.Counter for counting word frequencies.
    - scipy.stats.gmm for fitting Gaussian mixture models.

    Raises:
    ValueError: If num_gaussians is less than or equal to 0.
    Exception: If num_gaussians is greater than the number of unique words.
    
    Examples:
    >>> freqs, means = task_func("Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]")
    >>> freqs
    {'Josie': 1, 'Smith': 2, 'Mugsy': 1, 'Dog': 1}
    '''

    np.random.seed(seed)
    names = re.findall(r'(.*?)(?:\[.*?\]|$)', text)
    words = ' '.join(names).split()
    word_freqs = Counter(words)
    if num_gaussians <= 0:
        raise ValueError('Number of Gaussians must be greater than 0.')
    if len(word_freqs) < num_gaussians:
        raise Exception('Number of Gaussians must be less than or equal to the number of unique words.')

    mixture = GaussianMixture(n_components=num_gaussians)
    mixture.fit([[freq] for freq in word_freqs.values()])
    means = mixture.means_
    return dict(word_freqs), means

class TestTaskFunc(unittest.TestCase):
    
    def test_regular_input(self):
        text = "Josie Smith [3996 COLLEGE AVENUE, SOMETOWN, MD 21003]Mugsy Dog Smith [2560 OAK ST, GLENMEADE, WI 14098]"
        expected_freqs = {'Josie': 1, 'Smith': 2, 'Mugsy': 1, 'Dog': 1}
        freqs, means = task_func(text)
        self.assertEqual(freqs, expected_freqs)
        self.assertEqual(len(means), 1)  # Should return 1 mean for the default 1 Gaussian

    def test_multiple_gaussians(self):
        text = "Alice Bob Alice [Some random text] Charlie Bob"
        freqs, means = task_func(text, num_gaussians=2)
        self.assertEqual(len(means), 2)  # Should return 2 means
    
    def test_zero_gaussians(self):
        text = "Alice Bob Alice Charlie Bob"
        with self.assertRaises(ValueError):
            task_func(text, num_gaussians=0)
    
    def test_negative_gaussians(self):
        text = "Alice Bob Alice Charlie Bob"
        with self.assertRaises(ValueError):
            task_func(text, num_gaussians=-1)

    def test_too_many_gaussians(self):
        text = "John Doe Jane"
        with self.assertRaises(Exception):
            task_func(text, num_gaussians=4)

if __name__ == '__main__':
    unittest.main()