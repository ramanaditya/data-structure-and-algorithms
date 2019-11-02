'''
## Question
### 628. [Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/)
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6

Example 2:
Input: [1,2,3,4]
Output: 24


Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''

## Solutions

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if not nums or len(nums) < 3:
            return 0
        nums.sort()
        first = nums[0] * nums[1] * nums[-1]
        second = nums[-1] * nums[-2] * nums[-3]
        return max(first,second)

# Runtime: 324 ms, faster than 43.37% of Python3 online submissions for Maximum Product of Three Numbers.
# Memory Usage: 14.9 MB, less than 6.67% of Python3 online su
