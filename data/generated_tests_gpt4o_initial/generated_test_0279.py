import random
from collections import Counter
import unittest

# Constants
CARDS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

def task_func(x=1):
    """
    Draw x random 5-card poker hands from a 52-card pack (without suits) and return
    the hands along with a counter of the drawn cards.

    Parameters:
    x (int, optional): Number of hands to draw. Default is 1.

    Returns:
    tuple: A tuple containing two elements:
        - list of list str: Each inner list contains 5 strings, representing a 5-card poker hand.
        - Counter: A counter of the drawn cards.


    The output is random; hence, the returned list will vary with each call.

    Requirements:
    - random
    - collections.Counter

    Example:
    >>> random.seed(0)
    >>> result = task_func(1)
    >>> len(result[0][0])
    5
    >>> result[0][0][0] in CARDS
    True
    """

    result = []
    card_counts = Counter()

    for i in range(x):
        drawn = random.sample(CARDS, 5)
        result.append(drawn)
        card_counts.update(drawn)

    return result, card_counts

class TestTaskFunc(unittest.TestCase):

    def test_single_hand_length(self):
        result, _ = task_func(1)
        self.assertEqual(len(result[0]), 5)

    def test_multiple_hands_length(self):
        result, _ = task_func(3)
        self.assertEqual(len(result), 3)
        for hand in result:
            self.assertEqual(len(hand), 5)

    def test_card_in_hand(self):
        random.seed(0)  # Set seed for reproducibility
        result, _ = task_func(1)
        for card in result[0]:
            self.assertIn(card, CARDS)

    def test_card_count(self):
        random.seed(0)  # Set seed for reproducibility
        result, card_counts = task_func(2)
        total_cards = sum(card_counts.values())
        self.assertEqual(total_cards, 10)

    def test_drawn_cards_unique(self):
        result, _ = task_func(1)
        drawn_cards = set(result[0])
        self.assertEqual(len(drawn_cards), len(result[0]))  # All cards should be unique in a single hand

if __name__ == '__main__':
    unittest.main()