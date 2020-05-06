"""
## Questions
### 169. [Majority Element](https://leetcode.com/problems/majority-element/)
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋
times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
"""
## Solutions


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        n = len(nums)
        for i in nums:
            d[i] = d.get(i, 0) + 1
            if d[i] > n // 2:
                return i


# Runtime: 180 ms, faster than 52.91% of Python3 online submissions
# Memory Usage: 15.3 MB, less than 7.14% of Python3 online submissions


class Solution:
    """Using Boyer Moore Voting Algorithm"""

    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]  # Initialization
        counter = 0  # Counter

        for i in range(len(nums)):
            if counter == 0:
                res = nums[i]
                counter = 1
            elif res == nums[i]:
                counter += 1
            else:
                counter -= 1

        return res


# Runtime: 160 ms, faster than 98.42% of Python3 online submissions
# Memory Usage: 15.2 MB, less than 7.14% of Python3 online submissions
