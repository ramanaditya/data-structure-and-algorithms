"""
## Questions

### 189. [Rotate Array](https://leetcode.com/problems/rotate-array/)

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]

Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

## Solutions


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()
        while k > 0:
            nums.append(nums.pop(0))
            k = k - 1
        nums.reverse()


# Runtime: 80 ms
# Memory Usage: 13.4 MB


class Solution:
    """
    Time Complexity: O( n^2 )
    Space Complexity: O( 1 )
    """

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = n - (k % n)

        start = 0
        while start < k:
            nums.append(nums.pop(0))
            start += 1


# Runtime       : 84 ms, faster than 46.25% of Python3 online submissions
# Memory Usage  : 15.5 MB, less than 7.38% of Python3 online submissions


class Solution:
    """
    Two Pointers
    Time Complexity: O( n )
    Space Complexity: O( 1 )
    """

    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end - 1] = arr[end - 1], arr[start]
            start += 1
            end -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = n - k % n

        self.reverse(nums, 0, k)
        self.reverse(nums, k, n)
        self.reverse(nums, 0, n)


# Runtime       : 60 ms, faster than 89.80% of Python3 online submissions
# Memory Usage  : 15.2 MB, less than 79.81% of Python3 online submissions
