"""
## Question : Easy
### 231. [Power of Two](https://leetcode.com/problems/power-of-two/)
Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true 
Explanation: 20 = 1

Example 2:
Input: 16
Output: true
Explanation: 24 = 16

Example 3:
Input: 218
Output: falseOutput: 4
"""

## Solutions


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        bit_len = n.bit_length()
        return (2**(bit_len - 1) == n)


# Runtime: 32 ms, faster than 60.00% of Python3 online submissions
# Memory Usage: 14 MB, less than 11.42% of Python3 online submissions


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return False if n < 0 else bin(n)[2:].count("1") == 1
   

# Runtime: 32 ms, faster than 60.00% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 51.79% of Python3 online submissions
