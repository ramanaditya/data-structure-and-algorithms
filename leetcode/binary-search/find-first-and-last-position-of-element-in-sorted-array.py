"""
## Questions: MEDIUM
### 34. [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target
value.

If target is not found in the array, return [-1, -1].

Follow up: Could you write an algorithm with O(log n) runtime complexity?

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""

# Solutions
from typing import List


class Solution:
    def binary_search_first(self, array, target):
        low, high = 0, len(array) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if array[mid] == target:
                if mid > 0 and array[mid - 1] == target:
                    high = mid - 1
                else:
                    return mid
            elif array[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    def binary_search_last(self, array, target, low):
        high = len(array) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if array[mid] == target:
                if mid < high and array[mid + 1] == target:
                    low = mid + 1
                else:
                    return mid
            elif array[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        res[0] = self.binary_search_first(nums, target)
        if res[0] != -1:
            res[1] = self.binary_search_last(nums, target, res[0])

        return res


# Runtime       : 76 ms, faster than 96.53% of Python3 online submissions
# Memory Usage  : 15.4 MB, less than 79.65% of Python3 online submissions
