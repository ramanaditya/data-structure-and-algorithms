"""
## Question : MEDIUM

### 11. [Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
(blue section) the container can contain is 49.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

# Solutions


class Solution:
    """
    Two Pointers
    Time Complexity: O( n )
    Space Complexity: O( 1 )
    """

    def maxArea(self, height: List[int]) -> int:

        start = 0
        end = len(height) - 1

        res = 0

        while start < end:
            area = max(0, (end - start) * min(height[start], height[end]))
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
            res = max(area, res)

        return res


# Runtime       : 144 ms, faster than 48.55% of Python3 online submissions
# Memory Usage  : 15.4 MB, less than 47.16% of Python3 online submissions
