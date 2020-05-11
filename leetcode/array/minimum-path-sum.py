"""
## Question
### 64. [Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the
sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7

Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

## Solutions


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if len(grid) <= 0 or grid is None:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if row == 0 and col == 0:
                    continue

                # for first row
                if row - 1 < 0:
                    grid[row][col] = grid[row][col] + grid[row][col - 1]

                # for first column
                elif col - 1 < 0:
                    grid[row][col] = grid[row][col] + grid[row - 1][col]

                # for remaining cells
                else:
                    grid[row][col] = grid[row][col] + min(
                        grid[row - 1][col], grid[row][col - 1]
                    )

        return grid[rows - 1][cols - 1]


# Runtime: 108 ms, faster than 54.50% of Python3 online submissions
# Memory Usage: 15.3 MB, less than 22.81% of Python3 online submissions
