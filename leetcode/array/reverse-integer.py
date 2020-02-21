"""
## Questions :

### 7. [Reverse Integer](https://leetcode.com/problems/reverse-integer/)

Given a 32-bit signed integer, reverse digits of an integer.

**Example 1:**
Input: 123
Output: 321

Example 2:
<pre>
Input: -123
Output: -321
</pre>

Example 3:

Input: 120
Output: 21


Note:

Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

## Solutions

import math


class Solution:
    def reverse(self, x: int) -> int:
        if x > ((2 ** 31) - 1) or x < ((-1) * (2 ** 31)):
            return 0
        else:
            if x < 0:
                x = abs(x)
                flag = 1
            else:
                flag = 0
            s = str(x)
            s = s[::-1]
            s = int(s)
            if s > ((2 ** 31) - 1):
                return 0
            else:
                if flag == 1:
                    s = (-1) * s
                    if s < ((-1) * (2 ** 31)):
                        return 0
                    else:
                        return s
                else:
                    return s


# Runtime: 28 ms
# Memory Usage: 13.3 MB

# Other Solution


class Solution:
    def reverse(self, x: int) -> int:
        min_range = -(2 ** 31)
        max_range = 2 ** 31 - 1
        if x < min_range and x > max_range:
            return 0
        if x > 0:
            flag = 0
        else:
            x *= -1
            flag = 1
        res = 0
        while x > 0:
            res = res * 10 + x % 10
            x //= 10
        if flag == 1:
            res *= -1
            if res >= min_range and res <= max_range:
                return res
            return 0
        if res >= min_range and res <= max_range:
            return res
        return 0


# Runtime: 28 ms, faster than 77.76%
# Memory Usage: 12.8 MB, less than 100.00%
