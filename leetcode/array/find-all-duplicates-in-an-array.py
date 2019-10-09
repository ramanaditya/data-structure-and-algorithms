'''
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
'''

## Solutions

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        nums = []
        for k,v in d.items():
            if d[k] > 1:
                nums.append(k)
        return nums

# Runtime: 464 ms
# Memory Usage: 22.1
