'''
## Question

### 1. [Two Sum](https://leetcode.com/problems/two-sum/)

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

## Solutions

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in nums:
          a=target-i
          m=nums.index(i)
          if a in nums:
              try:
                  n = nums.index(a,m+1,len(nums))
                  return (m,n)
              except:
                  continue

# Runtime: 188 ms
# Memory Usage: -
