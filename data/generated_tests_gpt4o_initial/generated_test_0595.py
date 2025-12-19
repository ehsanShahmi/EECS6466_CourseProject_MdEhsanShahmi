import unittest
import random
from array import array

# Here is your prompt:
import random
import bisect
from array import array


def task_func(n=10, total=100):
    """
    Generates 'n' random integer numbers such that their sum equals 'total', sorts these numbers,
    and determines the position where a new random number can be inserted to maintain the sorted order.
    The function uses a retry mechanism to ensure the generated numbers sum up to 'total'.

    Parameters:
    n (int): The number of random numbers to generate. Default is 10.
    total (int): The total sum of the generated numbers. Default is 100.

    Returns:
    tuple: A tuple containing the sorted numbers as an array and the insertion position for a new number.

    Requirements:
    - random
    - bisect
    - array.array

    Examples:
    >>> sorted_nums, pos = task_func(5, 50)
    >>> len(sorted_nums) == 5
    True
    >>> sum(sorted_nums) == 50
    True
    """

    nums = []
    while sum(nums) != total:
        nums = [random.randint(0, total) for _ in range(n)]

    nums.sort()
    nums = array('i', nums)

    new_num = random.randint(0, total)
    pos = bisect.bisect(nums, new_num)

    return (nums, pos)


class TestTaskFunc(unittest.TestCase):

    def test_default_parameters(self):
        sorted_nums, pos = task_func()
        self.assertEqual(len(sorted_nums), 10)
        self.assertEqual(sum(sorted_nums), 100)

    def test_custom_number_count(self):
        sorted_nums, pos = task_func(n=5, total=50)
        self.assertEqual(len(sorted_nums), 5)
        self.assertEqual(sum(sorted_nums), 50)

    def test_custom_total_sum(self):
        total_sum = 200
        sorted_nums, pos = task_func(n=10, total=total_sum)
        self.assertEqual(sum(sorted_nums), total_sum)

    def test_sorted_array(self):
        sorted_nums, pos = task_func(n=10, total=100)
        self.assertTrue(all(sorted_nums[i] <= sorted_nums[i + 1] for i in range(len(sorted_nums) - 1)))

    def test_insertion_position(self):
        sorted_nums, pos = task_func(n=10, total=100)
        new_num = random.randint(0, 100)
        self.assertEqual(pos, bisect.bisect(sorted_nums, new_num))


if __name__ == '__main__':
    unittest.main()