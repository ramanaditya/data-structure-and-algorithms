"""
Easy
## Questions
### [441. Arranging Coins](https://leetcode.com/problems/arranging-coins/)

You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:
n = 5
The coins can form the following rows:
¤
¤ ¤
¤ ¤
Because the 3rd row is incomplete, we return 2.

Example 2:
n = 8
The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
Because the 4th row is incomplete, we return 3.
"""

## Solutions


import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + math.sqrt(1 + (8 * n))) / 2)


# Runtime: 28 ms, faster than 95.10% of Python3 online submissions
# Memory Usage: 13.6 MB, less than 97.98% of Python3 online submissions


class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 0, n
        while low <= high:
            mid = (high + low) // 2
            prod = (mid * (mid + 1)) // 2

            if prod == n:
                return mid
            elif prod < n:
                low = mid + 1
            else:
                high = mid - 1

        return high


# Runtime: 32 ms, faster than 86.75% of Python3 online submissions
# Memory Usage: 13.7 MB, less than 86.24% of Python3 online submissions
