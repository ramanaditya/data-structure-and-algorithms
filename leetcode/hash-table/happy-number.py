"""
## Questions : Easy

### 202. [Happy Number](https://leetcode.com/problems/happy-number/)

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by
the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:
Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""

## Solutions
import math


class Solution:
    def convert(self, n):
        return list(str(n))

    def isHappy(self, n: int) -> bool:
        square = {
            "0": 0,
            "1": 1,
            "2": 4,
            "3": 9,
            "4": 16,
            "5": 25,
            "6": 36,
            "7": 49,
            "8": 64,
            "9": 81,
        }
        tracker = {}
        while n != 1:
            if n in tracker.keys() and tracker[n] >= 1:
                return False
            elif n in tracker.keys():
                tracker[n] += 1
            else:
                tracker[n] = 0
            num = self.convert(n)
            n = 0
            for i in num:
                n += square[i]

        return True


# Runtime: 36 ms, faster than 30.40% of Python3 online submissions
# Memory Usage: 13.7 MB, less than 5.26% of Python3 online submissions


class Solution:
    def square_digit(self, n):
        res = 0
        while n > 0:
            res += int(math.pow(n % 10, 2))
            n = n // 10
        return res

    def isHappy(self, n: int) -> bool:

        while True:
            n = self.square_digit(n)

            if n == 1:
                return True

            if n in (4, 20, 37, 89):
                return False


# Runtime: 24 ms, faster than 96.98% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 5.26% of Python3 online submissions
