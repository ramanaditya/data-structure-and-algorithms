"""
## Questions

### 1051. [Height Checker](https://leetcode.com/problems/height-checker/)

Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must
move in order for all students to be standing in non-decreasing order of height.)

Example 1:
Input: heights = [1,1,4,2,1,3]
Output: 3
Explanation:
Current array : [1,1,4,2,1,3]
Target array  : [1,1,1,2,3,4]
On index 2 (0-based) we have 4 vs 1 so we have to move this student.
On index 4 (0-based) we have 1 vs 3 so we have to move this student.
On index 5 (0-based) we have 3 vs 4 so we have to move this student.

Example 2:
Input: heights = [5,1,2,3,4]
Output: 5

Example 3:
Input: heights = [1,2,3,4,5]
Output: 0

Constraints:
1 <= heights.length <= 100
1 <= heights[i] <= 100

"""

## Solutions


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a = heights.copy()
        a.sort()
        count = 0
        for i in range(len(heights)):
            if a[i] != heights[i]:
                count += 1
        return count


# Runtime: 36 ms, faster than 46.73% of Python3 online submissions
# Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        a = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if a[i] != heights[i]:
                count += 1
        return count


# Runtime: 28 ms, faster than 93.96% of Python3 online submissions
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions
