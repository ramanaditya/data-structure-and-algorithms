'''
## Question
### 1200. [Minimum Absolute Difference](https://leetcode.com/problems/minimum-absolute-difference/)
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
 

Constraints:

2 <= arr.length <= 10^5
-10^6 <= arr[i] <= 10^6
'''

## Solutions

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_ = abs(arr[0] - arr[1])
        index = 0
        b = []
        for i in range(0,len(arr) - 1):
            min_check = abs(arr[i] - arr[i+1])
            if min_check <= min_:
                min_ = min_check
        for i in range(0,len(arr) - 1):
            min_check = abs(arr[i] - arr[i+1])
            if min_check <= min_:
                min_ = min_check
                b.append(arr[i:i+2])
        return b

# Runtime: 424 ms
# Memory Usage: 27.8 MB
