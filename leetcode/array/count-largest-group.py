"""
## Question : EASY

### 1399. [Count Largest Group](https://leetcode.com/problems/count-largest-group/)

Given an integer n. Each number from 1 to n is grouped according to the sum of its digits.

Return how many groups have the largest size.

Example 1:
Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.

Example 2:
Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.

Example 3:
Input: n = 15
Output: 6

Example 4:
Input: n = 24
Output: 5

Constraints:
1 <= n <= 10^4
"""

# Solutions


class Solution:
    def dig_sum(self, n):
        total = 0
        while n > 0:
            rem = n % 10
            total += rem
            n = n // 10
        return total

    def countLargestGroup(self, n: int) -> int:
        from collections import Counter

        d = dict()
        for i in range(1, n + 1):
            sum_ = self.dig_sum(i)
            d[sum_] = d.get(sum_, 0) + 1
        new = Counter(d.values())
        return new[max(new.keys())]


# Runtime: 104 ms, faster than 71.25% of Python3 online submissions
# Memory Usage: 13.6 MB, less than 100.00% of Python3 online submissions
