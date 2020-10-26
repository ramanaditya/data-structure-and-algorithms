"""
## Questions: HARD
### 410. [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/)

Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty
continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)

Examples:
Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""

# Solutions


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def condition(val) -> bool:
            total, count = 0, 1
            start, end = 0, len(nums)

            while start < end:
                total += nums[start]
                if total > val:
                    total = nums[start]
                    count += 1
                    if count > m:
                        return False
                start += 1
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left


# Runtime       : 32 ms, faster than 87.70% of Python3 online submissions
# Memory Usage  : 13.9 MB, less than 67.67% of Python3 online submissions
