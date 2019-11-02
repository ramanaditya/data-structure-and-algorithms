'''
## Question
### 283. [Move Zeroes](https://leetcode.com/problems/move-zeroes//)
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

## Solutions

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                x = nums[i]
                nums.remove(nums[i])
                nums.append(x)

# Runtime: 204 ms, faster than 12.23% of Python3 online submissions for Move Zeroes.
# Memory Usage: 14.9 MB, less than 5.97% of Python3 online submissions for Move Zeroes.
