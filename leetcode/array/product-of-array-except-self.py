"""
## Question : Medium
### 238. [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of
all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole
array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of
space complexity analysis.)
"""

## Solutions


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)

        left = 1
        right = 1

        for i in range(len(nums)):
            ans[i] *= left
            ans[-1 - i] *= right
            left *= nums[i]
            right *= nums[-1 - i]

        return ans


# Runtime       : 116 ms, faster than 93.01% of Python3 online submissions
# Memory Usage  : 20.4 MB, less than 82.00% of Python3 online submissions


class Solution:
    """
    Two Pointers
    Time Complexity: O( n )
    Space Complexity: O( 1 )
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        start = 1
        res = [1 for _ in range(len(nums))]

        left, right = 1, 1

        while start < len(nums):
            left *= nums[start - 1]
            right *= nums[-start]
            res[-start - 1] *= right
            res[start] *= left

            start += 1

        return res


# Runtime       : 128 ms, faster than 71.92%  of Python3 online submissions
# Memory Usage  : 20.3 MB, less than 91.59% of Python3 online submissions
