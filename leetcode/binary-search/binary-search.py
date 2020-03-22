"""
Easy
## Questions
### [704. Binary Search](https://leetcode.com/problems/binary-search/)

Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search
target in nums. If target exists, then return its index, otherwise return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


Note:
You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999].
"""

## Solutions


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        if target < nums[0] or target > nums[-1]:
            return -1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return -1


# Runtime: 268 ms, faster than 36.39% of Python3 online submissions
# Memory Usage: 14.1 MB, less than 54.84% of Python3 online submissions
