"""
## Questions

### [367. Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false

"""

## Solutions


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num <= 0:
            return False
        elif num == 1:
            return True
        low = 0
        high = num
        while low <= high:
            mid = (low + high) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                high = mid - 1
            else:
                low = mid + 1
        return False


# Runtime: 28 ms, faster than 67.29% of Python3 online submissions
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
