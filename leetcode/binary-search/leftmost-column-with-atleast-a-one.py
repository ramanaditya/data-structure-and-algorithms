"""
Easy
## Questions
### [Leftmost Column with at Least a One]

(This problem is an interactive problem.)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in
non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If
such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that a
ttempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples.
You will not have access the binary matrix directly.

Example 1:
Input: mat = [[0,0],[1,1]]
Output: 0

Example 2:
Input: mat = [[0,0],[0,1]]
Output: 1

Example 3:
Input: mat = [[0,0],[0,0]]
Output: -1

Example 4:
Input: mat = [[0,0,0,1],[0,0,1,1],[0,1,1,1]]
Output: 1


Constraints:
1 <= mat.length, mat[i].length <= 100
mat[i][j] is either 0 or 1.
mat[i] is sorted in a non-decreasing way.
"""

## Solutions


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def binarySearch(self, row, low, high, binaryMatrix):
        n = high
        while low <= high:
            mid = low + (high - low) // 2
            val = binaryMatrix.get(row, mid)
            if val == 1 and (mid == 0 or binaryMatrix.get(row, mid - 1) == 0):
                return mid
            if val == 1:
                high = mid - 1
            else:
                low = mid + 1
        return n + 1

        return index

    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        m, n = binaryMatrix.dimensions()
        minimum = float("inf")
        for i in range(m):
            val = self.binarySearch(i, 0, n - 1, binaryMatrix)
            if val < minimum:
                minimum = val
        return -1 if minimum == n else minimum


# Runtime:
# Memory Usage:

## Solution

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        m, n = binaryMatrix.dimensions()
        minimum = float("inf")
        row = 0
        col = n
        while row < m and col > 0:
            val = binaryMatrix.get(row, col - 1)
            if val == 1:
                col -= 1
            else:
                row += 1
        return -1 if col == n else col
