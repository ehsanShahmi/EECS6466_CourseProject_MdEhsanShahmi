import numpy as np
import random
import itertools
import pandas as pd
import unittest

# Constants
PLANETS = [
    "Mercury",
    "Venus",
    "Earth",
    "Mars",
    "Jupiter",
    "Saturn",
    "Uranus",
    "Neptune",
]
ELEMENTS = [
    "Hydrogen",
    "Helium",
    "Oxygen",
    "Carbon",
    "Nitrogen",
    "Magnesium",
    "Silicon",
    "Iron",
    "Nickel",
]

def task_func():
    """
    Generate a DataFrame where each row contains random planet-element pairs.
    Each pair is formatted as 'Planet:Element'. The number of rows is determined by
    the number of planets, and each row will contain as many planet-element pairs as there are elements.

    Parameters:
    - None

    Returns:
    pandas.DataFrame: A DataFrame where each cell contains a string in the format 'Planet:Element'.
                      The DataFrame has a number of rows equal to the number of planets and
                      a number of columns equal to the number of elements.

    Requirements:
    - numpy
    - random
    - itertools
    - pandas

    Example:
    >>> random.seed(0)
    >>> planet_elements_table = task_func()
    >>> planet_elements_table.head(2)
              Hydrogen         Helium  ...          Iron         Nickel
    0   Uranus:Silicon  Earth:Silicon  ...  Earth:Nickel  Uranus:Helium
    1  Venus:Magnesium  Saturn:Helium  ...  Mercury:Iron   Venus:Helium
    <BLANKLINE>
    [2 rows x 9 columns]
    """

    # Generate all possible pairs
    pairs = [
        f"{planet}:{element}"
        for planet, element in itertools.product(PLANETS, ELEMENTS)
    ]
    # Shuffle the pairs to ensure randomness
    random.shuffle(pairs)

    # Convert the list of pairs into a numpy array, then reshape it to fit the DataFrame dimensions
    data = np.array(pairs).reshape(len(PLANETS), len(ELEMENTS))
    # Create the DataFrame with ELEMENTS as column headers
    df = pd.DataFrame(data, columns=ELEMENTS)

    return df

class TestTaskFunc(unittest.TestCase):

    def test_dataframe_shape(self):
        df = task_func()
        self.assertEqual(df.shape, (len(PLANETS), len(ELEMENTS)), "DataFrame shape should match number of planets and elements.")

    def test_dataframe_columns(self):
        df = task_func()
        self.assertListEqual(list(df.columns), ELEMENTS, "DataFrame columns should match ELEMENTS list.")

    def test_dataframe_index(self):
        df = task_func()
        self.assertEqual(list(df.index), list(range(len(PLANETS))), "DataFrame index should be a range object matching the number of planets.")

    def test_element_pairs_format(self):
        df = task_func()
        for i in range(len(PLANETS)):
            for j in range(len(ELEMENTS)):
                cell_value = df.iloc[i, j]
                expected_format = f"{PLANETS[i]}:{ELEMENTS[j]}"
                self.assertIn(cell_value.split(':')[0], PLANETS, f"Planet part of '{cell_value}' should be a valid planet.")
                self.assertIn(cell_value.split(':')[1], ELEMENTS, f"Element part of '{cell_value}' should be a valid element.")

    def test_randomness_of_pairs(self):
        random.seed(0)
        df1 = task_func()
        random.seed(0)
        df2 = task_func()
        # With the same seed, the outputs should be identical
        pd.testing.assert_frame_equal(df1, df2, "DataFrames should be identical when seeded with the same value.")

if __name__ == '__main__':
    unittest.main()