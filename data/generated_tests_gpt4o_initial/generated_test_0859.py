import unittest
import warnings
import sklearn.datasets as datasets
import sklearn.model_selection as model_selection
import sklearn.svm as svm
import sklearn.metrics as metrics

def task_func():
    """
    Perform an SVM classification of the iris dataset and warn if the accuracy is less than 0.9.
    The warning action is set to 'always'. The test size for the train-test split is 0.33.

    Parameters:
    - None

    Returns:
    tuple: A tuple containing:
        - accuracy (float): The accuracy of the SVM classification.
        - warning_msg (str or None): A warning message if the accuracy is below 0.9, None otherwise.

    Requirements:
    - warnings
    - sklearn

    Example:
    >>> task_func()
    (1.0, None)
    """

    warnings.simplefilter('always')
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = model_selection.train_test_split(
        iris.data, iris.target, test_size=0.33, random_state=42)
    
    clf = svm.SVC(random_state=42)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, predictions)

    warning_msg = None
    if accuracy < 0.9:
        warning_msg = "The accuracy of the SVM classification is below 0.9."
        warnings.warn(warning_msg)

    return accuracy, warning_msg

class TestTaskFunc(unittest.TestCase):

    def test_accuracy_type(self):
        accuracy, warning_msg = task_func()
        self.assertIsInstance(accuracy, float, "Accuracy should be a float.")

    def test_warning_message_not_warned(self):
        with self.assertNoWarnings():
            accuracy, warning_msg = task_func()
            self.assertIsNone(warning_msg, "Warning message should be None for accuracy >= 0.9.")

    def test_warning_message_warned(self):
        with self.assertRaises(RuntimeWarning):
            # Manually set accuracy to below 0.9 for this test
            with unittest.mock.patch('sklearn.metrics.accuracy_score', return_value=0.8):
                accuracy, warning_msg = task_func()
                self.assertEqual(warning_msg, "The accuracy of the SVM classification is below 0.9.", "Warning message does not match.")

    def test_return_type(self):
        accuracy, warning_msg = task_func()
        self.assertIsInstance(accuracy, float, "The first item of the returned tuple should be a float.")
        self.assertIsInstance(warning_msg, (str, type(None)), "The second item of the returned tuple should be a string or None.")

    def test_accuracy_value(self):
        accuracy, warning_msg = task_func()
        self.assertGreaterEqual(accuracy, 0.0, "Accuracy should be non-negative.")
        self.assertLessEqual(accuracy, 1.0, "Accuracy should not exceed 1.0.")

if __name__ == '__main__':
    unittest.main()