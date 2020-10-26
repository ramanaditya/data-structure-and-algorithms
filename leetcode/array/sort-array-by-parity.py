"""
# 905. [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/)

Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000

"""

# Solutions


class Solution:
    """
    Two Pointers
    Opposite Direction
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i = 0
        j = len(A) - 1
        while i < j:
            check1 = A[i] % 2
            check2 = A[j] % 2
            if check1 == 0 and check2 == 0:
                i += 1
            elif check1 == 0 and check2 == 1:
                i += 1
                j -= 1
            elif check1 == 1 and check2 == 1:
                j -= 1
            elif check1 == 1 and check2 == 0:
                A[i], A[j] = A[j], A[i]
                i += 1
                j -= 1
        return A


# Runtime: 96 ms
# Memory Usage: 14.6 MB


class Solution:
    """
    Two Pointers
    Same Direction
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def sortArrayByParity(self, A: List[int]) -> List[int]:
        slow, fast = 0, 1
        while fast < len(A):
            check_left = A[slow] & 1
            check_right = A[fast] & 1
            if check_left and not check_right:
                A[slow], A[fast] = A[fast], A[slow]
                slow += 1
                fast += 1
            elif check_left and check_right:
                fast += 1
            else:
                slow += 1
                fast += 1

        return A


# Runtime: 96 ms, faster than 44.64% of Python3 online submissions
# Memory Usage: 14.3 MB, less than 90.97% of Python3 online submissions
