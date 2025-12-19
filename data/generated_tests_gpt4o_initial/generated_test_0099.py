import unittest
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

# Provided prompt to test
def task_func():
    plt.rc('font', family='Arial')  # Set the global font to Arial.
    iris = load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['species'] = iris.target

    # Create a pair plot with the hue set to species.
    pair_plot = sns.pairplot(iris_df, hue='species', vars=iris.feature_names)
    pair_plot.fig.suptitle('Iris Dataset Pair Plot', fontsize=16)  # Title for the figure
    return pair_plot.fig

class TestIrisPairPlot(unittest.TestCase):

    def test_return_type(self):
        """Test if the function returns a matplotlib Figure."""
        fig = task_func()
        self.assertIsInstance(fig, plt.Figure, "The return type should be a matplotlib Figure.")

    def test_plot_title(self):
        """Test if the plot title is correctly set."""
        fig = task_func()
        self.assertEqual(fig._suptitle.get_text(), 'Iris Dataset Pair Plot', "The plot title should be 'Iris Dataset Pair Plot'.")

    def test_axis_labels(self):
        """Test if the axes of the first subplot contain the correct labels."""
        fig = task_func()
        axes = fig.get_axes()
        first_subplot = axes[0]  # Get the first subplot
        x_label = first_subplot.get_xlabel()
        y_label = first_subplot.get_ylabel()
        self.assertIn(x_label, load_iris().feature_names, "The x-axis label should be a feature name.")
        self.assertIn(y_label, load_iris().feature_names, "The y-axis label should be a feature name.")

    def test_species_column_exists(self):
        """Test if the species column is added to the DataFrame."""
        iris = load_iris()
        iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
        self.assertIn('species', iris_df.columns, "The DataFrame should contain a 'species' column.")

    def test_num_subplots(self):
        """Test if the number of subplots is correct."""
        fig = task_func()
        axes = fig.get_axes()
        expected_num_subplots = len(load_iris().feature_names) * (len(load_iris().feature_names) - 1) // 2
        self.assertEqual(len(axes), expected_num_subplots, f"The number of subplots should be {expected_num_subplots}.")

if __name__ == '__main__':
    unittest.main()