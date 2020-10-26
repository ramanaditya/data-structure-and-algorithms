"""
## Question
### 1539. [Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number/)
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Constraints:
1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length
"""

# Solutions


class Solution:
    """
    Time Complexity: O( n )
    Space Complexity: O( 1 )
    """

    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = None
        count = 0
        start = 0
        end = len(arr)
        while start < end:
            count += 1
            if arr[start] == count:
                start += 1
            else:
                num = count
                k -= 1
            if not k:
                return num
        return count + k


# Runtime: 80 ms, faster than 33.33% of Python3 online submissions
# Memory Usage: 14.1 MB, less than 50.00% of Python3 online submissions
