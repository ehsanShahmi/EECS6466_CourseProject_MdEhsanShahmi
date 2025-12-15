import pandas as pd
import matplotlib.pyplot as plt
import unittest

def task_func(df, items=None, locations=None):
    """
    Generates a bar chart representing the distribution of specified items across given locations.
    
    The function takes a DataFrame with 'Item' and 'Location' columns and plots the count of each item
    per location. If lists of items and locations are provided, the chart will only include those specified,
    otherwise it defaults to a predefined list.

    Parameters:
    - df (pandas.DataFrame): DataFrame containing 'Item' and 'Location' columns.
    - items (list of str, optional): Specific items to include in the chart. Defaults to a predefined list
      ['apple', 'banana', 'grape', 'orange', 'pineapple'] if None.
    - locations (list of str, optional): Specific locations to include in the chart. Defaults to a predefined
      list ['store1', 'store2', 'store3', 'store4', 'store5'] if None.

    Returns:
    - matplotlib.axes.Axes: Axes object with the plotted bar chart.

    Raises:
    - ValueError: If 'df' is not a DataFrame, or if 'Item' or 'Location' columns are missing.
    """
    
    if not isinstance(df, pd.DataFrame) or not all(col in df.columns for col in ['Item', 'Location']):
        raise ValueError("Invalid 'df': must be a DataFrame with 'Item' and 'Location' columns.")

    items = items or ['apple', 'banana', 'grape', 'orange', 'pineapple']
    locations = locations or ['store1', 'store2', 'store3', 'store4', 'store5']

    item_count_df = df.groupby(['Location', 'Item']).size().unstack().fillna(0)
    ax = item_count_df.plot(kind='bar', stacked=True)
    ax.set_title('Item Distribution by Location')
    ax.set_ylabel('Count')
    plt.show()
    return ax

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up a sample DataFrame for testing."""
        self.df = pd.DataFrame({
            'Item': ['apple', 'banana', 'apple', 'orange', 'banana', 'grape'],
            'Location': ['store1', 'store2', 'store1', 'store1', 'store2', 'store3']
        })

    def test_valid_dataframe(self):
        """Test valid DataFrame input."""
        ax = task_func(self.df)
        self.assertIsNotNone(ax)

    def test_invalid_dataframe_type(self):
        """Test raising ValueError for non-DataFrame input."""
        with self.assertRaises(ValueError):
            task_func("not a dataframe")

    def test_missing_columns(self):
        """Test raising ValueError for DataFrame missing columns."""
        df_invalid = pd.DataFrame({
            'Item': ['apple', 'banana'],
            # 'Location' column is missing
        })
        with self.assertRaises(ValueError):
            task_func(df_invalid)

    def test_custom_items(self):
        """Test the function with specified items."""
        items = ['apple', 'banana']
        ax = task_func(self.df, items=items)
        self.assertEqual(ax.get_title(), 'Item Distribution by Location')

    def test_custom_locations(self):
        """Test the function with specified locations."""
        locations = ['store1', 'store3']
        ax = task_func(self.df, locations=locations)
        self.assertEqual(ax.get_title(), 'Item Distribution by Location')

if __name__ == '__main__':
    unittest.main()