import unittest
from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ls = []
        n = len(nums)
        res = 0
        for i in range(n):
            res += nums[i]
            ls.append(res)

        return ls

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [1,2,3,4]
        expected_output = [1,3,6,10]
        self.assertEqual(self.solution.runningSum(nums), expected_output)
        print(f"Test case 1 - Success")

    def test_case_2(self):
        nums = [1,1,1,1,1]
        expected_output = [1,2,3,4,5]
        self.assertEqual(self.solution.runningSum(nums), expected_output)
        print(f"Test case 2 - Success")