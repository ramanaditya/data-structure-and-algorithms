"""
## Questions: MEDIUM

### 1551. [Minimum Operations to Make Array Equal](https://leetcode.com/problems/minimum-operations-to-make-array-equal/)

You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y]
(i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed
that all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements of
arr equal.

Example 1:
Input: n = 3
Output: 2
Explanation: arr = [1, 3, 5]
First operation choose x = 2 and y = 0, this leads arr to be [2, 3, 4]
In the second operation choose x = 2 and y = 0 again, thus arr = [3, 3, 3].

Example 2:
Input: n = 6
Output: 9

Constraints:
1 <= n <= 10^4
"""


# Solutions


class Solution:
    """
    Time Complexity: O( n )
    Space Complexity: O( 1 )
    """

    def minOperations(self, n: int) -> int:
        step = 0
        for i in range(1, n + 1, 2):
            step += n - i
        return step


# Runtime       : 52 ms, faster than 60.00% of Python3 online submissions
# Memory Usage  : 13.9 MB, less than 60.00% of Python3 online submissions


class Solution:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    def minOperations(self, n: int) -> int:
        terms = (n + (1 if n & 1 else 0)) // 2
        return terms * (terms - (1 if n & 1 else 0))


# Runtime       : 28 ms, faster than 87.49% of Python3 online submissions
# Memory Usage  : 14.2 MB, less than 73.51% of Python3 online submissions
