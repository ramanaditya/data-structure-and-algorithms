"""
## Question

### 442. [Find All Duplicates in an Array](https://leetcode.com/problems/find-all-duplicates-in-an-array/)

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
"""

# Solutions


class Solution:
    """
    Time Complexity: Adding in Dictionary ( n ) + Loop( n ) = O( n )
    Space Complexity: Dictionary ( n ) = O( n )
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        nums = []
        for k, v in d.items():
            if d[k] > 1:
                nums.append(k)
        return nums


# Runtime: 464 ms
# Memory Usage: 22.1


class Solution:
    """
    Time Complexity: Sorting (n log(n) ) + Loop( n ) = O( n log (n) )
    Space Complexity: Constant = O( 1 )
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = list()
        start = 1
        end = len(nums)
        while start < end:
            if nums[start] == nums[start - 1]:
                res.append(nums[start])
            start += 1
        return res


# Runtime: 408 ms, faster than 60.15% of Python3 online submissions
# Memory Usage: 20.7 MB, less than 96.50% of Python3 online submissions


class Solution:
    """
    Time Complexity: Loop( n ) = O( n )
    Space Complexity: Constant = O( 1 )
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return ans


# Runtime: 420 ms, faster than 52.90% of Python3 online submissions
# Memory Usage: 21.2 MB, less than 41.96% of Python3 online submissions
