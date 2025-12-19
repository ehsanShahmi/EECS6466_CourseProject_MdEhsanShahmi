import unittest
from collections import Counter
import random

# Constants
HAND_RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['H', 'D', 'C', 'S']


def task_func():
    """
    Generate a random poker hand consisting of five cards, and count the frequency of each card rank.
    """
    hand = []
    for _ in range(5):
        rank = random.choice(HAND_RANKS)
        suit = random.choice(SUITS)
        card = f'{rank}{suit}'
        hand.append(card)

    rank_counts = Counter([card[:-1] for card in hand])

    return hand, rank_counts


class TestPokerHandGeneration(unittest.TestCase):
    
    def setUp(self):
        random.seed(42)  # For reproducibility in tests

    def test_hand_size(self):
        hand, _ = task_func()
        self.assertEqual(len(hand), 5, "The hand should consist of 5 cards.")

    def test_rank_count(self):
        hand, rank_counts = task_func()
        rank_set = set(card[:-1] for card in hand)  # Create set of ranks in the hand
        self.assertEqual(len(rank_counts), len(rank_set), "Rank counts should match the unique ranks in hand.")

    def test_card_format(self):
        hand, _ = task_func()
        for card in hand:
            self.assertRegex(card, r'^[2-9]|10|[JQKA][HDS]$', "Each card should be in the format RANKSUIT where RANK is valid.")

    def test_randomness(self):
        hand1, _ = task_func()
        hand2, _ = task_func()
        self.assertNotEqual(hand1, hand2, "Two consecutive hands should not be the same, asserting randomness.")

    def test_rank_frequency(self):
        hand, rank_counts = task_func()
        for rank, count in rank_counts.items():
            self.assertGreaterEqual(count, 1, "Each rank should occur at least once if it exists in the hand.")

if __name__ == "__main__":
    unittest.main()