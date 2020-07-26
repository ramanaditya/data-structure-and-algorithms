"""
## Questions

### 258. [Add Digits](https://leetcode.com/problems/add-digits/)

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""


# Solutions


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9


# Runtime: 28 ms, faster than 90.22% of Python3 online submissions
# Memory Usage: 13.6 MB, less than 99.13% of Python3 online submissions
