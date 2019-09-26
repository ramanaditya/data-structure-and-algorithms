'''
# 922. [Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/)

Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
 

Note:

2 <= A.length <= 20000
A.length % 2 == 0
0 <= A[i] <= 1000

'''

# Solutions

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res_list = [0] * len(A)
        odd = 1
        even = 0
        for i in A:
            if i % 2 == 0:
                res_list[even] = i
                even += 2
            else:
                res_list[odd] = i
                odd += 2
        return res_list

# Runtime: 244 ms
# Memory Usage: 15.9 MB
