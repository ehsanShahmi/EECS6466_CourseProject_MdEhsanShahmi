import numpy as np
import matplotlib.pyplot as plt
import unittest

# Here is your prompt:
import numpy as np
import matplotlib.pyplot as plt

# Constants
NUM_SAMPLES = 100
NUM_OUTLIERS = 5


def task_func(num_samples=NUM_SAMPLES, num_outliers=NUM_OUTLIERS):
    """
    Generate a dataset comprising both normal data and artificially introduced outliers,
    and plot a histogram of the combined data. The function detects outliers in the dataset
    using the Interquartile Range (IQR) method, but it only considers the normally distributed
    portion of the data for outlier detection. The outliers detected and the artificially
    introduced outliers might not always coincide.

    Parameters:
    - num_samples (int): Number of samples to be drawn from a normal distribution. The default 
      value is 100. If set to zero or a negative number, no normal data will be generated, 
      and the dataset will only contain artificially introduced outliers.
    - num_outliers (int): Number of outliers to be artificially introduced into the dataset. 
      These outliers are uniformly distributed between -10 and 10. The default value is 5. 
      If set to zero, no outliers will be artificially introduced.


    Returns:
    - data (numpy array): The combined dataset, including both normally distributed data and 
      the artificially introduced outliers.
    - outliers_detected (numpy array): The outliers detected using the IQR method. This 
      detection is based solely on the normally distributed portion of the data.
    - ax (matplotlib.axes._axes.Axes): The Axes object for the histogram 
      plot of the combined dataset.

    Requirements:
    - numpy
    - matplotlib

    Note:
    - The artificially introduced outliers are not necessarily the same as the outliers
    detected by the IQR method. The IQR method is applied only to the normally distributed
    data, and thus some of the artificially introduced outliers may not be detected,
    and some normal data points may be falsely identified as outliers.

    Example:
    >>> import numpy as np
    >>> np.random.seed(0)
    >>> data, outliers_detected, ax = task_func()
    >>> print(outliers_detected)
    [-9.61613603 -3.96850367  3.20347075]
    """

    normal_data = np.random.normal(size=num_samples)
    outliers = np.random.uniform(low=-10, high=10, size=num_outliers)
    data = np.concatenate([normal_data, outliers]) if num_samples > 0 else outliers

    # Identify outliers using IQR (only if there is normal data)
    outliers_detected = np.array([])
    if num_samples > 0:
        q75, q25 = np.percentile(normal_data, [75, 25])
        iqr = q75 - q25
        lower_bound = q25 - (iqr * 1.5)
        upper_bound = q75 + (iqr * 1.5)
        outliers_detected = data[(data < lower_bound) | (data > upper_bound)]

    # Plot histogram
    _, ax = plt.subplots()
    ax.hist(data, bins=30)

    return data, outliers_detected, ax

class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        data, outliers_detected, ax = task_func()
        self.assertEqual(len(data), 105)  # 100 normal + 5 outliers
        self.assertTrue(isinstance(outliers_detected, np.ndarray))
        self.assertTrue(isinstance(ax, plt.Axes))

    def test_no_normal_data(self):
        data, outliers_detected, ax = task_func(0)
        self.assertEqual(len(data), 5)  # Only outliers
        self.assertTrue(np.all((data >= -10) & (data <= 10)))  # Check range of outliers
        self.assertEqual(len(outliers_detected), 0)  # No normal data means no detected outliers

    def test_no_outliers(self):
        data, outliers_detected, ax = task_func(num_outliers=0)
        self.assertEqual(len(data), 100)  # Only normal data
        self.assertTrue(np.all(np.isclose(data, np.random.normal(size=100), atol=1e-5)))  # Ensure normal data

    def test_custom_sample_sizes(self):
        data, outliers_detected, ax = task_func(num_samples=50, num_outliers=10)
        self.assertEqual(len(data), 60)  # 50 normal + 10 outliers
        self.assertTrue(np.all((data >= -10) & (data <= 10)))  # Check range of outliers

    def test_outlier_detection(self):
        data, outliers_detected, ax = task_func()
        self.assertIsInstance(outliers_detected, np.ndarray)
        for outlier in outliers_detected:
            self.assertTrue(outlier < np.percentile(data, 25) - 1.5 * (np.percentile(data, 75) - np.percentile(data, 25)) or
                            outlier > np.percentile(data, 75) + 1.5 * (np.percentile(data, 75) - np.percentile(data, 25)))

if __name__ == '__main__':
    unittest.main()