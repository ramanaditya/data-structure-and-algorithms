"""
Question : EASY
191. [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming
weight).

Note:
Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as
a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the
same, whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input
represents the signed integer. -3.

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Constraints:
The input must be a binary string of length 32.
"""


class Solution:
    """
    Time Complexity: O(n.bit_length())
    Space Complexity: O(1)
    """
    def hammingWeight(self, n: int) -> int:
        bin_n = bin(n)[2:]
        count = 0
        for bit in bin_n:
            if bit == '1':
                count += 1
        return count


# Runtime: 28 ms, faster than 89.33% of Python3 online submissions
# Memory Usage: 14.2 MB, less than 70.55% of Python3 online submissions


class Solution:
    """
    Time Complexity: O(n.bit_length())
    Space Complexity: O(1)
    """
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            # Check if the rightmost bit is 1
            if n & 1:
                count += 1
            # Right Shift by 1
            n >>= 1

        return count


# Runtime: 24 ms, faster than 96.85% of Python3 online submissions
# Memory Usage: 14.2 MB, less than 42.11% of Python3 online submissions
