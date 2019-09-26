'''
## Question

### 1122. [Relative Sort Array](https://leetcode.com/problems/relative-sort-array/)

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

Constraints:

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.

'''

## Solutions

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        b = []
        for i in range(len(arr2)):
            b.append(arr2[i])
            b = b*arr1.count(arr2[i])
            res.extend(b)
            b = []
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                b.append(arr1[i])
        b.sort()
        res.extend(b)
        return res

# Runtime: 48 ms
# Memory Usage: 13.8 MB
