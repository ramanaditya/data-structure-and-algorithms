"""
## Question : Easy
### 136. [Single Number](https://leetcode.com/problems/single-number/)
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4
"""

# Solutions


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                return nums[i]
        return nums[-1]


# Runtime: 84 ms, faster than 85.53% of Python3 online submissions
# Memory Usage: 15.3 MB, less than 8.20% of Python3 online submissions


class Solution:
    """XOR with same number is 0 and other number is other number"""

    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for ele in nums:
            res ^= ele
        return res


# Runtime: 84 ms, faster than 85.53% of Python3 online submissions
# Memory Usage: 16.3 MB, less than 6.58% of Python3 online submissions
