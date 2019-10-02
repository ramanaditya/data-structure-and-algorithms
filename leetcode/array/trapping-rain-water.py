'''
## Questions

# 42. [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.

'''

# Solutions

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        max_ = height[0]
        trap_water = 0
        for i in range(len(height)):
            if(max_ - height[i] > 0):
                trap_water += (max_ - height[i])
            else:
                max_ = height[i]
        sum_ = 0
        print(trap_water)
        second_max = height[-1]
        j = len(height) - 1
        for i in range(len(height)-1, 0, -1):
            if second_max - height[i] > 0:
                sum_ += (max_ - second_max)
            else:
                if max_ == second_max:
                    break
                second_max = height[i]
                sum_ += (max_ - second_max)
        return trap_water - sum_

# Runtime: 36 ms
# Memory Usage: 12.2 MB
