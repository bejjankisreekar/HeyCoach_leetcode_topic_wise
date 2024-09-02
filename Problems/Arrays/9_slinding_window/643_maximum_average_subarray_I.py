from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Find the maximum average of any contiguous subarray of length k.

        Args:
        nums (List[int]): List of integers representing the array.
        k (int): Length of the subarray to consider for the average.

        Returns:
        float: The maximum average of any contiguous subarray of length k.
        """

        # Step 1: Calculate the sum of the first 'k' elements
        current_sum = sum(nums[:k])

        # Initialize 'res' to store the maximum sum found so far.
        # Start with the sum of the first 'k' elements.
        res = current_sum

        # Step 2: Slide through the array from the k-th element to the end.
        for i in range(k, len(nums)):
            # Update the current sum by subtracting the element that's sliding out
            # of the window and adding the element that's sliding into the window.
            current_sum += nums[i] - nums[i - k]

            # Update the result with the maximum sum found so far.
            res = max(res, current_sum)

        # Step 3: Return the maximum average by dividing the maximum sum by 'k'.
        return res / k
