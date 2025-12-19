import collections
import pandas as pd
import unittest

def task_func(obj_list, attr):
    """
    Count the frequency of each value of the given attribute from a list of objects.
    
    This function returns a pandas Dataframe containing frequency count of the specified attribute from the objects in the list.
    The DataFrame consist of two columns ('attribute' and 'count'), which contain the attribute and its
    specific count respectively.
    
    If no attributes are found, an empty DataFrame is returned.

    Parameters:
    obj_list (list): The list of objects with attributes.
    attr (str): The attribute to count.

    Returns:
    collections.Counter: The frequency count of each value of the attribute.

    Requirements:
    - collections
    - pandas
    """
    attr_values = [getattr(obj, attr) for obj in obj_list]
    count = collections.Counter(attr_values)
    if len(count.keys()) == 0:
        return pd.DataFrame()

    df = pd.DataFrame.from_dict(count, orient='index').reset_index()
    df = df.rename(columns={'index':'attribute', 0:'count'})
    return df

class TestTaskFunc(unittest.TestCase):

    class ExampleObject:
        def __init__(self, color):
            self.color = color

    def test_single_object(self):
        obj_list = [self.ExampleObject('Red')]
        result = task_func(obj_list, 'color')
        expected = pd.DataFrame({'attribute': ['Red'], 'count': [1]})
        pd.testing.assert_frame_equal(result, expected)

    def test_multiple_objects_with_same_attribute(self):
        obj_list = [self.ExampleObject('Red'), self.ExampleObject('Red'), self.ExampleObject('Green')]
        result = task_func(obj_list, 'color')
        expected = pd.DataFrame({'attribute': ['Red', 'Green'], 'count': [2, 1]})
        pd.testing.assert_frame_equal(result, expected)

    def test_multiple_objects_with_different_attributes(self):
        obj_list = [self.ExampleObject('Red'), self.ExampleObject('Green'), self.ExampleObject('Blue')]
        result = task_func(obj_list, 'color')
        expected = pd.DataFrame({'attribute': ['Red', 'Green', 'Blue'], 'count': [1, 1, 1]})
        pd.testing.assert_frame_equal(result, expected)

    def test_empty_object_list(self):
        obj_list = []
        result = task_func(obj_list, 'color')
        expected = pd.DataFrame(columns=['attribute', 'count'])
        pd.testing.assert_frame_equal(result, expected)
    
    def test_no_matching_attribute(self):
        with self.assertRaises(AttributeError):
            obj_list = [self.ExampleObject('Red')]
            task_func(obj_list, 'shape')

if __name__ == '__main__':
    unittest.main()