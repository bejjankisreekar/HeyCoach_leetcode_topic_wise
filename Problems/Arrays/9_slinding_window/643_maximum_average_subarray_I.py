from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        current_sum = sum(nums[:k])
        res = current_sum

        for i in range(k, len(nums)):
            current_sum += nums[i] - nums[i - k]

            res = max(res, current_sum)

        return res / k
