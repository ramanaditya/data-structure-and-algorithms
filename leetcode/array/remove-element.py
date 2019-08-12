'''
## Question

### 27. Remove Element

Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

[Link - leetcode](https://leetcode.com/problems/remove-element/)
'''

## Solutions

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        x = len(nums)
        if x == 1:
            if nums[0] == val:
                nums.remove(val)
                return len(nums)
        while i < x :
            if nums[i] == val:
                nums.remove(nums[i])
                x = len(nums)
                if x == 1:
                    if nums[0] == val:
                        nums.remove(val)
                        return len(nums)
                i = 0
            else:
                i = i + 1
        return len(nums)

# Runtime: 28 ms
# Memory Usage: 13.1 MB
