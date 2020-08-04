"""
Question : Medium
[342. Power of Four](https://leetcode.com/problems/power-of-four/)
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example 1:
Input: 16
Output: true

Example 2:
Input: 5
Output: false

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        bin_form = bin(num)[2:].count("1")
        return True if num >= 0 and bin_form == 1 and num.bit_length() & 1 else False


# Runtime: 36 ms, faster than 51.59% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 57.02% of Python3 online submissions


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        bit_len = num.bit_length()
        return 4 ** ((bit_len - 1) // 2) == num


# Runtime: 28 ms, faster than 88.81% of Python3 online submissions
# Memory Usage: 13.6 MB, less than 96.49% of Python3 online submissions
