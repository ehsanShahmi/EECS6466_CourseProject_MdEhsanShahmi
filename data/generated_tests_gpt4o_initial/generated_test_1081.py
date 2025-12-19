import pandas as pd
import seaborn as sns
import unittest

# Here is your provided prompt code:

def task_func(data=None):
    """
    Converts string-formatted weights to floats and plots a scatter plot of weight against height.

    This function takes a dictionary with two keys: 'Weight_String' and 'Height'. The 'Weight_String' key should 
    contain a list of weight values in string format, while the 'Height' key should have a list of corresponding 
    height values in numerical format. If the input dictionary is not provided, the function uses a default dataset.
    The function then converts the string-formatted weights into float, and plots a scatter plot to visualize 
    the relationship between weight and height.
       
    Parameters:
    - data (dict, optional): A dictionary with keys 'Weight_String' and 'Height'. 'Weight_String' is expected to be 
                           a list of weight values in string format (e.g., ['60.5', '65.7']), and 'Height' is expected 
                           to be a list of corresponding numerical height values (e.g., [160, 165]). If no dictionary 
                           is provided, a default dataset with predetermined values is used.
                           Default dictionary:
                           {
                               'Weight_String': ['60.5', '65.7', '70.2', '75.9', '80.1'],
                               'Height': [160, 165, 170, 175, 180]
                           }

    Returns:
    - ax (matplotlib.axes._axes.Axes): A scatter plot with weight on the x-axis and height on the y-axis, titled "Weight vs Height".

    Raises:
    - ValueError: If any of the values in the 'Weight_String' key are not formatted as strings. This validation ensures 
                that the weight data is in the expected format for conversion to float.

    Requirements:
    - pandas
    - seaborn

    Example:
    >>> ax = task_func()
    >>> print(ax.get_title())
    Weight vs Height
    """

    if data is None:
        data = {
            "Weight_String": ["60.5", "65.7", "70.2", "75.9", "80.1"],
            "Height": [160, 165, 170, 175, 180],
        }

    df = pd.DataFrame(data)

    # Validate weight values are strings
    if not all(isinstance(weight, str) for weight in df["Weight_String"]):
        raise ValueError("Weights must be provided as strings.")

    # Convert string weights to floats
    df["Weight_Float"] = df["Weight_String"].astype(float)

    # Plotting the scatter plot
    ax = sns.scatterplot(data=df, x="Weight_Float", y="Height")
    ax.set_title("Weight vs Height")
    return ax


# The test suite
class TestTaskFunc(unittest.TestCase):

    def test_default_data(self):
        ax = task_func()
        self.assertEqual(ax.get_title(), "Weight vs Height")
        self.assertEqual(ax.collections[0].get_offsets().shape[0], 5)

    def test_custom_data(self):
        custom_data = {
            "Weight_String": ["50.0", "60.0", "70.0"],
            "Height": [150, 160, 170],
        }
        ax = task_func(data=custom_data)
        self.assertEqual(ax.get_title(), "Weight vs Height")
        self.assertEqual(ax.collections[0].get_offsets().shape[0], 3)

    def test_invalid_weight_format(self):
        invalid_data = {
            "Weight_String": [60.5, "65.7", "70.2"],  # First value is a float, not a string
            "Height": [160, 165, 170],
        }
        with self.assertRaises(ValueError) as context:
            task_func(data=invalid_data)
        self.assertEqual(str(context.exception), "Weights must be provided as strings.")

    def test_empty_data(self):
        empty_data = {
            "Weight_String": [],
            "Height": [],
        }
        ax = task_func(data=empty_data)
        self.assertEqual(ax.get_title(), "Weight vs Height")
        self.assertEqual(ax.collections[0].get_offsets().shape[0], 0)

    def test_non_empty_and_empty_height(self):
        mixed_data = {
            "Weight_String": ["60.5", "65.0", "70.5"],
            "Height": [],  # No height values provided
        }
        with self.assertRaises(ValueError):  # Assuming function should handle this case
            task_func(data=mixed_data)

if __name__ == '__main__':
    unittest.main()