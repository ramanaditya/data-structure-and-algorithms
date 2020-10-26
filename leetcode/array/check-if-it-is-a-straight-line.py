"""
## Question
### 1232. [Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:
2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
"""

# Solutions


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        try:
            slope = (coordinates[1][1] - coordinates[0][1]) / (
                coordinates[1][0] - coordinates[0][0]
            )
        except ZeroDivisionError:
            slope = 0
        for i in range(1, len(coordinates) - 1):
            try:
                m = (coordinates[i + 1][1] - coordinates[i][1]) / (
                    coordinates[i + 1][0] - coordinates[i][0]
                )
            except ZeroDivisionError:
                m = 0
            if m != slope:
                return False
        return True


# Runtime: 76 ms, faster than 46.62% of Python3 online submissions for Check If It Is a Straight Line.
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions


class Solution:
    def isCollinear(self, x1, x2, x3, y1, y2, y3):
        area = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)
        return area == 0

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        for i in range(1, len(coordinates) - 3):
            if not self.isCollinear(
                coordinates[i][0],
                coordinates[i + 1][0],
                coordinates[i + 2][0],
                coordinates[i][1],
                coordinates[i + 1][1],
                coordinates[i + 2][1],
            ):
                return False
        return True


# Runtime: 72 ms, faster than 78.20% of Python3 online submissions for Check If It Is a Straight Line.
# Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions
