'''
## Questions
### 665. [Non-decreasing Array](https://leetcode.com/problems/non-decreasing-array/)
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
'''
## Solutions

import random
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1 or n == 2:
            return True
        i = 0
        nums1 = nums[:]
        while i < n-1:
            if nums[i] <= nums[i+1]:
                i += 1
                continue
            else:
                nums = nums[:i]+nums[i+1:]
                nums1 = nums1[:i+1] + nums1[i+2:]
                break
            i += 1
        if nums == sorted(nums) or nums1 == sorted(nums1):
            return True
        return False

# Runtime: 248 ms
# Memory Usage: 14.8 MB
