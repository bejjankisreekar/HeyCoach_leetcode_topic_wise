

# Brute force :
def targetIndices(nums, target):
    nums.sort()
    result = []
    for i in range(len(nums)):
        if nums[i] == target:
            result.append(i)
    return result

"""
Time Complexity: O(n log n) due to sorting, and O(n) for the iteration, so overall O(n log n). 
Space Complexity: O(1) if you don't count the output list as extra space.
"""


# in Binary search
import bisect

def targetIndices(nums, target):
    nums.sort()
    left = bisect.bisect_left(nums, target)
    right = bisect.bisect_right(nums, target)
    return list(range(left, right)) if left < right else []


"""
Time Complexity: O(n log n) for sorting, and O(log n) for binary search, so overall O(n log n). 
Space Complexity: O(1) excluding the output list.
"""