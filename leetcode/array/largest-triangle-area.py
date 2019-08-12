'''
## Questions

### 812. [Largest Triangle Area](https://leetcode.com/problems/largest-triangle-area/)

You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:

Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest. 

Notes:

- 3 <= points.length <= 50.
- No points will be duplicated.
- -50 <= points[i][j] <= 50.
- Answers within 10^-6 of the true value will be accepted as correct.

'''
## Solutions

import math
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        max_ = 0
        for i in range(0,len(points) - 2):
            for j in range(1,len(points) - 1):
                for k in range(2,len(points)):
                    a = abs(math.sqrt(((points[i][0] - points[j][0])**2) + ((points[i][1] - points[j][1])**2)))
                    b = abs(math.sqrt(((points[i][0] - points[k][0])**2) + ((points[i][1] - points[k][1])**2)))
                    c = abs(math.sqrt(((points[k][0] - points[j][0])**2) + ((points[k][1] - points[j][1])**2)))
                    s = (a+b+c)/2
                    area_tri = round(math.sqrt(abs(s*(s-a)*(s-b)*(s-c))),1)
                    if area_tri > max_:
                        max_ = area_tri
        return max_

# Runtime: 2540 ms
# Memory Usage: 13.2 MB
