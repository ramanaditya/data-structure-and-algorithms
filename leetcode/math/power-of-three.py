"""
## Questions

### 326. [Power of Three](https://leetcode.com/problems/power-of-three/)

Given an integer n, return true if it is a power of three. Otherwise, return false.

An integer n is a power of three, if there exists an integer x such that n == 3x.

Example 1:
Input: n = 27
Output: true

Example 2:
Input: n = 0
Output: false

Example 3:
Input: n = 9
Output: true

Example 4:
Input: n = 45
Output: false

Constraints:
-231 <= n <= 231 - 1
"""


# Solutions


class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1


# Runtime: 56 ms, faster than 98.78% of Python3 online submissions
# Memory Usage: 14.3 MB, less than 46.96% of Python3 online submissions


class Solution:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)

    integer data types lies in the range [-2^32, 2^32-1]
    Highest power of 3 that lies within this range is 3^19 ie., 1162261467
    3^19 has 3 as only factors and is the highest possible input, so if any number divides it
    - if that number has only 3 as a factors will have 0 as remainder
    - else remainder won't be zero
    """
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return 1162261467 % n == 0


# Runtime: 60 ms, faster than 97.27% of Python3 online submissions
# Memory Usage: 14 MB, less than 91.48% of Python3 online submissions
