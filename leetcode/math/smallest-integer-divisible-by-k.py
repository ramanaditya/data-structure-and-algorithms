"""
## Questions: MEDIUM

### 1015. [Smallest Integer Divisible by K](https://leetcode.com/problems/smallest-integer-divisible-by-k)

Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K, and N only
contains the digit 1.

Return the length of N.  If there is no such N, return -1.

Example 1:
Input: 1
Output: 1
Explanation: The smallest answer is N = 1, which has length 1.

Example 2:
Input: 2
Output: -1
Explanation: There is no such positive integer N divisible by 2.

Example 3:
Input: 3
Output: 3
Explanation: The smallest answer is N = 111, which has length 3.

Note:
1 <= K <= 10^5
"""


# Solutions


class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        N = 1
        track = dict()
        while True:
            rem = N % K
            if rem == 0:
                return len(str(N))
            if track.get(rem):
                return -1
            track[rem] = True
            N = N * 10 + 1


# Runtime       : 2008 ms, faster than 33.74% of Python3 online submissions
# Memory Usage  : 18.7 MB, less than 5.29% of Python3 online submissions
