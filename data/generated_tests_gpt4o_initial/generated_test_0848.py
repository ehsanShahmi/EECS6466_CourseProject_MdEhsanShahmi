import heapq
import random
import unittest

# The provided prompt

def task_func(obj_list, attr, top_n=5, seed=None):
    """
    Find the top N values of the specified attribute in a list of objects.
    Return the top N values as well as a randomly sampled value of all attributes.

    Parameters:
    obj_list (list): The list of objects.
    attr (str): The attribute to find the top N values.
    top_n (int, optional): The number of top values to retrieve. Defaults to 5.
    seed (float, optional): The seed used for randomly choosing an attribute.

    Returns:
    list[int]: The top N values as a list of integers. Empty list if there are no attributes.
    float: A randomly chosen value of all attributes, None if there are no attributes.
    """
    
    random.seed(seed)
    attr_values = [getattr(obj, attr) for obj in obj_list]
    if len(attr_values) == 0:
        return [], None

    top_values = heapq.nlargest(top_n, attr_values)
    random_value = random.choice(attr_values)

    return top_values, random_value

# Test suite
class TestTaskFunc(unittest.TestCase):

    class Object:
        def __init__(self, value):
            self.value = value

    def test_basic_functionality(self):
        random.seed(1)
        obj_list = [self.Object(random.randint(1, 100)) for _ in range(33)]
        top_values, random_value = task_func(obj_list, 'value', 5, seed=1)
        self.assertEqual(top_values, [99, 98, 98, 98, 93])
        self.assertEqual(random_value, 58)

    def test_different_attribute(self):
        random.seed(2)
        obj_list = [self.Object(random.randint(1, 12)) for _ in range(13)]
        top_values, random_value = task_func(obj_list, 'value', 2, 12)
        self.assertEqual(top_values[0] <= 12, True)  # Test that top value is max 12
        self.assertEqual(top_values[1] <= 12, True)  # Test that second top value is max 12

    def test_empty_object_list(self):
        obj_list = []
        top_values, random_value = task_func(obj_list, 'value', 5, seed=3)
        self.assertEqual(top_values, [])
        self.assertIsNone(random_value)

    def test_less_than_top_n(self):
        random.seed(4)
        obj_list = [self.Object(random.randint(1, 10)) for _ in range(3)]
        top_values, random_value = task_func(obj_list, 'value', 5, seed=4)
        self.assertEqual(len(top_values), 3)  # We can only get 3 because there are 3 objects
        self.assertIsInstance(random_value, int)  # Random value should still be an integer

    def test_attribute_not_present(self):
        class AnotherObject:
            def __init__(self, value):
                self.other = value
        
        random.seed(5)
        obj_list = [AnotherObject(random.randint(1, 50)) for _ in range(10)]
        top_values, random_value = task_func(obj_list, 'value', 5, seed=5)
        self.assertEqual(top_values, [])  # 'value' attribute does not exist
        self.assertIsNone(random_value)  # Should return None for the random choice

if __name__ == '__main__':
    unittest.main()