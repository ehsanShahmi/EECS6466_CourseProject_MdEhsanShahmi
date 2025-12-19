import random
import matplotlib.pyplot as plt
import seaborn as sns
import unittest
from unittest.mock import patch

# Here is your prompt:
def task_func(result, colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']):
    """
    Draws a histogram of the "from_user" values in the provided result. The color of the histogram bars is selected at random from the provided colors list.

    Parameters:
    result (list): A list of dictionaries containing the key "from_user".
    colors (list, optional): A list of colors to choose from for the histogram bars. Defaults is ['b', 'g', 'r', 'c', 'm', 'y', 'k'].

    Returns:
    None: The function displays the histogram and does not return any value.

    Requirements:
    - random
    - matplotlib
    - seaborn

    Example:
    >>> result = [{"from_user": 0}, {"from_user": 0}, {"from_user": 1}]
    >>> task_func(result)
    """

    from_user_values = [d['from_user'] for d in result if 'from_user' in d]
    color = random.choice(colors)
    plt.figure()
    sns.histplot(from_user_values, color=color)
    plt.show()

class TestTaskFunc(unittest.TestCase):
    
    @patch('matplotlib.pyplot.show')
    def test_empty_result(self, mock_show):
        """Test when the result list is empty."""
        result = []
        task_func(result)
        # Expecting no errors, since it should just generate an empty histogram
        mock_show.assert_called_once()

    @patch('matplotlib.pyplot.show')
    def test_single_value(self, mock_show):
        """Test when there is a single value in the result."""
        result = [{"from_user": 1}]
        task_func(result)
        mock_show.assert_called_once()

    @patch('matplotlib.pyplot.show')
    def test_multiple_values(self, mock_show):
        """Test when there are multiple values in the result."""
        result = [{"from_user": 1}, {"from_user": 1}, {"from_user": 2}]
        task_func(result)
        mock_show.assert_called_once()

    @patch('matplotlib.pyplot.show')
    def test_random_color_selection(self, mock_show):
        """Test if the function can randomly select a color from the provided list."""
        result = [{"from_user": 0}, {"from_user": 1}, {"from_user": 2}]
        colors = ['r', 'g', 'b', 'y']
        with patch('random.choice', return_value='g'):
            task_func(result, colors)
            # We can't test the output histogram, but we can check if the show was called
            mock_show.assert_called_once()

    @patch('matplotlib.pyplot.show')
    def test_missing_from_user_key(self, mock_show):
        """Test when the dictionaries do not contain the 'from_user' key."""
        result = [{"user": 0}, {"user": 1}]
        task_func(result)
        mock_show.assert_called_once()

if __name__ == '__main__':
    unittest.main()