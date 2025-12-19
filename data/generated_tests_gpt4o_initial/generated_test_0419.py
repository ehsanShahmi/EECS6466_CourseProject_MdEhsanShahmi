import numpy as np
import unittest
from sklearn.model_selection import train_test_split
from sklearn.metrics import precision_recall_curve
from tensorflow import keras
import matplotlib.pyplot as plt

# Here is your prompt:
def task_func(X, Y):
    """
    This function should:
    - Splits the input data into training (70%) and test (30%) sets.
    - Constructs a Keras Sequential model with one hidden dense layer and sigmoid activation.
      The input dimension is determined based on the first feature set of X.
    - Compiles the model using binary cross-entropy loss and SGD optimizer.
    - Fits the model to the training data in a non-verbose mode.
    - Plots the Precision-Recall curve for the model based on the test set data.

    Parameters:
    X (np.ndarray): Input data for the model. Must have at least one feature.
    Y (np.ndarray): Target labels for the model.

    Returns:
    - keras.models.Sequential: The trained Keras model.
    - matplotlib.axes._axes.Axes: The matplotlib Axes object for the Precision-Recall curve plot.
    
    Notes:
    - The plot's x-axis is labeled 'Recall', and the y-axis is labeled 'Precision'.
    - The title of the axes is set to 'Precision-Recall Curve'.
    - The axes object allows for further customization of the plot outside the function.

    Requirements:
    - tensorflow.keras
    - sklearn.model_selection.train_test_split
    - sklearn.metrics.precision_recall_curve
    - matplotlib.pyplot

    Examples:
    >>> X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    >>> Y = np.array([[0], [1], [1], [0]])
    >>> model, ax = task_func(X, Y)
    >>> isinstance(model, Sequential)
    True
    >>> isinstance(ax, plt.Axes)
    True
    """

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
    input_dim = X.shape[1]  # Dynamically set input dimension

    model = keras.models.Sequential([keras.layers.Dense(units=1, input_dim=input_dim, activation='sigmoid')])
    model.compile(loss='binary_crossentropy', optimizer=keras.optimizers.SGD(learning_rate=0.1))

    model.fit(X_train, Y_train, epochs=200, batch_size=1, verbose=0)

    Y_pred = model.predict(X_test, verbose=0).ravel()
    precision, recall, thresholds = precision_recall_curve(Y_test, Y_pred)

    fig, ax = plt.subplots()  # Modify here to return Axes object
    ax.plot(recall, precision, label='Precision-Recall curve')
    ax.set_xlabel('Recall')
    ax.set_ylabel('Precision')
    ax.set_title('Precision-Recall Curve')
    ax.legend(loc='best')

    return model, ax  # Return both the model and the axes object


class TestTaskFunc(unittest.TestCase):

    def test_output_type(self):
        X = np.array([[0, 0], [1, 1], [0, 1], [1, 0]])
        Y = np.array([[0], [0], [1], [1]])
        model, ax = task_func(X, Y)
        self.assertIsInstance(model, keras.models.Sequential)
        self.assertIsInstance(ax, plt.Axes)

    def test_model_training(self):
        X = np.array([[0, 0], [1, 1], [0, 1], [1, 0]])
        Y = np.array([[0], [0], [1], [1]])
        model, _ = task_func(X, Y)
        weights = model.get_weights()
        self.assertTrue(len(weights) > 0)  # Ensure model has weights after training

    def test_output_shape(self):
        X = np.array([[0, 0], [1, 1], [0, 1], [1, 0]])
        Y = np.array([[0], [0], [1], [1]])
        model, _ = task_func(X, Y)
        self.assertEqual(model.output_shape, (None, 1))  # Make sure the output shape is (None, 1)

    def test_model_compilation(self):
        X = np.array([[0, 0], [1, 1], [0, 1], [1, 0]])
        Y = np.array([[0], [0], [1], [1]])
        model, _ = task_func(X, Y)
        self.assertIn('binary_crossentropy', model.loss)  # Ensure binary cross-entropy loss is used

    def test_plot_labels(self):
        X = np.array([[0, 0], [1, 1], [0, 1], [1, 0]])
        Y = np.array([[0], [0], [1], [1]])
        _, ax = task_func(X, Y)
        self.assertEqual(ax.get_xlabel(), 'Recall')
        self.assertEqual(ax.get_ylabel(), 'Precision')
        self.assertEqual(ax.get_title(), 'Precision-Recall Curve')


if __name__ == '__main__':
    unittest.main()