"""
## Question : Easy
### 53. [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is
more subtle.
"""

## Solutions


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return
        maxsum = currentsum = nums[0]
        for i in range(1, len(nums)):
            currentsum = max(currentsum + nums[i], nums[i])
            if currentsum > maxsum:
                maxsum = currentsum
        return maxsum


# Runtime: 60 ms, faster than 94.34% of Python3 online submissions
# Memory Usage: 14.5 MB, less than 5.69% of Python3 online submissions
