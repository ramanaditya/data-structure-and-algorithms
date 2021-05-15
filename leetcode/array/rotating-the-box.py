"""
Medium
1861. [Rotating the Box](https://leetcode.com/problems/rotating-the-box/)

You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the
following:
 - A stone '#'
 - A stationary obstacle '*'
 - Empty '.'

The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down
until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles'
positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

Example 1:
Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]

Example 2:
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]

Example 3:
Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]

Constraints:
m == box.length
n == box[i].length
1 <= m, n <= 500
box[i][j] is either '#', '*', or '.'.
"""

# Solutions


from collections import deque
from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])

        queue = deque()
        for i in range(m):
            j = n - 1
            temp = ["." for _ in range(n)]
            rest = n - 1
            while j >= 0:
                if box[i][j] == "*":
                    temp[j] = "*"
                    rest = j - 1
                elif box[i][j] == "#":
                    temp[rest] = "#"
                    rest -= 1
                j -= 1

            queue.appendleft(temp)

        res = [["." for _ in range(m)] for _ in range(n)]
        for i in range(m):
            for j in range(n):
                res[j][i] = queue[i][j]

        return res


# Runtime       : 2484 ms, faster than 100.00% of Python3 online submissions
# Memory Usage  : 26.3 MB, less than 100.00% of Python3 online submissions
