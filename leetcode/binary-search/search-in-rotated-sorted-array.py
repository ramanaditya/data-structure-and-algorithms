"""
Medium
## Questions
### [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""

## Solutions


class Solution:
    def search_rotated_index(self, nums, left, right):
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        if left == 0 and nums[left] < nums[left + 1]:
            return -1
        return left

    def binary_search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        rotation_index = self.search_rotated_index(nums, 0, len(nums) - 1)

        if rotation_index == -1:
            result = self.binary_search(nums, target)
            return result

        result = self.binary_search(nums[:rotation_index], target)

        if result == -1:
            result = self.binary_search(nums[rotation_index:], target)
            return result if result == -1 else result + rotation_index

        return result


# Runtime: 36 ms, faster than 88.05% of Python3 online submissions
# Memory Usage: 14.1 MB, less than 6.29% of Python3 online submissions
