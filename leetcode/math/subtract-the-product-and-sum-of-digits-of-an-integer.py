"""
Questions: EASY

1281. [Subtract the Product and Sum of Digits of an Integer](https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/)

Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:
Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21

Constraints:
1 <= n <= 10^5
"""


# Solutions


class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def subtractProductAndSum(self, n: int) -> int:
        prod, add = 1, 0

        while n:
            rem = n % 10
            prod *= rem
            add += rem
            n //= 10

        return prod - add


# Runtime       : 20 ms, faster than 98.84% of Python3 online submissions
# Memory Usage  : 13.9 MB, less than 45.03% of Python3 online submissions
