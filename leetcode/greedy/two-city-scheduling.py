"""
## Questions

### 1029. [Two City Scheduling](https://leetcode.com/problems/two-city-scheduling/)
There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0],
and the cost of flying the i-th person to city B is costs[i][1].

Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

Example 1:
Input: [[10,20],[30,200],[400,50],[30,20]]
Output: 110
Explanation:
The first person goes to city A for a cost of 10.
The second person goes to city A for a cost of 30.
The third person goes to city B for a cost of 50.
The fourth person goes to city B for a cost of 20.
The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.


Note:
1 <= costs.length <= 100
It is guaranteed that costs.length is even.
1 <= costs[i][0], costs[i][1] <= 1000
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
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costA = [i for i, j in costs]
        diff = [j - i for i, j in costs]
        return sum(costA) + sum(sorted(diff)[: len(costs) // 2])


# Runtime: 36 ms, faster than 90.00% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 7.69% of Python3 online submissions
