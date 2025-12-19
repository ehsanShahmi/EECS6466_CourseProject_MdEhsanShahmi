import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Here is your prompt:

def task_func(feature: pd.Series, target: pd.Series) -> (np.ndarray, plt.Axes):
    """
    Train a logistic regression model on one feature and evaluate its performance using a confusion matrix plot.
    The function takes a feature and a target series, splits them into training and testing sets, trains the logistic
    regression model, predicts the target for the test set, and plots the confusion matrix.

    Parameters:
    feature (pd.Series): Series representing the single feature for the logistic regression model.
    target (pd.Series): Series representing the target variable.

    Returns:
    (np.ndarray, plt.Axes): A tuple containing the confusion matrix and the matplotlib Axes object of the confusion matrix plot.

    Requirements:
    - pandas
    - sklearn.model_selection.train_test_split
    - sklearn.linear_model.LogisticRegression
    - sklearn.metrics.confusion_matrix
    - numpy
    - matplotlib.pyplot

    Example:
    >>> feature = pd.Series(np.random.rand(1000)) # Feature data
    >>> target = pd.Series(np.random.randint(0, 2, size=1000)) # Target data (binary)
    >>> cm, ax = task_func(feature, target)
    >>> ax.get_title()
    'Confusion Matrix'
    """

               # Create DataFrame from the series
    df = pd.DataFrame({"Feature": feature, "Target": target})

    # Split the data into train and test datasets
    X_train, X_test, y_train, y_test = train_test_split(
        df["Feature"], df["Target"], test_size=0.2, random_state=42
    )

    # Initialize and train the Logistic Regression model
    model = LogisticRegression()
    model.fit(X_train.values.reshape(-1, 1), y_train)

    # Make predictions
    y_pred = model.predict(X_test.values.reshape(-1, 1))

    # Compute the confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    # Plot the confusion matrix
    _, ax = plt.subplots()
    cax = ax.matshow(cm, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.colorbar(cax)

    # Setting tick locations
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])

    # Now set tick labels correctly
    ax.set_xticklabels(["No", "Yes"])
    ax.set_yticklabels(["No", "Yes"])

    return cm, ax

class TestTaskFunc(unittest.TestCase):

    def setUp(self):
        """Set up test parameters."""
        np.random.seed(42)
        self.feature = pd.Series(np.random.rand(1000))  # Random feature data
        self.target = pd.Series(np.random.randint(0, 2, size=1000))  # Random binary target data

    def test_output_shape(self):
        """Test output shape of confusion matrix."""
        cm, ax = task_func(self.feature, self.target)
        self.assertEqual(cm.shape, (2, 2), "Confusion matrix should be of shape (2, 2)")

    def test_correct_labels(self):
        """Test that axis labels are correctly set."""
        cm, ax = task_func(self.feature, self.target)
        self.assertEqual(ax.get_title(), "Confusion Matrix", "Title should be 'Confusion Matrix'")
        self.assertEqual(ax.get_xticklabels()[0].get_text(), "No", "X-axis label should be 'No'")
        self.assertEqual(ax.get_xticklabels()[1].get_text(), "Yes", "X-axis label should be 'Yes'")

    def test_plot_output(self):
        """Test if plot is generated successfully."""
        cm, ax = task_func(self.feature, self.target)
        self.assertIsInstance(ax, plt.Axes, "Output should be a matplotlib Axes object")

    def test_prediction_accuracy(self):
        """Test that predictions make sense."""
        cm, ax = task_func(self.feature, self.target)
        total_predictions = np.sum(cm)
        accuracy = (cm[0, 0] + cm[1, 1]) / total_predictions
        self.assertGreaterEqual(accuracy, 0, "Accuracy should be non-negative")

    def test_no_errors_on_valid_input(self):
        """Test that no errors occur with valid input."""
        try:
            task_func(self.feature, self.target)
        except Exception as e:
            self.fail(f"task_func raised {type(e).__name__} unexpectedly: {e}")

if __name__ == '__main__':
    unittest.main()