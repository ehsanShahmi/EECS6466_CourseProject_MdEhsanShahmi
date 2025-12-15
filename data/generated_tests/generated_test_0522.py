import collections
import matplotlib.pyplot as plt
import unittest

# Here is your prompt:
def task_func(data):
    """
    Combine a list of dictionaries with possibly differing keys (student names) into a single dictionary,
    calculate the average score for each student, and return a bar chart of average student scores with
    student on the x-axis and average score on the y-axis.

    This function handles data with varying dictionary lengths and missing keys by averaging available scores,
    ignoring None. If there is any negative score, the function raises ValueError.
    Bar colors can be: 'red', 'yellow', 'green', 'blue', 'purple'.

    Parameters:
    data (list): A list of dictionaries. The keys are student names and the values are scores.

    Returns:
    ax (matplotlib.axes._axes.Axes or None): A bar chart showing the 'Average Student Scores', with
                                             'Student' on the x-axis and 'Average Score' on the y-axis.
                                             If data is empty, return None.

    Requirements:
    - collections
    - matplotlib.pyplot

    Example:
    >>> data = [{'John': 5, 'Jane': 10, 'Joe': 7},\
                {'John': 6, 'Jane': 8, 'Joe': 10},\
                {'John': 5, 'Jane': 9, 'Joe': 8},\
                {'John': 7, 'Jane': 10, 'Joe': 9}]
    >>> ax = task_func(data)
    >>> type(ax)
    <class 'matplotlib.axes._axes.Axes'>
    >>> ax.get_xticklabels()
    [Text(0, 0, 'Jane'), Text(1, 0, 'Joe'), Text(2, 0, 'John')]
    """

    if not data:
        return None

    combined_dict = {}
    for d in data:
        for k, v in d.items():
            if v is None:
                continue
            elif v < 0:
                raise ValueError("Scores must be non-negative.")
            if k in combined_dict:
                combined_dict[k].append(v)
            else:
                combined_dict[k] = [v]

    avg_scores = {k: sum(v) / len(v) for k, v in combined_dict.items()}
    avg_scores = collections.OrderedDict(sorted(avg_scores.items()))
    labels, values = zip(*avg_scores.items())

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=["red", "yellow", "green", "blue", "purple"])
    ax.set_title("Average Student Scores")
    ax.set_xlabel("Student")
    ax.set_ylabel("Average Score")

    return ax

class TestTaskFunction(unittest.TestCase):
    
    def test_empty_data(self):
        result = task_func([])
        self.assertIsNone(result)

    def test_single_student(self):
        data = [{'John': 10}, {'John': 20}, {'John': 30}]
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(ax.get_xticks().size, 1)  # Should only have one x-tick for John

    def test_multiple_students(self):
        data = [{'John': 5, 'Jane': 10}, {'John': 8, 'Jane': 12}]
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        self.assertEqual(len(ax.get_xticks()), 2)  # Should have two x-ticks for John and Jane

    def test_ignore_none_scores(self):
        data = [{'John': None, 'Jane': 10}, {'John': 5, 'Jane': None}]
        ax = task_func(data)
        self.assertIsInstance(ax, plt.Axes)
        # John should be averaged as 5, Jane should be averaged as 10
        self.assertEqual(ax.patches[0].get_height(), 10)
        self.assertEqual(ax.patches[1].get_height(), 5)

    def test_negative_score(self):
        data = [{'John': -5}, {'Jane': 10}]
        with self.assertRaises(ValueError):
            task_func(data)

if __name__ == '__main__':
    unittest.main()