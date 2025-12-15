import unittest
import bisect
import random

def task_func(num, list_length=5, min_value=0, max_value=0):
    numbers = [random.randint(min_value, max_value) for _ in range(list_length)]
    sorted_list = numbers.copy()
    bisect.insort(sorted_list, num)
    return numbers, sorted_list

class TestTaskFunc(unittest.TestCase):
    
    def test_insert_into_empty_list(self):
        """Test inserting into an empty sorted list."""
        result = task_func(10, 0, 0, 0)
        self.assertEqual(result[0], [])
        self.assertEqual(result[1], [10])

    def test_insert_into_sorted_list(self):
        """Test inserting a number into a sorted list."""
        random.seed(1)
        numbers = [1, 2, 3, 4, 5]
        sorted_list = sorted(numbers + [6])  # 6 should be added to the list
        self.assertEqual(task_func(6, 5, 1, 5)[1], sorted_list)

    def test_insert_lower_bound(self):
        """Test inserting a lower value than the smallest in the list."""
        random.seed(2)
        result = task_func(0, 5, 1, 5)  # List will contain values from 1 to 5
        self.assertTrue(result[1].index(0) == 0)  # 0 should be the first element

    def test_insert_upper_bound(self):
        """Test inserting a number larger than all existing numbers in the list."""
        random.seed(3)
        result = task_func(10, 5, 1, 9)  # List will contain values between 1 and 9
        self.assertTrue(result[1][-1] == 10)  # 10 should be the last element

    def test_insert_into_large_list(self):
        """Test inserting into a larger random list."""
        random.seed(4)
        numbers, sorted_list = task_func(5, 100, 0, 100)  # Random list of length 100
        self.assertEqual(len(numbers), 100)  # Check the length of the random list
        self.assertTrue(sorted_list.index(5) > -1)  # 5 should be in the sorted list

if __name__ == '__main__':
    unittest.main()