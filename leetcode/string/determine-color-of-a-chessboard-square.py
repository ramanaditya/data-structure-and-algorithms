"""
## Questions : EASY
### 1812. [Determine Color of a Chessboard Square](https://leetcode.com/problems/determine-color-of-a-chessboard-square/)

You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a
chessboard for your reference.

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and
the number second.

Example 1:
Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.

Example 2:
Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.

Example 3:
Input: coordinates = "c7"
Output: false

Constraints:
coordinates.length == 2
'a' <= coordinates[0] <= 'h'
'1' <= coordinates[1] <= '8'
"""

# Solutions


class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        white = ['b', 'd', 'f', 'h']
        if coordinates[0] in white:
            if int(coordinates[1]) & 1:
                return True
            else:
                return False
        else:
            if int(coordinates[1]) & 1:
                return False
            else:
                return True


# Runtime: 28 ms, faster than 86.26% of Python3 online submissions
# Memory Usage: 14.2 MB, less than 41.67% of Python3 online submissions


class Solution:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    def squareIsWhite(self, coordinates: str) -> bool:
        """
        To get the index at constant time we can use dictionary as well, but since we only have 8 chars,
        it doesn't matter much

        chars = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
        return bool((chars.get(coordinates[0]) + int(coordinates[1])) & 1)
        """
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        coordinate_sum = chars.index(coordinates[0]) + int(coordinates[1])
        return not bool(coordinate_sum & 1)  # instead of using not we can add 1 to the coordinate_sum

# Runtime: 16 ms, faster than 99.91% of Python3 online submissions
# Memory Usage: 14.3 MB, less than 41.67% of Python3 online submissions


class Solution:
    """
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    def squareIsWhite(self, coordinates: str) -> bool:
        """
        ord('a') = 97
        ord('1') = 49
        """
        return bool((ord(coordinates[0]) + ord(coordinates[1])) & 1)


# Runtime: 32 ms, faster than 64.33% of Python3 online submissions
# Memory Usage: 14.2 MB, less than 70.66% of Python3 online submissions
