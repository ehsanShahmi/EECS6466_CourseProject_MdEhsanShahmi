import unittest
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def task_func(data: pd.DataFrame) -> (pd.DataFrame, list):
    """
    This function takes a pandas DataFrame and standardizes its features using sklearn's StandardScaler,
    which standardizes features by removing the mean and scaling to unit variance.
    After standardization, it draws a histogram for each feature with 20 bins.

    Parameters:
    - data (pd.DataFrame): The input data to be standardized and plotted. It is expected to have
                           columns named 'Feature1', 'Feature2', 'Feature3', 'Feature4', and 'Feature5'.
                           If there are additional data columns, they are ignored.


    Returns:
    - standardized_data (pd.DataFrame): The standardized data.
    - axes_list (list): A list of matplotlib Axes objects representing the histograms for each feature.

    Requirements:
    - pandas
    - matplotlib.pyplot
    - sklearn.preprocessing.StandardScaler
    
    Example:
    >>> data = pd.DataFrame({
    ...     'Feature1': [0.5, 0.6, 0.7, 0.8, 0.9],
    ...     'Feature2': [0.1, 0.2, 0.3, 0.4, 0.5],
    ...     'Feature3': [0.9, 0.8, 0.7, 0.6, 0.5],
    ...     'Feature4': [0.5, 0.4, 0.3, 0.2, 0.1],
    ...     'Feature5': [0.1, 0.3, 0.5, 0.7, 0.9]
    ... })
    >>> standardized_data, axes_list = task_func(data)
    >>> type(standardized_data)
    <class 'pandas.core.frame.DataFrame'>
    >>> axes_list
    [<Axes: title={'center': 'Histogram of Feature1'}>, <Axes: title={'center': 'Histogram of Feature2'}>, <Axes: title={'center': 'Histogram of Feature3'}>, <Axes: title={'center': 'Histogram of Feature4'}>, <Axes: title={'center': 'Histogram of Feature5'}>]
    >>> type(axes_list[0])
    <class 'matplotlib.axes._axes.Axes'>
    """
    
    FEATURES = ["Feature1", "Feature2", "Feature3", "Feature4", "Feature5"]

    scaler = StandardScaler()
    data_standardized = pd.DataFrame(
        scaler.fit_transform(data[FEATURES]), columns=FEATURES
    )

    axes_list = []
    for feature in FEATURES:
        fig, ax = plt.subplots()
        ax.hist(data_standardized[feature], bins=20, alpha=0.5)
        ax.set_title("Histogram of {}".format(feature))
        axes_list.append(ax)

    return data_standardized, axes_list


class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        self.valid_data = pd.DataFrame({
            'Feature1': [0.5, 0.6, 0.7, 0.8, 0.9],
            'Feature2': [0.1, 0.2, 0.3, 0.4, 0.5],
            'Feature3': [0.9, 0.8, 0.7, 0.6, 0.5],
            'Feature4': [0.5, 0.4, 0.3, 0.2, 0.1],
            'Feature5': [0.1, 0.3, 0.5, 0.7, 0.9]
        })
        self.extra_data = pd.DataFrame({
            'Feature1': [0.5, 0.6, 0.7, 0.8, 0.9],
            'UnrelatedFeature': [10, 20, 30, 40, 50]
        })

    def test_standardized_data_type(self):
        standardized_data, _ = task_func(self.valid_data)
        self.assertIsInstance(standardized_data, pd.DataFrame)

    def test_standardized_data_shape(self):
        standardized_data, _ = task_func(self.valid_data)
        self.assertEqual(standardized_data.shape, (5, 5))

    def test_axes_list_length(self):
        _, axes_list = task_func(self.valid_data)
        self.assertEqual(len(axes_list), 5)

    def test_histogram_title(self):
        _, axes_list = task_func(self.valid_data)
        for i, feature in enumerate(["Feature1", "Feature2", "Feature3", "Feature4", "Feature5"]):
            self.assertEqual(axes_list[i].get_title(), f"Histogram of {feature}")

    def test_function_with_extra_columns(self):
        standardized_data, _ = task_func(self.extra_data)
        self.assertEqual(standardized_data.shape[1], 1)


if __name__ == "__main__":
    unittest.main()