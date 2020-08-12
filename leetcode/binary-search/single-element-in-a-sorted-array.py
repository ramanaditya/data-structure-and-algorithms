"""
## Question : Medium
### 540. [Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/)
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one
element which appears exactly once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10
"""

# Solutions


class Solution:
    """
    XOR with same number is 0 and other number is other number
    Time Complexity: O( n )
    Space Complexity: O( 1 )
    """

    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for ele in nums:
            res ^= ele
        return res


# Runtime: 68 ms, faster than 88.60% of Python3 online submissions
# Memory Usage: 16.1 MB, less than 7.69% of Python3 online submissions


class Solution:
    """
    Using Binary Search
    Time Complexity: O( log (n) )
    Space Complexity: O( 1 )
    """

    def singleNonDuplicate(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = 2 * ((low + high) // 4)  # To get even index
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid
        return nums[low]


# Runtime: 72 ms, faster than 69.50% of Python3 online submissions
# Memory Usage: 16.1 MB, less than 7.69% of Python3 online submissions
