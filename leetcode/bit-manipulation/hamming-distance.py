"""
[461. Hamming Distance](https://leetcode.com/problems/hamming-distance/)
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

The above arrows point to positions where the corresponding bits are different.
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        xor = x ^ y
        count = 0
        # Counting no of 1's
        while xor:
            xor = xor & (xor - 1)
            count += 1
        return count


# Runtime: 24 ms, faster than 86.36% of Python3 online submissions
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
