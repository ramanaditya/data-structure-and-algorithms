"""
## Questions: MEDIUM

### 435. [Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the
intervals non-overlapping.

Example 1:
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""

# Solutions


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals = sorted(intervals, key=lambda ele: (ele[1], ele[0]), reverse=False)
        count = 0
        last = float("-inf")

        for interval in intervals:
            if last > interval[0]:
                count += 1
            else:
                last = interval[1]

        return count


# Runtime       : 76 ms, faster than 71.23% of Python3 online submissions
# Memory Usage  : 16.8 MB, less than 94.45% of Python3 online submissions
