from collections import Counter
import logging
import unittest
import os

def task_func(letter_list, element, log_path):
    """
    Count the frequency of a particular letter in a given list of letters with logging.

    Logs are written to a file named 'task_func.log' with encoding 'utf-8' and logging level DEBUG.
    The log file is created by the function or overwritten if already exists.
    For each function call the following is logged with the respective logging level:
        - info: f"Function called with list: {letter_list} and element: {element}"
        - error: if the element is not in the letter list
        - info: f"Frequency of '{element}' is {element_frequency}"
    
    After the last info has been logged, the logging is shutdown, such that all
    files are released.

    Parameters:
    letter_list (list of str): The list of letters.
    element (str): The specific letter for which the frequency needs to be counted.
    log_path (str): the path to the folder in which to save the log file

    Returns:
    int: The frequency of the letter.

    Raises:
    ValueError: If element is not in letter_list.

    Requirements:
    - collections
    - logging
    """

    formatter = logging.Formatter('%(levelname)s:%(message)s')
    handler = logging.FileHandler(log_path+'/task_func.log', mode='w')
    logger = logging.getLogger()
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.info(f"Function called with list: {letter_list} and element: {element}")

    if element not in letter_list:
        logger.error("The element is not in the letter list.")
        logger.handlers[0].close
        logger.removeHandler(logger.handlers[0])
        logging.shutdown()

        raise ValueError("The element is not in the letter list.")
        
    letter_frequencies = Counter(letter_list)
    element_frequency = letter_frequencies[element]
    
    logger.info(f"Frequency of '{element}' is {element_frequency}")
    logger.handlers[0].close
    logger.removeHandler(logger.handlers[0])
    logging.shutdown()

    return element_frequency

class TestTaskFunc(unittest.TestCase):
    
    def setUp(self):
        self.log_path = './'
        self.log_file = os.path.join(self.log_path, 'task_func.log')

    def tearDown(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_counting_frequency_of_an_existing_element(self):
        result = task_func(['a', 'b', 'a', 'c', 'a'], 'a', self.log_path)
        self.assertEqual(result, 3)
        with open(self.log_file) as log:
            log_contents = log.read()
            self.assertIn("Function called with list: ['a', 'b', 'a', 'c', 'a'] and element: a", log_contents)
            self.assertIn("Frequency of 'a' is 3", log_contents)

    def test_counting_frequency_of_another_existing_element(self):
        result = task_func(['x', 'y', 'z'], 'y', self.log_path)
        self.assertEqual(result, 1)
        with open(self.log_file) as log:
            log_contents = log.read()
            self.assertIn("Function called with list: ['x', 'y', 'z'] and element: y", log_contents)
            self.assertIn("Frequency of 'y' is 1", log_contents)

    def test_error_when_element_not_in_list(self):
        with self.assertRaises(ValueError):
            task_func(['x', 'y', 'z'], 'a', self.log_path)
        
        with open(self.log_file) as log:
            log_contents = log.read()
            self.assertIn("Function called with list: ['x', 'y', 'z'] and element: a", log_contents)
            self.assertIn("ERROR:The element is not in the letter list.", log_contents)

    def test_counting_frequency_without_repetition(self):
        result = task_func(['a', 'b', 'c'], 'b', self.log_path)
        self.assertEqual(result, 1)
        with open(self.log_file) as log:
            log_contents = log.read()
            self.assertIn("Function called with list: ['a', 'b', 'c'] and element: b", log_contents)
            self.assertIn("Frequency of 'b' is 1", log_contents)

    def test_multiple_occurrences_with_different_letters(self):
        result = task_func(['a', 'a', 'b', 'b', 'c', 'c', 'a'], 'c', self.log_path)
        self.assertEqual(result, 2)
        with open(self.log_file) as log:
            log_contents = log.read()
            self.assertIn("Function called with list: ['a', 'a', 'b', 'b', 'c', 'c', 'a'] and element: c", log_contents)
            self.assertIn("Frequency of 'c' is 2", log_contents)

if __name__ == '__main__':
    unittest.main()