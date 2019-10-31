'''
## Questions
### 169. [Majority Element](https://leetcode.com/problems/majority-element/)
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2
'''
## Solutions

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return 0
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        maxEle = nums[0]
        maxVal = d[maxEle]
        for k,v in d.items():
            if maxVal > d[k]:
                pass
            else:
                maxVal = d[k]
                maxEle = k
        return maxEle

# Runtime: 196 ms, faster than 71.47% of Python3 online submissions for Majority Element
# Memory Usage: 15.2 MB
