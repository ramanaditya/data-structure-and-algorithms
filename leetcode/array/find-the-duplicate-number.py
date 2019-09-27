'''
## Questions

### 287. [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/)

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2

Example 2:

Input: [3,1,3,4,2]
Output: 3

Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

'''

## Solutions

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            try:
                if d[i]:
                    return i
            except:
                d[i] = d.get(i, 0) + 1
        return 0

# Runtime: 60 ms
# Memory Usage: 16.3 MB

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = len(nums) - 1
        while i < len(nums):
            if i == j:
                i += 1
                j = len(nums) - 1
            elif nums[i] == nums[j]:
                return nums[i]
            else:
                j -= 1
        return 0
# TLE
