"""
## Questions: MEDIUM
### 695. [Max Area of Island](https://leetcode.com/problems/max-area-of-island/)

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally
(horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [
    [0,0,0,0,0,0,0,0]
]
Output: 0

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 50
grid[i][j] is either 0 or 1.
"""

# Solutions
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        def dfs(grid, i, j, count):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
                return count

            grid[i][j] = -1
            return (1 +
                    dfs(grid, i + 1, j, count) +
                    dfs(grid, i - 1, j, count) +
                    dfs(grid, i, j + 1, count) +
                    dfs(grid, i, j - 1, count))

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    temp = dfs(grid, i, j, 0)
                    res = max(temp, res)

        return res


# Runtime       : 140 ms, faster than 65.29% of Python3 online submissions
# Memory Usage  : 16.8 MB, less than 47.54% of Python3 online submissions
