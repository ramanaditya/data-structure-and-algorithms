'''
## Questions

### 1051. [Height Checker](https://leetcode.com/problems/height-checker/)

Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

Example 1:

Input: [1,1,4,2,1,3]
Output: 3
Explanation: 
Students with heights 4, 3 and the last 1 are not standing in the right positions.
 
Note:

1 <= heights.length <= 100
1 <= heights[i] <= 100

'''

## Solutions

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        i = 0
        k = len(A)
        for i in A:
            i.reverse()
            for j in range(len(i)):
                temp = i[j]
                if temp == 0:
                    i[j] = 1
                else:
                    i[j] = 0
        return A

# Runtime: 44 ms
# Memory Usage: 13.7 MB
