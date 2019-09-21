'''
## Questions

### 1198. [Find Smallest Common Element in All Rows](https://leetcode.com/problems/find-smallest-common-element-in-all-rows/)

Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.

If there is no common element, return -1.

Example:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5

Constraints:

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in increasing order.

'''

## Solutions

class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        a = []
        for i in mat:
            for j in i:
                a.append(j)
        a.sort()
        count = 1
        for i in range(1,len(a)):
            if a[i] == a[i - 1]:
                count += 1 
                if count == len(mat) - 1:
                    return a[i]
            else:
                count = 0
        return -1

# Runtime: 660 ms
# Memory Usage: 39.2 MB