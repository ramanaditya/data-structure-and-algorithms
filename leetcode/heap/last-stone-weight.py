"""
## Questions: EASY

### 1046. [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)

We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with
x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)

Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last stone.


Note:
1 <= stones.length <= 30
1 <= stones[i] <= 1000
"""

## Solutions


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """Slow using sort each time"""
        if len(stones) <= 1:
            return stones[0] if len(stones) == 1 else None
        temp = sorted(stones, reverse=True)
        while len(temp) > 2:
            new_weight = abs(temp[0] - temp[1])
            temp = sorted(temp[2:] + [new_weight], reverse=True)
        return abs(temp[0] - temp[1])


# Runtime: 32 ms, faster than 49.02% of Python3 online submissions
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions


# Solution


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """faster than previous solution because now size of list keeps on reducing"""

        if len(stones) <= 1:
            return stones[0] if len(stones) == 1 else None
        temp = sorted(stones)
        while len(temp) > 2:
            temp.append(abs(temp.pop() - temp.pop()))
            temp.sort()
        return abs(temp[-1] - temp[-2])


# Runtime: 28 ms, faster than 75.54% of Python3 online submissions
# Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions

import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) <= 1:
            return stones[0] if len(stones) == 1 else None

        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)
        while len(stones) > 2:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            heapq.heappush(stones, -abs(first - second))
            heapq.heapify(stones)
        return abs(stones[-1] - stones[-2])


# Runtime: 36 ms, faster than 50.74% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 54.37% of Python3 online submissions
