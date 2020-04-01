"""
## Questions : Medium

### 347. [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
Given a non-empty array of integers, return the k most frequent elements.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

## Solutions
import collections
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        d = Counter(nums)
        res = []
        val = sorted(d.values())[-k:]
        for k, v in d.items():
            if d[k] in val:
                res.append(k)
        return res


# Runtime: 116 ms, faster than 17.63% of Python3 online submissions
# Memory Usage: 17.2 MB, less than 6.25% of Python3 online submissions


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = collections.Counter(nums)
        return heapq.nlargest(k, d.keys(), key=d.get)


# Runtime: 100 ms, faster than 89.27% of Python3 online submissions
# Memory Usage: 18.4 MB, less than 6.25% of Python3 online submissions
