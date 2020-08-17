"""
## Questions: EASY
### 69. [Sqrt(x)](https://leetcode.com/problems/sqrtx/)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""

# Solutions


class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1
        while left < right:
            mid = left + (right - left) // 2

            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid

        return left - 1


# Runtime       : 28 ms, faster than 95.12% of Python3 online submissions
# Memory Usage  : 13.8 MB, less than 51.18% of Python3 online submissions


class Solution:
    """Using Binary Search Template"""

    def mySqrt(self, x: int) -> int:
        left, right = 0, x + 1

        while left < right:
            mid = left + (right - left) // 2

            if mid * mid > x:
                right = mid
            else:
                left = mid + 1

        return left - 1


# Runtime       : 40 ms, faster than 58.98% of Python3 online submissions
# Memory Usage  : 13.7 MB, less than 85.90% of Python3 online submissions
