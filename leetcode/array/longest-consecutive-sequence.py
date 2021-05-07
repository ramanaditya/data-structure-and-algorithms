"""
## Question
### 128. [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 104
-109 <= nums[i] <= 109

Follow up: Could you implement the O(n) solution?
"""

# Solutions
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        count = 1
        res = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                continue
            if nums[i + 1] - nums[i] == 1:
                count += 1
            else:
                res = max(count, res)
                count = 1

        return max(res, count)


# Runtime       : 56 ms, faster than 74.86% of Python3 online submissions
# Memory Usage  : 15 MB, less than 97.78% of Python3 online submissions
