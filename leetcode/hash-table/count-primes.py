"""
204. [Count Primes](https://leetcode.com/problems/count-primes/)
Count the number of prime numbers less than a non-negative number, n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0

Constraints:
0 <= n <= 5 * 106
"""

# Solutions


class Solution:
    def countPrimes(self, n: int) -> int:
        is_prime = [False, False]
        is_prime.extend([True for _ in range(2, n)])

        i = 2
        while i * i < n:
            if not is_prime[i]:
                i += 1
                continue
            for j in range(i * i, n, i):
                is_prime[j] = False
            i += 1

        count = 0
        for i in range(2, n):
            if is_prime[i]:
                count += 1

        return count

# Runtime       : 1708 ms, faster than 32.52% of Python3 online submissions
# Memory Usage  : 105.2 MB, less than 14.99% of Python3 online submissions
