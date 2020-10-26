"""
## Question: EASY
### 1582. [Special Positions in a Binary Matrix](https://leetcode.com/problems/special-positions-in-a-binary-matrix/)
Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1, return the number of special positions in mat.

A position (i,j) is called special if mat[i][j] == 1 and all other elements in row i and column j are 0 (rows and
columns are 0-indexed).

Example 1:
Input: mat = [[1,0,0],
              [0,0,1],
              [1,0,0]]
Output: 1
Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.

Example 2:
Input: mat = [[1,0,0],
              [0,1,0],
              [0,0,1]]
Output: 3
Explanation: (0,0), (1,1) and (2,2) are special positions.

Example 3:
Input: mat = [[0,0,0,1],
              [1,0,0,0],
              [0,1,1,0],
              [0,0,0,0]]
Output: 2

Example 4:
Input: mat = [[0,0,0,0,0],
              [1,0,0,0,0],
              [0,1,0,0,0],
              [0,0,1,0,0],
              [0,0,0,1,1]]
Output: 3

Constraints:
rows == mat.length
cols == mat[i].length
1 <= rows, cols <= 100
mat[i][j] is 0 or 1.
"""

# Solutions


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_track = dict()
        col_track = dict()
        row, col = len(mat), len(mat[0])
        i, j = 0, 0
        while i < row:
            count, j = 0, 0
            while j < col:
                if mat[i][j] == 1:
                    count += 1
                j += 1
            row_track[i] = count
            i += 1

        i, j = 0, 0
        while j < col:
            count, i = 0, 0
            while i < row:
                if mat[i][j] == 1:
                    count += 1
                i += 1
            col_track[j] = count
            j += 1

        res = 0
        for i in range(0, row):
            for j in range(0, col):
                if mat[i][j] == 1 and row_track[i] == 1 and col_track[j] == 1:
                    res += 1

        return res


# Runtime       : 200 ms, faster than 16.67% of Python3 online submissions
# Memory Usage  : 14.1 MB, less than 16.67% of Python3 online submissions


class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        row_track = [0 for _ in range(row)]
        col_track = [0 for _ in range(col)]
        i, j = 0, 0
        while i < row:
            j = 0
            while j < col:
                if mat[i][j] == 1:
                    row_track[i] += 1
                    col_track[j] += 1
                j += 1
            i += 1

        res = 0
        for i in range(0, row):
            for j in range(0, col):
                if mat[i][j] == 1 and row_track[i] == 1 and col_track[j] == 1:
                    res += 1

        return res


# Runtime       : 176 ms, faster than 66.67% of Python3 online submissions
# Memory Usage  : 13.9 MB, less than 16.67% of Python3 online submissions
