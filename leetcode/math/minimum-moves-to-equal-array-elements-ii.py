"""
## Questions

### 462. [Minimum Moves to Equal Array Elements II](https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/)

Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

In one move, you can increment or decrement an element of the array by 1.

Example 1:
Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

Example 2:
Input: nums = [1,10,2,9]
Output: 16

Constraints:
n == nums.length
1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""


# Solutions
from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        steps = 0
        for num in nums:
            steps += abs(num - median)
        return steps


# Runtime       : 72 ms, faster than 70.13% of Python3 online submissions
# Memory Usage  : 15.5 MB, less than 13.52% of Python3 online submissions
