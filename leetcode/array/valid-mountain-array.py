"""
## Question
### 941. [Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/)
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

Example 1:
Input: [2,1]
Output: false

Example 2:
Input: [3,5,5]
Output: false

Example 3:
Input: [0,3,2,1]
Output: true

Note:
0 <= A.length <= 10000
0 <= A[i] <= 10000
"""

## Solutions


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) <= 2:
            return False
        i = 0
        j = len(A) - 1
        while i < j - 1:
            if A[i] > A[i + 1]:
                break
            if A[i] == A[i + 1]:
                return False
            i += 1
        while j > i:
            if A[j] > A[j - 1]:
                break
            if A[j] == A[j - 1]:
                return False
            j -= 1

        if i == j and j != len(A) - 1 and i != 0:
            return True
        return False


# Runtime: 220 ms, faster than 68.91% of Python3 online submissions
# Memory Usage: 14 MB, less than 63.16% of Python3 online submissions
