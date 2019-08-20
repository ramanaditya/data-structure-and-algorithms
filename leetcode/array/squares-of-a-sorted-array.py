'''
# 977. [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.

'''

# Solutions

class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        while i < j:
            A[i] = A[i] * A[i]
            A[j] = A[j] * A[j]
            i += 1
            j -= 1
        if i == j:
            A[i] = A[i] * A[i]
        A.sort()
        return A

# Runtime: 240 ms
# Memory Usage: 15.2 MB