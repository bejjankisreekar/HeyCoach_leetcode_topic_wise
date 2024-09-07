from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)

        # Euclidean algorithm
        while min_num != 0:
            max_num, min_num = min_num, max_num % min_num

        return max_num
