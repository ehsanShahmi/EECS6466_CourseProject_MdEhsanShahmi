import pandas as pd
import itertools
import random
import unittest

def task_func(colors, states):
    combinations = list(itertools.product(colors, states))
    random.seed(42)
    random.shuffle(combinations)
    num_columns = min(len(colors), len(states))

    data = {
        f"Color:State {i+1}": [
            f"{comb[0]}:{comb[1]}" for comb in combinations[i::num_columns]
        ]
        for i in range(num_columns)
    }
    df = pd.DataFrame(data)

    return df

class TestTaskFunc(unittest.TestCase):

    def test_empty_lists(self):
        """Test with empty colors and states lists."""
        colors = []
        states = []
        expected_df = pd.DataFrame(columns=["Color:State 1"])
        result_df = task_func(colors, states)
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_one_color_and_one_state(self):
        """Test with one color and one state."""
        colors = ['Red']
        states = ['Solid']
        expected_df = pd.DataFrame({'Color:State 1': ['Red:Solid']})
        result_df = task_func(colors, states)
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_multiple_colors_and_single_state(self):
        """Test with multiple colors but only one state."""
        colors = ['Red', 'Blue', 'Green']
        states = ['Liquid']
        expected_df = pd.DataFrame({
            'Color:State 1': ['Blue:Liquid', 'Green:Liquid', 'Red:Liquid']
        })
        result_df = task_func(colors, states)
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_single_color_and_multiple_states(self):
        """Test with a single color and multiple states."""
        colors = ['Red']
        states = ['Solid', 'Liquid', 'Gas']
        expected_df = pd.DataFrame({
            'Color:State 1': ['Red:Liquid'],
            'Color:State 2': ['Red:Gas'],
            'Color:State 3': ['Red:Solid']
        })
        result_df = task_func(colors, states)
        pd.testing.assert_frame_equal(result_df, expected_df)

    def test_multiple_colors_and_multiple_states(self):
        """Test with multiple colors and multiple states."""
        colors = ['Red', 'Blue', 'Green']
        states = ['Solid', 'Liquid']
        result_df = task_func(colors, states)
        self.assertEqual(result_df.shape[1], 2)
        self.assertTrue(set(result_df['Color:State 1']).issubset({ 'Red:Solid', 'Blue:Solid', 'Green:Solid', 'Red:Liquid', 'Blue:Liquid', 'Green:Liquid' }))
        self.assertTrue(set(result_df['Color:State 2']).issubset({ 'Red:Solid', 'Blue:Solid', 'Green:Solid', 'Red:Liquid', 'Blue:Liquid', 'Green:Liquid' }))

if __name__ == '__main__':
    unittest.main()