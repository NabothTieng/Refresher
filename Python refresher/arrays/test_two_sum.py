import unittest
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from twosum import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum_basic(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 1])

    def test_two_sum_another(self):
        nums = [3, 2, 4]
        target = 7
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 2])

    def test_two_sum_negative(self):
        nums = [3, 3]
        target = 6
        result = self.solution.twoSum(nums, target)
        self.assertEqual(result, [0, 1])

if __name__ == "__main__":
    unittest.main()