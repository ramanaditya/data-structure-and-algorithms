"""
Question : EASY
[476. Number Complement](https://leetcode.com/problems/number-complement/)
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary
representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010.
So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1(no leading zero bits), and its complement is 0.So you need to output 0.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
"""


class Solution:
    def findComplement(self, num: int) -> int:
        binary = bin(num)[2:]
        comp = ""

        for i in binary:
            if i == "0":
                comp += "1"
            else:
                comp += "0"

        return int(comp, 2)


# Runtime: 24 ms, faster than 89.09% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 10.00% of Python3 online submissions


class Solution:
    def findComplement(self, num: int) -> int:
        return ((1 << num.bit_length()) - 1) ^ num


# Runtime: 20 ms, faster than 96.98% of Python3 online submissions
# Memory Usage: 13.6 MB, less than 10.00% of Python3 online submissions
